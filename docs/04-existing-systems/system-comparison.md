# Existing System Comparison

**Status:** revised for pre-defense 1 (DIP-18); architectures added in a separate document on 23 Oct 2026 (DIP-28)  
**Last updated:** 23 Oct 2026  
**Related:** [how the systems are built](system-architectures.md) · [literature matrix](../03-literature/literature-matrix.md)

## 1. What I compared and why

I compared existing systems that are close to what I want to build: software that watches repeated patient measurements and warns clinicians about sepsis or deterioration. I chose five systems that have peer-reviewed evaluations and used the same nine criteria for each.

Systems included:

1. Epic Sepsis Model (ESM)
2. Epic Deterioration Index (EDI)
3. COMPOSER
4. CHARTwatch
5. TREWS

Not counted as systems, but used elsewhere in the project:

- **NEWS2** is a rule-based score, not a software system. Full NEWS2 cannot be computed from my dataset (no consciousness level), so it is not used as a baseline.
- **eCART and the Rothman Index** appear in Edelson et al. (2024) as AI scores compared with NEWS. They were left out to keep the comparison to five systems with the most detailed evidence.
- **Open-source Challenge 2019 entries.** After the PhysioNet/CinC Challenge 2019 all participant software was posted publicly (91 archives on the [dataset page](https://physionet.org/content/challenge-2019/1.0.0/sources/)). This is research code for the prediction task, not a system with users, alerts and an interface, so it is discussed in §4 rather than compared as a system.

**Sources and their strength.** Source IDs `LIT-#` refer to the [literature matrix](../03-literature/literature-matrix.md), whose full texts I reviewed. `S-#` are other peer-reviewed sources listed in §5, used through their abstracts or published summaries. Press articles are not used as evidence. Where a source does not report something, the cell says "not reported".

How four of these systems are built — where the data come from, where the model runs and how the alert reaches the staff — is described in [system-architectures.md](system-architectures.md), with a reconstructed architecture diagram for each.

## 2. Comparison table

| Criterion | Epic Sepsis Model | Epic Deterioration Index | COMPOSER | CHARTwatch | TREWS |
|---|---|---|---|---|---|
| **C1. Clinical problem** | Early sepsis prediction in hospitalized patients [LIT-6] | Clinical deterioration: rapid-response activation, ICU transfer, cardiopulmonary arrest [LIT-12] | Early sepsis (Sepsis-3) prediction [LIT-7] | Deterioration of general internal medicine patients: death or ICU transfer [LIT-11, S-2] | Sepsis early warning [S-1] |
| **C2. Setting and users** | Hospitalized adults at one academic centre (validation site); alert recipients not reported [LIT-6] | Four general medicine units; alerts go to a nurse and a physician, followed by a structured huddle [LIT-12]; medical-surgical wards at 7 hospitals in a comparison study [LIT-5] | ICU and emergency department cohorts [LIT-7]; deployed in two emergency departments, alerts to nurses [LIT-9] | General internal medicine ward of one teaching hospital; clinicians are notified of high-risk patients [LIT-11] | Five hospitals (two academic, three community); providers confirm the alert in the health record [S-1, S-3] |
| **C3. Input data** | Routine health-record data; variable list not reported [LIT-6] | 31 health-record measures [LIT-12] | Routine clinical variables from the health record, real-time feed in deployment [LIT-7, LIT-9]; full list not reported in the sources reviewed | Laboratory values, vital signs and other health-record data [LIT-11, S-2]; exact count not reported in the sources reviewed | Health-record data; specific inputs not reported in the abstract [S-1] |
| **C4. Prediction method** | Proprietary penalized logistic regression [LIT-6] | Ordinal logistic regression [LIT-12] | Deep model with representation learning and a conformal-prediction layer that can output "indeterminate" [LIT-7] | Time-aware multivariate adaptive regression splines (MARS) [LIT-11] | Machine-learning model; type not reported in the abstract [S-1] |
| **C5. Real-time operation and alerts** | Score threshold 6 evaluated; update frequency not reported [LIT-6] | Score every 15 minutes; alert at threshold 65 with a defined nurse–physician response [LIT-12] | Hourly predictions; cloud platform with health-record data feed and a nurse-facing alert inside the health record [LIT-9] | Real-time risk levels (high/medium/low), alerts with silencing, and a care pathway for high-risk patients [LIT-11] | Alert in the health record that a provider can confirm [S-1] |
| **C6. Explanation of the output** | Not reported [LIT-6] | Not reported [LIT-12] | Marks unfamiliar inputs as "indeterminate"; deployed alert shows the top contributing features [LIT-7, LIT-9] | Not reported in the sources reviewed | Not reported in the abstract [S-1] |
| **C7. Evidence of validation or deployment** | External validation, 38,455 hospitalizations: AUC 0.63; sensitivity 33%, PPV 12% at threshold 6 [LIT-6] | AUROC 0.808 vs NEWS 0.829 in 362,926 encounters at 7 hospitals [LIT-5]; regression-discontinuity study of 9,938 patients: −10.4 percentage points in the composite outcome at the threshold [LIT-12] | 515,720 patients in six cohorts; AUC 0.925–0.953 (ICU) and 0.938–0.945 (ED) [LIT-7]; deployment in 6,217 septic patients: mortality 1.9 points (17% relative) lower than expected [LIT-9] | Nonrandomized controlled study: non-palliative death 2.1% before vs 1.6% during the intervention, adjusted RR 0.74 (0.55–1.00) [LIT-11] | Prospective multi-site study: 590,736 patients monitored; confirmation of the alert within 3 hours associated with 3.3 points lower adjusted mortality [S-1] |
| **C8. Transparency and access** | Proprietary (Epic) [LIT-6] | Proprietary (Epic) [LIT-12] | Method described in peer-reviewed papers; code availability not reported in the sources reviewed [LIT-7] | In-house hospital system with published methods [LIT-11, S-2] | Commercial product; details limited in the abstract [S-1] |
| **C9. Limitations reported or visible** | Missed 67% of sepsis cases; alerts in 18% of hospitalizations; one centre [LIT-6] | Lower AUROC than NEWS in one large comparison [LIT-5]; effect measured only near the threshold at one centre [LIT-12] | Retrospective development [LIT-7]; deployment nonrandomized, two EDs of one health system, short follow-up [LIT-9] | Nonrandomized; possible unmeasured confounding; the model and pipeline changed after the study window [LIT-11] | Observational: benefit linked to provider response within 3 hours, which does not prove that the alert caused it (my interpretation) [S-1] |

## 3. What I notice (my interpretation)

- Most systems use ordinary statistical or machine-learning models (logistic regression, MARS). What differs is the surrounding system: thresholds, alert recipients, response pathways and monitoring (EDI, CHARTwatch, COMPOSER deployment).
- The strongest evidence exists where the developers also describe the workflow. The evidence for the proprietary Epic sepsis model is mostly independent external validation, and it is weak (AUC 0.63).
- Explanation of the output (C6) is the least reported criterion. COMPOSER is the only system with documented uncertainty handling ("indeterminate") and displayed contributing features.
- Alert burden is a recurring problem: the Epic sepsis model alerted in 18% of hospitalizations while missing two thirds of sepsis cases.

## 4. Why the proposed diploma solution is still needed

My project does not try to beat these systems. They are hospital-integrated, often proprietary, and evaluated on data I cannot access. The need I see is narrower.

- **Open systems vs open models.** The deployed systems above are proprietary or in-house; I could not confirm public code for any of them. On the other hand, open research code exists: the Challenge 2019 entries were published. That code covers model training and scoring for the Challenge, not a system that a user works with. The gap is therefore not "no open sepsis model" but **no open, tested system** that combines leakage-safe processing, an API, alert logic with suppression and data-quality states, explanations, and a user interface.
- **A fair comparison on shared ground.** Results are hard to compare and often drop at a new hospital (LIT-1, LIT-6, LIT-8). An open pipeline that evaluates the model and two baselines on the same patients, internally and on a second hospital system, makes that comparison visible.
- **Alert behaviour as a first-class result.** False alarms and workflow decide usefulness (LIT-6, LIT-10). My prototype reports PPV, alerts per patient-day and lead time next to AUROC.
- **A Software Engineering contribution.** Deployment papers describe pipelines, interfaces and monitoring only briefly (LIT-9, LIT-10). A small, tested, documented system that shows these parts is a reasonable diploma outcome.

Limits: the prototype uses public de-identified data, is not clinically validated, and makes no claim of better outcomes than these systems. Whether the need is real for users is checked in the user discussions ([evidence](../02-evidence/evidence-plan.md)).

## 5. Sources

Literature-matrix sources (full texts reviewed): LIT-5 Edelson et al. 2024; LIT-6 Wong et al. 2021; LIT-7 Shashikumar et al. 2021; LIT-9 Boussina et al. 2024; LIT-11 Verma et al. 2024; LIT-12 Gallo et al. 2024. Full citations and DOIs are in the [literature matrix](../03-literature/literature-matrix.md).

Other peer-reviewed sources:

- [S-1] Adams R, et al. *Prospective, multi-site study of patient outcomes after implementation of the TREWS machine learning-based early warning system for sepsis.* Nature Medicine. 2022;28(7):1455–1460. DOI 10.1038/s41591-022-01894-0. Used through the abstract ([PubMed 35864252](https://pubmed.ncbi.nlm.nih.gov/35864252/)).
- [S-2] Pou-Prom C, et al. *From compute to care: Lessons learned from deploying an early warning system into clinical practice.* Frontiers in Digital Health. 2022. DOI 10.3389/fdgth.2022.932123. ([PMC9483018](https://pmc.ncbi.nlm.nih.gov/articles/PMC9483018))
- [S-3] Commentary on Adams et al. describing the hospital setting ([PMC9512693](https://pmc.ncbi.nlm.nih.gov/articles/PMC9512693)).

Other resources:

- PhysioNet/CinC Challenge 2019 — published participant software: https://physionet.org/content/challenge-2019/1.0.0/sources/

## 6. Changes in this revision

| Change | Reason |
|---|---|
| Source IDs aligned with the literature matrix (`LIT-#`) | One numbering across documents; the earlier list had duplicate numbers and a missing S7 |
| EDI, COMPOSER and CHARTwatch cells filled from the full texts in the literature matrix | These details were available in the reviewed full texts |
| Press sources removed from the table | Only peer-reviewed sources are used as evidence |
| CHARTwatch "aged 55–80" removed | It is the interquartile range of age, not an inclusion criterion (literature matrix, §9) |
| TREWS FDA-status claim removed | Only a press source supported it |
| Open-source Challenge 2019 entries added to §1 and §4 | The gap is stated precisely: open research code exists, an open tested system does not |
| Remaining unknowns written as "not reported" | Details missing from the sources are not filled in by assumption |
