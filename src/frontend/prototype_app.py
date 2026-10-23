"""Clickable dashboard prototype (DIP-14, updated in DIP-30).

Run from the repository root:

    streamlit run src/frontend/prototype_app.py

It uses synthetic data only (see demo_data.py). The real dashboard will show the same
views but read everything from the backend API.
"""
from __future__ import annotations

import pandas as pd
import plotly.graph_objects as go
import streamlit as st
from plotly.subplots import make_subplots

import demo_data as dd

DISCLAIMER = "Research prototype — not a diagnosis."
SYNTHETIC_NOTE = "Synthetic demo data: not real patients and not the output of a trained model."
REASON_TEXT = {"threshold": "the risk reached the threshold",
               "risk_rose": f"the risk rose by at least {dd.REALERT_MARGIN * 100:.0f} points since the last alert"}
LEVEL_STYLE = {"High": "background-color: #f8d7da; color: #842029",
               "Medium": "background-color: #fff3cd; color: #664d03",
               "Low": "background-color: #d1e7dd; color: #0f5132"}

st.set_page_config(page_title="Sepsis early-warning prototype", layout="wide")
cohort = dd.demo_cohort()
if "acks" not in st.session_state:
    # Acknowledgements given in this browser session: (patient, alert hour) -> outcome (FR-20)
    st.session_state.acks = dict(dd.DEMO_ACKS)


def header() -> None:
    st.caption(f"{SYNTHETIC_NOTE} {DISCLAIMER}")


def risk_text(s: dict) -> str:
    """Risk as a percentage with its level label (FR-08)."""
    return "Insufficient data" if s["risk"] is None else f"{s['percent']}% · {s['level']} risk"


def alert_state(pid: str, s: dict, hour: int) -> str:
    """State of the current alert as the nurse sees it (FR-20).

    One prototype hour is longer than the 30-minute limit, so an alert from an earlier hour
    that nobody acknowledged is shown as "not acknowledged".
    """
    alert = s["current_alert"]
    if alert is None:
        return ""
    if st.session_state.acks.get((pid, alert["hour"])):
        return "Acknowledged"
    return "New alert" if alert["hour"] == hour else "Not acknowledged"


def patient_list() -> None:
    st.title("Patients")
    st.write("Alerts that nobody has acknowledged come first, then acknowledged alerts, then the other "
             "patients by risk. Patients without recent vital signs are at the bottom.")
    rows = []
    for pid, df in cohort.items():
        last = int(df["hour"].max())
        s = dd.status_at(df, last)
        state = alert_state(pid, s, last)
        group = 3 if s["risk"] is None else (0 if state in ("New alert", "Not acknowledged")
                                             else 1 if state == "Acknowledged" else 2)
        rows.append({
            "_group": group,
            "_risk": -1.0 if s["risk"] is None else s["risk"],
            "_level": s["level"],
            "Patient": pid,
            "ICU hour": last,
            "Risk": risk_text(s),
            "Alert": state,
            "Vitals updated": "never" if s["hours_since_vitals"] is None else f"{s['hours_since_vitals']} h ago",
        })
    table = pd.DataFrame(rows).sort_values(["_group", "_risk"], ascending=[True, False])
    levels = table["_level"].tolist()
    shown = table.drop(columns=["_group", "_risk", "_level"]).reset_index(drop=True)
    styled = shown.style.apply(lambda col: [LEVEL_STYLE.get(lv, "") for lv in levels], subset=["Risk"])
    st.dataframe(styled, hide_index=True, use_container_width=True)
    st.caption(f"Alert threshold {dd.THRESHOLD * 100:.0f}%; after an alert, repeats are suppressed for "
               f"{dd.SUPPRESSION_HOURS} h unless the risk rises by {dd.REALERT_MARGIN * 100:.0f} points; "
               f"an alert not acknowledged within {dd.ACK_LIMIT_MINUTES} min is marked \"not acknowledged\"; "
               f"no risk is shown when vital signs are older than {dd.INSUFFICIENT_DATA_HOURS} h.")


def alert_banner(pid: str, s: dict, hour: int) -> None:
    """Alert with the fixed prompt (FR-19) and the acknowledgement (FR-20)."""
    alert = s["current_alert"]
    st.error(f"**Alert at ICU hour {alert['hour']}:** {REASON_TEXT[alert['reason']]}.  \n"
             f"**{dd.PROMPT}**")
    key = (pid, alert["hour"])
    outcome = st.session_state.acks.get(key)
    if outcome:
        st.success(f"Acknowledged: {dd.ACK_OUTCOMES[outcome]}.")
        return
    if alert["hour"] < hour:
        st.warning(f"Not acknowledged for more than {dd.ACK_LIMIT_MINUTES} minutes.")
    a, b = st.columns([3, 1])
    choice = a.radio("Outcome", list(dd.ACK_OUTCOMES), format_func=dd.ACK_OUTCOMES.get,
                     horizontal=True, key=f"outcome-{pid}-{alert['hour']}")
    if b.button("Acknowledge", key=f"ack-{pid}-{alert['hour']}", type="primary"):
        st.session_state.acks[key] = choice
        st.rerun()


def patient_detail() -> None:
    st.title("Patient detail")
    ids = list(cohort)
    default = st.query_params.get("patient", "demo-02")
    pid = st.selectbox("Patient", ids, index=ids.index(default) if default in ids else 0)
    df = cohort[pid]
    last = int(df["hour"].max())
    start = min(int(st.query_params.get("hour", last)), last)
    hour = st.slider("ICU hour", 0, last, start)
    s = dd.status_at(df, hour)

    c1, c2, c3 = st.columns(3)
    c1.metric("Risk", risk_text(s))
    c2.metric("Alert", alert_state(pid, s, hour) or "None")
    c3.metric("Vitals updated", "never" if s["hours_since_vitals"] is None else f"{s['hours_since_vitals']} h ago")
    if s["alert"]:
        alert_banner(pid, s, hour)
    if s["risk"] is None:
        st.warning(f"Key vital signs have not been measured for more than {dd.INSUFFICIENT_DATA_HOURS} hours, "
                   "so no risk is shown. Please measure the patient.")

    # Last value of each vital sign and its age (FR-09)
    for col, m in zip(st.columns(len(dd.VITALS)), dd.last_measurements(df, hour)):
        if m["value"] is None:
            col.markdown(f"{m['label']}  \n**—**  \n:gray[not measured]")
        else:
            age = "measured this hour" if m["hours_ago"] == 0 else f"measured {m['hours_ago']} h ago"
            col.markdown(f"{m['label']}  \n**{m['value']:.1f} {m['unit']}**  \n:gray[{age}]")

    left, right = st.columns([2.6, 1.5])
    with left:
        past = df[df["hour"] <= hour]
        fig = make_subplots(rows=len(dd.VITALS) + 1, cols=1, shared_xaxes=True, vertical_spacing=0.035,
                            row_heights=[0.25] + [0.15] * len(dd.VITALS),
                            subplot_titles=["Risk"] + [f"{lab} ({unit})" for lab, unit in dd.VITALS.values()])
        fig.add_trace(go.Scatter(x=past["hour"], y=past["risk"], mode="lines", name="Risk",
                                 line=dict(color="#c0392b", width=2)), row=1, col=1)
        fig.add_hline(y=dd.THRESHOLD, line_dash="dash", line_color="#7f8c8d", row=1, col=1,
                      annotation_text="threshold", annotation_position="top left")
        if s["alerts"]:
            fig.add_trace(go.Scatter(
                x=[a["hour"] for a in s["alerts"]], y=[a["risk"] for a in s["alerts"]], mode="markers",
                marker=dict(symbol="triangle-up", size=11, color="#c0392b"), name="Alert",
                hovertext=[REASON_TEXT[a["reason"]] for a in s["alerts"]]), row=1, col=1)
        for i, v in enumerate(dd.VITALS, start=2):
            fig.add_trace(go.Scatter(x=past["hour"], y=past[v], mode="lines+markers", connectgaps=False,
                                     marker=dict(size=3), line=dict(color="#2c3e50", width=1.4), name=v),
                          row=i, col=1)
        fig.update_yaxes(range=[0, 1], tickformat=".0%", row=1, col=1)
        fig.update_layout(height=700, showlegend=False, margin=dict(l=10, r=10, t=30, b=10))
        fig.update_xaxes(title_text="ICU hour", row=len(dd.VITALS) + 1, col=1)
        st.plotly_chart(fig, use_container_width=True)
    with right:
        st.subheader("Why this risk")
        if s["risk"] is None:
            st.write("No explanation: risk is not shown.")
        else:
            contrib = dd.contributions(df, hour)
            bar = go.Figure(go.Bar(
                x=contrib["contribution"], y=contrib["feature"], orientation="h",
                marker_color=["#c0392b" if c > 0 else "#2980b9" for c in contrib["contribution"]],
                text=[f"{v:.1f}" for v in contrib["value"]], textposition="auto"))
            bar.update_layout(height=300, margin=dict(l=10, r=40, t=10, b=10),
                              yaxis=dict(autorange="reversed", automargin=True), xaxis_title="Effect on risk")
            st.plotly_chart(bar, use_container_width=True)
            st.caption("Red raises the risk, blue lowers it. Numbers on the bars are the current values.")
        st.subheader("Not used by the model")
        st.write("Notes, medications, examinations and anything not measured hourly. "
                 "Check the patient before acting on a warning.")
    st.caption(DISCLAIMER)


def model_comparison() -> None:
    st.title("Model comparison")
    st.write("All models are evaluated on the same patients and features. "
             "Internal test = held-out patients from set A; external test = set B (another hospital system).")
    metrics = ["AUROC", "AUPRC", "Sensitivity", "Specificity", "PPV", "Alerts per patient-day",
               "Septic stays alerted before onset", "Median lead time (h)"]
    models = ["Partial SIRS rule", "Logistic regression", "LightGBM"]
    for test_set in ["Internal test (set A)", "External test (set B)"]:
        st.subheader(test_set)
        table = pd.DataFrame("—", index=models, columns=metrics)
        st.dataframe(table, use_container_width=True)
    st.info("Values are filled in from the evaluation report after training (FR-04, FR-13), "
            "each with a 95% confidence interval. Precision–recall curves will be shown below the tables.")


PAGES = {"list": ("Patients", patient_list), "detail": ("Patient detail", patient_detail),
         "models": ("Model comparison", model_comparison)}

current = st.query_params.get("page", "list")
keys = list(PAGES)
choice = st.sidebar.radio("View", keys, index=keys.index(current) if current in keys else 0,
                          format_func=lambda k: PAGES[k][0])
st.sidebar.caption(SYNTHETIC_NOTE)
header()
PAGES[choice][1]()
