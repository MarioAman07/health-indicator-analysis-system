# Literature Review and Analysis Matrix

**Project:** Development of a Machine Learning-Based System for Analyzing Patient Health Indicators  
**Current proposed direction:** time-series monitoring / early warning with early sepsis prediction as the concrete candidate task  
**Status:** Complete against the 24 October literature-count requirement; revised on 21 Oct 2026 (DIP-17): search log restored, retrieval queries added, limitation → project response table added.  
**Last updated:** 21 Oct 2026

## 1. Research question

What published evidence exists on machine-learning-based early prediction of sepsis or clinical deterioration from physiological and laboratory data, which models and baselines are used, how is performance evaluated, and which methodological and implementation limitations should be taken into account when designing a reproducible Software Engineering prototype?

## 2. Review scope and source selection

A source was retained when it contributed meaningfully to at least one of the following:

- early prediction of sepsis or patient deterioration;
- time-series clinical data and temporal prediction;
- comparison of ML with simple statistical or clinical baselines;
- external or temporal validation and dataset shift;
- evaluation beyond AUROC, including imbalance and alert burden;
- uncertainty, false alarms, or alert fatigue;
- real-time deployment, data pipelines, user alerts, and clinical workflow;
- limitations that affect design or evaluation of the diploma prototype.

The core body is recent: 11 of the 12 publications are from 2021–2024. Reyna et al. (2020) is retained as a foundational source because it defines the PhysioNet/Computing in Cardiology Challenge 2019 task and dataset that are central to the proposed project.

## 3. Search and verification process

Sources #1–#6 were found on 10 Oct 2026 with the searches in §3.1, and I reviewed their full texts.

Sources #7–#12 were added during the literature expansion, and I reviewed their full published texts on 13 Oct 2026. The verification covered bibliographic metadata, study design, data/cohorts, model or intervention, baselines, evaluation measures, main results, limitations, and deployment details where present. No newspaper or press-summary numbers are used in the analysis matrix.

The original queries that led to #7–#12 were not recorded when the sources were added. To keep retrieval reproducible, §3.2 lists title-based queries, re-run on 21 Oct 2026, that find each source. They document how each source can be found again, not how it was first discovered.

### 3.1 Search log — sources #1–#6 (10 Oct 2026)

| # | Search channel | Query | Outcome |
|---|---|---|---|
| 1 | Web search → PubMed / PMC | `machine learning early prediction sepsis systematic review PMC open access` | Moor et al. (2021) identified and selected |
| 2 | Web search → PubMed / PMC | `External Validation Epic Sepsis Model JAMA Internal Medicine Wong` | Wong et al. (2021) identified and selected |
| 3 | Web search → PubMed / PMC | `machine learning versus National Early Warning Score NEWS clinical deterioration prediction AUROC open access` | Lashen et al. (2023) and Edelson et al. (2024) identified and selected |
| 4 | Web search → PubMed / PhysioNet | `Reyna PhysioNet Computing in Cardiology Challenge 2019 early prediction sepsis` | Reyna et al. (2020) identified; full text and official dataset documentation reviewed |
| 5 | Web search → PubMed / PMC | `sepsis machine learning systematic review meta-analysis traditional scoring systems` | Yadgarov et al. (2024) identified and selected |

### 3.2 Retrieval queries — sources #7–#12 (re-run 21 Oct 2026)

| # | Query | Result |
|---|---|---|
| 7 | `COMPOSER sepsis prediction algorithm learns to say "I don't know" npj Digital Medicine 2021` | Found: PMC8429719 |
| 8 | `predicting sepsis using deep learning across international sites retrospective development validation eClinicalMedicine 2023` | Found: PMC10425671 |
| 9 | `impact of a deep learning sepsis prediction model on quality of care and survival npj Digital Medicine 2024` | Found: PMC10805720 (and the author correction, PMC11169238) |
| 10 | `systematic review longitudinal analysis implementing artificial intelligence predict clinical deterioration adult hospitals JAMIA 2024` | Found: PMC10797271 |
| 11 | `clinical evaluation machine learning-based early warning system patient deterioration CMAJ 2024 CHARTwatch` | Found: CMAJ 196(30):E1027 |
| 12 | `effectiveness of an artificial intelligence-enabled intervention for detecting clinical deterioration JAMA Internal Medicine 2024` | Found: PMC10964159 |

### 3.3 Seen but not used

| Item | Reason not used |
|---|---|
| medRxiv version related to Moor et al. | Published peer-reviewed version was available and used instead |
| Research Square work using PhysioNet Challenge 2019 data | Preprint |
| arXiv work on predictive-model voting for Challenge 2019 | Peer-reviewed publication status was not verified |
| Zubair and Din, *Revolutionizing sepsis diagnosis using machine learning and deep learning models: a systematic literature review* | Full text was not verified during the search |
| *Artificial Intelligence-Based Predictive Modeling for Early Detection of Sepsis in Hospitalized Patients: A Systematic Review and Meta-Analysis* | Full text was not verified during the search |
| Watson et al., study comparing ML with NEWS | Seen as a candidate but not reviewed in full text |
| Scientific Reports study on interpretable ML for acute clinical deterioration | Seen as a candidate but not reviewed in full text |
| Steitz et al., ML model for imminent clinical deterioration | Seen as a candidate but not reviewed in full text |
| *Factors underpinning the performance of implemented artificial intelligence-based patient deterioration prediction systems* (PMC11833469) | Found on 21 Oct 2026; candidate for the next revision; full text not yet reviewed |
| COMPOSER-LLM (follow-up work on COMPOSER), seen as a publisher blog post | Peer-reviewed publication not yet checked; candidate for the next revision |

**Background sources checked separately:** official PhysioNet Challenge 2019 documentation and Royal College of Physicians NEWS2 information. These are supporting resources and are not counted among the scientific publications.

## 4. Bibliographic table

| # | Authors | Year | Title | Venue | DOI | Access / verification |
|---|---|---:|---|---|---|---|
| 1 | Moor M, Rieck B, Horn M, Jutzeler CR, Borgwardt K | 2021 | *Early Prediction of Sepsis in the ICU Using Machine Learning: A Systematic Review* | Frontiers in Medicine 8:607952 | 10.3389/fmed.2021.607952 | Open full text; previously reviewed |
| 2 | Reyna MA, Josef CS, Jeter R, Shashikumar SP, Westover MB, Nemati S, Clifford GD, Sharma A | 2020 | *Early Prediction of Sepsis From Clinical Data: The PhysioNet/Computing in Cardiology Challenge 2019* | Critical Care Medicine 48(2):210–217 | 10.1097/CCM.0000000000004145 | Open full text; previously reviewed |
| 3 | Lashen H, St John TL, Almallah YZ, Sasidhar M, Shamout FE | 2023 | *Machine Learning Models Versus the National Early Warning Score System for Predicting Deterioration* | JMIR AI 2:e45257 | 10.2196/45257 | Open full text; previously reviewed |
| 4 | Yadgarov MY, Landoni G, Berikashvili LB, et al. | 2024 | *Early detection of sepsis using machine learning algorithms: a systematic review and network meta-analysis* | Frontiers in Medicine 11:1491358 | 10.3389/fmed.2024.1491358 | Open full text; previously reviewed |
| 5 | Edelson DP, Churpek MM, Carey KA, et al. | 2024 | *Early Warning Scores With and Without Artificial Intelligence* | JAMA Network Open 7(10):e2438986 | 10.1001/jamanetworkopen.2024.38986 | Open full text; previously reviewed |
| 6 | Wong A, Otles E, Donnelly JP, et al. | 2021 | *External Validation of a Widely Implemented Proprietary Sepsis Prediction Model in Hospitalized Patients* | JAMA Internal Medicine 181(8):1065–1070 | 10.1001/jamainternmed.2021.2626 | Open full text; previously reviewed |
| 7 | Shashikumar SP, Wardi G, Malhotra A, Nemati S | 2021 | *Artificial intelligence sepsis prediction algorithm learns to say “I don’t know”* | npj Digital Medicine 4:134 | 10.1038/s41746-021-00504-6 | Published full text reviewed |
| 8 | Moor M, Bennett N, Plečko D, Horn M, Rieck B, Meinshausen N, Bühlmann P, Borgwardt K | 2023 | *Predicting sepsis using deep learning across international sites: a retrospective development and validation study* | eClinicalMedicine 62:102124 | 10.1016/j.eclinm.2023.102124 | Open access (CC BY-NC-ND 4.0); full text reviewed |
| 9 | Boussina A, Shashikumar SP, Malhotra A, Owens RL, El-Kareh R, Longhurst CA, Quintero K, Donahue A, Chan TC, Nemati S, Wardi G | 2024 | *Impact of a deep learning sepsis prediction model on quality of care and survival* | npj Digital Medicine 7:14 | 10.1038/s41746-023-00986-6 | Published full text reviewed; article has a later correction adding omitted Table 3/citation |
| 10 | van der Vegt AH, Campbell V, Mitchell I, et al. | 2024 | *Systematic review and longitudinal analysis of implementing Artificial Intelligence to predict clinical deterioration in adult hospitals: what is known and what remains uncertain* | Journal of the American Medical Informatics Association 31(2):509–524 | 10.1093/jamia/ocad220 | Open access (CC BY 4.0); full text reviewed |
| 11 | Verma AA, Stukel TA, Colacci M, Bell S, Ailon J, Friedrich JO, Murray J, Kuzulugil S, Yang Z, Lee Y, Pou-Prom C, Mamdani M | 2024 | *Clinical evaluation of a machine learning-based early warning system for patient deterioration* | CMAJ 196:E1027–E1037 | 10.1503/cmaj.240132 | Open access (CC BY-NC-ND 4.0); full text reviewed |
| 12 | Gallo RJ, Shieh L, Smith M, Marafino BJ, Geldsetzer P, Asch SM, Shum K, Lin S, Westphal J, Hong G, Li RC | 2024 | *Effectiveness of an Artificial Intelligence-Enabled Intervention for Detecting Clinical Deterioration* | JAMA Internal Medicine 184(5):557–562 | 10.1001/jamainternmed.2024.0084 | Open access (CC BY after July 2024 correction); full text reviewed |

Supporting resources, not counted among the 12 scientific publications:

- PhysioNet. *Early Prediction of Sepsis from Clinical Data: The PhysioNet/Computing in Cardiology Challenge 2019 (version 1.0.0).* DOI: 10.13026/v64v-d857.
- Royal College of Physicians. *National Early Warning Score (NEWS2).*

## 5. Structured analysis matrix

| # | Study / data | Model or approach | Baseline / comparison | Evaluation | Main findings | Limitations | Relevance to this diploma |
|---|---|---|---|---|---|---|---|
| **1** | Systematic review of 22 peer-reviewed studies on ML-based sepsis-onset prediction in adult ICU patients | LSTM, GRU, CNN, temporal convolutional networks, boosted trees, random forests, SVM and other methods across included studies | No single common baseline; review compared study designs, prediction setups and validation | AUROC common; authors recommend AUPRC for imbalanced sepsis data and explicit 3 h / 4 h horizons | ML results were promising, but heterogeneous definitions, cohorts, horizons and evaluation made direct numerical comparison unreliable | High heterogeneity; limited external validation and code/label sharing; adult ICU scope; selected databases; possible publication bias | **My interpretation:** define the prediction horizon clearly, report AUPRC alongside AUROC, prevent leakage and make preprocessing reproducible |
| **2** | PhysioNet/CinC Challenge 2019; hourly ICU data from hospital systems A, B and C; public training data from A/B | 853 submissions from 104 teams under a common early-sepsis task | Algorithms compared under the same task and scoring framework | Challenge clinical utility score and AUROC | Early prediction was feasible, but AUROC and timing-sensitive clinical utility could rank models differently; ranking changed on unseen hospital C | Original hidden test set cannot be reproduced with public data; cross-hospital generalization remained difficult | **My interpretation:** central dataset/task source; supports sequential prediction, strict temporal validity and evaluation beyond AUROC |
| **3** | Retrospective single-centre cohort: 16,901 patients, 26,073 encounters, 951,591 observation sets | Logistic regression, XGBoost, feed-forward neural network; SHAP | NEWS from the same seven input types | AUROC, AUPRC; 6/12/24/36 h windows | XGBoost AUROC 0.778 and NN 0.756 outperformed NEWS 0.682; logistic regression 0.654 did not; performance decreased at longer horizons | Single centre; internal validation; seven inputs only; no NEWS2; temporal vs random split differences | **My interpretation:** supports fair same-input comparisons and shows that a simple ML model does not automatically beat an established score |
| **4** | Systematic review/network meta-analysis: 73 studies, 457,932 septic patients, 256 models | Neural networks, decision trees, SVM, logistic regression, Naive Bayes, GLM, KNN and others | SOFA, qSOFA, NEWS/NEWS2, MEWS, SIRS, SAPS II | AUC; network meta-analysis and meta-regression | Pooled ML AUC 0.825; pooled NEWS/NEWS2 AUC 0.719; model type, dataset and horizon affected reported performance | Very high heterogeneity; 30/73 high risk of bias; external validation only in 16 studies; low certainty of ML superiority; AUC alone weak for imbalance | **My interpretation:** compare ML with transparent baselines but do not assume ML will win |
| **5** | Multicentre retrospective cohort across 7 hospitals: 362,926 medical-surgical ward encounters; general deterioration outcome | eCARTv5, Rothman Index, Epic Deterioration Index | MEWS, NEWS, NEWS2 | AUROC, sensitivity, specificity, PPV, NPV, precision-recall, trigger frequency, lead time | eCART AUROC 0.895; NEWS2 0.831; NEWS 0.829; simple NEWS outperformed some proprietary AI systems | Mixed retrospective/prospective score calculation; imperfect threshold matching; could not determine whether warnings identified unknown deterioration; one regional system | **My interpretation:** a public/simple comparator can remain meaningful; PPV, trigger frequency and lead time matter |
| **6** | External validation at Michigan Medicine: 27,697 patients, 38,455 hospitalizations, 2,552 sepsis cases | Epic Sepsis Model, proprietary penalized logistic regression | Independent real-world performance vs previously reported developer performance | AUC, sensitivity, specificity, PPV, NPV, calibration, lead time, alert burden | Hospitalization AUC 0.63; at threshold 6 sensitivity 33%, specificity 83%, PPV 12%, NPV 95%; 67% of sepsis cases missed; alerts in 18% of hospitalizations; corrected number needed to evaluate = 8 | Single academic centre; composite sepsis definition; timing choices materially affect performance | **My interpretation:** development results are insufficient; calibration, timing and alert burden must be considered |
| **7** | Six ICU/ED cohorts, **515,720 patients**, two US academic health systems; internal, temporal and external validation | **COMPOSER**: deep model with representation learning and conformal prediction; unfamiliar/out-of-distribution inputs can be labelled indeterminate | GB-Vital XGBoost on six vital signs; 2-layer FFNN using the same features; commercial Epic sepsis prediction model in the available temporal comparison | Modified AUC under an alert policy, PPV, NPV, specificity, diagnostic odds ratio, false alarms per patient-hour, missed detection, lead time | Overall AUC ranges: ICU 0.925–0.953, ED 0.938–0.945. External Hospital-B vs FFNN: false-alarm rate reduced about **85.5% in ICU** and **77.9% in ED**. Temporal AUC: **0.952 ICU**, **0.940 ED**. The system explicitly rejects some unfamiliar cases instead of forcing a prediction | Retrospective; two US systems; ICU/ED only; no prospective patient-outcome evidence in this paper; indeterminate outputs create their own workflow question | **My interpretation:** directly relevant to missingness, dataset shift, false-alert control and presenting uncertainty instead of false confidence |
| **8** | Retrospective international multicentre cohort: **136,478 ICU admissions**, 25,694 sepsis cases; MIMIC-III, eICU, HiRID and AmsterdamUMCdb/AUMC across US, Switzerland and Netherlands | Deep causal self-attention; GRU, LightGBM and LASSO logistic regression as ML alternatives; 63 inputs (59 vital/lab + 4 static) at hourly resolution | NEWS, MEWS, SIRS, SOFA, qSOFA, plus alternative ML models | Patient-level AUROC; PPV at 80% sensitivity; lead time; calibration/SHAP in supplementary analyses | Mean internal AUC **0.846**; external AUC **0.761**; 10% target-site fine-tuning improved to **0.807**. Internal PPV at 80% sensitivity **42.0%**, median lead time **3.7 h**, about **1.4 false alerts per true alert** | Retrospective/observational; prospective international bedside evaluation still needed; cross-site data distributions differ; harmonization/filtering and eligibility choices constrain generalization | **My interpretation:** strongest direct evidence that performance falls at new sites; supports explicit external-validity limits and recalibration considerations |
| **9** | Before-and-after quasi-experimental deployment in two UC San Diego EDs; **6,217 adult septic patients** | Real-time COMPOSER; AWS-hosted platform, ADT stream, FHIR APIs with OAuth2, hourly extraction, HL7v2 write-back, nurse-facing Epic BPA, top features, secure chat; data-quality/model monitoring | Historical pre-intervention period with Bayesian structural time-series counterfactual analysis | Mortality, bundle compliance, 72-h SOFA change, ICU outcomes, antibiotic timing, alert acknowledgement | Post mortality 9.49% vs expected counterfactual 11.39%; **1.9 percentage-point absolute / 17% relative decrease** associated with deployment. Bundle compliance +5.0 pp; 72-h SOFA change about −4%. Nurse choice to notify physician immediately was associated with shorter time to antibiotics | Nonrandomized; two EDs in one health system; no concurrent non-COMPOSER ED comparator; short post period; external validity and sustainability uncertain; effect on non-septic patients, unnecessary antibiotics and cost not evaluated | **My interpretation:** highly useful SE example of end-to-end data → model → alert → human workflow, plus monitoring and change control. It does not justify claiming the diploma will improve clinical outcomes |
| **10** | Systematic review of real-time clinical-deterioration ML implementation: **37 articles, 14 algorithm groups** | PRISMA review mapped to the five-stage SALIENT framework | Cross-study comparison of retrospective, silent, pilot, live and post-deployment stages | **107 distinct implementation/evaluation metrics**, barriers/enablers/uncertainties, algorithm/alert/process/patient outcomes | **24 barriers, 40 enablers, 14 uncertainties**. Performance decreased from in-silico to later trial stages in studies with comparable data. Alert-threshold configuration and suppression were common anti-fatigue strategies. Simpler logistic-regression systems with fewer variables were among implemented systems associated with positive outcomes, but intervention components confound attribution | Small number of deployed algorithm groups; heterogeneous reporting; post-deployment metrics often missing; publication bias possible; mortality studies moderate-high risk of bias; SALIENT does not cover the full AI lifecycle | **My interpretation:** core Software Engineering source for data pipeline, HCI, workflow, thresholding, silent trials, monitoring and implementation planning |
| **11** | Nonrandomized controlled implementation at St. Michael’s Hospital: **13,649 GIM patients** (9,626 pre, 4,023 intervention) plus **8,470 subspecialty patients** | **CHARTwatch**, time-aware MARS model; high/medium/low risk; high-risk care pathway; alert silencing; clinician notification | Pre-intervention GIM plus contemporaneous cardiology/nephrology/respirology controls; propensity-score overlap weighting and difference-in-differences | Primary: non-palliative in-hospital death; secondary death/ICU/LOS; process measures after alerts | Weighted non-palliative death **2.1% pre vs 1.6% intervention**, adjusted RR 0.74 (0.55–1.00). High-risk subgroup 10.3% vs 7.1%, RR 0.69 (0.46–1.02). Difference-in-differences RR 0.79 (0.50–1.24), so the broader controlled estimate was less conclusive. Antibiotic use and vital-sign measurement increased after alerts | No randomized control; possible unmeasured confounding, including pandemic-era changes; possibly underpowered; one centre/GIM setting; not all relevant outcomes or patient experiences captured; model/pipeline changed after study window | **My interpretation:** shows that a relatively simple model can be useful only as part of a defined alert and response pathway; software/process measures should be evaluated separately from outcome claims |
| **12** | Cohort study: **9,938 patients** admitted to 4 general medicine units; **963** in primary regression-discontinuity analysis near threshold | Epic Deterioration Index, ordinal logistic regression using 31 EHR measures every 15 min; **threshold 65** triggered nurse/physician alert and structured huddle/checklist | Regression discontinuity: patients immediately below vs above alert threshold | Primary composite: rapid-response activation, ICU transfer, cardiopulmonary arrest; secondary composite included inpatient death | At threshold, intervention associated with **−10.4 percentage points** in primary outcome (95% CI −20.1 to −0.8; p=.03). Inpatient death alone was not significantly reduced | Maximum EDI as assignment variable may reduce power or introduce bias; some comfort-care patients remained; RDD effect is local to threshold and may not generalize to very high/low risk; single academic hospital | **My interpretation:** evaluation should cover the complete intervention—model + threshold + alert + human workflow—not the score alone |

## 6. Critical synthesis

### 6.1 Consistent findings

**ML can improve discrimination, but complexity does not guarantee superiority.**  
Lashen et al. found XGBoost and a neural network above NEWS by AUROC while logistic regression was below NEWS. Edelson et al. showed that NEWS remained stronger than some proprietary AI systems. van der Vegt et al. also found that relatively simple models can support successful implementations. Therefore, the diploma should compare rather than assume superiority.

**External and temporal validation matter.**  
Wong et al. showed a large performance drop during independent validation. Reyna et al. showed that rankings changed on an unseen hospital. Moor et al. (2023) quantified a drop from mean internal AUC 0.846 to cross-site AUC 0.761, with partial recovery after target-site fine-tuning. Generalization must therefore be treated as an empirical question.

**AUROC alone is insufficient.**  
The studies repeatedly use or recommend AUPRC, PPV, sensitivity, specificity, calibration, lead time, clinical utility, and alert frequency. Reyna et al. showed that AUROC and a timing-sensitive utility score can rank algorithms differently. Shashikumar et al. and Wong et al. show why false-alert burden matters in continuous monitoring.

**The full software-and-workflow system matters.**  
Boussina et al., Verma et al., and Gallo et al. evaluate interventions in which the algorithm is connected to thresholds, alerts, user interfaces or messages, and a defined human response. van der Vegt et al. explicitly separates the data pipeline, AI model, HCI, and clinical workflow. A diploma prototype should therefore not be presented as only an ML notebook.

### 6.2 Important differences

The studies are not directly interchangeable:

- **Outcome:** sepsis in some studies; broader deterioration, ICU transfer, arrest, or death in others.
- **Setting:** ICU, ED, and general wards have different data density and workflows.
- **Prediction horizon:** studies use different time windows, changing task difficulty.
- **Inputs:** from six/seven vital-sign variables to dozens of labs and temporal features.
- **Validation:** random/internal, temporal, cross-hospital, and live deployment answer different questions.
- **Evaluation unit:** prediction window, patient, alert, and intervention outcomes differ.
- **Intervention:** deployed studies test a package of model + threshold + alert + human response, so downstream outcome changes cannot be attributed to the model alone.

### 6.3 Repeated limitations across the literature

1. Dataset shift and limited generalizability.
2. Retrospective evidence dominates.
3. Sepsis labels and onset timing vary.
4. High AUROC can coexist with poor PPV or heavy alert burden.
5. Different horizons, thresholds, and outcomes reduce comparability.
6. Missing/irregular EHR measurements are common.
7. Alert fatigue, automation bias, trust, and unclear response actions can reduce usefulness.
8. Real-world deployment evidence is often observational or quasi-experimental.
9. Proprietary models, hidden test sets, and incomplete deployment descriptions limit reproducibility.

## 7. Literature-derived project decisions

The literature supports the following design choices:

- use leakage-safe temporal preprocessing;
- split data by patient;
- document missing-data handling;
- keep the experiment reproducible on accessible data;
- compare the selected model with at least one simple transparent baseline;
- use a rule-based clinical baseline only if it can be reproduced fairly from available variables;
- report AUROC and AUPRC together;
- also report sensitivity and PPV, and alert burden / lead time where the final setup permits;
- define the prediction horizon and alert logic explicitly;
- show uncertainty and limitations rather than a diagnostic verdict;
- treat the result as decision support;
- version the model, preprocessing, threshold, and evaluation configuration;
- separate software verification from claims about patient outcomes;
- make no clinical-validity claim for the student prototype.

## 8. Defensible project gap

The project gap is **not** that early-sepsis ML models do not exist.

A defensible gap is:

> Published studies show promising machine-learning performance for early sepsis and deterioration prediction, but results are difficult to compare because datasets, temporal definitions, validation procedures, metrics, and alert workflows differ. Performance can degrade across institutions, and real-world usefulness depends on data quality, false-alert control, transparency, and integration into a human workflow. This creates a practical Software Engineering need for a transparent and reproducible prototype that applies time-valid preprocessing to an open dataset, compares a selected model with reproducible baselines, evaluates it with multiple alert-aware metrics, and exposes the result through a testable API/dashboard without making clinical-validation claims.

## 9. Verification notes for the six newly added papers

The previously open items were resolved from the supplied published full texts:

- **#7:** 515,720 refers to patients, not encounters. The 85.5%/77.9% external false-alarm reductions, temporal AUC 0.952/0.940, modified AUC protocol, two-layer FFNN baseline, and commercial Epic comparator are present in the article.
- **#8:** article number 102124, DOI 10.1016/j.eclinm.2023.102124, four database names, 63 inputs, clinical/ML baselines, PPV 42.0%, lead time 3.7 h, and 1.4 false alerts per true alert are present in the article.
- **#9:** Bayesian structural time-series analysis, counterfactual mortality, AWS/FHIR/HL7v2 deployment architecture, antibiotic-timing analysis, and deployment limitations are present in the article.
- **#10:** DOI 10.1093/jamia/ocad220, 107 metrics, performance decline between implementation stages, alert-suppression/threshold strategies, and the reported observations about simpler logistic-regression systems are present in the article.
- **#11:** full authorship, CMAJ 196:E1027–E1037, MARS model, RR/CI values, difference-in-differences, process measures, and limitations are present. The previously mentioned “age 55–80” is **not an inclusion age range**; it is the IQR around median age 68 in the intervention GIM cohort.
- **#12:** the official JAMA citation is 184(5):557–562. The article confirms 9,938 patients, four units, EDI threshold 65, 31 measures every 15 minutes, −10.4 pp (95% CI −20.1 to −0.8; p=.03), and no statistically significant inpatient-mortality effect.

## 10. Requirement count

| Requirement | Current literature status |
|---|---|
| At least 12 meaningfully used sources | **12 / 12** |
| At least 8 scientific publications | **12 peer-reviewed journal publications** |
| Core body mainly within last five years | **8 of 12 are from 2023–2024 and 3 from 2021 (at the edge of the five-year window in Oct 2026); Reyna 2020 retained as foundational. Newer sources are planned (§12).** |
| Critical review | **Included** |
| Structured analysis table | **Included** |
| Existing approaches, findings, differences and limitations identified | **Included** |
| Project implications grounded in literature | **Included** |

This completes the literature component for the current 24 October package, while the supervisor may still request revisions.

## 11. Limitations in the literature and how the project responds

| Limitation found in the literature | Sources | How the project responds | Where |
|---|---|---|---|
| Different sepsis definitions, horizons and setups make results incomparable | #1, #4 | One documented label and horizon (`SepsisLabel`, 6 h before Sepsis-3 onset) used for every model | ML methodology §3 |
| Performance drops at a new hospital | #2, #6, #8 | External test on set B (a different hospital system), never used for training or tuning | ML methodology §4 |
| AUROC alone hides poor performance on rare events | #1, #2 | AUPRC, PPV at a fixed sensitivity, calibration and patient-level metrics | ML methodology §9 |
| High alert burden and alarm fatigue | #6, #7, #10 | Alerts per patient-day reported; threshold chosen on validation data; suppression window | FR-07, ML methodology §8 |
| Complex ML does not automatically beat simple scores | #3, #4, #5 | Two baselines (partial SIRS, logistic regression) and a paired bootstrap comparison | ML methodology §7, §9 |
| Missing and irregular measurements | #1, #7 | Missingness features; "insufficient data" state instead of a confident risk | ML methodology §6, FR-11 |
| Proprietary models cannot be inspected | #6; system comparison | Open code, model card, per-prediction explanations | FR-10, NFR-08 |
| Outcome benefit depends on the whole workflow, not on the model | #9, #10, #11, #12 | No clinical-benefit claims; workflow elements (alerts, explanations, data-quality states) designed and checked with users | Proposal §7, verification plan §6 |
| Retrospective evidence dominates | #4, #10 | Stated as a limitation; evaluation is retrospective only | ML methodology §11 |

## 12. Planned update

Before pre-defense 2 the review will be extended with peer-reviewed sources from 2025–2026, starting with the candidates in §3.3, and with studies that report methods on the PhysioNet/CinC Challenge 2019 data.
