# Requirements Specification

**Status:** revised after the supervisor meeting of 23 Oct 2026 (DIP-12, DIP-27)  
**Last updated:** 23 Oct 2026  
**Related:** [proposal](01-proposal.md) · [ML methodology](05-technology/ml-methodology.md) · [architecture](07-architecture/architecture.md) · [target system](07-architecture/target-system.md) · [verification plan](09-verification.md) · [evidence](02-evidence/evidence-plan.md)

## 1. Conventions

- **Priority (MoSCoW):** Must — required for the diploma result; Should — important, planned; Could — only if time allows; Won't — explicitly excluded from this diploma.
- **Source** shows where a requirement comes from: `LIT-#` (literature matrix source), `EV-#` (user evidence, see [user-evidence.md](02-evidence/user-evidence.md)), `DATA` (dataset properties or data analysis), `AS-#` (assumption AS-01 – AS-06 from the evidence plan; current status in [user-evidence.md](02-evidence/user-evidence.md) §3), `GUIDE` (diploma guidelines or supervisor feedback).
- **Verified by** points to a test or check in the [verification plan](09-verification.md): `UT` unit test, `AT` acceptance test, `IN` inspection, `DM` demonstration, `UX` user check (not to be confused with the use cases UC-01 – UC-09).
- After the user discussions (DIP-4, DIP-8), requirements confirmed or changed by evidence get `EV-#` in the Source column, and the change is recorded in the evidence-to-requirement table.

## 2. Users and constraints

| ID | Constraint |
|---|---|
| C-01 | Only public, de-identified data (PhysioNet/CinC Challenge 2019, CC BY 4.0) are used. |
| C-02 | One developer; the system must run on a single laptop without a GPU or cloud services. |
| C-03 | Python technology stack (see [technology comparison](05-technology/technology-comparison.md)). |
| C-04 | The system is a research prototype. It does not diagnose, prescribe or replace clinical judgement. |

Users: the ICU nurse (primary: sees and acknowledges alerts) and the ICU physician (assesses alerted patients), both supported by the user evidence (EV-01); the clinical-informatics researcher or ML engineer is the secondary user. See the [proposal](01-proposal.md#2-target-users). How the system is used in an ICU, step by step, is described in the [target system](07-architecture/target-system.md).

## 3. Functional requirements

| ID | Requirement | Priority | Acceptance criterion | Source | Verified by |
|---|---|---|---|---|---|
| FR-01 | The system imports patient files in the Challenge format (pipe-separated, one row per hour) and validates their schema. | Must | A valid file with the 41 expected columns loads. A file with a missing or unknown column, or a non-numeric value, is rejected with a message naming the file, row and column. | DATA | UT-01, AT-01 |
| FR-02 | The system builds model features for hour *t* only from measurements recorded at hours ≤ *t*. | Must | Appending future hours to a patient does not change the features computed for any earlier hour. | LIT-1, LIT-2 | UT-02 |
| FR-03 | The system trains the baselines and the main model with one command from a configuration file and saves each model with its metadata. | Must | `make train` produces a model file and a metadata file with model type, library versions, seed, configuration hash and validation metrics. | LIT-1, GUIDE | AT-03 |
| FR-04 | The system evaluates every model on the internal and external test sets under the same protocol and writes a report. | Must | `make evaluate` writes a report with AUROC, AUPRC, sensitivity, specificity and PPV at the operating point, Brier score, patient-level alert metrics and 95% confidence intervals for each model and both test sets. | LIT-1, LIT-2, LIT-6, LIT-8 | AT-04 |
| FR-05 | The system computes the partial SIRS score (0–4) from the last observed values. | Must | For hand-made input rows, each criterion and the total score match the expected values, including boundary values. | LIT-3, LIT-4, LIT-5 | UT-05 |
| FR-06 | The API returns a risk estimate for a patient's history up to hour *t*. | Must | A valid request returns status 200 with a risk score in [0, 1], risk level, alert flag, threshold and model version. An invalid request returns status 422 with field-level errors. | AS-03 | AT-06 |
| FR-07 | The system raises an alert when the risk reaches the threshold, suppresses repeated alerts for the same patient during a configurable window, and raises a new alert inside the window when the risk rises further by a configurable margin. | Must | With a 6-hour window, a 0.10 margin and a risk above the threshold at hours 10 (0.40), 12 (0.42) and 13 (0.55), alerts are raised at hours 10 and 13 only; every alert starts a new window, so without a further rise the next alert is possible from hour 19. | LIT-6, LIT-10, AS-04, EV-06, EV-10 | UT-07 |
| FR-08 | The dashboard shows the patient list ordered by urgency, with the risk as a percentage together with a colour-coded level label. | Must | Order: unacknowledged alerts, acknowledged alerts, the other patients by descending risk, patients with insufficient data last. Each row shows the risk as a percentage and a label (Low green, Medium yellow, High red), e.g. "72% · High risk". | AS-01, EV-01, EV-03, EV-08, EV-09, EV-14 | AT-08 |
| FR-09 | The dashboard shows, for a selected patient, the trends of HR, Temp, Resp, MAP and O2Sat together with the risk curve, the threshold and alert hours on one time axis, and the time since the last measurement of each vital sign. | Must | For any demo patient, the five vital signs and the risk are plotted against ICU hour, the threshold is drawn, alert hours are marked, and each vital sign shows its last value and how many hours ago it was measured. | AS-02, LIT-9, EV-07, EV-13, EV-14 | AT-09 |
| FR-10 | Each LightGBM risk estimate comes with the five measurements that contributed most to it. | Should | The API response contains five features with signed contributions; the dashboard lists them under readable names. | AS-03, AS-05, LIT-7, LIT-10, EV-07, EV-08 | AT-10 |
| FR-11 | When none of the key vital signs (HR, O2Sat, Temp, SBP, MAP, Resp) has been measured for longer than a configurable number of hours (default 4), the system reports "insufficient data" instead of a risk value and asks for a new measurement. | Should | With the default limit, a patient whose last key vital-sign measurement is more than 4 hours old receives the state `insufficient_data`, no risk value and no alert; changing the limit to 1 hour in the configuration changes the result without code changes. | LIT-7, EV-02, EV-08, DATA | UT-11 |
| FR-12 | The system stores each prediction with time, patient ID, risk, alert state and model version. | Should | After *N* predictions the database holds *N* records with these fields, and the API returns them for a patient. | LIT-9, LIT-10 | AT-12 |
| FR-13 | The dashboard has a model comparison view with metrics and precision–recall curves of all models on both test sets. | Should | The values shown equal the values in the evaluation report. | LIT-4, secondary user | AT-13 |
| FR-14 | The API returns metadata of the model in use: type, version, training date, threshold and validation metrics. | Should | `GET /api/v1/models/current` returns these fields, matching the metadata file. | GUIDE | AT-14 |
| FR-15 | The system trains a recurrent sequence model (GRU) for comparison. | Could | The GRU appears in the evaluation report under the same protocol. | LIT-1 | AT-04 |
| FR-16 | The evaluation report includes the official Challenge utility score. | Could | The score is computed with the official scoring logic on the internal and external test sets. | LIT-2 | AT-04 |
| FR-17 | Live integration with hospital information systems (HL7, FHIR). The integration is designed ([target system](07-architecture/target-system.md) §3, §6) but not implemented in this diploma. | Won't | — | C-04 | — |
| FR-18 | Treatment or medication recommendations. | Won't | — | C-04 | — |
| FR-19 | Every alert is shown with one fixed prompt: "Re-check the measurements and inform the responsible physician". | Should | The patient view of every alerted patient shows exactly this sentence; no other advice text exists in the code. | EV-12, C-04 | AT-19 |
| FR-20 | The nurse acknowledges an alert with one of three outcomes (re-checked, physician informed; re-checked, change not confirmed; already known and being treated); an alert not acknowledged within a configurable time (default 30 min) is marked "not acknowledged". | Should | `POST /api/v1/alerts/{id}/ack` with an outcome stores the outcome, user and time and clears the banner; an open alert older than the limit is listed first and marked "not acknowledged"; the share of each outcome is reported. | LIT-9, LIT-10, EV-06, EV-10 | AT-20, UT-20 |
| FR-21 | Patient data enter the system through a data-source interface; the diploma implements it as a replay of the PhysioNet files that releases, at simulated hour *t*, only rows with ICULOS ≤ *t*, and an hourly cycle processes the new values. | Must | Running the cycle for hours 1…*t* gives the same features and predictions as building them directly from rows ≤ *t*; no row with ICULOS > *t* is ever returned for hour *t*. | C-01, DATA, GUIDE | UT-21, AT-21 |

## 4. Non-functional requirements

| ID | Quality | Requirement | Priority | Acceptance criterion | Source | Verified by |
|---|---|---|---|---|---|---|
| NFR-01 | Reproducibility | Results can be reproduced exactly from the repository and the dataset. | Must | Re-running training and evaluation with the same configuration and seed gives the same metrics (±0.001); the data split is stored as lists of patient IDs. | LIT-1, LIT-2 | AT-N01 |
| NFR-02 | Data protection | No patient data, secrets or personal information are stored in Git. | Must | `git ls-files` contains no `.psv`, `.zip` or `.env` files; the evidence register contains no names or contacts. | C-01, GUIDE | IN-N02 |
| NFR-03 | Performance | A prediction request is answered quickly enough for interactive use. | Should | `POST /api/v1/predict` for the longest stay in the test set answers within 500 ms at the 95th percentile on the development laptop. *(Target to be confirmed after the first measurement.)* | AS-01 | AT-N03 |
| NFR-04 | Maintainability | Critical code is covered by automated tests. | Should | Line coverage of `src/ml` and `src/backend` is at least 70% (pytest-cov). | GUIDE | IN-N04 |
| NFR-05 | Portability | The system runs on a clean machine by following the README. | Must | On a fresh Python 3.10–3.12 environment, the README steps start the API and dashboard without extra manual changes. | GUIDE | DM-N05 |
| NFR-06 | Safety of interpretation | Results are never presented as a diagnosis. | Must | Every API response with a risk and every dashboard screen with a risk shows "Research prototype — not a diagnosis". | C-04, LIT-9, EV-05, EV-11 | UT-N06, IN-N06 |
| NFR-07 | Usability | The main screen explains a warning at a glance. | Should | On the patient view, risk, trends and contributing measurements are visible without scrolling at 1366×768; at least 2 of 3 respondents explain from the mockup why the risk is high. | AS-03, AS-05 | UX-N07 |
| NFR-08 | Transparency | The model is documented for its intended use. | Should | A model card describes data, intended use, limitations and metrics for the model in use. | LIT-10 | IN-N08 |
| NFR-09 | Robustness | Invalid input never crashes the API or exposes internals. | Should | Malformed payloads return structured 4xx errors without stack traces. | GUIDE | UT-N09 |
| NFR-10 | Accountability | Views of a patient, acknowledgements and changes of settings are recorded. | Should | Each such action creates an audit record with user, action, patient and time; records cannot be changed through the API. | GUIDE (national MIS requirements, [target system](07-architecture/target-system.md) §2.2) | AT-N10 |

## 5. Traceability summary

| Source | Requirements |
|---|---|
| Literature (LIT-1 – LIT-10) | FR-02 – FR-05, FR-07, FR-09 – FR-13, FR-15, FR-16, NFR-01, NFR-06, NFR-08 |
| Dataset properties (DATA) | FR-01, FR-11 |
| User assumptions (AS-01 – AS-05) | FR-06 – FR-10, NFR-03, NFR-07 |
| Guidelines and supervisor (GUIDE) | FR-03, FR-14, FR-21, NFR-02, NFR-04, NFR-05, NFR-09, NFR-10 |
| User evidence (EV-01 – EV-14) | FR-07 – FR-11, FR-19, FR-20, NFR-06 |

## 6. Open points

- NFR-03 and NFR-04 targets are first estimates and will be confirmed or changed after the first implementation measurements.
- The five changes proposed from the user evidence were adopted on 23 Oct 2026 after the supervisor meeting: the risk as a percentage with a colour-coded label (FR-08), a new alert when the risk rises further (FR-07), the time since each measurement (FR-09), the 4-hour default for "insufficient data" (FR-11) and the fixed prompt (FR-19).
- FR-20, FR-21 and NFR-10 were added on 23 Oct 2026 to describe how the system works in an ICU, as asked by the supervisor ([target system](07-architecture/target-system.md)). The 30-minute limit and the 0.10 re-alert margin are first values to be checked in the next user discussions.
