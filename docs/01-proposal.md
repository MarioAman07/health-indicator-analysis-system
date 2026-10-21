# Project Proposal and Scope

**Project title:** Development of a Machine Learning-Based System for Analyzing Patient Health Indicators  
**Concrete focus:** early sepsis-risk prediction from hourly ICU measurements ([ADR-001](decisions/ADR-001-scope.md), [research justification](01-research-justification.md))  
**Student:** Aman Baku (Баку Аман Сағынғалиұлы), SE-2422  
**Supervisor:** Altynbek Seitenov (Сейтенов Алтынбек Серикович)  
**Format:** individual diploma project  
**Status:** revised on 21 Oct 2026 after supervisor feedback of 19 Oct (feedback log FB-03, FB-04). On 21 Oct the supervisor asked for a research justification of the sepsis focus (FB-12); it is in the [research justification](01-research-justification.md), and confirmation is expected at the meeting on 23 Oct (Q-01).

## 1. Problem statement

ICU patients are monitored through dozens of vital signs and laboratory values, recorded at different times and often missing. Sepsis can develop over a few hours, and recognising it early matters, but early signs are easy to miss in this stream of partial data. Machine-learning models that predict sepsis from such data have been published. However, their results are hard to compare, often drop at a new hospital, and can produce many false alerts (#2, #6, #8). The tools deployed in hospitals are mostly proprietary, and publications describe the surrounding software only briefly.

The project therefore addresses an engineering problem: building an open, tested system that turns ICU time-series data into a transparent early-warning result, evaluates it honestly against simple baselines and on a second hospital system, and shows the user why a warning appears.

## 2. Target users

| User | Who | What they need from the system | Status |
|---|---|---|---|
| **Primary** | ICU nurse or physician who monitors several patients during a shift | See which patients need attention first, how their measurements changed, and why the risk is high, without being flooded by alerts | Supported by the first user evidence (AS-01, EV-01; 2 respondents); checking continues (DIP-4) |
| **Secondary** | Clinical-informatics researcher or ML engineer evaluating early-warning models | A reproducible pipeline, fair baselines, honest metrics, and an external test on a different hospital system | Based on literature (#1, #2, #4) |

Patients, hospital managers and IT administrators are not users of this prototype.

## 3. Aim

To design, implement and evaluate a reproducible decision-support prototype that analyses time-series patient measurements and estimates early sepsis risk, using an open, de-identified clinical dataset.

## 4. Objectives

1. Define a reproducible early-prediction task on the PhysioNet/CinC Challenge 2019 public data.
2. Build an ingestion and validation pipeline for hourly patient measurements.
3. Implement documented preprocessing and missing-data handling that never uses future values.
4. Train a gradient-boosted model and compare it with two baselines (partial SIRS rule, logistic regression) under one protocol.
5. Evaluate internally and on a second hospital system with discrimination, calibration and alert-related metrics.
6. Expose inference through a backend API.
7. Build a dashboard that shows measurement trends, the risk result, alerts and the main contributing measurements.
8. Cover critical behaviour with automated tests and document how to reproduce every result.

## 5. My proposed solution

### 5.1 Main functions

1. **Import and validate** patient files in the Challenge format; reject malformed input with a clear error.
2. **Estimate risk every hour** from features built only from past and current measurements.
3. **Turn risk into an alert state** using a threshold chosen on validation data, a suppression window against repeated alerts, and an "insufficient data" state when key vital signs are missing or outdated.
4. **Explain each result** by showing the measurements that contributed most to the risk.
5. **Compare models** (partial SIRS, logistic regression, LightGBM) on the same patients and show the metrics.
6. **Serve everything through a REST API** used by the dashboard and usable by other clients.

### 5.2 How it works

1. *Offline:* raw files → validation → feature building → training → evaluation → model file with metadata and a metrics report.
2. *Online:* the dashboard asks the API for a patient's data → the API builds features with the same code used in training → the model returns a risk → the alert logic and explanation are added → the result is stored and displayed.

Using one feature-building module for both training and inference prevents differences between what the model learned and what it sees later. The component view is in the [architecture description](07-architecture/architecture.md).

### 5.3 Expected outcomes

1. A documented, leakage-safe preprocessing pipeline for clinical time series.
2. A trained early-sepsis model with two reproducible baselines.
3. An evaluation report with internal and external results, confidence intervals and alert metrics.
4. A REST API for inference with an OpenAPI description.
5. A dashboard with patient list, patient detail and model comparison views.
6. Automated tests for validation, feature building, alert logic and the API.
7. A discussion of dataset shift, missing data, false alerts and the absence of clinical validation.

## 6. Data and method in brief

- **Data:** PhysioNet/CinC Challenge 2019 training sets A and B (40,336 ICU stays, hourly, 40 variables + `SepsisLabel`; CC BY 4.0; DOI 10.13026/v64v-d857). The data are de-identified and are never committed to the repository ([data/README.md](../data/README.md)).
- **Task:** hourly prediction of `SepsisLabel`, which is 1 from 6 hours before Sepsis-3 onset.
- **Split:** patient-level split of set A for training, validation and internal testing; set B as an external test.
- **Models:** partial SIRS rule and logistic regression as baselines; LightGBM as the main model.
- **Evaluation:** AUROC, AUPRC, sensitivity, specificity, PPV, calibration, alerts per patient-day and lead time, with bootstrap confidence intervals.

All decisions and their reasons: [ML methodology](05-technology/ml-methodology.md). Test plan: [verification plan](09-verification.md).

## 7. Scope

### In scope

- ingestion and validation of the selected public dataset;
- temporal preprocessing and missing-data handling;
- model training, baseline comparison and reproducible evaluation;
- alert logic and explanation of results;
- backend API for inference;
- minimal storage of predictions and model metadata;
- dashboard with trends, risk and alerts;
- automated tests for critical components;
- experiment and evaluation documentation.

### Out of scope

- autonomous diagnosis or treatment recommendations;
- replacing clinical judgement;
- deployment in a hospital or integration with a hospital information system;
- identifiable patient data;
- use on real patients;
- medical-device certification or claims of clinical validity;
- claims about hospitals or populations not represented in the evaluation.

## 8. Engineering complexity

- time-series ingestion and schema validation;
- missing-data processing and leakage-safe temporal features;
- model training, versioning and inference shared with the API;
- alert logic with thresholds, suppression and data-quality states;
- REST API and dashboard integration;
- evaluation pipeline with bootstrap confidence intervals and an external test;
- automated tests;
- traceability through Git, pull requests and YouTrack.

## 9. Main risks

The full register is in [risks](10-management/risks.md). The most important for scope:

| Risk | Mitigation |
|---|---|
| Temporal leakage inflates results | Leakage rules plus a dedicated unit test |
| Poor transfer to a new hospital | External test on set B; no clinical-validity claims |
| Too many false alerts | Report PPV and alerts per patient-day; suppression window |
| Scope grows beyond one student | One target, one main model; recurrent model kept optional |
| Output mistaken for medical advice | "Research prototype, not a diagnosis" on every result screen |

## 10. Evidence and literature

- The literature review uses 12 peer-reviewed publications ([literature matrix](03-literature/literature-matrix.md)).
- Existing systems are compared on 9 criteria ([system comparison](04-existing-systems/system-comparison.md)).
- User evidence and data analysis are in [docs/02-evidence](02-evidence/). The first answers support the primary-user definition (AS-01), but they come from two respondents only; checking continues.

## 11. Open decisions for the supervisor

1. Is early sepsis prediction an acceptable concrete focus for the agreed topic? (Q-01; see the [research justification](01-research-justification.md))
2. Are partial SIRS and logistic regression acceptable baselines?
3. Is the proposed engineering scope sufficient for the diploma?

## 12. Key references

1. Reyna MA, Josef CS, Jeter R, et al. *Early Prediction of Sepsis From Clinical Data: The PhysioNet/Computing in Cardiology Challenge 2019.* Critical Care Medicine. 2020;48(2):210–217. DOI: 10.1097/CCM.0000000000004145.
2. PhysioNet. *Early Prediction of Sepsis from Clinical Data: The PhysioNet/Computing in Cardiology Challenge 2019 (version 1.0.0).* DOI: 10.13026/v64v-d857.
3. Other sources (#1–#12) are listed in the [literature matrix](03-literature/literature-matrix.md).
