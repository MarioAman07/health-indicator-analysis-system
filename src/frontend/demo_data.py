"""Synthetic demo data for the dashboard prototype (DIP-14).

Everything in this module is generated. It is NOT patient data and NOT the output of a
trained model. It only shows how the dashboard will present real results later, and it
uses the same alert rules that the real system will use (FR-07, FR-08, FR-09, FR-11, FR-19).
"""
from __future__ import annotations

import numpy as np
import pandas as pd

# Vital signs shown in the patient view (FR-09): column -> (label, unit)
VITALS = {
    "HR": ("Heart rate", "/min"),
    "Temp": ("Temperature", "°C"),
    "Resp": ("Respiratory rate", "/min"),
    "MAP": ("Mean arterial pressure", "mmHg"),
    "O2Sat": ("Oxygen saturation", "%"),
}

# Prototype settings. Real values come from validation data and the configuration file.
THRESHOLD = 0.30            # alert threshold (chosen on validation data in the real system)
SUPPRESSION_HOURS = 6       # no repeated alert for the same patient within this window
REALERT_MARGIN = 0.10       # ...unless the risk rises this much above the risk at the last alert (FR-07)
INSUFFICIENT_DATA_HOURS = 4 # vital signs older than this -> "insufficient data" (FR-11)
ACK_LIMIT_MINUTES = 30      # an alert not acknowledged within this time is marked "not acknowledged" (FR-20)

# The only advice text in the system (FR-19).
PROMPT = "Re-check the measurements and inform the responsible physician."

# Acknowledgement outcomes (FR-20): stored value -> text shown to the nurse
ACK_OUTCOMES = {
    "physician_informed": "Re-checked, physician informed",
    "not_confirmed": "Re-checked, change not confirmed",
    "already_treated": "Already known and being treated",
}

# One synthetic acknowledgement, so that the patient list shows every alert state (FR-20).
DEMO_ACKS = {("demo-04", 62): "physician_informed"}

# id, length of stay in hours, scenario
PATIENTS = [
    ("demo-01", 60, "stable"),
    ("demo-02", 72, "deteriorating"),
    ("demo-03", 48, "stable"),
    ("demo-04", 66, "late_deteriorating"),
    ("demo-05", 54, "data_gap"),
    ("demo-06", 40, "stable"),
    ("demo-07", 70, "recovering"),
    ("demo-08", 58, "stable"),
]

BASE = {"HR": 82.0, "Temp": 36.9, "Resp": 16.0, "MAP": 82.0, "O2Sat": 97.0}
NOISE = {"HR": 3.0, "Temp": 0.15, "Resp": 1.2, "MAP": 3.0, "O2Sat": 0.8}
# Change per hour while a patient deteriorates
TREND = {"HR": 0.9, "Temp": 0.05, "Resp": 0.35, "MAP": -0.6, "O2Sat": -0.12}
# Weights of the synthetic risk formula (stand-in for the model)
WEIGHTS = {"HR": 0.05, "Temp": 1.1, "Resp": 0.22, "MAP": -0.06, "O2Sat": -0.25}

FEATURE_LABELS = {
    "HR": "Heart rate, last value",
    "Temp": "Temperature, last value",
    "Resp": "Respiratory rate, last value",
    "MAP": "Mean arterial pressure, last value",
    "O2Sat": "Oxygen saturation, last value",
}


def _deterioration(hour: np.ndarray, scenario: str, hours: int) -> np.ndarray:
    """How many hours of deterioration have accumulated at each hour."""
    if scenario == "deteriorating":
        start = hours * 0.35
    elif scenario == "late_deteriorating":
        start = hours * 0.75
    elif scenario == "recovering":
        peak = hours * 0.45
        return np.clip(np.minimum(hour - hours * 0.15, peak - (hour - peak)), 0, None)
    else:
        return np.zeros_like(hour, dtype=float)
    return np.clip(hour - start, 0, None)


def make_patient(patient_id: str, hours: int, scenario: str, seed: int) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    hour = np.arange(hours)
    worse = _deterioration(hour, scenario, hours)
    df = pd.DataFrame({"hour": hour})
    for v in VITALS:
        df[v] = BASE[v] + TREND[v] * worse + rng.normal(0, NOISE[v], hours)
        # About 1 in 8 hours without a measurement, as in real monitoring data
        df.loc[rng.random(hours) < 0.12, v] = np.nan
    if scenario == "data_gap":
        df.loc[df["hour"] >= hours - 7, list(VITALS)] = np.nan
    df["O2Sat"] = df["O2Sat"].clip(upper=100)
    filled = df[list(VITALS)].ffill()
    score = sum(WEIGHTS[v] * (filled[v] - BASE[v]) for v in VITALS)
    df["risk"] = (1 / (1 + np.exp(-(score - 2.6)))).clip(upper=0.97).round(3)
    # No risk when vital signs are too old (FR-11): the model is not asked to guess.
    last_measured = df["hour"].where(df[list(VITALS)].notna().any(axis=1)).ffill()
    df.loc[(df["hour"] - last_measured).gt(INSUFFICIENT_DATA_HOURS) | last_measured.isna(), "risk"] = np.nan
    df.insert(0, "patient_id", patient_id)
    return df


def demo_cohort() -> dict[str, pd.DataFrame]:
    return {pid: make_patient(pid, hours, scenario, seed=i) for i, (pid, hours, scenario) in enumerate(PATIENTS)}


def alerts_raised(risk: pd.Series, hours: pd.Series, threshold: float = THRESHOLD,
                  suppression: int = SUPPRESSION_HOURS, margin: float = REALERT_MARGIN) -> list[dict]:
    """Alerts by the rules of FR-07.

    An alert fires when the risk reaches the threshold and no alert was raised for the patient in
    the previous `suppression` hours. Inside that window a new alert fires only if the risk has
    risen by at least `margin` above the risk at the last alert; it starts a new window.
    """
    alerts: list[dict] = []
    for h, r in zip(hours, risk):
        if pd.isna(r) or r < threshold:
            continue
        h, r = int(h), float(r)
        if not alerts or h - alerts[-1]["hour"] >= suppression:
            alerts.append({"hour": h, "risk": r, "reason": "threshold"})
        elif r >= alerts[-1]["risk"] + margin - 1e-9:
            alerts.append({"hour": h, "risk": r, "reason": "risk_rose"})
    return alerts


def alert_hours(risk: pd.Series, hours: pd.Series, threshold: float = THRESHOLD,
                suppression: int = SUPPRESSION_HOURS) -> list[int]:
    """Hours at which an alert fires (FR-07)."""
    return [a["hour"] for a in alerts_raised(risk, hours, threshold, suppression)]


def hours_since_vitals(df: pd.DataFrame, hour: int) -> int | None:
    """Hours since the most recent measurement of any key vital sign, up to `hour`."""
    past = df[df["hour"] <= hour]
    measured = past[past[list(VITALS)].notna().any(axis=1)]
    if measured.empty:
        return None
    return int(hour - measured["hour"].max())


def last_measurements(df: pd.DataFrame, hour: int) -> list[dict]:
    """Last value of each vital sign up to `hour` and how many hours ago it was measured (FR-09)."""
    past = df[df["hour"] <= hour]
    out = []
    for v, (label, unit) in VITALS.items():
        measured = past[past[v].notna()]
        if measured.empty:
            out.append({"vital": v, "label": label, "unit": unit, "value": None, "hours_ago": None})
        else:
            last = measured.iloc[-1]
            out.append({"vital": v, "label": label, "unit": unit, "value": float(last[v]),
                        "hours_ago": int(hour - last["hour"])})
    return out


def risk_level(risk: float) -> str:
    """Level label shown next to the percentage (FR-08)."""
    return "High" if risk >= THRESHOLD else ("Medium" if risk >= THRESHOLD / 2 else "Low")


def status_at(df: pd.DataFrame, hour: int) -> dict:
    """Risk, level, alert and data state at a given hour, as the API will return it."""
    row = df[df["hour"] == hour].iloc[0]
    since = hours_since_vitals(df, hour)
    alerts = alerts_raised(df.loc[df["hour"] <= hour, "risk"], df.loc[df["hour"] <= hour, "hour"])
    if since is None or since > INSUFFICIENT_DATA_HOURS:
        return {"risk": None, "percent": None, "level": "Insufficient data", "alert": False,
                "current_alert": None, "hours_since_vitals": since, "alerts": alerts}
    risk = float(row["risk"])
    current = alerts[-1] if alerts and hour - alerts[-1]["hour"] < SUPPRESSION_HOURS else None
    return {"risk": risk, "percent": int(round(risk * 100)), "level": risk_level(risk),
            "alert": current is not None, "current_alert": current,
            "hours_since_vitals": since, "alerts": alerts}


def contributions(df: pd.DataFrame, hour: int, top: int = 5) -> pd.DataFrame:
    """Signed contribution of each input to the synthetic risk (stand-in for SHAP values, FR-10)."""
    filled = df[df["hour"] <= hour][list(VITALS)].ffill().iloc[-1]
    rows = [{"feature": FEATURE_LABELS[v], "value": filled[v],
             "contribution": WEIGHTS[v] * (filled[v] - BASE[v])} for v in VITALS]
    out = pd.DataFrame(rows)
    return out.reindex(out["contribution"].abs().sort_values(ascending=False).index).head(top)
