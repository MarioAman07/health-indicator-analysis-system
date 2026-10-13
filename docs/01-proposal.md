# Project Proposal

## Project Title

**Development of a Machine Learning-Based System for Analyzing Patient Health Indicators**

**Status:** DRAFT - requires supervisor approval.

---

## Working Definition of Patient Health Indicators

For this project, **patient health indicators** are provisionally defined as structured, de-identified measurements that describe a patient's physiological or clinical state.

Depending on the final project direction and selected dataset, these indicators may include:

- vital signs;
- laboratory measurements;
- demographic variables;
- other structured clinical measurements available in the selected dataset.

The exact set of indicators has not yet been selected. It will depend on the final health problem, machine learning task, target variable, and dataset.

**Status:** DRAFT - requires dataset verification and supervisor approval.

---

## DRAFT: Scope Options Under Evaluation

The current project topic is broad and does not yet define a specific health problem, target variable, dataset, or machine learning task.

Before finalizing the project scope, several possible directions are being considered. The final direction should be selected based on:

- availability and accessibility of legitimate data;
- support from scientific literature;
- clearly defined machine learning task and target variable;
- software engineering complexity;
- feasibility for one student;
- ability to evaluate the result objectively;
- privacy and medical-safety considerations;
- supervisor feedback.

No option below is currently considered the final project direction.

---

## Option A — Health Risk Assessment from Structured Patient Indicators

### Data Type

Structured health indicators collected at a particular examination or assessment point, such as:

- examination measurements;
- laboratory measurements;
- demographic variables;
- other structured health information.

### Possible ML Task

Classification or risk estimation for a specific health condition or health-related outcome.

The exact condition and target variable have **not yet been selected**.

### Possible Data Source

One candidate source is the **National Health and Nutrition Examination Survey (NHANES)** maintained by the U.S. Centers for Disease Control and Prevention.

CDC provides NHANES datasets and accompanying questionnaire, examination, laboratory, and documentation resources for research and analysis.

Official source:

https://www.cdc.gov/nchs/nhanes/

The suitability of particular NHANES variables for the final ML task still needs to be established.

### Potential Advantages

- Public-use health data are available for investigation.
- A clearly measurable classification or risk-estimation problem may be possible.
- Tabular data would generally make preprocessing and model evaluation more manageable for an individual diploma project.
- The ML model could be integrated into a larger software system rather than developed only as a standalone notebook.

### Risks / Limitations

- The specific health condition has not yet been selected.
- The target variable has not yet been defined.
- The relationship between input variables and target must be carefully examined to prevent data leakage.
- A simple tabular classifier alone may provide insufficient Software Engineering complexity, so the surrounding system design would need to provide meaningful engineering work.
- Suitability of a specific NHANES dataset for this diploma has not yet been verified.

**Status:** [DRAFT] [MUST VERIFY]

---

## Option B - Time-Series Monitoring and Early Warning

### Data Type

Repeated patient measurements collected over time, including physiological measurements, laboratory values, and demographic information.

### Possible ML Task

Early prediction of patient deterioration or another clinically relevant event using time-dependent patient data.

A concrete candidate problem is **early prediction of sepsis**, but this is not yet the final project decision.

### Candidate Data Source

A candidate is the **PhysioNet/Computing in Cardiology Challenge 2019: Early Prediction of Sepsis from Clinical Data**.

The official PhysioNet dataset contains measurements recorded over time and provides 40 time-dependent variables together with `SepsisLabel`.

The variables include vital signs, laboratory values, and demographic/administrative information. Missing measurements are explicitly represented in the files.

Training data are publicly downloadable from PhysioNet.

Official source:

https://physionet.org/content/challenge-2019/1.0.0/

The Challenge task is specifically designed around early prediction of sepsis, and its official evaluation rewards sufficiently early predictions while penalizing late, missed, and incorrect predictions.

### Potential Advantages

- The ML task is already clearly connected to temporal patient measurements.
- Time-dependent data may provide greater engineering depth than a single static patient record.
- The system could include:
  - temporal data ingestion;
  - input validation;
  - missing-data processing;
  - ML inference;
  - risk monitoring;
  - alert logic;
  - visualization of indicator trends;
  - presentation of results to a human reviewer.
- There is a clear separation between the ML component and the surrounding software system.
- The candidate training data are openly accessible.

### Risks / Limitations

- Time-series preprocessing is more complex than ordinary tabular classification.
- The dataset contains missing measurements that must be handled correctly.
- The final system would become focused on a specific clinical problem rather than general health analysis.
- The evaluation methodology must be selected carefully.
- The usefulness and interpretation of the system must not be presented as clinically validated without evidence.
- The final target, prediction horizon, model family, and software workflow still require literature review and supervisor approval.
- The official Challenge test set is hidden and cannot be used for independent evaluation. The diploma evaluation would therefore require a reproducible split or validation strategy using the publicly available data.
- Publicly released Challenge data come from two hospital systems, while data from another hospital system were used as part of the hidden evaluation data.
- `SepsisLabel` is defined so that positive labels begin six hours before the defined sepsis onset time.
- Any monitoring model must respect temporal causality: predictions must use only current and past information, not future patient measurements.
- Full NEWS2 cannot be reproduced directly because consciousness/new confusion and a direct supplemental-oxygen indicator are absent from the available variables.

### Possible Baseline

The official Challenge 2019 data dictionary was checked on 10 October 2026.

Five physiological inputs required by NEWS2 are directly available in the dataset:

- `Resp` — respiration rate;
- `O2Sat` — oxygen saturation;
- `SBP` — systolic blood pressure;
- `HR` — heart rate / pulse;
- `Temp` — temperature.

However, the dataset does not contain a variable representing consciousness or new confusion, and it does not contain a direct supplemental-oxygen indicator.

Although `FiO2` is available, it should not automatically be treated as equivalent to the NEWS2 supplemental-oxygen indicator without scientific justification.

Therefore, **full NEWS2 cannot be reproduced directly using the Challenge 2019 dataset**.

Possible baseline approaches are:

1. A simple statistical baseline such as logistic regression using the same available input data.
2. A clearly documented partial NEWS2-style score using only compatible variables, but only if such an adaptation can be scientifically justified.
3. Another established and reproducible early-warning baseline identified through the literature review.

The final baseline must be selected after literature review and discussion with the supervisor.

**Status:** [DRAFT] [REQUIRES SUPERVISOR APPROVAL]

---

## Option C - ICU Analysis Using MIMIC-IV

### Data Type

Detailed de-identified clinical data from hospital and intensive-care settings.

### Possible ML Task

Potential tasks could include:

- patient-risk prediction;
- deterioration analysis;
- another outcome-prediction task supported by the selected MIMIC-IV data.

No particular ML target has been selected.

### Candidate Data Source

**MIMIC-IV**, hosted through PhysioNet.

Unlike the PhysioNet Challenge 2019 training dataset, MIMIC-IV is a **restricted-access resource**.

Official PhysioNet requirements state that a user must:

1. become a credentialed PhysioNet user;
2. complete the required CITI “Data or Specimens Only Research” training;
3. sign the project's Data Use Agreement;
4. obtain access before downloading the restricted files.

Official source:

https://physionet.org/content/mimiciv/

### Potential Advantages

- Rich clinical data are available once access requirements are satisfied.
- The dataset may support technically and scientifically substantial ML problems.
- It could support a deeper patient-monitoring or prediction system.

### Risks / Limitations

- Access is not immediate.
- Credentialing, required training, and the Data Use Agreement introduce additional preparation.
- Restricted data would require stricter handling than an openly downloadable dataset.
- Access requirements could delay development.
- For the current diploma schedule, this creates additional project risk without yet providing a clearly demonstrated advantage over an openly accessible alternative.

For this reason, MIMIC-IV is currently being treated as an **alternative candidate rather than the preferred dataset**.

**Status:** [DRAFT] [MUST VERIFY] — not selected.

---

## Preliminary Comparison

The following table is a **project-planning comparison**, not an experimentally proven ranking.

Terms such as “lower”, “moderate”, and “higher” represent preliminary judgments about implementation effort and schedule risk and should not be interpreted as scientific findings.

| Criterion | Option A — Structured Indicators | Option B — Time-Series / Early Warning | Option C — MIMIC-IV |
|---|---|---|---|
| Candidate data access | Public-use NHANES data are available; final dataset not selected | PhysioNet Challenge 2019 training data are publicly downloadable | Credentialed PhysioNet access required |
| Possible ML task | Classification / risk estimation; target not selected | Defined candidate task: early-event prediction | Task still to be selected |
| Temporal information | Not necessarily required | Central to the candidate approach | Available depending on selected data |
| Data-processing difficulty | Preliminary judgment: relatively manageable | Preliminary judgment: greater because of temporal and missing data | Preliminary judgment: potentially high |
| Potential software-system depth | Depends strongly on system design | Potentially substantial: temporal processing, inference, alerts and visualization | Potentially substantial |
| Schedule risk | Preliminary judgment: relatively lower | Preliminary judgment: moderate | Preliminary judgment: higher because access is restricted |
| Clear candidate dataset already identified | Partially — NHANES still requires target selection | Yes — PhysioNet Challenge 2019 | Yes, but restricted |
| Final supervisor approval required | Yes | Yes | Yes |

**Important:** this table is not evidence that one approach is clinically or scientifically superior to another.

---

## Current Preliminary Preference

At this stage, **Option B — Time-Series Monitoring and Early Warning** is the preliminary preferred direction.

This preference is based primarily on **project-design and Software Engineering considerations**, not on evidence that Option B is medically superior.

The candidate PhysioNet Challenge 2019 dataset already provides:

- temporal patient measurements;
- a defined early-prediction problem;
- a labelled outcome;
- openly downloadable training data;
- an official evaluation framework.

Official source:

https://physionet.org/content/challenge-2019/1.0.0/

This could support a software system consisting of:

1. ingestion of patient measurements over time;
2. input validation;
3. preprocessing and missing-value handling;
4. ML inference;
5. calculation of an early-warning or risk result;
6. alert logic;
7. visualization of measurements and results;
8. presentation of relevant information to a human reviewer.

This may provide greater Software Engineering depth than implementing only a static ML classifier.

However, this preference remains **preliminary** because:

- no user interviews or discussions have yet validated the problem;
- the literature review has not yet established whether this is the most appropriate research direction;
- baseline compatibility still needs to be verified;
- feasibility for one student still needs to be assessed;
- the supervisor has not yet approved the direction.

Therefore, Option B must **not** yet be described as the final project scope.

**Status:** DRAFT - requires supervisor approval.

---

## Preliminary Target User

A possible primary user is:

**Clinical staff or another healthcare professional responsible for reviewing patient health indicators.**

The proposed system would support the user by presenting analytical information derived from patient measurements.

The system would be treated as an **analytical or decision-support prototype**, not as an autonomous medical diagnostic system.

No real-user evidence has yet been collected to confirm this target-user definition.

**Status:** [DRAFT] [REQUIRES USER EVIDENCE] [REQUIRES SUPERVISOR APPROVAL]

---

## Preliminary System Output

Depending on the final project direction, the system may provide:

- a risk estimate or warning level;
- visualization of patient indicators;
- visualization of indicator changes over time;
- identification or explanation of factors contributing to an ML result, where technically appropriate;
- an analytical result for review by a human user.

The system will **not** be presented as:

- an autonomous diagnostic tool;
- a treatment-recommendation system;
- a clinically validated medical device.

**Status:** [DRAFT]

---

## Preliminary Scope Boundary

### In Scope

Potential scope currently includes:

- analysis of de-identified structured patient health data;
- use of an openly accessible or properly authorized dataset;
- preprocessing and validation of health-indicator data;
- machine-learning-based risk estimation or early warning;
- integration of an ML model into a software system;
- backend/API functionality;
- storage or management of application data where required;
- minimal web interface or dashboard;
- visualization of analytical results;
- evaluation of the ML approach using defined metrics;
- comparison against an appropriate and reproducible baseline;
- software testing.

### Out of Scope

The following are currently outside the intended diploma scope:

- autonomous medical diagnosis;
- prescribing or recommending treatment;
- replacing clinical judgement;
- production deployment in a hospital;
- use of identifiable real patient data without appropriate authorization;
- clinical validation as a medical device;
- integration with real hospital information systems;
- claims that the resulting model is safe for actual clinical use.

**Status:** DRAFT - requires supervisor approval.

---

## Open Decisions for Supervisor

The following questions should be discussed with the supervisor before the scope is finalized:

1. Should the project focus on general health-risk analysis or one specific clinical problem?
2. Is **time-series early warning / early sepsis prediction** an acceptable interpretation of the approved diploma topic?
3. Is it acceptable to base the project entirely on public and de-identified data?
4. Is the PhysioNet/Computing in Cardiology Challenge 2019 dataset an appropriate candidate for the project?
5. Who should be defined as the primary user of the system?
6. Is the proposed combination of data processing, ML, backend/API, monitoring logic, evaluation, and dashboard sufficient Software Engineering complexity?
7. Should Option A remain the safer alternative if Option B is considered too complex or too medically specific?
8. What level of medical-domain specificity is expected for the diploma project?
9. Since full NEWS2 cannot be reproduced with the Challenge 2019 variables, what baseline would you consider appropriate: a simple statistical model such as logistic regression, a scientifically justified partial NEWS2-style score, or another established early-warning method?
10. Should the final project remain a decision-support prototype rather than make any diagnostic claim?

---

## Verified Sources Used in This Draft

The following sources are currently used only to establish factual information about candidate datasets and the NEWS2 scoring system.

They do **not** yet constitute the full literature review.

### 1. PhysioNet / Computing in Cardiology Challenge 2019

**Dataset citation:**  
Reyna M, Josef C, Jeter R, Shashikumar S, Moody B, Westover MB, Sharma A, Nemati S, Clifford GD. *Early Prediction of Sepsis from Clinical Data: The PhysioNet/Computing in Cardiology Challenge 2019 (version 1.0.0).* PhysioNet, 2019.

**Dataset DOI:**  
10.13026/v64v-d857

**License:**  
Creative Commons Attribution 4.0 International (CC BY 4.0)

**Access:**  
Anyone may access the files subject to the license terms.

**Official source:**  
https://physionet.org/content/challenge-2019/1.0.0/

**Accessed:**  
10 October 2026

**Associated peer-reviewed publication:**  
Reyna MA, Josef CS, Jeter R, Shashikumar SP, Westover MB, Nemati S, Clifford GD, Sharma A. *Early Prediction of Sepsis From Clinical Data: The PhysioNet/Computing in Cardiology Challenge 2019.* Critical Care Medicine. 2020;48(2):210–217.

**DOI:**  
10.1097/CCM.0000000000004145

**Open full text:**  
Available through PubMed Central (PMCID: PMC6964870).
**Title:** Early Prediction of Sepsis from Clinical Data — The PhysioNet/Computing in Cardiology Challenge 2019

**Organization:** PhysioNet / Computing in Cardiology

**Purpose in this draft:**  
Used to verify the availability of the candidate dataset, temporal patient measurements, `SepsisLabel`, missing measurements, and the early-prediction task.

**Official source:**  
https://physionet.org/content/challenge-2019/1.0.0/

---

### 2. MIMIC-IV

**Organization:** PhysioNet / MIT Laboratory for Computational Physiology

**Purpose in this draft:**  
Used to verify that MIMIC-IV is a restricted-access dataset and requires credentialing, required training, and acceptance of a Data Use Agreement.

**Official source:**  
https://physionet.org/content/mimiciv/

---

### 3. National Early Warning Score 2 (NEWS2)

**Organization:** Royal College of Physicians

**Purpose in this draft:**  
Used to verify the physiological parameters used by NEWS2 and its consideration of supplemental oxygen.

**Official source:**  
https://www.rcp.ac.uk/resources/national-early-warning-score-news-2/

---

### 4. National Health and Nutrition Examination Survey (NHANES)

**Organization:** U.S. Centers for Disease Control and Prevention / National Center for Health Statistics

**Purpose in this draft:**  
Used to verify the availability of public-use NHANES health datasets and accompanying documentation.

**Official source:**  
https://www.cdc.gov/nchs/nhanes/