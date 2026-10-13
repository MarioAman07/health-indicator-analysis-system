# Existing System Comparison

**Status:** DRAFT. Not yet reviewed by my supervisor.
**Last updated:** 13 Oct 2026

## 1. What I compared and why

I looked for existing systems that are close to what I want to build: software that watches repeated patient measurements and warns clinicians about sepsis or deterioration. I chose five that have peer-reviewed evaluations. For each one I use the same nine criteria.

Systems included:

1. Epic Sepsis Model (ESM)
2. Epic Deterioration Index (EDI)
3. COMPOSER
4. CHARTwatch
5. TREWS

Not counted as systems, but used elsewhere in the project:

- **NEWS2** (Royal College of Physicians) is a rule-based score, not a software system. I plan to use a NEWS-style score as a possible baseline, not as a compared system.
- **eCART and Rothman Index** appear in Edelson et al. (2024) as AI scores that were compared with NEWS. I did not add them to keep the comparison to five systems.

Limits of this comparison:

- Two of the five are proprietary Epic tools. I did not find or open vendor documentation. What I know about them comes from peer-reviewed studies by independent or university groups.
- I used abstracts and indexed article text. I did not read full texts for this file. Details I could not find are marked "not found" or [MUST VERIFY]. A few facts come from press articles; they are marked "press".
- Source IDs like [S1] point to the list in Section 5.

## 2. Comparison table

| Criterion | Epic Sepsis Model | Epic Deterioration Index | COMPOSER | CHARTwatch | TREWS |
|---|---|---|---|---|---|
| **C1. Clinical problem** | Early sepsis prediction in hospitalized patients [S1] | Clinical deterioration: rapid-response activation, ICU transfer, cardiopulmonary arrest or death [S3b] | Early sepsis (Sepsis-3) prediction, 4–48 h before clinical suspicion [S4] | Deterioration, defined as in-hospital death or ICU transfer [S9] | Sepsis early warning [S6] |
| **C2. Setting and users** | Hospitalized patients at an academic centre (the validation site). Who receives the alert: not found [S1] | Inpatient wards. In one study, alerts went to a nurse and a physician within a shared workflow [S3, S3b]. Another study used medical-surgical ward encounters at 7 hospitals [S2] | ICU and emergency department cohorts [S4]. Deployed in two emergency departments of one health system [S5] | General internal medicine ward at one teaching hospital. Risk scores reach physicians and nurses [S9] | Five hospitals (two academic, three community). Providers can confirm the alert in the health record [S6, S6c] |
| **C3. Input data** | Routine health-record data. Variable list not found [S1] | 31 health-record measures (per a summary of Gallo et al.) [S3b] | Routine clinical variables from the health record, real-time feed in deployment [S4, S5]. Exact list [MUST VERIFY] | Labs, vitals and other health-record data [S9]. "Over 100 variables" is from a podcast with the lead author (press) [N3]. [MUST VERIFY] | Health-record data. Specific inputs [MUST VERIFY] [S6] |
| **C4. Prediction method** | Proprietary penalized logistic regression [S1] | Ordinal logistic regression [S3b] | Deep learning with a conformal-prediction layer that can output "indeterminate" [S4] | "Time-aware" MARS model, chosen after trying logistic regression, Lasso, generalized additive models and neural networks. Training and validation split by calendar date [S9] | Machine-learning model. Model type [MUST VERIFY] [S6] |
| **C5. Real-time operation and alerts** | Alert model, evaluated at a score threshold of 6. Update frequency not found [S1] | Score calculated every 15 minutes (per a summary). Alert at a score threshold, plus a defined nurse–physician workflow [S3, S3b] | Hourly sequential prediction in the study [S4]. Real-time health-record data in deployment [S5]. Alert recipients and format [MUST VERIFY] | Real-time risk scores, clinical alerts and a care pathway for high-risk patients [S8]. Press adds twice-daily alert emails to nursing teams [N1] | Alert in the health record that a provider can confirm. High-risk flag [S6] |
| **C6. Explanation of the output** | Not found in the sources I opened [MUST VERIFY] | Not found [MUST VERIFY] | Marks unfamiliar inputs as "indeterminate" instead of forcing a prediction [S4]. Display of contributing variables [MUST VERIFY] | Not found [MUST VERIFY] | Not found [MUST VERIFY] |
| **C7. Evidence of validation or deployment** | External validation at one hospital, 38,455 hospitalizations: AUC 0.63, sensitivity 33% and PPV 12% at threshold 6 [S1] | AUROC 0.808 versus NEWS 0.829 in 362,926 encounters at 7 hospitals [S2]. Regression-discontinuity study (9,938 patients): 10.4 percentage points lower risk of care escalation [S3] | Six cohorts, 515,720 patients, internal, temporal and external validation, AUC 0.925–0.953 (ICU) and 0.938–0.945 (ED) [S4]. Emergency department deployment study (6,217 patients): mortality 9.49% after, 1.9 points lower (17% relative) [S5] | Nonrandomized controlled study, 13,649 general-medicine admissions: lower non-palliative death than before. Press reports 2.1% before and 1.6% after [S8, N1] | Prospective multi-site cohort: 590,736 patients monitored, 6,877 sepsis patients alerted before antibiotics. Confirmation within 3 h was linked to 3.3 points lower adjusted mortality [S6] |
| **C8. Transparency and access** | Proprietary (Epic) [S1] | Proprietary (Epic Systems Corporation) [S3] | Peer-reviewed description [S4]. Code availability [MUST VERIFY]. A press report says some authors co-founded a company to commercialize such tools [N4]. [MUST VERIFY in the paper] | In-house hospital system with published methods [S8, S9]. Press says the developers want to make it available for testing [N5]. [MUST VERIFY] | Commercial product from Bayesian Health, founded by lead investigators (press). FDA clearance claim in press [N2]. [MUST VERIFY on the FDA site] |
| **C9. Limitations reported or visible** | Missed 67% of sepsis cases and alerted on 18% of hospitalizations. Poor calibration. One hospital [S1] | Lower AUROC than NEWS in one large comparison [S2]. Effect measured near the threshold at one centre [S3] | Retrospective development. Deployment was non-randomized in two EDs with a 145-day post-period [S4, S5] | Nonrandomized. Observation ended when the model changed for new software and data pipelines [S8]. Study group aged 55–80 per press [N1] | Observational. The benefit was linked to provider response within 3 hours, which does not prove the alert caused it (my interpretation) [S6] |

## 3. What I notice (my interpretation)

- Most of these systems predict with ordinary statistical or machine-learning models. The surrounding system matters just as much: alerts, thresholds, a clinical response and monitoring (CHARTwatch, EDI, TREWS, COMPOSER's deployment).
- The best evidence is for systems whose developers also describe the workflow around them. The evidence for the proprietary Epic tools is mostly independent external validation, and it is not good for the sepsis model (AUC 0.63).
- Explanation of the output (C6) is the criterion I know least about. I found little in the sources I opened. COMPOSER's "indeterminate" output is the clearest example of showing uncertainty.
- None of the sources I opened shows a system that a student can run and inspect end to end.

## 4. Why the proposed diploma solution is still needed

My project does not try to beat these systems. They are large, mostly hospital-integrated and some are commercial, and I cannot evaluate them. The need I see is smaller and more specific.

- **Transparency and reproducibility.** From the sources I opened, I could not confirm that the code, trained models or full variable lists of these systems are publicly available. Two of them are proprietary. A transparent pipeline on an open dataset lets a reader inspect every step: preprocessing, leakage prevention, baselines and metrics.
- **A fair comparison on shared ground.** The literature I reviewed says results are hard to compare and often drop at a new hospital (Moor 2021, Moor 2023, Wong 2021). An open pipeline with the same split and metrics for the model and the baselines makes the comparison visible.
- **Alert behaviour as a first-class result.** Studies show that false alarms and workflow decide usefulness (Wong 2021; van der Vegt 2024). My prototype will report PPV and alert burden next to AUROC, and I will present the output as decision support with its limits.
- **A Software Engineering contribution.** The deployment papers describe pipelines, interfaces and monitoring only briefly. A small, tested, documented system that shows these parts is a reasonable diploma outcome.

Limits: the prototype will use public de-identified data, will not be clinically validated, and will not claim better outcomes than these systems. Whether this need is real for users is not yet confirmed. User discussions are not done (see `docs/02-evidence/`). So this section is a draft that depends on that evidence.

## 5. Sources

Peer-reviewed papers (opened: abstract and indexed text, not full text, unless noted):

- [S1] Wong A, et al. External Validation of a Widely Implemented Proprietary Sepsis Prediction Model in Hospitalized Patients. JAMA Intern Med, 2021. https://pmc.ncbi.nlm.nih.gov/articles/PMC8218233/ (full text read earlier)
- [S2] Edelson DP, et al. Early Warning Scores With and Without Artificial Intelligence. JAMA Netw Open 2024;7(10):e2438986. https://pmc.ncbi.nlm.nih.gov/articles/PMC11544488/ (full text read earlier)
- [S3] Gallo RJ, et al. Effectiveness of an Artificial Intelligence-Enabled Intervention for Detecting Clinical Deterioration. JAMA Intern Med 2024. https://pmc.ncbi.nlm.nih.gov/articles/PMC10964159/
- [S3b] Summary of Gallo et al. in The Hospitalist, used for the model description (31 measures, every 15 minutes, ordinal logistic regression): https://www.the-hospitalist.org/hospitalist/article/38326/in-the-literature/efficacy-of-ai-models-in-detecting-clinical-deterioration/ [MUST VERIFY against the paper]
- [S4] Shashikumar SP, et al. Artificial intelligence sepsis prediction algorithm learns to say "I don't know". npj Digit Med 2021;4:134. https://pmc.ncbi.nlm.nih.gov/articles/PMC8429719/
- [S5] Boussina A, et al. Impact of a deep learning sepsis prediction model on quality of care and survival. npj Digit Med 2024;7:14. https://pmc.ncbi.nlm.nih.gov/articles/PMC10805720/
- [S6] Adams R, et al. Prospective, multi-site study of patient outcomes after implementation of the TREWS machine learning-based early warning system for sepsis. Nat Med 2022;28(7):1455–1460. DOI 10.1038/s41591-022-01894-0. PubMed record 35864252: https://pubmed.ncbi.nlm.nih.gov/35864252/
- [S6c] Commentary on Adams et al. (hospital setting: two academic and three community hospitals): https://pmc.ncbi.nlm.nih.gov/articles/PMC9512693
- [S8] Verma AA, et al. Clinical evaluation of a machine learning-based early warning system for patient deterioration. CMAJ 2024. DOI 10.1503/cmaj.240132. https://www.cmaj.ca/lookup/doi/10.1503/cmaj.240132
- [S9] Pou-Prom C, et al. From compute to care: Lessons learned from deploying an early warning system into clinical practice. Front Digit Health 2022. DOI 10.3389/fdgth.2022.932123. https://pmc.ncbi.nlm.nih.gov/articles/PMC9483018

Press and secondary sources (use only as pointers, not as evidence):

- [N1] HospiMedica, AI-Based System Reduces Risk of Unexpected Deaths in Hospitalized Patients (17 Sep 2024): https://www.hospimedica.com/critical-care/articles/294802475/ai-based-system-reduces-risk-of-unexpected-deaths-in-hospitalized-patients.html
- [N2] PulmCCM, FDA Clears A Slightly Better Sepsis Alert: https://www.pulmccm.org/p/fda-clears-a-slightly-better-sepsis
- [N3] CMAJ podcast with Amol Verma: https://buzzsprout.com/1815691/episodes/15776595-ai-versus-physicians-who-s-better-at-spotting-high-risk-patients
- [N4] Physician's Weekly, HealthDay summary of Boussina et al.: https://www.physiciansweekly.com/?p=505145
- [N5] National Seniors Australia, AI system reduces hospital deaths: https://nationalseniors.com.au/news/health/ai-system-reduces-hospital-deaths

## 6. Still to check

| Item | Status |
|---|---|
| Open each [S] link and confirm title, authors and DOI | [MUST VERIFY] |
| Epic documentation for ESM and EDI (variables, update frequency, explanation) | Not opened; [MUST VERIFY] |
| Inputs and model type of TREWS and COMPOSER, alert recipients and explanation display | [MUST VERIFY] against the papers |
| CHARTwatch variable count, availability statement | [MUST VERIFY] |
| FDA status of TREWS | [MUST VERIFY] on the FDA database |
| Conflict-of-interest statements of S5, S6, S8 | [MUST VERIFY] |
| Whether these five are the right set for my committee | [REQUIRES SUPERVISOR APPROVAL] |