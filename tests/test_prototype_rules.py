"""Tests for the alert and data rules used by the dashboard prototype (DIP-30).

The prototype applies the same rules that the real alert module will apply. These tests
fix the expected behaviour now; they will be reused for the real module (UT-07, UT-11).
"""
import numpy as np
import pandas as pd

from src.frontend import demo_data as dd


def hours(n):
    return pd.Series(range(n))


def test_alert_fires_at_threshold_and_repeats_are_suppressed():
    # FR-07 (a): risk above the threshold at hours 10, 12 and 17, no further rise
    risk = pd.Series([0.1] * 22)
    risk[[10, 12, 17]] = 0.40
    assert dd.alert_hours(risk, hours(22)) == [10, 17]


def test_new_alert_when_risk_rises_by_margin():
    # FR-07 (b): 0.40, 0.42 and 0.55 at hours 10, 12 and 13 with a 0.10 margin
    risk = pd.Series([0.1] * 22)
    risk[[10, 12, 13]] = [0.40, 0.42, 0.55]
    alerts = dd.alerts_raised(risk, hours(22))
    assert [(a["hour"], a["reason"]) for a in alerts] == [(10, "threshold"), (13, "risk_rose")]


def test_every_alert_starts_a_new_window():
    # After the re-alert at hour 13 the next alert without a further rise is possible from hour 19
    risk = pd.Series([0.1] * 22)
    risk[[10, 13]] = [0.40, 0.55]
    risk[14:22] = 0.50
    assert dd.alert_hours(risk, hours(22)) == [10, 13, 19]


def test_no_risk_and_no_alert_when_vital_signs_are_old():
    # FR-11: last vital-sign measurement more than 4 hours ago
    df = dd.make_patient("t-01", 30, "stable", seed=1)
    df.loc[df["hour"] >= 24, list(dd.VITALS)] = np.nan
    df.loc[df["hour"] >= 24, "risk"] = np.nan
    status = dd.status_at(df, 29)
    assert status["level"] == "Insufficient data"
    assert status["risk"] is None and status["alert"] is False


def test_risk_is_shown_as_percent_with_level():
    # FR-08: percentage and level label
    df = dd.make_patient("t-02", 72, "deteriorating", seed=1)
    status = dd.status_at(df, 71)
    assert status["percent"] == round(status["risk"] * 100)
    assert status["level"] == dd.risk_level(status["risk"])


def test_last_measurements_report_age_of_each_vital_sign():
    # FR-09: last value and hours since measurement
    df = dd.make_patient("t-03", 20, "stable", seed=2)
    df.loc[df["hour"] >= 17, "Temp"] = np.nan
    temp = next(m for m in dd.last_measurements(df, 19) if m["vital"] == "Temp")
    assert temp["hours_ago"] >= 3
