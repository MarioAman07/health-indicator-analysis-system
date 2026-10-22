"""Clickable dashboard prototype (DIP-14).

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
LEVEL_ICON = {"High": "High", "Medium": "Medium", "Low": "Low", "Insufficient data": "Insufficient data"}

st.set_page_config(page_title="Sepsis early-warning prototype", layout="wide")
cohort = dd.demo_cohort()


def header() -> None:
    st.caption(f"{SYNTHETIC_NOTE} {DISCLAIMER}")


def patient_list() -> None:
    st.title("Patients")
    st.write("Sorted by current risk. Patients with an active alert are at the top.")
    rows = []
    for pid, df in cohort.items():
        last = int(df["hour"].max())
        s = dd.status_at(df, last)
        rows.append({
            "Patient": pid,
            "ICU hour": last,
            "Risk": s["risk"],
            "Level": LEVEL_ICON[s["level"]],
            "Alert": "ALERT" if s["alert"] else "",
            "Vitals updated": f"{s['hours_since_vitals']} h ago" if s["hours_since_vitals"] is not None else "never",
        })
    table = pd.DataFrame(rows).sort_values(["Alert", "Risk"], ascending=[False, False], na_position="last")
    st.dataframe(
        table, hide_index=True, use_container_width=True,
        column_config={"Risk": st.column_config.ProgressColumn("Risk", min_value=0.0, max_value=1.0, format="%.2f")},
    )
    st.caption(f"Alert threshold {dd.THRESHOLD:.2f}; repeated alerts suppressed for {dd.SUPPRESSION_HOURS} h; "
               f"no risk is shown when vital signs are older than {dd.INSUFFICIENT_DATA_HOURS} h.")


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

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Risk", "—" if s["risk"] is None else f"{s['risk']:.2f}")
    c2.metric("Level", "No data" if s["level"] == "Insufficient data" else s["level"])
    c3.metric("Alert", "Active" if s["alert"] else "None")
    c4.metric("Vitals updated", "never" if s["hours_since_vitals"] is None else f"{s['hours_since_vitals']} h ago")
    if s["level"] == "Insufficient data":
        st.info("Key vital signs have not been measured recently, so no risk is shown.")

    left, right = st.columns([3, 1.3])
    with left:
        past = df[df["hour"] <= hour]
        fig = make_subplots(rows=len(dd.VITALS) + 1, cols=1, shared_xaxes=True, vertical_spacing=0.025,
                            subplot_titles=["Risk"] + [f"{lab} ({unit})" for lab, unit in dd.VITALS.values()])
        fig.add_trace(go.Scatter(x=past["hour"], y=past["risk"], mode="lines", name="Risk",
                                 line=dict(color="#c0392b", width=2)), row=1, col=1)
        fig.add_hline(y=dd.THRESHOLD, line_dash="dash", line_color="#7f8c8d", row=1, col=1,
                      annotation_text="threshold", annotation_position="top left")
        alerts = [h for h in s["alerts"]]
        if alerts:
            fig.add_trace(go.Scatter(x=alerts, y=past.set_index("hour").loc[alerts, "risk"], mode="markers",
                                     marker=dict(symbol="triangle-up", size=11, color="#c0392b"), name="Alert"),
                          row=1, col=1)
        for i, v in enumerate(dd.VITALS, start=2):
            fig.add_trace(go.Scatter(x=past["hour"], y=past[v], mode="lines+markers", connectgaps=False,
                                     marker=dict(size=3), line=dict(color="#2c3e50", width=1.4), name=v),
                          row=i, col=1)
        fig.update_yaxes(range=[0, 1], row=1, col=1)
        fig.update_layout(height=760, showlegend=False, margin=dict(l=10, r=10, t=30, b=10))
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
                              yaxis=dict(autorange="reversed"), xaxis_title="Effect on risk")
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
