# Verification and Evaluation Plan

**Status:** initial version for supervisor review (DIP-15)  
**Last updated:** 21 Oct 2026  
**Related:** [requirements](06-requirements.md) · [ML methodology](05-technology/ml-methodology.md) · [architecture](07-architecture/architecture.md) · [prototype](08-prototype/README.md)

The project aim is demonstrated in three ways: (1) the software does what the requirements say — automated tests and acceptance checks; (2) the model is evaluated honestly against baselines on an internal and an external test set; (3) users can understand the output — a user check of the prototype screens.

## 1. What is verified and how

| Level | What it checks | Tool | When it runs |
|---|---|---|---|
| Unit tests (`UT-`) | Single functions: validation, features, partial SIRS, alert logic, data-quality rule | pytest | On every change (locally and later in CI) |
| Integration tests | Pipeline from raw files to features and predictions on a small fixed sample | pytest | On every change to `src/ml` |
| API tests | Endpoints, request validation, error format | pytest + FastAPI `TestClient` | On every change to `src/backend` |
| Acceptance tests (`AT-`) | One check per Must/Should requirement, written from the user's or researcher's point of view | pytest scripts and documented manual steps | Before each pre-defense |
| Inspections (`IN-`) | Things a test cannot fully decide: repository content, documentation, disclaimer on screens | Checklist | Before each pre-defense |
| Demonstrations (`DM-`) | Running the system from a clean environment by following the README | Manual, recorded | Before each pre-defense |
| User check (`UX-`) | Whether users understand the screens | Short sessions with respondents | After the prototype and after the first real dashboard |
| Model evaluation | Discrimination, calibration, alert behaviour, transfer to set B | Evaluation pipeline (`make evaluate`) | After each training run |

## 2. Requirement → test traceability

| Requirement | Test | Test idea | Expected result |
|---|---|---|---|
| FR-01 Import and validate files | UT-01, AT-01 | Load a valid file; load files with a missing column, an unknown column and a text value | Valid file loads; each broken file is rejected with file, row and column named |
| FR-02 No future data in features | UT-02 | Build features for a stay; append 10 more hours; rebuild | Features for all original hours are identical |
| FR-03 Training with one command | AT-03 | Run `make train` on the sample configuration | Model file and metadata (type, versions, seed, configuration hash, validation metrics) exist |
| FR-04 Evaluation report | AT-04 | Run `make evaluate` | Report contains all metrics of §3 for every model, both test sets, with 95% CIs |
| FR-05 Partial SIRS score | UT-05 | Hand-made rows at, below and above each cut-off (38 °C, 36 °C, 90 /min, 20 /min, 32 mmHg, 12 and 4 ×10⁹/L) | Criterion flags and total score match the expected values |
| FR-06 Prediction endpoint | AT-06 | Valid request; request with a text value; request with negative hour | 200 with all fields; 422 with field-level errors |
| FR-07 Alert and suppression | UT-07 | Risk above threshold at hours 10, 12 and 17 with a 6-hour window | Alerts at 10 and 17 only |
| FR-08 Patient list | AT-08 | Open the list view with the demo set | All demo patients: active alerts first, then by risk; patients without a risk value (insufficient data) last |
| FR-09 Patient trends | AT-09 | Open a demo patient | Five vital signs and risk on one time axis, threshold and alerts marked |
| FR-10 Contributing measurements | AT-10 | Request a prediction from LightGBM | Five features with signed contributions; shown in the dashboard |
| FR-11 Insufficient data | UT-11 | Stay whose last vital-sign measurement is older than the limit | State `insufficient_data`, no risk, no alert |
| FR-12 Stored predictions | AT-12 | Make *N* predictions; read them back | *N* records with time, patient, risk, alert, model version |
| FR-13 Model comparison view | AT-13 | Open the view after evaluation | Values equal those in the report file |
| FR-14 Model metadata | AT-14 | `GET /api/v1/models/current` | Fields match the metadata file |
| NFR-01 Reproducibility | AT-N01 | Train and evaluate twice with the same configuration | Metrics identical within ±0.001; same patient-ID split files |
| NFR-02 No sensitive data in Git | IN-N02 | `git ls-files` search for `.psv`, `.zip`, `.env`; review evidence register | Nothing found |
| NFR-03 Response time | AT-N03 | 100 requests for the longest test stay on the development laptop | 95th percentile ≤ target (first target 500 ms) |
| NFR-04 Test coverage | IN-N04 | `pytest --cov=src/ml --cov=src/backend` | ≥ target (first target 70%) |
| NFR-05 Clean setup | DM-N05 | Fresh virtual environment, follow README only | API and dashboard start without extra steps |
| NFR-06 Disclaimer | UT-N06, IN-N06 | Check every API response with a risk; check every dashboard screen | Disclaimer always present |
| NFR-07 Understandable screen | UX-N07 | User check, §6 | ≥ 2 of 3 respondents explain why the risk is high |
| NFR-08 Model card | IN-N08 | Review the model card | Data, intended use, limitations and metrics described |
| NFR-09 Robust errors | UT-N09 | Malformed JSON, missing fields, wrong types | Structured 4xx, no stack trace |

Already implemented: tests for the data-analysis script (`tests/test_eda.py`), which cover reading, schema rejection, derived onset and measurement gaps.

## 3. Model evaluation

The full protocol is in the [ML methodology](05-technology/ml-methodology.md) (§4, §8, §9). In short:

### 3.1 Test sets

| Set | Content | Question it answers |
|---|---|---|
| Internal test | 15% of set-A patients, never used for training or tuning | How well does the model work on new patients from the same hospital system? |
| External test | All of set B | How much does performance drop at a different hospital system? |

### 3.2 Metrics

| Metric | Level | Definition |
|---|---|---|
| AUROC | Hour | Area under the ROC curve of the hourly risk |
| AUPRC | Hour | Area under the precision–recall curve; compared with the prevalence of positive hours |
| Sensitivity, specificity, PPV, F1 | Hour | At the operating point: highest threshold that still gives sensitivity ≥ 0.80 on validation |
| Brier score, calibration curve | Hour | Mean squared error of the risk; observed vs predicted risk in 10 bins |
| Septic stays alerted before onset | Patient | Share of septic stays with at least one alert before the derived onset |
| Median lead time | Patient | Median hours between the first alert and the derived onset, among alerted septic stays |
| Non-septic stays with an alert | Patient | Share of non-septic stays with at least one alert |
| Alerts per patient-day | Patient | Number of alerts divided by total ICU days |

### 3.3 Baselines

| Baseline | Why |
|---|---|
| Partial SIRS rule (score ≥ 2) | Transparent clinical rule computable from the data; qSOFA and NEWS2 are not computable because mental status is missing |
| Regularized logistic regression | Simplest reproducible ML model on the same features; an honest floor |

### 3.4 Success rule

- **Primary:** LightGBM AUPRC on the internal test is higher than logistic regression, and the 95% CI of the paired bootstrap difference excludes 0.
- **Always reported:** comparison with partial SIRS; internal → external drop for every model; patient-level alert metrics.
- A primary criterion that is not met is reported as a result; it does not hide the comparison.

### 3.5 Measurement conditions

| Condition | Value |
|---|---|
| Dataset | PhysioNet/CinC Challenge 2019 training data, v1.0.0 |
| Split | Patient-level, stratified by sepsis, seed 42; patient-ID lists stored |
| Confidence intervals | 1,000 bootstrap resamples of patients |
| Hardware | Development laptop (Apple Silicon MacBook), CPU only |
| Software | Library versions pinned in `requirements.txt` and recorded in model metadata |
| Configuration | One configuration file per run; its hash stored with the model |

## 4. Test data

- **Unit tests** use small hand-made patient files created inside the tests; no real data are needed.
- **Integration and acceptance tests** use a fixed sample of 50 patients from the training split, selected by a stored list of IDs. The data stay in the ignored `data/` folder; the tests skip with a clear message if the data are not present.
- **No test fixture** in the repository contains rows copied from the dataset.

## 5. Entry and exit criteria

| | Criterion |
|---|---|
| Ready to evaluate the model | All unit tests pass; UT-02 (no future data) passes; the split files exist |
| Ready for a pre-defense | All Must acceptance tests pass or have a documented, accepted reason; inspections IN-N02 and IN-N06 pass; README setup demonstrated |
| Defects | A failing check becomes a YouTrack task linked to the requirement; it is closed only after the check passes |

## 6. User check

| Item | Plan |
|---|---|
| Who | 2–3 respondents from the user discussions (DIP-4) |
| Material | Prototype screens 1–3 ([prototype](08-prototype/README.md)); later the real dashboard |
| Questions | Why is the risk high for this patient? What would you do next? What is missing or confusing? |
| Success | At least 2 of 3 explain the reason for the high risk correctly from the screen (NFR-07) |
| Record | Anonymous summary in the evidence register; changes go into the requirements with an `EV-` source |

## 7. Schedule

| Milestone | Verification activity |
|---|---|
| Pre-defense 1 (24 Oct 2026) | Plan presented for approval; tests for the data-analysis script; user check of the prototype screen prepared (the survey of 21 Oct did not include the screen, so the check is done with the next respondents) |
| Data pipeline and baselines | UT-01, UT-02, UT-05, integration test, AT-03 |
| Main model and evaluation | AT-04, AT-N01, model evaluation §3 |
| API and dashboard | AT-06 – AT-14, UT-07, UT-11, UT-N06, UT-N09, AT-N03, user check on the real dashboard |
| Final pre-defense | Full acceptance run, coverage (IN-N04), clean setup (DM-N05), inspections |

Dates of the later milestones are in [milestones](10-management/milestones.md).
