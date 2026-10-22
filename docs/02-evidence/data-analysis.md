# Data Analysis: PhysioNet/CinC Challenge 2019 Training Data

**Status:** done (DIP-9)  
**Last updated:** 21 Oct 2026  
**Reproduce:** `make eda` (or `python -m src.ml.eda --data-dir data/raw --out-dir docs/02-evidence`). Every number below comes from [`eda-summary.json`](eda-summary.json), produced by [`src/ml/eda.py`](../../src/ml/eda.py) on the full public training data (v1.0.0, 40,336 files). Only aggregate statistics leave `data/raw`.  
**Related:** [ML methodology](../05-technology/ml-methodology.md) · [requirements](../06-requirements.md) · [user evidence](user-evidence.md)

## 1. Why this analysis

The analysis serves two purposes:

1. **Evidence of relevance.** It checks, on real ICU data, the claims of the problem statement: the measurements are irregular and often missing, sepsis is present but rare, and hospitals differ.
2. **Input for the method.** It provides the facts the ML methodology depends on: class balance, cases that cannot be predicted early, variables to exclude, and the time limit for the "insufficient data" state (FR-11).

Variable and model decisions use **set A only**. Set B is the external test set, so its numbers are only reported, to explain later external results. They do not change the design.

## 2. Size and class balance

| | Set A | Set B | Both |
|---|---:|---:|---:|
| ICU stays | 20,336 | 20,000 | 40,336 |
| Patient-hours (rows) | 790,215 | 761,995 | 1,552,210 |
| Septic stays | 1,790 (8.80%) | 1,142 (5.71%) | 2,932 (7.27%) |
| Hours with `SepsisLabel` = 1 | 17,136 (2.17%) | 10,780 (1.42%) | 27,916 (1.80%) |
| Septic stays already positive at the first hour | 203 | 223 | 426 (14.5% of septic stays) |
| Stay length, median (IQR), hours | 39 (25–47) | 38 (23–47) | 38 (24–47) |
| Stay length, range, hours | 8–336 | 8–336 | 8–336 |
| Age, median (IQR), years | 64.7 (52.3–75.7) | 62.0 (50.0–72.0) | 63.1 (51.0–74.0) |
| `Gender` = 1 (male, per the dataset description) | 58.2% | 53.7% | 56.0% |
| Stays with both `Unit1` and `Unit2` missing | 46.8% | 30.5% | 38.7% |

**What follows from this:**

- Only 1.8% of hours are positive, so AUROC alone would look good even for a weak model. AUPRC is reported next to this prevalence. A random model has an AUPRC of about 0.022 on set-A hours.
- 426 septic stays (14.5%) are already positive in their first hour. They cannot be warned about in advance. As planned in the methodology (§3), they stay in hour-level metrics but are excluded from lead-time analysis.
- Set B has a lower share of septic stays than set A (5.7% vs 8.8%). This alone changes PPV and AUPRC on the external test, independently of the model.

## 3. When sepsis starts

For septic stays that are not positive at the first hour, the derived onset (first positive hour + 6 h) has a median of **43 h** after the first record (IQR 19–89 h, range 7–336 h). Figure: [onset-hour.png](figures/onset-hour.png).

In every septic stay the label is positive for **at most 10 hours** (median 10). The record of a septic patient therefore ends no later than about 3 hours after the derived onset: 6 h before onset plus up to 3 h after it. The data contain almost nothing after onset, so the task can only be early warning, not monitoring of sepsis that has already developed.

Septic and non-septic stays have similar median lengths, but septic stays vary much more:

| Stay length, hours | Median | IQR |
|---|---:|---:|
| Septic stays | 37.5 | 15–81 |
| Non-septic stays | 39 | 24–46 |

Figure: [stay-length.png](figures/stay-length.png). Septic stays are more often long: a quarter of them last more than 81 h, against 46 h for non-septic stays. Time in the ICU (`ICULOS`) may therefore carry a dataset-specific signal. This is checked when the model is trained (methodology §6).

## 4. Missing values

Figure: [missingness.png](figures/missingness.png). The table shows the share of hours without a measurement and the share of stays in which the variable is never measured.

| Variable | Hours missing, A | Hours missing, B | Stays never measured, A | Stays never measured, B |
|---|---:|---:|---:|---:|
| HR | 7.7% | 12.1% | 0.0% | 0.0% |
| MAP | 10.2% | 14.8% | 0.0% | 0.5% |
| O2Sat | 12.0% | 14.1% | 0.1% | 0.0% |
| SBP | 15.2% | 13.9% | 1.3% | 0.1% |
| Resp | 9.8% | 21.1% | 0.1% | 0.2% |
| DBP | 48.1% | 13.9% | 36.3% | 0.1% |
| Temp | 66.2% | 66.1% | 1.2% | 0.2% |
| Glucose | 87.8% | 77.8% | 2.0% | 5.9% |
| WBC | 92.5% | 94.7% | 3.1% | 10.0% |
| Lactate | 96.6% | 98.1% | 62.0% | 76.2% |
| BaseExcess | 89.6% | 99.8% | 37.8% | 97.2% |
| HCO3 | 92.0% | 99.8% | 2.6% | 97.9% |
| Chloride | 91.7% | 99.4% | 2.7% | 91.9% |
| FiO2 | 85.8% | 97.7% | 41.1% | 70.9% |
| TroponinI | 99.9% | 98.2% | 97.6% | 67.2% |
| Bilirubin_direct | 99.9% | 99.8% | 97.1% | 92.6% |
| EtCO2 | 100.0% | 92.4% | 100.0% | 83.9% |

All 34 measured variables, in both sets, are in `eda-summary.json` (`missing_hours_pct`, `never_measured_stays_pct`).

**What follows from this:**

- **The problem statement's claim is confirmed.** Vital signs are present in most hours (HR is missing in 7.7–12.1% of hours). Over both sets, each of the 26 laboratory values is missing in 83–99.8% of hours. Temperature is missing in about two thirds of hours.
- **Missingness must be modelled, not hidden.** This supports the missingness features and LightGBM's native missing-value handling (methodology §6, §7.3).
- **The two hospital systems record different things.** EtCO2 is never recorded in set A. BaseExcess, HCO3 and Chloride are almost never recorded in set B, although they are routine in set A. DBP is missing in 36% of set-A stays. A model trained on set A will meet a different pattern of missing values on set B. This is an expected cause of the external drop and will be reported as such. It is not corrected by using set B.

## 5. How often vital signs are measured

Hours between two consecutive measurements of the same variable, over all stays:

| Variable | Median | 90th percentile | 95th | 99th | Max |
|---|---:|---:|---:|---:|---:|
| HR | 1 | 1 | 2 | 3 | 28 |
| O2Sat | 1 | 1 | 2 | 4 | 44 |
| SBP | 1 | 1 | 2 | 3 | 116 |
| MAP | 1 | 1 | 2 | 3 | 45 |
| Resp | 1 | 1 | 2 | 4 | 64 |
| Temp | 2 | 5 | 6 | 9 | 114 |

The rule in FR-11 asks a different question: how long until *any* of the key vital signs (HR, O2Sat, Temp, SBP, MAP, Resp) is measured again? The answer: median 1 h, 95th percentile 1 h, 99th percentile 3 h, 99.9th percentile 6 h, maximum 28 h. Only **0.23%** of these gaps are longer than 4 hours.

**What follows from this:** in this data, a gap of more than 4 hours without any key vital sign is rare, so the prototype's 4-hour limit flags only unusual stays. The ICU resident in the user evidence (EV-02) considers data out of date when they are not updated every hour. A limit of 1–2 hours would flag stays much more often: up to 5% of gaps are longer than 1 hour. The default limit is decided after the meeting on 23 Oct; it stays configurable (FR-11).

## 6. Decisions taken from this analysis

| Decision | Basis | Where recorded |
|---|---|---|
| Exclude `EtCO2`, `TroponinI` and `Bilirubin_direct` from the model inputs | Never measured in more than 90% of set-A stays (100%, 97.6% and 97.1%). Re-checked on the training split in M1; any change is recorded. | Methodology §6 |
| Exclude `Unit1` and `Unit2` | Administrative ICU-unit identifiers (dataset description), missing in 46.8% of set-A stays | Methodology §6 |
| Keep the other variables with missingness features, even those rare in set B | Set B must not influence the design; the difference is reported as a cause of external results | Methodology §4, §6 |
| Report the 426 stays positive at the first hour separately | They cannot be predicted early | Methodology §3 |
| Show AUPRC next to the prevalence (2.17% of set-A hours) | Strong class imbalance | Methodology §9 |
| Check the influence of `ICULOS` (feature importance; a variant without it) | Stay length differs between septic and non-septic stays | Methodology §6 |
| Candidate default for the insufficient-data limit: 4 h (0.23% of gaps); alternative from user evidence: 1–2 h | Measurement-gap analysis, §5; EV-02 | Requirements FR-11, open points |

## 7. Limitations of this analysis

- It is descriptive. It does not show whether any variable predicts sepsis; that is the task of the model and its evaluation.
- "Missing" means "not recorded in this dataset". It does not say whether the measurement was taken at the bedside.
- The hidden third hospital system of the Challenge is not public and is not analysed.
- Set B was described here in aggregate. This does not affect the external test, because no design decision uses set-B values.
