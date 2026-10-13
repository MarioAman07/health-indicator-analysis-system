# Project Proposal and Scope

**Project title:** Development of a Machine Learning-Based System for Analyzing Patient Health Indicators  
**Student:** Baku Aman  
**Supervisor:** Altynbek Seitenov (Сейтенов Алтынбек Серикович)  
**Format:** Individual diploma project  
**Status:** Working proposal for supervisor review. The concrete sepsis direction described below is proposed, not yet treated as supervisor-approved.

## 1. Problem statement

Hospitals collect repeated physiological and laboratory measurements for patients. Published research shows that machine-learning models can use such time-series data to estimate the risk of sepsis or clinical deterioration before the event is clinically recognized. The same literature also shows important limitations: results vary with the dataset and prediction setup, performance can fall at a new hospital, and a model with good retrospective discrimination can still create many false alerts or fail when integrated into real clinical workflow.

The engineering problem addressed by this diploma is therefore not only model training. The project will design a reproducible decision-support prototype that ingests time-series patient measurements, applies time-valid preprocessing, produces a risk estimate, exposes the result through an API, and presents the result and measurement trends to a human reviewer.

The prototype is for research and demonstration only. It will not diagnose, prescribe treatment, replace clinical judgement, connect to a live hospital system, or be presented as a clinically validated medical device.

## 2. Target users

The working primary user is a healthcare professional who reviews patient measurements and needs to identify possible deterioration over time.

This user definition is still an assumption. It will be checked through the evidence-of-relevance discussions and reviewed with the supervisor before it is treated as final.

## 3. Aim

To design, implement, and evaluate a reproducible decision-support prototype that analyzes time-series patient measurements and estimates early sepsis risk using an open, de-identified clinical dataset.

## 4. Objectives

1. Define a reproducible time-series prediction task on an openly available clinical dataset.
2. Build a data-ingestion and validation pipeline for repeated patient measurements.
3. Implement documented preprocessing and missing-data handling.
4. Prevent temporal leakage by using only information available up to each prediction time.
5. Train at least one machine-learning model for early sepsis-risk estimation.
6. Implement at least one simple and reproducible baseline under the same evaluation protocol.
7. Expose model inference through a backend API.
8. Build a minimal dashboard that shows measurement trends and the current risk result.
9. Evaluate the model using several discrimination and alert-related metrics.
10. Add automated tests for critical software behaviour and document how to reproduce the system and experiments.

## 5. Proposed project direction

The proposed direction is **time-series monitoring and early warning, with early sepsis prediction as the concrete machine-learning task**.

This direction is preferred because it provides:

- a clearly defined temporal prediction problem;
- an open candidate dataset;
- objective evaluation;
- meaningful Software Engineering work beyond a notebook, including ingestion, validation, preprocessing, inference, API design, alert logic, visualization, experiment tracking, and testing.

This is a project-design choice, not a claim that sepsis prediction is medically superior to other possible topics. A structured-indicator risk model using a public dataset remains a lower-complexity fallback if the supervisor asks to narrow the scope differently.

## 6. Candidate data source

The candidate dataset is **PhysioNet / Computing in Cardiology Challenge 2019: Early Prediction of Sepsis from Clinical Data**.

The public training data contain hourly ICU records with 40 variables:

- 8 vital-sign variables;
- 26 laboratory variables;
- 6 demographic or administrative variables;
- plus `SepsisLabel`.

Missing measurements are represented in the data, and the public dataset is de-identified.

Dataset DOI: `10.13026/v64v-d857`

Only public, de-identified data will be used. Patient datasets will not be committed to the Git repository.

## 7. Machine-learning task

The prototype will estimate sepsis risk from measurements available up to a given patient-hour.

The experimental protocol will follow these rules:

- split patients rather than individual rows between training and evaluation data;
- learn preprocessing only from the training portion;
- never use future patient measurements for an earlier prediction;
- document missing-data handling;
- evaluate the main model and baselines under the same temporal setup;
- record the exact model, preprocessing, threshold, and evaluation configuration.

The exact prediction horizon and the final handling of the Challenge `SepsisLabel` will be fixed before implementation and reviewed with the supervisor. The original Challenge labels begin six hours before the defined onset; the diploma protocol must therefore state clearly how those labels are interpreted.

The original hidden Challenge test set is not publicly available. The diploma will use a reproducible evaluation on the public data and will explicitly state that this does not reproduce the original hidden-hospital test.

## 8. Baselines and model comparison

A simple **logistic-regression baseline** using the same evaluation split is proposed as the minimum reproducible baseline.

It is intentionally treated as a floor rather than assumed to be a strong clinical comparator. Literature reviewed for the project shows that logistic regression can underperform rule-based scores in some settings, while stronger ML models may outperform them.

The main model will be selected after the technology comparison. Reasonable candidates include:

- gradient-boosted trees;
- a time-aware neural model.

A NEWS/NEWS2-style score will only be used if it can be reproduced fairly from the selected data. The Challenge dataset directly contains respiration rate, oxygen saturation, systolic blood pressure, heart rate, and temperature, but it does not directly contain all information required for full NEWS2. Therefore, the project will not label an incomplete approximation as full NEWS2.

## 9. Planned system workflow

1. Load de-identified time-series data.
2. Validate the input schema and values.
3. Apply documented missing-data and preprocessing rules.
4. Construct model inputs without future-information leakage.
5. Run baseline and main-model inference.
6. Convert the model output into a clearly defined risk state.
7. Serve the result through a backend API.
8. Display the risk result together with measurement trends in the dashboard.
9. Record experiment and evaluation outputs for reproducibility.

## 10. Scope

### In scope

- ingestion and validation of the selected public dataset;
- temporal preprocessing and missing-data handling;
- model training and reproducible evaluation;
- baseline comparison;
- backend/API inference;
- minimal application/model metadata storage where needed;
- minimal dashboard;
- visualization of time-series indicators and analytical results;
- automated tests for critical components;
- experiment and evaluation documentation.

### Out of scope

- autonomous medical diagnosis;
- treatment or medication recommendations;
- replacement of clinical judgement;
- production hospital deployment;
- integration with a real hospital information system;
- identifiable patient data;
- intervention on real patients;
- medical-device certification or claims of clinical validation;
- claims of generalization to hospitals or populations not represented in the evaluation.

## 11. Expected outcomes

1. A documented preprocessing pipeline for clinical time-series data.
2. A trained early-sepsis prediction model.
3. At least one reproducible baseline.
4. A backend API for inference.
5. A minimal dashboard for trends and risk results.
6. Automated tests for critical behaviour.
7. A reproducible evaluation report.
8. A documented discussion of dataset shift, missingness, temporal validity, false alerts, and lack of prospective clinical validation.

## 12. Preliminary evaluation plan

The final evaluation plan will use multiple metrics because the task is imbalanced and time-dependent:

- AUROC;
- AUPRC;
- sensitivity / recall;
- specificity;
- precision / positive predictive value;
- F1 where useful;
- lead time before onset where supported by the final setup;
- false-alert burden or alert frequency where supported by the final setup.

All compared models will use the same split, preprocessing rules, and temporal constraints.

## 13. Engineering complexity

The engineering work includes:

- time-series data ingestion and validation;
- missing-data processing;
- leakage-safe temporal feature construction;
- model training and versioned inference;
- backend/API development;
- risk and alert logic;
- dashboard integration;
- experiment/evaluation pipeline;
- automated testing;
- traceability through Git and YouTrack.

The supervisor will review whether the proposed scope is sufficient and whether it should be narrowed or adjusted.

## 14. Main risks

| Risk | Mitigation |
|---|---|
| Missing and irregular measurements | Define explicit preprocessing rules and test them |
| Temporal leakage | Use only current and past measurements for each prediction |
| Class imbalance | Report AUPRC and class-sensitive metrics alongside AUROC |
| Poor generalization | Avoid clinical-validity claims and discuss dataset shift |
| Excessive false alerts | Measure PPV and alert burden where possible |
| Scope becomes too large | Keep one main prediction target and a minimal interface |
| Output is mistaken for medical advice | Label the prototype clearly as research decision support |
| Results cannot be reproduced | Version code, model settings, preprocessing, and evaluation configuration |

## 15. Link to evidence and literature

The literature review contains 12 meaningfully used peer-reviewed publications covering:

- early sepsis prediction;
- clinical-deterioration prediction;
- ML versus clinical baselines;
- external validation;
- alert burden;
- deployment and human workflow.

User evidence is documented separately. Until real discussions are completed, the primary-user and workflow assumptions remain assumptions rather than findings.

## 16. Open decisions for supervisor review

The following decisions still require supervisor discussion rather than being presented as settled facts:

- whether early sepsis prediction is an acceptable concrete interpretation of the approved diploma topic;
- final primary user;
- exact prediction horizon and label interpretation;
- final baseline strategy;
- whether to include the official Challenge utility score;
- whether the proposed engineering scope is appropriate for the diploma.

## 17. Key supporting references

1. Reyna MA, Josef CS, Jeter R, et al. *Early Prediction of Sepsis From Clinical Data: The PhysioNet/Computing in Cardiology Challenge 2019.* Critical Care Medicine. 2020;48(2):210–217. DOI: 10.1097/CCM.0000000000004145.
2. PhysioNet. *Early Prediction of Sepsis from Clinical Data: The PhysioNet/Computing in Cardiology Challenge 2019 (version 1.0.0).* DOI: 10.13026/v64v-d857.
3. The remaining scientific sources are documented in `literature-matrix.md`.
