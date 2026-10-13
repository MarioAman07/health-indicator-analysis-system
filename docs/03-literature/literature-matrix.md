# Literature Matrix

**Status:** DRAFT -  first 6 verified sources. This is not the final literature review.  
**Last updated:** 10 Oct 2026

## Research Question

What published evidence exists on machine-learning-based early prediction of sepsis or patient deterioration from vital signs and laboratory values, what ML methods are used, what baselines they compare against, what evaluation metrics are used, and what limitations are reported?

## How to Read This File

- Evidence columns record what the papers report, in my own words.
- Project-level conclusions are prefixed **"My interpretation:"**.
- Verification: all 6 sources were reviewed in full text.
- "Recent core" = publications from 2021–2026.
- "Foundational" = an older work retained because it is essential to the project.
- Official requirement for 24 October: at least 12 meaningfully used sources, including at least 8 scientific publications. This file contains the first 6 sources.

---

## 1. Search Log

Search date: **10 Oct 2026**

| # | Search channel / source | Query / target | Outcome |
|---|---|---|---|
| 1 | Web search → PubMed / PMC | `machine learning early prediction sepsis systematic review PMC open access` | Moor et al. (2021) identified and selected |
| 2 | Web search → PubMed / PMC | `External Validation Epic Sepsis Model JAMA Internal Medicine Wong` | Wong et al. (2021) identified and selected |
| 3 | Web search → PubMed / PMC | `machine learning versus National Early Warning Score NEWS clinical deterioration prediction AUROC open access` | Lashen et al. (2023) and Edelson et al. (2024) identified and selected |
| 4 | Web search → PubMed / PhysioNet | `Reyna PhysioNet Computing in Cardiology Challenge 2019 early prediction sepsis` | Reyna et al. (2020) identified; full text and official PhysioNet dataset documentation reviewed |
| 5 | Web search → PubMed / PMC | `sepsis machine learning systematic review meta-analysis traditional scoring systems` | Yadgarov et al. (2024) identified and selected |

### Seen but Not Used

These items appeared during the search but were not included in the current six-source set.

| Item | Reason not used |
|---|---|
| medRxiv version related to Moor et al. | Published peer-reviewed version was available and used instead |
| Research Square work using PhysioNet Challenge 2019 data | Preprint |
| arXiv work on predictive-model voting for Challenge 2019 | Peer-reviewed publication status was not verified |
| Zubair and Din, *Revolutionizing sepsis diagnosis using machine learning and deep learning models: a systematic literature review* | Full text was not verified during the current search |
| *Artificial Intelligence-Based Predictive Modeling for Early Detection of Sepsis in Hospitalized Patients: A Systematic Review and Meta-Analysis* | Full text was not verified during the current search |
| Watson et al., study comparing ML with NEWS | Seen as a candidate but not reviewed in full text |
| Scientific Reports study on interpretable ML for acute clinical deterioration | Seen as a candidate but not reviewed in full text |
| Steitz et al., ML model for imminent clinical deterioration | Seen as a candidate but not reviewed in full text |

**Background sources checked separately:** official PhysioNet Challenge 2019 documentation and Royal College of Physicians NEWS2 information. These are supporting resources and are not counted among the six scientific publications below.

---

## 2. Sources / Bibliographic Table

| # | Authors | Year | Title | Venue | DOI | Open full-text URL | Verification |
|---|---|---|---|---|---|---|---|
| 1 | Moor M, Rieck B, Horn M, Jutzeler CR, Borgwardt K | 2021 | Early Prediction of Sepsis in the ICU Using Machine Learning: A Systematic Review | Frontiers in Medicine 8:607952 | 10.3389/fmed.2021.607952 | https://pmc.ncbi.nlm.nih.gov/articles/PMC8193357/ | Full text reviewed |
| 2 | Reyna MA, Josef CS, Jeter R, Shashikumar SP, Westover MB, Nemati S, Clifford GD, Sharma A | 2020 | Early Prediction of Sepsis From Clinical Data: The PhysioNet/Computing in Cardiology Challenge 2019 | Critical Care Medicine 48(2):210–217 | 10.1097/CCM.0000000000004145 | https://pmc.ncbi.nlm.nih.gov/articles/PMC6964870/ | Full text reviewed |
| 3 | Lashen H, St John TL, Almallah YZ, Sasidhar M, Shamout FE | 2023 | Machine Learning Models Versus the National Early Warning Score System for Predicting Deterioration: Retrospective Cohort Study in the United Arab Emirates | JMIR AI 2:e45257 | 10.2196/45257 | https://pmc.ncbi.nlm.nih.gov/articles/PMC11041421/ | Full text reviewed |
| 4 | Yadgarov MY, Landoni G, Berikashvili LB, Polyakov PA, Kadantseva KK, Smirnova AV, Kuznetsov IV, Shemetova MM, Yakovlev AA, Likhvantsev VV | 2024 | Early detection of sepsis using machine learning algorithms: a systematic review and network meta-analysis | Frontiers in Medicine 11:1491358 | 10.3389/fmed.2024.1491358 | https://pmc.ncbi.nlm.nih.gov/articles/PMC11523135/ | Full text reviewed |
| 5 | Edelson DP, Churpek MM, Carey KA, Lin Z, Huang C, Siner JM, Johnson J, Krumholz HM, Rhodes DJ | 2024 | Early Warning Scores With and Without Artificial Intelligence | JAMA Network Open 7(10):e2438986 | 10.1001/jamanetworkopen.2024.38986 | https://pmc.ncbi.nlm.nih.gov/articles/PMC11544488/ | Full text reviewed |
| 6 | Wong A, Otles E, Donnelly JP, Krumm A, McCullough J, DeTroyer-Cooley O, Pestrue J, Phillips M, Konye J, Penoza C, Ghous M, Singh K | 2021 | External Validation of a Widely Implemented Proprietary Sepsis Prediction Model in Hospitalized Patients | JAMA Internal Medicine 181(8):1065–1070 | 10.1001/jamainternmed.2021.2626 | https://pmc.ncbi.nlm.nih.gov/articles/PMC8218233/ | Full text reviewed |

### Notes

Source 2 is cited as a 2020 *Critical Care Medicine* publication, although the associated PhysioNet Challenge is named Challenge 2019.

Source 6 was corrected on 2 Aug 2021. The corrected number needed to evaluate of **8** is used.

**Data resource — not counted as a scientific publication:**

Reyna M, Josef C, Jeter R, Shashikumar S, Moody B, Westover MB, Sharma A, Nemati S, Clifford GD. *Early Prediction of Sepsis from Clinical Data: The PhysioNet/Computing in Cardiology Challenge 2019* (version 1.0.0). PhysioNet, 2019. DOI: 10.13026/v64v-d857. License: CC BY 4.0.  
https://physionet.org/content/challenge-2019/1.0.0/

---

## 3. Literature Analysis Matrix

| # | Study | Study Type / Dataset | ML Methods | Baseline / Comparison | Metrics | Main Findings | Limitations | Relevance to My Project | Status | Verification |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Moor et al. (2021), *Early Prediction of Sepsis in the ICU Using Machine Learning: A Systematic Review* | Systematic review of 22 peer-reviewed studies on ML-based sepsis-onset prediction in adult ICU patients. Studies used heterogeneous datasets, sepsis definitions and experimental designs. | Multiple approaches across the reviewed studies, including neural networks such as LSTM, GRU, CNN and temporal convolutional networks, boosted-tree models, random forests, SVM and other models. | No single common rule-based baseline across all reviewed studies. The review compares study designs, prediction setups, validation procedures and reported model performance. | AUROC was commonly reported. The review recommends reporting AUPRC for imbalanced sepsis data and recommends reporting performance at a 3 h or 4 h prediction horizon in addition to other horizons. | ML approaches showed promising early-sepsis prediction results, but studies were difficult to compare because of different sepsis definitions, prediction windows, cohort construction and evaluation. 19 of 22 studies used offline training with horizon evaluation, while 2 used an online setup. External validation and code/label sharing were uncommon. The review also discusses possible circularity when labels and predictors depend on overlapping clinical measurements. | High inter-study heterogeneity prevented quantitative meta-analysis. Comparability and reproducibility were poor. Few studies used external validation or shared sufficient code. The review was restricted to selected databases and adult ICU studies, excluded grey literature and may have been affected by publication bias. | My interpretation: this source is important for the project methodology. The diploma should clearly define its temporal prediction setup, avoid future-information leakage, report AUPRC as well as AUROC, document preprocessing and make the experiment reproducible. It also shows why selecting a model only because it has the highest reported AUROC would be inappropriate. | Recent core source | Full text reviewed |
| 2 | Reyna et al. (2020), *Early Prediction of Sepsis From Clinical Data: The PhysioNet/Computing in Cardiology Challenge 2019* | Challenge study using hourly ICU data from three hospital systems A, B and C. Data and labels for 40,336 patients from systems A and B were publicly released. Hidden test data covering 24,819 patients from systems A, B and C were used for scoring. The dataset contains 40 clinical variables: 8 vital signs, 26 laboratory variables and 6 demographic/administrative variables, plus `SepsisLabel`. Sepsis labels were based on Sepsis-3 criteria. | 104 groups from academia and industry participated, contributing 853 submissions. The paper evaluates submitted algorithms collectively rather than proposing one ML architecture. | No NEWS/NEWS2 comparator was identified in the supplied full text. Submitted algorithms were compared under a common dataset, prediction task and scoring framework. | Challenge clinical utility score, designed to reward sufficiently early correct predictions and penalize late predictions, missed cases and false alarms. AUROC was also examined and compared with the utility score. | Diverse computational approaches predicted sepsis several hours before clinical recognition. High AUROC did not necessarily correspond to high clinical utility. Algorithms that performed well on hospital systems represented in the available training data did not necessarily retain the same performance ranking on the unseen hospital system C. | Generalization across hospital systems remained difficult. Traditional metrics such as AUROC did not necessarily reflect clinical utility or the timing of predictions. | My interpretation: this is the central source for Option B because it provides the candidate dataset and an hourly sequential prediction setup in which only information available up to the current prediction time should be used. It supports time-aware evaluation, prevention of future-data leakage and the use of evaluation measures beyond AUROC. Because only systems A and B are publicly available, the original hidden-hospital validation cannot be reproduced in my diploma and this limitation must be stated. | Foundational source | Full text reviewed |
| 3 | Lashen et al. (2023), *Machine Learning Models Versus the National Early Warning Score System for Predicting Deterioration: Retrospective Cohort Study in the United Arab Emirates* | Retrospective single-centre cohort from Cleveland Clinic Abu Dhabi: 16,901 patients, 26,073 inpatient emergency encounters and 951,591 observation sets collected from 2015 to 2021. Inputs were the 7 variables required for NEWS: heart rate, respiratory rate, temperature, systolic blood pressure, oxygen saturation, consciousness status and supplementary oxygen status. | Logistic regression, XGBoost gradient boosting and a feed-forward neural network. SHAP was used for feature-importance analysis. | Direct comparison with the National Early Warning Score (NEWS), computed using the same 7 types of input information. | AUROC and AUPRC with bootstrapped confidence intervals. Prediction windows of 6, 12, 24 and 36 hours were evaluated. | On the holdout test set, NEWS achieved AUROC 0.682, XGBoost 0.778 and the neural network 0.756. Logistic regression achieved AUROC 0.654 and therefore did not outperform NEWS by AUROC. Performance decreased as the prediction window became longer. Temperature was the most important XGBoost feature, followed closely by respiratory rate. | Single-centre study with internal testing only and no external validation cohort. Only 7 input variables were used and laboratory measurements were not included. Multiple encounters or observation sets per patient could introduce some bias despite patient-level splitting. NEWS2 was not evaluated. Random and temporal splits produced different results, highlighting possible distribution shift over time. | My interpretation: this is one of the most directly relevant studies because it provides an example of comparing ML against an established rule-based early-warning system using the same available inputs. It supports using AUROC together with AUPRC, evaluating multiple prediction horizons and including interpretability analysis. Lashen et al. also show one possible way of deriving supplementary-oxygen status from FiO2. Whether this can be transferred to the Challenge 2019 dataset must be verified from its data encoding and missingness before it is used in a NEWS-style baseline. The result for logistic regression also shows that a simple ML baseline does not automatically outperform a rule-based score. | Recent core source | Full text reviewed |
| 4 | Yadgarov et al. (2024), *Early detection of sepsis using machine learning algorithms: a systematic review and network meta-analysis* | Systematic review and network meta-analysis of 73 studies, 457,932 septic patients and 256 predictive models. Studies included ICU, hospital ward and emergency-department settings and used both public and private datasets. 53% used public datasets such as MIMIC, eICU and Challenge 2019 data. | Models were grouped into categories including neural networks, decision trees, SVM, logistic regression, Naive Bayes, generalized linear models and KNN. | ML models were compared with traditional systems including SOFA, qSOFA, NEWS/NEWS2, MEWS, SIRS and SAPS II. | AUC was the main common performance metric used for pooled analysis, network meta-analysis and meta-regression. | The pooled AUC for ML models was 0.825. The pooled NEWS/NEWS2 AUC was 0.719 across 9 studies. Neural-network and decision-tree models had the strongest performance in the network meta-analysis. ML model type, dataset type and prediction window significantly influenced reported AUC. Models using freely available datasets had lower reported AUCs than models based on non-public hospital datasets. | Clinical heterogeneity was very high, with I² above 95%. The certainty of evidence supporting the superiority of ML over traditional scores was rated low. 30 of 73 studies were rated at high risk of bias. External validation was performed in only 16 studies (21.9%). AUC may also be inadequate as the only metric for highly imbalanced data. Definitions, prediction windows, preprocessing and validation methods varied across studies. | My interpretation: this recent synthesis supports investigating ML against clinical scoring systems, but it does not justify claiming in advance that ML will be better. Since studies using public datasets reported lower AUCs, I should not expect unrealistically high performance from an open benchmark dataset. The study supports transparent validation, multiple evaluation metrics and comparison with a simple interpretable baseline. | Recent core source | Full text reviewed |
| 5 | Edelson et al. (2024), *Early Warning Scores With and Without Artificial Intelligence* | Multicentre retrospective cohort across 7 hospitals in the Yale New Haven Health System with 362,926 adult medical-surgical ward encounters between 2019 and 2023. The outcome was general clinical deterioration, defined as ward death or direct ICU transfer within 24 hours. This study is not specifically a sepsis study. | Three proprietary AI-based scores were evaluated: eCARTv5, Rothman Index and Epic Deterioration Index. eCART is a gradient-boosted ML model. | Direct head-to-head comparison with the non-AI scores MEWS, NEWS and NEWS2. | AUROC, sensitivity, specificity, PPV, NPV, precision-recall analysis, trigger frequency and lead time. | eCART achieved the highest AUROC at 0.895. NEWS2 achieved 0.831, NEWS 0.829, Rothman Index 0.828, Epic Deterioration Index 0.808 and MEWS 0.757. NEWS and NEWS2 were statistically indistinguishable by AUROC across the hospitals. The simple public NEWS score performed better than some proprietary AI systems. eCART had the strongest PPV and good lead time. The authors support using NEWS as a standard comparator because it is public, performs well and has defined thresholds. | Some scores were calculated retrospectively while others were calculated prospectively, complicating direct comparison. Differences in score granularity made threshold matching imperfect. The study could not determine whether the warning systems identified deterioration that clinicians were not already aware of. All hospitals were geographically located in the northeastern United States. Conflict-of-interest disclosures included equity in AgileMD and an eCART patent for Edelson, and an eCART patent for Churpek. | My interpretation: this study is useful because it demonstrates that an AI-labelled model is not automatically better than a transparent clinical score. It supports NEWS as a reasonable reference comparator and shows why PPV, false-alarm burden and lead time should be considered alongside AUROC. NEWS and NEWS2 being statistically similar by AUROC also supports considering a NEWS-style baseline if full NEWS2 cannot be reproduced. Because the study predicts general deterioration rather than sepsis, its results should not be transferred directly to the sepsis task. | Recent core source | Full text reviewed |
| 6 | Wong et al. (2021), *External Validation of a Widely Implemented Proprietary Sepsis Prediction Model in Hospitalized Patients* | Retrospective external validation at Michigan Medicine involving 27,697 patients and 38,455 hospitalizations. Sepsis occurred in 2,552 hospitalizations. | Epic Sepsis Model (ESM), a proprietary penalized logistic-regression model using routinely collected EHR data. | External validation against real-world clinical practice. Potential added benefit was evaluated in relation to timely antibiotic administration and compared with previously reported developer performance. This was not a NEWS/NEWS2 comparison. | Hospitalization-level AUC, time-horizon AUC, sensitivity, specificity, PPV, NPV, calibration, lead time and alert burden, including number needed to evaluate. | External performance was substantially worse than developer-reported performance. Hospitalization-level AUC was 0.63. At a threshold of 6, sensitivity was 33%, specificity 83%, PPV 12% and NPV 95%. The model failed to identify 67% of sepsis cases while generating alerts for 18% of hospitalizations, creating substantial alert burden. Calibration was poor. The corrected number needed to evaluate was 8. | External validation was performed at a single academic medical centre. A composite sepsis definition was used, while sepsis definitions remain debated. Reported model performance also depended strongly on how the timing of predictions relative to sepsis onset was handled. | My interpretation: this study is an important warning against relying only on development-set performance. Generalization testing, calibration, prediction timing and alert burden should be considered when evaluating the diploma model. It also supports using transparent and reproducible methods rather than relying on inaccessible proprietary model behaviour. | Recent core source | Full text reviewed |

---

## 4. Preliminary Synthesis

The six sources provide consistent evidence that machine-learning methods can be useful for early detection of sepsis or patient deterioration, but they also show that reported performance depends strongly on the dataset, prediction horizon, outcome definition, validation strategy and evaluation metric.

Moor et al. (2021) show that the sepsis-prediction literature has major comparability and reproducibility problems. Differences in sepsis definitions, patient selection, prediction horizons and evaluation metrics make simple numerical comparisons between studies unreliable. The review also emphasizes the importance of AUPRC for imbalanced outcomes and the limited use of external validation.

Reyna et al. (2020) provide a standardized benchmark for sequential early-sepsis prediction. Their Challenge demonstrates both the feasibility of making predictions before clinical recognition and the difficulty of transferring performance between hospital systems. It also shows that conventional AUROC and a timing-sensitive clinical utility metric do not necessarily rank models in the same way.

Lashen et al. (2023) provide a direct comparison between ML and NEWS using the same routine patient measurements. XGBoost and the neural network outperformed NEWS by AUROC, while logistic regression did not. This shows that the use of ML alone does not guarantee better performance and that model choice matters.

Yadgarov et al. (2024) provide broader quantitative evidence that ML models tend to achieve higher AUC than traditional scoring systems. However, the certainty of this evidence was rated low and study heterogeneity was very high. External validation remained uncommon.

Edelson et al. (2024) reinforce the importance of strong simple baselines. Although eCART achieved the best performance, NEWS outperformed some proprietary AI-based systems. This supports using a transparent clinical score as a meaningful comparator rather than assuming that any AI-based system should perform better.

Wong et al. (2021) show the risk of relying on internally reported model performance. The Epic Sepsis Model performed substantially worse during independent external validation and produced a large alert burden. This highlights the importance of generalization, calibration and clinically meaningful evaluation.

**My interpretation:** the current literature supports continuing with Option B as a reasonable research and engineering direction, but it does not justify claiming that ML is inherently superior to clinical scoring systems. The diploma should therefore be framed as a controlled comparison and system-development project. The model should be evaluated using reproducible temporal validation, multiple performance metrics and at least one simple baseline.

---

## 5. Preliminary Implications for the Diploma

**My interpretation:** based on the first six sources, the current design direction should consider:

- using PhysioNet Challenge 2019 as the main candidate dataset;
- predicting sepsis risk from structured time-series clinical indicators;
- ensuring that predictions use only information available up to the prediction time;
- avoiding future-information leakage;
- including a simple ML baseline such as logistic regression;
- considering a NEWS-style rule-based baseline if it can be reproduced fairly from the available variables;
- evaluating AUROC together with AUPRC;
- considering sensitivity, specificity, PPV, lead time and alert burden where appropriate;
- documenting the prediction horizon explicitly;
- reporting preprocessing, missing-data treatment and dataset splitting clearly;
- treating generalization as a limitation if an independent external hospital dataset is not available;
- avoiding claims of clinical validity or readiness for real medical use.

These decisions remain preliminary until the project scope and baseline approach are reviewed with the supervisor.

---

## 6. Open Verification and Supervisor Items

| Item | Status |
|---|---|
| Whether supplementary-oxygen status can be reliably derived from FiO2 in the Challenge 2019 public data, including units, missingness and measurement frequency | [MUST VERIFY] |
| Whether the official Challenge utility-scoring code can be run reproducibly on the public A and B datasets | [MUST VERIFY] |
| Whether a NEWS-style baseline without a directly available consciousness variable is methodologically acceptable | [REQUIRES SUPERVISOR APPROVAL] |
| Whether the Challenge clinical utility score should be a primary or secondary evaluation metric | [REQUIRES SUPERVISOR APPROVAL] |
| Whether Option B — early sepsis prediction / early warning — should become the final project direction | [REQUIRES SUPERVISOR APPROVAL] |

---

## 7. Current Literature Status

Current progress:

- **6 / 12+** required meaningfully used sources collected;
- **6 / 8+** required scientific publications collected;
- **5 recent core sources** from 2021–2024;
- **1 foundational source** from 2020;
- all 6 current sources reviewed in full text;
- initial evidence on models, baselines, metrics, validation problems and limitations recorded.

The remaining literature search will be completed after supervisor feedback and will expand the evidence base to at least 12 meaningfully used sources.