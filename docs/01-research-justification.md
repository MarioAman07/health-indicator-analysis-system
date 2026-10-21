# Research Justification: Early Sepsis-Risk Prediction from ICU Measurements

**Prepared for:** meeting with the supervisor on 23 Oct 2026 (feedback log FB-12)  
**Author:** Aman Baku, SE-2422  
**Last updated:** 21 Oct 2026  
**Related:** [proposal](01-proposal.md) · [ADR-001](decisions/ADR-001-scope.md) · [literature matrix](03-literature/literature-matrix.md) · [ML methodology](05-technology/ml-methodology.md)

## 1. Summary

The topic agreed with the supervisor is the analysis of patient health indicators with machine learning (the official decision on the topic is expected after the pre-defense). I propose to study it on one concrete, measurable problem: **predicting sepsis about six hours before onset from the hourly vital signs and laboratory values of ICU patients**. Sepsis is common and deadly, its early signs appear in exactly these indicators, international guidelines call for systematic screening, and published machine-learning work shows both promise and open problems that a Software Engineering project can address on open data.

## 2. How the focus fits the agreed topic

| Words of the agreed topic | How the project realises them |
|---|---|
| *Patient health indicators* | 8 vital signs, 26 laboratory values and 6 demographic variables, arranged in one row per ICU hour; an hour without a measurement is recorded as missing |
| *Analyzing* | Trends, missingness and short-term changes of these indicators, turned into an hourly risk estimate with explanations |
| *Machine learning-based* | Gradient-boosted trees compared with a clinical rule and logistic regression under one evaluation protocol |
| *System* | Validation, feature pipeline, REST API, alert logic, dashboard and automated tests — not a single notebook |

## 3. Why sepsis

1. **Burden.** WHO reports 48.9 million sepsis cases and 11 million sepsis-related deaths worldwide, which is 20% of all global deaths (data published in 2020 [R2]); for every 1,000 hospitalized patients, an estimated 15 develop sepsis as a complication of receiving health care [R1].
2. **Time matters.** WHO states that treatment for sepsis is most effective when started early, and that early diagnosis and timely clinical management are crucial to increase the likelihood of survival [R1]. The 2021 Surviving Sepsis Campaign guidelines strongly recommend that hospitals run sepsis screening programmes (moderate-quality evidence) [R3].
3. **Simple screening tools are imperfect.** The same guidelines recommend against using qSOFA alone as a screening tool compared with SIRS, NEWS or MEWS, and note that machine learning may improve the performance of screening tools [R3]. This is why the project compares a machine-learning model with a simple rule instead of assuming that either is better.
4. **The signal lives in the indicators.** Sepsis-3 defines sepsis as life-threatening organ dysfunction caused by infection and identifies that dysfunction with the SOFA score, which is built largely from routine laboratory values and vital signs [R4]. Heart rate, temperature, respiratory rate, blood pressure, oxygenation and lab trends are exactly the indicators the system analyses.
5. **Local relevance.** I did not find a national estimate of sepsis incidence for Kazakhstan. A study in a 12-bed ICU in Astana describes hospital-associated infections there, including bloodstream infections and ventilator-associated pneumonia — infections that can lead to sepsis [R5]. Whether early warning is seen as useful by clinicians here is checked in the survey and discussions (DIP-4).

## 4. What research already shows

| Finding | Sources |
|---|---|
| Machine-learning models can predict sepsis hours before onset, but study designs, horizons and metrics differ so much that results are hard to compare | Literature #1, #4 |
| Models lose performance at a new hospital: in a multinational study (#8) the mean internal AUROC of 0.846 fell to 0.761 at external sites | #2, #6, #8 |
| AUROC alone hides the practical cost: a widely used commercial model missed 67% of sepsis cases and alerted in 18% of hospitalizations | #6 |
| Machine learning does not automatically beat simple scores; a logistic model can even fall below NEWS | #3, #4, #5 |
| Benefit in real hospitals comes from the whole package — model, threshold, alert and human response — not from the model alone | #9 – #12 |

## 5. Research gap

Research code for this exact prediction task exists — the PhysioNet/CinC Challenge 2019 published its entries — and several hospital systems are deployed, but they are proprietary or in-house. What is missing is an **open, tested system** that (a) evaluates a model honestly against transparent baselines, internally and on a second hospital system, (b) reports alert behaviour, not only discrimination, and (c) presents each warning with its reasons and with an explicit "insufficient data" state. This project fills that gap at diploma scale.

## 6. Research questions and hypotheses

| | Question | Hypothesis | How it is tested |
|---|---|---|---|
| **RQ1** | How well can a gradient-boosted model using only measurements recorded up to the current hour predict Sepsis-3 onset about six hours in advance, compared with a partial SIRS rule and logistic regression? | **H1:** LightGBM achieves a higher AUPRC than logistic regression on the internal test set (95% CI of the paired difference excludes 0). | Internal test on held-out patients of set A |
| **RQ2** | How much does performance change when the model is applied to patients from a different hospital system? | **H2:** All models lose performance on set B; the size of the drop is reported for each model. | External test on set B, never used for training or tuning |
| **RQ3** | Can the prediction be delivered as a decision-support system that potential users interpret correctly? | **H3:** At least two of three respondents correctly explain from the patient screen why the risk is high. | User check of the prototype and later the real dashboard |

## 7. Why this data and why it is feasible

- **Open and ethical:** PhysioNet/CinC Challenge 2019 public training data, de-identified, CC BY 4.0 licence; no access procedure, no patient contact.
- **Defined label:** sepsis onset follows Sepsis-3; the label turns positive six hours before onset, which fixes the prediction horizon.
- **External test possible:** 40,336 ICU stays from two hospital systems (sets A and B).
- **Fits one developer:** tabular hourly data, CPU-only training, Python stack; implementation milestones are planned until spring 2027.

## 8. Expected contribution

1. **Evaluation contribution:** a reproducible comparison of a machine-learning model with two transparent baselines, including cross-hospital performance and alert burden.
2. **Engineering contribution:** an open, tested reference system — validation, leakage-safe features, API, alert logic, explanations, dashboard.
3. **User-centred contribution:** presentation choices (trends next to risk, reasons, insufficient-data state, alert suppression) grounded in the literature and checked with people who have clinical experience.

## 9. Limitations and ethics

- Retrospective data from US ICUs; results are not claimed to transfer to Kazakh hospitals without local data.
- The label is derived from records, so onset timing has its own error.
- The prototype is decision support for research and teaching; it is not a medical device and makes no claim of clinical benefit.
- User evidence is anonymous; no patient information is collected.

## 10. Alternatives considered

A general risk model on single-visit survey data (NHANES) and an ICU project on MIMIC-IV were also considered. The first lacked a defined target and temporal depth; the second needs credentialed access that would delay the work. Details: [ADR-001](decisions/ADR-001-scope.md).

## 11. What I ask the supervisor to confirm on 23 Oct

1. Early sepsis-risk prediction from ICU measurements is accepted as the concrete focus of the agreed topic (Q-01).
2. RQ1–RQ3 are accepted as the research part of the diploma.
3. The anonymous survey with follow-up questions, together with the analysis of the PhysioNet data, is accepted as relevance evidence (Q-03).
4. Whether the survey and the short discussions need any ethics or university approval.

## References

- [R1] World Health Organization. *Sepsis* — fact sheet, 3 May 2024. https://www.who.int/news-room/fact-sheets/detail/sepsis
- [R2] Rudd KE, Johnson SC, Agesa KM, et al. Global, regional, and national sepsis incidence and mortality, 1990–2017: analysis for the Global Burden of Disease Study. *The Lancet*. 2020;395(10219):200–211. PMID 31954465
- [R3] Evans L, Rhodes A, Alhazzani W, et al. Surviving Sepsis Campaign: international guidelines for management of sepsis and septic shock 2021. *Intensive Care Medicine*. 2021;47:1181–1247. DOI 10.1007/s00134-021-06506-y
- [R4] Singer M, et al. The Third International Consensus Definitions for Sepsis and Septic Shock (Sepsis-3). *JAMA*. 2016;315(8):801–810.
- [R5] Viderman D, Khamzina Y, Kaligozhin Z, Khudaibergenova M, Zhumadilov A. An observational case study of hospital associated infections in a critical care unit in Astana, Kazakhstan. *Antimicrobial Resistance and Infection Control*. 2018. DOI 10.1186/s13756-018-0350-0
- Literature #1 – #12: see the [literature matrix](03-literature/literature-matrix.md).
