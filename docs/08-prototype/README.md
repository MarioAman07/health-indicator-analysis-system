# UX Prototype

**Status:** first version (DIP-14), updated on 23 Oct 2026 with the adopted changes FR-07 – FR-09, FR-19 and FR-20 (DIP-30)  
**Last updated:** 23 Oct 2026  
**Related:** [requirements](../06-requirements.md) · [architecture](../07-architecture/architecture.md) · [target system](../07-architecture/target-system.md) · [API examples](api-examples.md)

The prototype is a clickable dashboard built with the same technology as the planned system (Streamlit + Plotly). It runs on **synthetic data**: generated vital signs and a hand-written risk formula stand in for real patients and the trained model. The goal is to show how a user will interact with the system and to collect feedback before the real pipeline exists.

## How to run

```
pip install -r requirements.txt
streamlit run src/frontend/prototype_app.py
```

Code: [`src/frontend/prototype_app.py`](../../src/frontend/prototype_app.py) (screens) and [`src/frontend/demo_data.py`](../../src/frontend/demo_data.py) (synthetic data and the alert rules). The alert and data rules are tested in [`tests/test_prototype_rules.py`](../../tests/test_prototype_rules.py).

## Key screens

### 1. Patient list — UC-01 (FR-08)

![Patient list](screens/01-patient-list.png)

The list answers the first question of a shift: whom to check first. Alerts that nobody has acknowledged come first, then acknowledged alerts, then the other patients by risk. The risk is shown as a percentage, which R2 finds clearest, together with a coloured level label, which R1 reads faster under workload ("97% · High risk", EV-09). A patient whose vital signs are too old shows "Insufficient data" instead of a number and is listed last. The caption states the alert rules in use.

### 2. Patient detail at the first alert — UC-02, UC-03, UC-04 (FR-07, FR-09, FR-10)

![Patient detail](screens/02-patient-detail-first-alert.png)

The alert banner states why the alert fired (the risk reached the threshold, or it rose by 10 points since the last alert) and gives the only advice the system ever gives: "Re-check the measurements and inform the responsible physician" (FR-19). Below it the nurse acknowledges the alert with one of three outcomes (FR-20); an alert from an earlier hour that nobody acknowledged is marked "not acknowledged".

Under the banner, each vital sign shows its last value and how long ago it was measured (FR-09), so the nurse sees at once whether the risk rests on fresh data. One time axis then shows the risk and five vital signs, so the user sees *what changed* together with the risk. The threshold is drawn; triangles mark alerts. The time slider replays the stay hour by hour. The right panel shows which measurements raised or lowered the risk and reminds the user what the model does not see.

In the prototype the acknowledgement is kept only in the browser session; in the real system it is stored with the user and the time, and leaves an audit record (NFR-10).

### 3. Insufficient data — UC-04 (FR-11)

![Insufficient data](screens/03-insufficient-data.png)

When key vital signs have not been measured for more than 4 hours, no risk is shown, no alert can fire, and the screen asks for a new measurement. The row of last values shows how old each measurement is. This follows the idea of an "indeterminate" output from COMPOSER (literature #7): it is better to say "I don't know" than to show a confident number built on stale data.

### 4. Model comparison — UC-07 (FR-13)

![Model comparison](screens/04-model-comparison.png)

The same metrics for the partial SIRS rule, logistic regression and LightGBM, on the internal test (set A) and the external test (set B). The cells stay empty until the evaluation report exists; no example numbers are shown, to avoid presenting invented results.

## Design decisions and where they come from

| Decision | Reason | Source |
|---|---|---|
| Risk shown together with trends, not alone | A number without context is hard to trust or act on | AS-03, AS-05; literature #10 |
| Top contributing measurements next to the risk | Users need to see why a warning appears | AS-03; literature #7, #10 |
| Suppression of repeated alerts, with a new alert when the risk rises further | Alert fatigue reduces usefulness, but a worsening patient must not be hidden by the suppression window | AS-04; literature #6, #10; EV-06, EV-10 |
| Risk as a percentage with a coloured label | One respondent reads a percentage best, the other a coloured label; both are shown | EV-09 |
| Time since each measurement | Shows whether the risk rests on fresh data | EV-07, EV-11 |
| One fixed prompt, acknowledgement with an outcome | The system supports the nurse's usual escalation and does not give treatment advice | EV-12, C-04; literature #9 |
| "Insufficient data" state | Avoids confident output on stale data | literature #7 |
| Disclaimer on every screen | The system is decision support, not a diagnosis | C-04, NFR-06 |
| Unacknowledged alerts listed first | The first question on a shift is "whom do I check first?" | AS-01; both respondents chose a list sorted by risk (EV-08); the alert-first order itself is not yet tested |

## What is synthetic and what changes later

| In the prototype | In the real system |
|---|---|
| Generated vital signs for 8 demo patients | Demo patients taken from the test sets of the PhysioNet data |
| Hand-written risk formula | LightGBM model trained as described in the ML methodology |
| Contributions from the same formula | SHAP values of the trained model |
| Insufficient-data rule over the 5 simulated vital signs (SBP is not simulated) | Rule over the six key vital signs of FR-11 |
| Threshold 0.30, suppression 6 h, re-alert margin 0.10, data limit 4 h, acknowledgement limit 30 min | Threshold chosen on validation data; limits set from the data analysis and checked with users; all in the configuration file |
| One synthetic acknowledgement (demo-04) and acknowledgements kept in the browser session | Acknowledgements stored in the database with user and time (FR-20, NFR-10) |
| Data computed inside the dashboard | Dashboard calls the backend API (see [API examples](api-examples.md)) |

## Known gap

NFR-07 requires risk, trends and contributing measurements to be visible without scrolling at 1366×768. The prototype does not meet this yet: at that size the patient view is about 1,680 px high (the chart alone is 700 px), so the risk, the alert banner and the last values are visible without scrolling, but the trends are not. The real dashboard must meet the criterion; the layout will be compacted when it is built (M3).

## Planned user check

The screens will be shown to 2–3 of the respondents from the user discussions (DIP-4). Questions:

1. Looking at screen 2, why is the risk high for this patient?
2. What would you do next?
3. What is missing or confusing on this screen?
4. Is the acknowledgement with three outcomes realistic for your ward, and is 30 minutes a realistic limit?

The answers check NFR-07 and feed back into the requirements.
