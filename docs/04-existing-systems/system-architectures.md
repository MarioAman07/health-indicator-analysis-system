# Existing Systems: How They Are Built

**Status:** first version after the supervisor meeting of 23 Oct 2026 (DIP-28)  
**Last updated:** 23 Oct 2026  
**Related:** [system comparison](system-comparison.md) · [target system](../07-architecture/target-system.md) · [literature matrix](../03-literature/literature-matrix.md)

## 1. Purpose and limits

The [system comparison](system-comparison.md) compares five systems on nine criteria. At the meeting on 23 Oct 2026 the supervisor asked me to also show how these systems are built — their architecture or data model — as far as public information allows.

None of the five systems has published an entity–relationship diagram or an official architecture diagram. For three of them (COMPOSER, CHARTwatch, TREWS), the publications describe the data flow, the deployment and the way alerts reach the staff in enough detail to reconstruct a simplified architecture. For the two Epic models, the vendor has published nothing about the internals. Only independent studies describe their inputs, thresholds and use.

The figures below are therefore my reconstructions. Each element on them comes from the cited text. Where a source does not say something, the figure says "not described", and nothing is added from guesswork.

## 2. COMPOSER (UC San Diego Health)

**Figure 1.** [composer-architecture.png](../../diagrams/export/composer-architecture.png)

COMPOSER is the most fully described deployment [LIT-9, LIT-7]. The model does not run inside the health record. It runs on a cloud platform (AWS), and the hospital record system (Epic) is connected to it in three ways:

- an ADT feed tells the platform which patients are currently in the emergency department;
- every hour the platform pulls their clinical data through the record's FHIR interface, authorised with OAuth 2.0;
- the score is written back into the record as an HL7 v2 message.

When the score passes the threshold, the record shows the nurse a Best Practice Advisory: an alert window inside Epic that lists the features that contributed most to the score. One of the nurse's options is to notify the physician at once. In the study, that choice was associated with a shorter time to antibiotics [LIT-9]. The deployment also monitors data quality and model performance.

The model itself can output "indeterminate" when the input does not resemble the data it was trained on [LIT-7].

**What this means for my design.**

- The architecture separates three concerns: getting data from the hospital, computing the risk, and showing the result inside the staff's normal tools. My data-source adapter plays the role of COMPOSER's FHIR extraction.
- The nurse is the first recipient, and the physician is reached through a choice inside the alert. I take this nurse-first path and the "physician informed" acknowledgement (FR-20).
- The "indeterminate" output is the model for my "insufficient data" state (FR-11).

## 3. CHARTwatch (St. Michael's Hospital, Toronto)

**Figure 2.** [chartwatch-architecture.png](../../diagrams/export/chartwatch-architecture.png)

CHARTwatch shows how far a relatively simple model can go with careful engineering around it [S-2, LIT-11].

The model was trained on historical data from the hospital's enterprise data warehouse. In production, an R pipeline on a local server runs every hour. It extracts the current census and each patient's data from the hospital's source databases, cleans them, builds 6-hour windows, scores them with a MARS model and assigns a High, Medium or Low risk group.

The results reach people through tools they already use:

- "high risk" alerts go to a pager app on the phones of the medical team and of the charge nurse;
- risk groups appear hourly in an electronic sign-out tool built in the hospital;
- e-mail sends the charge nurse a census with risk groups twice a day, for assigning nurses, and the palliative care team a daily list of new high-risk patients.

The alert rules are strict:

- no repeat for the same patient for 48 hours;
- a new alert only after the patient has dropped to Medium or Low and returned to High;
- silence for 24 hours after a transfer from the ICU;
- since 2022, no more than five alerts per patient.

The system went through a silent testing period before going live. The team monitors AUC, PPV, alerts per day, run time and uptime; failures trigger e-mails; and an implementation committee reviews the figures first weekly, then monthly. Over 14,016 hours the system was up 99.6% of the time. When extraction fails, it may use an extract up to 3 hours old.

**What this means for my design.**

- The alert-suppression rule with an exception is close to mine. My window is shorter (6 hours rather than 48), because both respondents asked for a new alert when the state changes.
- The use of existing channels — phone for the team, a list for the charge nurse — supports showing alerts at the nurse station rather than in a new device.
- Silent testing, uptime and alert-frequency monitoring are adopted in the introduction plan ([target system](../07-architecture/target-system.md) §6.2).

## 4. TREWS (five hospitals in the United States)

**Figure 3.** [trews-architecture.png](../../diagrams/export/trews-architecture.png)

TREWS uses routine record data: laboratory results, vital signs, notes, and medication and procedure history [S-4, S-1].

Its main design choice is a passive alert. Instead of a pop-up, the patient gets an icon in the patient list. Clicking it opens a TREWS page in the chart, which shows the factors that triggered the alert, the estimated probabilities of sepsis and death, and the status of sepsis treatment. Nurses can pre-screen the alert and pass it to a physician or advanced practice provider. The provider evaluates the alert and confirms or dismisses it; an evaluation within 3 hours counts as timely. In the multi-site study, patients whose alert was confirmed within 3 hours had lower adjusted mortality [S-1].

The sources I reviewed do not say where the model is computed or how often.

**What this means for my design.**

- A flag in the patient list plus a short page with the reasons is less disruptive than pop-ups. My patient list with the alert at the top and the patient view with five reasons follow the same idea.
- Recording the clinician's response (confirm or dismiss) makes the alert measurable in use. My acknowledgement outcomes serve the same purpose.

## 5. Epic Sepsis Model and Epic Deterioration Index

**Figure 4.** [epic-models.png](../../diagrams/export/epic-models.png)

Both models run inside the Epic health record and belong to the vendor. Their architecture, data model and update schedule are not published. The independent studies describe them only from outside:

- The **Sepsis Model** is a penalized logistic regression. At the validated threshold it found a third of sepsis cases and alerted in 18% of hospitalisations; external AUC was 0.63 [LIT-6].
- The **Deterioration Index** is an ordinal logistic regression over 31 measures, updated every 15 minutes [LIT-12]. At the study site, a score of 65 sent an alert to the nurse and the physician and started a structured huddle with a checklist. The intervention around this threshold reduced the composite outcome by 10.4 percentage points [LIT-12]. In a seven-hospital comparison, its AUROC (0.808) was lower than that of the simple NEWS score (0.829) [LIT-5].

**What this means for my design.** A closed model cannot be inspected, and its published performance may not hold in a new hospital. This is the strongest argument for the openness of my system: open code, a model card, and an external test on a second hospital system. It is also an argument for always comparing the model with a simple score.

## 6. Summary

The four publicly described architectures share a pattern:

1. data are taken from the hospital record on a schedule;
2. the risk is computed outside or beside the record;
3. the result is returned into the tools the staff already use;
4. the response of the staff is part of the design;
5. the system is monitored after go-live.

They differ in where the model runs (cloud, local server, inside the vendor's record) and in how hard they push the alert (pager, alert window, passive icon).

My [target system](../07-architecture/target-system.md) follows the same five steps. It differs in three ways:

- the data source is a replaceable adapter, so the same system runs on open data in the diploma and on a hospital MIS in the target;
- the alert is shown at the nurse station, and the acknowledgement is recorded with an outcome;
- the code, the model and the evaluation are open.

## Sources

The IDs are the same as in the [system comparison](system-comparison.md): `LIT-#` are sources from the [literature matrix](../03-literature/literature-matrix.md), `S-#` are other peer-reviewed sources. S-4 is new in this document.

- [LIT-5] Edelson DP, et al. Early Warning Scores With and Without Artificial Intelligence. *JAMA Netw Open.* 2024;7(10):e2438986. (Literature matrix #5.)
- [LIT-6] Wong A, et al. External Validation of a Widely Implemented Proprietary Sepsis Prediction Model in Hospitalized Patients. *JAMA Intern Med.* 2021;181(8):1065–1070. (#6.)
- [LIT-7] Shashikumar SP, et al. Artificial intelligence sepsis prediction algorithm learns to say "I don't know". *npj Digit Med.* 2021;4:134. (#7.)
- [LIT-9] Boussina A, et al. Impact of a deep learning sepsis prediction model on quality of care and survival. *npj Digit Med.* 2024;7:14. (#9.)
- [LIT-11] Verma AA, et al. Clinical evaluation of a machine learning-based early warning system for patient deterioration. *CMAJ.* 2024;196:E1027–E1037. (#11.)
- [LIT-12] Gallo RJ, et al. Effectiveness of an Artificial Intelligence-Enabled Intervention for Detecting Clinical Deterioration. *JAMA Intern Med.* 2024;184(5):557–562. (#12.)
- [S-1] Adams R, et al. Prospective, multi-site study of patient outcomes after implementation of the TREWS machine learning-based early warning system for sepsis. *Nat Med.* 2022;28(7):1455–1460. DOI 10.1038/s41591-022-01894-0.
- [S-2] Pou-Prom C, et al. From compute to care: Lessons learned from deploying an early warning system into clinical practice. *Front Digit Health.* 2022;4:932123. DOI 10.3389/fdgth.2022.932123.
- [S-4] Henry KE, et al. Evaluating adoption, impact, and factors driving adoption for TREWS, a machine learning-based sepsis alerting system. medRxiv preprint 2021.07.02.21259941. The text consulted is the preprint; the hospital setting described in S-3 of the system comparison is not used here.
