"""Tests for the exploratory data analysis helpers (DIP-9)."""
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

from src.ml import eda


def write_stay(folder: Path, name: str, labels, hr=None) -> Path:
    """Write a small patient file in the Challenge format."""
    n = len(labels)
    data = {column: [np.nan] * n for column in eda.EXPECTED_COLUMNS}
    data["HR"] = hr if hr is not None else [80.0] * n
    data["Age"] = [60.0] * n
    data["Gender"] = [1.0] * n
    data["ICULOS"] = list(range(1, n + 1))
    data[eda.LABEL] = labels
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / f"{name}.psv"
    pd.DataFrame(data)[eda.EXPECTED_COLUMNS].to_csv(path, sep="|", index=False, na_rep="NaN")
    return path


def test_load_stay_adds_set_patient_and_hour(tmp_path):
    path = write_stay(tmp_path / "training_setA", "p000001", [0, 0, 0])
    df = eda.load_stay(path)
    assert list(df["set"].unique()) == ["A"]
    assert list(df["patient_id"].unique()) == ["p000001"]
    assert list(df["hour"]) == [0, 1, 2]


def test_load_stay_rejects_wrong_columns(tmp_path):
    path = tmp_path / "training_setA" / "bad.psv"
    path.parent.mkdir(parents=True)
    path.write_text("HR|SepsisLabel\n80|0\n")
    with pytest.raises(eda.SchemaError):
        eda.load_stay(path)


def test_stay_table_derives_onset_six_hours_after_first_positive(tmp_path):
    folder = tmp_path / "training_setB"
    write_stay(folder, "p100001", [0, 0, 0, 1, 1])          # first positive at hour 3
    write_stay(folder, "p100002", [0, 0, 0])                # never septic
    write_stay(folder, "p100003", [1, 1])                   # positive from the first hour
    stays = eda.stay_table(eda.load_all(tmp_path))
    assert stays.loc["p100001", "derived_onset_hour"] == 3 + eda.LABEL_SHIFT_HOURS
    assert not stays.loc["p100002", "septic"]
    assert np.isnan(stays.loc["p100002", "derived_onset_hour"])
    assert stays.loc["p100003", "label_at_first_hour"]


def test_measurement_gaps_counts_hours_between_measurements():
    values = pd.Series([80.0, np.nan, np.nan, 82.0, 85.0, np.nan, 90.0])
    assert list(eda.measurement_gaps(values)) == [3, 1, 2]


def test_summary_counts_septic_stays_and_positive_hours(tmp_path):
    folder = tmp_path / "training_setA"
    write_stay(folder, "p000001", [0, 0, 1, 1])
    write_stay(folder, "p000002", [0, 0, 0, 0])
    summary = eda.summarize(eda.load_all(tmp_path))
    a = summary["sets"]["A"]
    assert a["stays"] == 2
    assert a["septic_stays"] == 1
    assert a["positive_hours"] == 2
    assert a["patient_hours"] == 8


def test_load_all_rejects_duplicate_patient_ids_across_sets(tmp_path):
    write_stay(tmp_path / "training_setA", "p000001", [0, 0])
    write_stay(tmp_path / "training_setB", "p000001", [0, 0])
    with pytest.raises(eda.SchemaError):
        eda.load_all(tmp_path)


def test_summary_splits_stay_length_and_counts_positive_hours(tmp_path):
    folder = tmp_path / "training_setA"
    write_stay(folder, "p000001", [0, 0, 1, 1, 1])        # septic, 5 h, 3 positive hours
    write_stay(folder, "p000002", [0, 0, 0])              # not septic, 3 h
    a = eda.summarize(eda.load_all(tmp_path))["sets"]["A"]
    assert a["stay_length_hours_septic"]["median"] == 5
    assert a["stay_length_hours_non_septic"]["median"] == 3
    assert a["positive_hours_per_septic_stay"]["median"] == 3


def test_any_key_vital_gap_uses_hours_with_at_least_one_vital(tmp_path):
    # HR measured at hours 0 and 5 only; Temp at hour 2: gaps between "any vital" hours are 2 and 3
    hr = [80.0, np.nan, np.nan, np.nan, np.nan, 82.0]
    path = write_stay(tmp_path / "training_setA", "p000001", [0] * 6, hr=hr)
    df = pd.read_csv(path, sep="|")
    df.loc[2, "Temp"] = 37.0
    df.to_csv(path, sep="|", index=False, na_rep="NaN")
    gaps = eda.any_key_vital_gaps(eda.load_all(tmp_path))
    assert gaps["n_gaps"] == 2
    assert gaps["max"] == 3
    assert gaps["gaps_over_4h_pct"] == 0
