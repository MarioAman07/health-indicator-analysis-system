"""Exploratory data analysis of the PhysioNet/CinC Challenge 2019 training data (DIP-9).

Usage (from the repository root):

    python -m src.ml.eda --data-dir data/raw --out-dir docs/02-evidence

The script reads every ``*.psv`` file under ``--data-dir`` (expected sub-folders
``training_setA/`` and ``training_setB/``), computes descriptive statistics and writes

* ``<out-dir>/eda-summary.json`` - every number used in ``data-analysis.md``;
* ``<out-dir>/figures/*.png``    - the figures used in ``data-analysis.md``.

Only aggregate statistics are written. No patient-level rows leave ``data/raw``.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

VITALS = ["HR", "O2Sat", "Temp", "SBP", "MAP", "DBP", "Resp", "EtCO2"]
LABS = [
    "BaseExcess", "HCO3", "FiO2", "pH", "PaCO2", "SaO2", "AST", "BUN", "Alkalinephos",
    "Calcium", "Chloride", "Creatinine", "Bilirubin_direct", "Glucose", "Lactate",
    "Magnesium", "Phosphate", "Potassium", "Bilirubin_total", "TroponinI", "Hct", "Hgb",
    "PTT", "WBC", "Fibrinogen", "Platelets",
]
DEMOGRAPHICS = ["Age", "Gender", "Unit1", "Unit2", "HospAdmTime", "ICULOS"]
LABEL = "SepsisLabel"
EXPECTED_COLUMNS = VITALS + LABS + DEMOGRAPHICS + [LABEL]
MEASURED_VARIABLES = VITALS + LABS
# Vital signs used for trend features and the "insufficient data" rule (FR-11).
KEY_VITALS = ["HR", "O2Sat", "Temp", "SBP", "MAP", "Resp"]
# SepsisLabel becomes 1 six hours before onset (dataset definition).
LABEL_SHIFT_HOURS = 6


class SchemaError(ValueError):
    """Raised when a patient file does not have the expected columns."""


def load_stay(path: Path) -> pd.DataFrame:
    """Read one patient file and check that its columns match the Challenge format."""
    df = pd.read_csv(path, sep="|")
    columns = list(df.columns)
    if columns != EXPECTED_COLUMNS:
        missing = [c for c in EXPECTED_COLUMNS if c not in columns]
        unknown = [c for c in columns if c not in EXPECTED_COLUMNS]
        raise SchemaError(f"{path}: unexpected columns (missing={missing}, unknown={unknown})")
    df = df.astype("float32")
    df.insert(0, "hour", np.arange(len(df), dtype="int32"))
    df.insert(0, "patient_id", path.stem)
    df.insert(0, "set", set_name(path))
    return df


def set_name(path: Path) -> str:
    """Return 'A' or 'B' from a path such as data/raw/training_setA/p000001.psv."""
    for part in reversed(path.parts):
        if part.lower().startswith("training_set") and len(part) > len("training_set"):
            return part[len("training_set"):].upper()
    return "unknown"


def load_all(data_dir: Path, cache: Path | None = None) -> pd.DataFrame:
    """Load every stay under data_dir into one table (optionally cached as a pickle)."""
    if cache is not None and cache.exists():
        return pd.read_pickle(cache)
    files = sorted(data_dir.rglob("*.psv"))
    if not files:
        sys.exit(f"No .psv files found under {data_dir}. See data/README.md for how to download the data.")
    stems = pd.Series([f.stem for f in files])
    if stems.duplicated().any():
        raise SchemaError(f"Duplicate patient file names, e.g. {stems[stems.duplicated()].iloc[0]}: "
                          "patient IDs must be unique across sets")
    frames = []
    for i, path in enumerate(files, start=1):
        frames.append(load_stay(path))
        if i % 5000 == 0:
            print(f"  read {i}/{len(files)} files", file=sys.stderr)
    df = pd.concat(frames, ignore_index=True)
    if cache is not None:
        cache.parent.mkdir(parents=True, exist_ok=True)
        df.to_pickle(cache)
    return df


def stay_table(df: pd.DataFrame) -> pd.DataFrame:
    """One row per stay: length, sepsis flag, first positive hour and derived onset."""
    grouped = df.groupby("patient_id", sort=False)
    stays = pd.DataFrame({
        "set": grouped["set"].first(),
        "n_hours": grouped.size(),
        "septic": grouped[LABEL].max().astype(bool),
        "label_at_first_hour": grouped[LABEL].first().astype(bool),
        "age": grouped["Age"].first(),
        "gender": grouped["Gender"].first(),
        "unit_missing": grouped["Unit1"].count().eq(0) & grouped["Unit2"].count().eq(0),
    })
    positive = df[df[LABEL] == 1].groupby("patient_id", sort=False)["hour"].min()
    stays["first_positive_hour"] = positive.reindex(stays.index)
    stays["derived_onset_hour"] = stays["first_positive_hour"] + LABEL_SHIFT_HOURS
    return stays


def measurement_gaps(values: pd.Series) -> np.ndarray:
    """Hours between consecutive measurements of one variable within one stay."""
    measured = np.flatnonzero(values.notna().to_numpy())
    return np.diff(measured)


def gap_quantiles(df: pd.DataFrame, variable: str) -> dict:
    """Distribution of hours between consecutive measurements of a variable (all stays)."""
    measured = df.loc[df[variable].notna(), ["patient_id", "hour"]]
    gaps = measured.groupby("patient_id", sort=False)["hour"].diff().dropna().to_numpy()
    if len(gaps) == 0:
        return {"n_gaps": 0}
    q = np.percentile(gaps, [50, 90, 95, 99])
    return {"n_gaps": int(len(gaps)), "p50": float(q[0]), "p90": float(q[1]),
            "p95": float(q[2]), "p99": float(q[3]), "max": int(gaps.max())}


def any_key_vital_gaps(df: pd.DataFrame) -> dict:
    """Hours between consecutive hours in which at least one key vital sign was measured.

    This is the quantity behind the "insufficient data" rule (FR-11): the rule fires when
    none of the key vital signs has been measured for longer than a limit.
    """
    measured = df.loc[df[KEY_VITALS].notna().any(axis=1), ["patient_id", "hour"]]
    gaps = measured.groupby("patient_id", sort=False)["hour"].diff().dropna().to_numpy()
    if len(gaps) == 0:
        return {"n_gaps": 0}
    q = np.percentile(gaps, [50, 90, 95, 99, 99.9])
    return {"n_gaps": int(len(gaps)), "p50": float(q[0]), "p90": float(q[1]), "p95": float(q[2]),
            "p99": float(q[3]), "p99_9": float(q[4]), "max": int(gaps.max()),
            "gaps_over_4h_pct": round(100 * float((gaps > 4).mean()), 3)}


def describe(series: pd.Series) -> dict:
    s = series.dropna()
    if s.empty:
        return {}
    q = np.percentile(s, [25, 50, 75])
    return {"median": float(q[1]), "q1": float(q[0]), "q3": float(q[2]),
            "min": float(s.min()), "max": float(s.max())}


def summarize_set(df: pd.DataFrame, stays: pd.DataFrame) -> dict:
    septic = stays[stays["septic"]]
    early_predictable = septic[~septic["label_at_first_hour"]]
    missing_hours = df[MEASURED_VARIABLES].isna().mean().mul(100).round(2)
    never = df.groupby("patient_id", sort=False)[MEASURED_VARIABLES].count().eq(0).mean().mul(100).round(2)
    return {
        "stays": int(len(stays)),
        "patient_hours": int(len(df)),
        "septic_stays": int(stays["septic"].sum()),
        "septic_stays_pct": round(100 * stays["septic"].mean(), 2),
        "positive_hours": int((df[LABEL] == 1).sum()),
        "positive_hours_pct": round(100 * (df[LABEL] == 1).mean(), 3),
        "septic_label_at_first_hour": int(septic["label_at_first_hour"].sum()),
        "stay_length_hours": describe(stays["n_hours"]),
        "stay_length_hours_septic": describe(stays.loc[stays["septic"], "n_hours"]),
        "stay_length_hours_non_septic": describe(stays.loc[~stays["septic"], "n_hours"]),
        "positive_hours_per_septic_stay": describe(
            df[df[LABEL] == 1].groupby("patient_id", sort=False).size().astype(float)),
        "derived_onset_hour_early_predictable": describe(early_predictable["derived_onset_hour"]),
        "age": describe(stays["age"]),
        "gender_1_pct": round(100 * stays["gender"].eq(1).mean(), 2),
        "unit_missing_pct": round(100 * stays["unit_missing"].mean(), 2),
        "missing_hours_pct": missing_hours.to_dict(),
        "never_measured_stays_pct": never.to_dict(),
    }


def summarize(df: pd.DataFrame) -> dict:
    stays = stay_table(df)
    summary = {"dataset": "PhysioNet/CinC Challenge 2019 training data v1.0.0",
               "label_shift_hours": LABEL_SHIFT_HOURS, "sets": {}}
    for name in sorted(stays["set"].unique()):
        ids = stays.index[stays["set"] == name]
        summary["sets"][name] = summarize_set(df[df["patient_id"].isin(ids)], stays.loc[ids])
    summary["sets"]["all"] = summarize_set(df, stays)
    summary["key_vital_gaps_hours"] = {v: gap_quantiles(df, v) for v in KEY_VITALS}
    summary["any_key_vital_gap_hours"] = any_key_vital_gaps(df)
    return summary


def make_figures(df: pd.DataFrame, summary: dict, fig_dir: Path) -> list[str]:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig_dir.mkdir(parents=True, exist_ok=True)
    written = []
    sets = [s for s in summary["sets"] if s != "all"]

    # 1. Missingness per variable, sorted, per set.
    miss = pd.DataFrame({s: summary["sets"][s]["missing_hours_pct"] for s in sets})
    miss = miss.loc[miss.mean(axis=1).sort_values().index]
    fig, ax = plt.subplots(figsize=(8, 10))
    y = np.arange(len(miss))
    height = 0.8 / max(len(sets), 1)
    for i, s in enumerate(sets):
        ax.barh(y + i * height, miss[s], height=height, label=f"Set {s}")
    ax.set_yticks(y + height * (len(sets) - 1) / 2, miss.index)
    ax.set_xlabel("Hours with no measurement (%)")
    ax.set_xlim(0, 100)
    ax.set_title("Missing values per variable")
    ax.legend(loc="lower right")
    fig.tight_layout()
    fig.savefig(fig_dir / "missingness.png", dpi=150)
    plt.close(fig)
    written.append("missingness.png")

    # 2. Stay length.
    stays = stay_table(df)
    fig, ax = plt.subplots(figsize=(8, 4))
    for s in sets:
        ax.hist(stays.loc[stays["set"] == s, "n_hours"], bins=range(0, 340, 6), alpha=0.6, label=f"Set {s}")
    ax.set_xlabel("ICU stay length (hours)")
    ax.set_ylabel("Stays")
    ax.set_title("Length of ICU stays")
    ax.legend()
    fig.tight_layout()
    fig.savefig(fig_dir / "stay-length.png", dpi=150)
    plt.close(fig)
    written.append("stay-length.png")

    # 3. Derived sepsis onset hour for stays that can be predicted early.
    early = stays[stays["septic"] & ~stays["label_at_first_hour"]]
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.hist(early["derived_onset_hour"], bins=range(0, 340, 6), color="tab:red", alpha=0.7)
    ax.set_xlabel("Derived sepsis onset (hours after the first record)")
    ax.set_ylabel("Septic stays")
    ax.set_title("When sepsis starts (septic stays without a positive label at the first hour)")
    fig.tight_layout()
    fig.savefig(fig_dir / "onset-hour.png", dpi=150)
    plt.close(fig)
    written.append("onset-hour.png")
    return written


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--data-dir", type=Path, default=Path("data/raw"))
    parser.add_argument("--out-dir", type=Path, default=Path("docs/02-evidence"))
    parser.add_argument("--cache", type=Path, default=Path("data/processed/all_stays.pkl"),
                        help="pickle cache of the loaded data (inside the ignored data/ folder)")
    parser.add_argument("--no-figures", action="store_true")
    args = parser.parse_args(argv)

    print(f"Reading data from {args.data_dir} ...", file=sys.stderr)
    df = load_all(args.data_dir, cache=args.cache)
    summary = summarize(df)
    args.out_dir.mkdir(parents=True, exist_ok=True)
    out_json = args.out_dir / "eda-summary.json"
    out_json.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote {out_json}", file=sys.stderr)
    if not args.no_figures:
        for name in make_figures(df, summary, args.out_dir / "figures"):
            print(f"Wrote {args.out_dir / 'figures' / name}", file=sys.stderr)

    for name, s in summary["sets"].items():
        print(f"Set {name}: {s['stays']} stays, {s['patient_hours']} hours, "
              f"septic stays {s['septic_stays']} ({s['septic_stays_pct']}%), "
              f"positive hours {s['positive_hours_pct']}%")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
