# Machine-Learning Methodology

**Status:** draft for supervisor review (DIP-10)  
**Last updated:** 21 Oct 2026  
**Related:** [proposal](../01-proposal.md) · [literature matrix](../03-literature/literature-matrix.md) · [technology comparison](technology-comparison.md) · [verification plan](../09-verification.md) · [data analysis](../02-evidence/data-analysis.md)

This document fixes how the prediction task, data, models and evaluation are defined, and why. Literature references use the numbering of the literature matrix (#1–#12). Facts about the data come from the reproducible [data analysis](../02-evidence/data-analysis.md) (DIP-9), not from estimates.

## 1. Summary of decisions

| Decision | Choice | Main reason |
|---|---|---|
| Dataset | PhysioNet/CinC Challenge 2019, public training sets A and B (v1.0.0, CC BY 4.0) | Open, de-identified, hourly ICU time series with a defined sepsis label; two hospital systems allow an external test (#2) |
| Prediction unit | One prediction per patient-hour, using data up to and including that hour | Matches continuous monitoring and the Challenge setup (#2) |
| Target | `SepsisLabel` as provided (1 from 6 h before sepsis onset) | Gives a fixed, documented early-warning horizon; comparable with published work (#1, #2) |
| Split | Patient-level split of set A (train / validation / internal test), plus set B as an external test | Prevents patient leakage; measures performance drop at a new hospital system (#2, #6, #8) |
| Baselines | Partial SIRS rule and regularized logistic regression | A transparent clinical rule and a simple ML model as a floor (#3, #4, #5) |
| Main model | Gradient-boosted trees (LightGBM) | Strong on tabular data, handles missing values natively, fast on a laptop, explainable with SHAP (#3) |
| Metrics | AUROC + AUPRC, sensitivity/specificity/PPV at a fixed operating point, calibration, patient-level alert metrics, lead time | AUROC alone is insufficient for imbalanced, alert-based prediction (#1, #2, #6, #7) |
| Success rule | Main model's AUPRC on the internal test set is higher than the logistic-regression baseline, with the 95% bootstrap CI of the difference excluding 0 | A measurable, honest comparison under one protocol |

## 2. Data

**Source.** *Early Prediction of Sepsis from Clinical Data: the PhysioNet/Computing in Cardiology Challenge 2019*, v1.0.0, DOI 10.13026/v64v-d857, Creative Commons Attribution 4.0 licence.

**Content (from the dataset page).**

- 40,336 ICU stays: 20,336 in training set A and 20,000 in training set B, from two different hospital systems. The third hospital system was used only for hidden Challenge scoring and is not public.
- One pipe-separated file per stay, one row per hour, missing values recorded as NaN.
- 40 variables + label:
  - 8 vital signs: `HR`, `O2Sat`, `Temp`, `SBP`, `MAP`, `DBP`, `Resp`, `EtCO2`;
  - 26 laboratory values: `BaseExcess`, `HCO3`, `FiO2`, `pH`, `PaCO2`, `SaO2`, `AST`, `BUN`, `Alkalinephos`, `Calcium`, `Chloride`, `Creatinine`, `Bilirubin_direct`, `Glucose`, `Lactate`, `Magnesium`, `Phosphate`, `Potassium`, `Bilirubin_total`, `TroponinI`, `Hct`, `Hgb`, `PTT`, `WBC`, `Fibrinogen`, `Platelets`;
  - 6 demographic/administrative variables: `Age`, `Gender`, `Unit1`, `Unit2`, `HospAdmTime`, `ICULOS`;
  - `SepsisLabel`.

**Facts from my analysis** ([data analysis](../02-evidence/data-analysis.md)): 2,932 of 40,336 stays are septic (7.27%; set A 8.80%, set B 5.71%); 1.80% of hours have `SepsisLabel` = 1; stays last a median of 38 h (range 8–336 h). Vital signs are present in most hours, while each laboratory value is missing in 83–99.8% of hours. The two hospital systems record different laboratory values: for example, BaseExcess and HCO3 are almost never recorded in set B, and EtCO2 is never recorded in set A.

**What the data cannot give.** There is no Glasgow Coma Scale or AVPU, so qSOFA and NEWS2 cannot be computed completely. There are no free-text notes, medications or interventions. The data are retrospective and come from US ICUs.

## 3. Prediction task and label

**Task.** For every patient-hour *t*, estimate the probability that `SepsisLabel` at *t* equals 1, using only data recorded at hours ≤ *t*.

**Label definition (from the dataset page).** Sepsis follows Sepsis-3. Onset `t_sepsis` is the earlier of `t_suspicion` (clinical suspicion of infection: the earlier of IV antibiotics and blood cultures, under the dataset's time-window rules) and `t_SOFA` (a SOFA increase of ≥ 2 points within 24 hours), provided that `t_SOFA` lies no more than 24 h before or 12 h after `t_suspicion`; otherwise the stay is not labelled as septic. `SepsisLabel = 1` for `t ≥ t_sepsis − 6` and 0 before; it is 0 for every hour of non-sepsis stays.

**My decision.** Use `SepsisLabel` as provided. Predicting it means raising a warning from about 6 hours before onset. I do not relabel to a different horizon because (a) the 6-hour shift is already defined and documented by the data owners, (b) results stay comparable with work on this dataset, and (c) a self-made horizon would add one more undocumented choice (#1 criticises exactly this heterogeneity).

**Derived onset.** For a septic stay, onset is reconstructed as *first hour with label 1* + 6 h. It is used only for patient-level evaluation (lead time), never as a model input.

**Special case.** Stays whose label is already 1 in the first hour cannot be predicted early. They stay in hour-level metrics but are reported separately and excluded from lead-time analysis. There are 426 such stays (203 in set A, 223 in set B; 14.5% of septic stays).

## 4. Data split

| Set | Content | Used for |
|---|---|---|
| Train | 70% of set-A patients | Fitting preprocessing and models |
| Validation | 15% of set-A patients | Hyper-parameters, early stopping, threshold choice |
| Internal test | 15% of set-A patients | Final internal result, used once |
| External test | All of set B | Performance at a different hospital system, used once |

- The split is by patient: all hours of a stay are in the same set.
- The split is stratified by whether the stay is septic, with a fixed seed (`RANDOM_SEED=42`).
- Set B is never used for fitting, tuning or threshold selection. The external result is therefore a genuine measure of transfer, which the literature shows is often much worse than internal results (#2, #6, #8: internal AUC 0.846 → external 0.761 in #8).

## 5. Leakage rules

1. Features for hour *t* use rows with `ICULOS ≤ t` only.
2. Missing values are filled forward inside one patient only; no backward filling and no interpolation that uses later values.
3. Imputation medians, scaling parameters and any variable selection are learned on the training set only.
4. No patient appears in more than one set.
5. A unit test checks rule 1: appending future hours to a patient must not change the features of earlier hours (see verification plan).

## 6. Features

| Group | Features | Why |
|---|---|---|
| Last observed value | Forward-filled value of every retained variable | Clinicians act on the latest known value |
| Missingness | Measured-this-hour flag; hours since last measurement; number of measurements so far (labs) | Ordering a test is itself informative; missingness is not random |
| Short-term dynamics | For `HR`, `O2Sat`, `Temp`, `SBP`, `MAP`, `Resp`: mean, min, max and standard deviation over the last 6 h and 12 h; change versus 6 h ago | Deterioration shows as trends, not single values |
| Context | `Age`, `Gender`, `HospAdmTime`, `ICULOS` | Baseline risk and time in ICU |

**Excluded variables** (decided on set A only; [data analysis](../02-evidence/data-analysis.md) §6): `EtCO2`, `TroponinI` and `Bilirubin_direct`, which are never measured in more than 90% of set-A stays, and the administrative unit identifiers `Unit1`/`Unit2`, missing in 46.8% of set-A stays. The rule is re-applied to the training split in M1, and any change is recorded here. All other variables are kept with missingness features, including those that are rare in set B: set B does not influence the design.

**`ICULOS` check.** Septic stays are more often long than non-septic stays (upper quartile 81 h vs 46 h), so `ICULOS` may carry a dataset-specific signal. Its feature importance is reported, together with a LightGBM variant trained without it.

## 7. Models

### 7.1 Baseline 1: partial SIRS rule

Score = number of criteria met on the last observed values:

- `Temp` > 38 °C or < 36 °C;
- `HR` > 90 /min;
- `Resp` > 20 /min or `PaCO2` < 32 mmHg;
- `WBC` > 12 or < 4 (×10⁹/L).

The score (0–4) is used as a continuous risk for AUROC/AUPRC; score ≥ 2 is the alert rule. It is called *partial* because the band-neutrophil part of the WBC criterion is not available.

*Why this rule:* it is a recognised, transparent clinical rule whose inputs all exist in the dataset. qSOFA and NEWS2 need mental status, which the dataset does not contain, so they cannot be reproduced fairly.

### 7.2 Baseline 2: regularized logistic regression

L2-regularized logistic regression on the same features as the main model, with training-set median imputation plus missingness flags and standardization. The regularization strength is tuned on the validation set.

*Why:* it is the simplest reproducible ML model and an honest floor. #3 shows that a logistic model does not automatically beat an established score, so the comparison is informative in both directions.

### 7.3 Main model: LightGBM

Gradient-boosted decision trees (LightGBM). Missing values are handled natively. A small search over `num_leaves`, `learning_rate` and `min_child_samples`, with early stopping on validation AUPRC. Fixed seeds.

*Why:*

- the input is tabular hourly data with engineered temporal features, where boosted trees are a strong standard choice (#3: XGBoost 0.778 vs NEWS 0.682 AUROC);
- native missing-value handling suits the heavily missing laboratory data;
- training takes minutes on a laptop, which keeps experiments reproducible within the diploma;
- per-prediction explanations with SHAP support the explanation requirement (FR-10).

### 7.4 Out of scope for now

A recurrent model (GRU/LSTM) works on raw sequences and is widely studied (#1), but it needs more tuning, is harder to explain and test, and adds risk to an individual project. It is kept as an optional extension, to be added only after the main pipeline and evaluation are complete.

## 8. Operating point and alert logic

- **Threshold.** Chosen on the validation set as the highest risk value at which hour-level sensitivity is still ≥ 0.80. A lower threshold would raise sensitivity further, at the cost of more false alerts. PPV at 80% sensitivity is also how #8 reports results, which makes the numbers comparable.
- **Alert.** An alert fires when the risk crosses the threshold. A new alert for the same patient is suppressed for *N* hours (default 6, configurable). This follows the threshold and suppression strategies reported in #10 and addresses the alert burden shown in #6.
- **Insufficient data.** If none of the key vital signs (`HR`, `O2Sat`, `Temp`, `SBP`, `MAP`, `Resp`) has been measured for more than *X* hours, the system shows "insufficient data" instead of a risk value. *X* is configurable; the data analysis gives a candidate of 4 h (only 0.23% of gaps between key vital-sign measurements are longer), and the default is decided after the meeting on 23 Oct. This adapts the idea of an indeterminate output from #7.

## 9. Evaluation

### 9.1 Metrics

| Level | Metric | Why |
|---|---|---|
| Hour | AUROC | Standard discrimination measure, comparable with literature |
| Hour | AUPRC, shown next to the positive-class prevalence | Informative under strong class imbalance (#1) |
| Hour | Sensitivity, specificity, PPV and F1 at the operating point | What an alert threshold means in practice |
| Hour | Brier score and calibration curve | Whether a risk of 0.3 actually means about 30% (#6) |
| Patient | Share of septic stays alerted before onset; median lead time (h) | Early warning is the purpose (#2, #8) |
| Patient | Share of non-septic stays with at least one alert; alerts per patient-day | Alert burden and alarm fatigue (#6, #7, #10) |
| Optional | Official Challenge utility score on my test sets | Timing-aware score; clearly not comparable with the hidden-set leaderboard (#2) |

### 9.2 Uncertainty and comparison

- 95% confidence intervals by patient-level bootstrap (1,000 resamples of patients, not hours).
- Model comparisons use the paired bootstrap difference on the same resamples.
- Every model is evaluated on exactly the same patients, features and rules.

### 9.3 Success criterion

1. **Primary:** LightGBM has higher AUPRC than logistic regression on the internal test set, and the 95% CI of the paired difference excludes 0.
2. **Reported regardless of outcome:** the comparison with partial SIRS, the internal → external drop for every model, and the patient-level alert metrics.
3. If the primary criterion is not met, that is reported as the result. The software contribution (reproducible pipeline, API, dashboard, tests) does not depend on the model winning.

## 10. Reproducibility

- Dataset version 1.0.0; the split is saved as lists of patient IDs.
- One configuration file holds the seed, feature settings, hyper-parameters, threshold and suppression window.
- Each trained model is saved with a metadata file: model type, library versions, configuration hash, training date and validation metrics.
- `make train` and `make evaluate` rebuild every number in the report.

## 11. Limitations

- The original hidden test set (third hospital system) is not public, so results are not comparable with the Challenge leaderboard.
- The label is derived algorithmically from records (Sepsis-3), so label timing has its own error.
- ICU data from US hospitals only; no claim is made about other settings or countries.
- Forward filling assumes a value stays valid until the next measurement.
- Retrospective evaluation only; no clinical validation and no claim of patient benefit (#9–#12 show that outcome benefit depends on the whole workflow, not the model alone).

## 12. Questions for the supervisor

1. Are partial SIRS and logistic regression an acceptable pair of baselines?
2. Should the official Challenge utility score be part of the required evaluation, or stay optional?
3. Is it acceptable to keep the recurrent model (GRU/LSTM) explicitly out of the core scope?
