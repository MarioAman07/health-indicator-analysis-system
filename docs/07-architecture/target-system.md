# Target System and Clinical Workflow

**Status:** first version after the supervisor meeting of 23 Oct 2026 (DIP-27)  
**Last updated:** 23 Oct 2026  
**Related:** [architecture](architecture.md) · [requirements](../06-requirements.md) · [user evidence](../02-evidence/user-evidence.md) · [transcripts](../02-evidence/transcripts.md) · [existing-system architectures](../04-existing-systems/system-architectures.md)

## 1. Purpose

At the meeting on 23 Oct 2026 the supervisor asked me to show how the system should work in a real hospital. That covers where its data come from, how a warning reaches the staff, what happens after the warning, and how all of this fits the way intensive care is organised in Kazakhstan.

This document describes that target system. The diploma does not connect to a real hospital: it uses open, de-identified data (C-01) and runs on one computer (C-02). The design is still made for the real setting. The part that talks to the hospital is a replaceable data-source adapter. The diploma implements it as a replay of the PhysioNet files, hour by hour. Everything behind the adapter — validation, features, risk, alert rules, storage, API and screens — is the same code in both cases. Section 6 states exactly what is built and what stays a design.

## 2. How patients are monitored in a Kazakhstani ICU today

This section is based on three regulatory documents and on the two user discussions. Practice differs between hospitals, so it describes the common frame, not one specific unit. The next user discussions will check it with an ICU nurse or physician.

### 2.1 Organisation and staffing

Intensive care is regulated by the Standard for organising anaesthesiology and resuscitation care (Order of the Minister of Health No. 78 of 26 April 2023, amended in 2025) [K1]. An intensive care unit (ОРИТ or ОАРИТ) has at least six beds and includes a separate room for infectious and septic patients. "Severe sepsis of any origin" is one of the listed reasons for ICU admission.

The staffing norm is at least 4.75 nurse posts per two ICU beds. A round-the-clock post is commonly staffed with 4.75 positions, so this corresponds to about one nurse on duty for every two beds. For patients on mechanical ventilation, ECMO and some other profiles, the norm is one round-the-clock post per bed.

The Standard requires continuous monitoring of the patient's functional state and a daily examination with the head of the department. Progress notes are written every 3 hours for severe or unstable patients and every 6 hours for stable ones.

### 2.2 Measurements and where they are recorded

For anaesthesia, the Standard lists the monitored parameters: heart rate, ECG, oxygen saturation, blood pressure (invasive when haemodynamics are unstable), temperature, ventilation and hourly urine output [K1]. For ICU patients the respondents describe the same bedside parameters together with respiratory rate [T, R2-Q5].

The ICU resident (R2) described a fixed recording schedule: "реанимация - ежечасно" (ICU — every hour). Ward patients are measured every 4 or 8 hours, and stable patients every 12 hours. The values are read "mostly on the monitor or in the prescription sheet" [T, R2-Q5]. Part of the information therefore exists only on the device until a nurse writes it down.

Laboratory results come from the hospital laboratory: blood gases and acid–base balance, complete blood count, biochemistry and urinalysis [T, R2-Q4].

Documentation follows the national forms of medical records. All state medical organisations had medical information systems (MIS) by 2020, and the Ministry has been moving them to paperless records [K4]. One commercial MIS, Damumed, covered more than 80% of the market in 2023 [K5]. A national repository of medical data (e-Densaulyq) is being developed.

The minimum requirements for medical digital systems were updated in July 2026 [K3]. They allow integration with laboratory, radiology and PACS systems, diagnostic equipment and patient monitoring devices, and they name HL7 and DICOM as usable standards. They also require that software and data are hosted in Kazakhstan, together with role-based access, encryption and logging of user actions. A hospital-side early-warning system would therefore receive data through the MIS or a device gateway, inside the hospital, under these rules.

### 2.3 How deterioration is recognised and escalated

Both respondents describe the same chain. A nurse notices a change during a routine measurement, checks the patient (consciousness, vital signs) and informs the physician. In a critical situation the nurse starts the necessary measures within her competence [T, R1-Q6; R2-Q6].

The physician then follows the national clinical protocol "Sepsis" (2020) [K2]. It uses the Sepsis-3 definition: suspected infection plus an acute rise of the SOFA score by at least 2 points. Outside the ICU it uses qSOFA for screening: respiratory rate above 22/min, altered mental state, systolic pressure of 100 mmHg or lower. The protocol sets a clear clock:

- lactate and blood cultures within 1.5 hours of a presumed diagnosis;
- fluid resuscitation started within the first hour;
- antibiotics not delayed;
- the source of infection controlled within 6 hours.

The weak points named by the respondents are at the start of this chain, before the protocol's clock begins:

- early signs such as fast breathing or unusual drowsiness are taken as minor;
- changes are lost at shift handover and at night;
- there are many patients for one nurse;
- a physician may not be available at once [T, R1-Q7; R2-FU4].

R2 stated it directly: "Отсутствие системы красных флагов! Кроме синий код и т.д." (there is no red-flag system, apart from code blue and the like) [T, R2-Q7]. In the parts of the Standard and of the sepsis protocol that I reviewed, there is no early-warning score and no automatic early-warning tool. Recognition depends on a person looking at the right numbers at the right time.

### 2.4 What this means for the system

The system cannot replace the monitor, the nurse or the protocol, and it should not try to. Its useful place is narrow:

- look at all patients every hour in the same way;
- notice a combination of changes that is easy to miss at night or at handover;
- raise a flag early enough that the protocol's steps — re-measurement, lactate, blood cultures, the physician's assessment — can start sooner.

Everything after the flag stays with the clinicians and the national protocol.

## 3. Where the data come from

In the target setting the system reads three kinds of data from the MIS:

- **Vital signs** charted by the nurse every hour. Charted values are preferred over raw monitor signals, because the nurse has already checked them and removed obvious artefacts.
- **Laboratory results**, when they are released by the laboratory.
- **Admission data:** age, sex, time of ICU admission.

They arrive through HL7 v2 messages (ADT for admissions and transfers, ORU for observations and results) or through the MIS's own interface, depending on what the hospital provides. Both are allowed by the national requirements [K3].

The PhysioNet data have the same shape: one row per patient-hour, with the vital signs and laboratory values recorded in that hour and empty cells where nothing was measured [D]. Each column corresponds to a real source:

- HR, O2Sat, Temp, SBP, MAP, DBP and Resp come from the bedside monitor via the nurse's hourly chart;
- EtCO2 comes from capnography in ventilated patients;
- the 26 laboratory values come from the laboratory;
- Age, Gender, HospAdmTime and ICULOS come from the admission record.

This is why a replay of the files is a fair stand-in for a live feed: the system sees, hour by hour, the same kind of record a hospital would send.

The replay adapter (FR-21) has one rule: at simulated hour *t* it releases only the rows with ICULOS ≤ *t*. The pipeline therefore cannot see the future, the same guarantee that the feature builder checks with its own test (FR-02, UT-02).

## 4. What happens every hour

The system works in an hourly cycle. Hourly matches the ICU recording schedule described by R2, and it is configurable. For each patient currently in the unit:

1. **Read.** The adapter returns the new values since the last cycle.
2. **Validate.** Values are checked against the schema and plausible ranges (FR-01). A rejected value is logged with patient, hour and field; it does not stop the cycle for other patients.
3. **Check freshness.** If none of the six key vital signs (HR, O2Sat, Temp, SBP, MAP, Resp) was recorded in the last 4 hours, the patient gets the state *insufficient data* (FR-11). No risk is computed and no alert can fire; instead the screen asks for a new measurement. The 4-hour default comes from the data analysis and from R1's answer; the limit is a setting, so a unit can choose R2's 1 hour.
4. **Build features** from hours ≤ *t* only (FR-02), with the same code that was used in training.
5. **Compute the risk** with the model in use, together with the five measurements that contributed most (FR-06, FR-10).
6. **Apply the alert rules** (FR-07):
   - an alert fires when the risk reaches the threshold;
   - after any alert, a repeat for the same patient is suppressed for 6 hours;
   - inside that window a new alert is allowed if the risk rises further by a set margin (proposed: 10 percentage points above the risk at the last alert); such an alert starts a new window.

   This follows both respondents: no constant repeats, but a new alert when the state changes [T, R1-FU2; R2-FU2].
7. **Store** the prediction with its time, model version, state and alert flag (FR-12), and write an audit record (NFR-10).
8. **Publish** the new state to the dashboard, which refreshes every minute.

For a unit of 6–12 beds this cycle takes seconds. The time limit that matters is clinical (one hour), not technical.

Failures are handled so that they cannot look like a stable unit. If the data source cannot be reached, the cycle records the failure and computes nothing new, and the dashboard shows the time of the last successful cycle. If the failure lasts, the patients pass into "insufficient data" after 4 hours, so a broken feed becomes visible to the staff instead of leaving old risks on the screen.

## 5. How the warning reaches the staff and what happens next

### 5.1 What the nurse sees

The dashboard runs in a browser on the ICU workstation.

**Patient list.** The list is ordered by urgency (FR-08):

1. unacknowledged alerts;
2. acknowledged alerts;
3. the remaining patients by risk;
4. patients with insufficient data, marked as such.

Each row shows the risk as a percentage together with a coloured label — for example "72% · High risk" in red (FR-08). R2 asked for a percentage and R1 for a colour with a short word, so the screen shows both [T, R1-FU3; R2-FU3]. A new alert also shows a banner at the top of the screen until it is acknowledged.

**Patient view.** Opening the patient shows:

- the risk curve and five vital signs on one time axis, with the threshold and alert hours (FR-09);
- the time since the last measurement next to each vital sign — for example "SpO₂ 91% · 2 h ago" (FR-09) — because R1 wanted to know when a value was measured [T, R1-Q11];
- the five measurements that raised or lowered the risk, in plain words (FR-10);
- one fixed sentence next to every alert: "Re-check the measurements and inform the responsible physician" (FR-19). It is the same sentence every time and it is not treatment advice (FR-18 stays Won't). R1 asked for exactly this prompt [T, R1-FU5];
- the line "Research prototype — not a diagnosis" (NFR-06).

### 5.2 The response to an alert

Figure 1 (the workflow) and Figure 2 (the sequence) show the steps:

1. The system raises the alert at hour *t*; the patient moves to the top of the list and the banner appears.
2. The nurse opens the patient and reads why the risk rose and how old each value is.
3. The nurse goes to the bedside, checks the patient and repeats the measurements. This is the same first step that R1 described for any suspected deterioration [T, R1-Q6].
4. The nurse acknowledges the alert with one of three outcomes (FR-20):
   - *re-checked, physician informed*;
   - *re-checked, change not confirmed* (for example, a measurement error);
   - *already known and being treated*.

   The acknowledgement clears the banner, and its time and outcome are stored.
5. If the physician was informed, the physician assesses the patient under the national sepsis protocol: SOFA or qSOFA, lactate and blood cultures within 1.5 hours, and treatment decisions [K2]. The system takes no part in these decisions.
6. New measurements and laboratory results enter the MIS. At the next cycle the risk is recomputed, and the physician sees whether the trend is turning.
7. An acute emergency (shock, arrest) is handled by the hospital's existing emergency procedures, outside the system.

If an alert is not acknowledged within a set time (proposed: 30 minutes), it stays at the top of the list marked "not acknowledged". In the target hospital the same event could also notify the duty physician through the MIS messaging. That notification is part of the target design only; the diploma shows the marker on the dashboard.

The acknowledgement outcomes are also evidence. The share of alerts marked "change not confirmed" is a direct, local measure of false alerts. It complements the retrospective PPV from the evaluation (09-verification §3).

### 5.3 Why the design looks like this

Each choice above answers a problem found in the literature, the existing systems or the user discussions:

- **Passive flag plus a short, fixed response path.** TREWS marks patients in the patient list instead of interrupting with pop-ups, and lets the clinician confirm or dismiss the alert [S-4]. COMPOSER shows the nurse the top features and offers a choice that includes notifying the physician; the choice to notify the physician at once was associated with shorter time to antibiotics [LIT-9]. CHARTwatch sends high-risk alerts to the team's phones and a risk list to the charge nurse for each shift [S-2].
- **Suppression with an exception.** CHARTwatch blocks repeats for 48 hours and re-alerts only after the risk falls and rises again [S-2]. The respondents asked for repeats only when the state changes, so this design uses a shorter window (6 hours) with a re-alert when the risk rises further.
- **No confident number on old data.** COMPOSER outputs "indeterminate" on unfamiliar input [LIT-7]. Here the same idea is applied to stale data, which R1 named as a reason not to trust a tool [T, R1-Q13].
- **The decision stays with clinicians.** Both respondents insisted that a tool must not replace professional judgement [T, R1-extra; R2-Q13].

## 6. Deployment and operation

### 6.1 Target deployment

Figure 3 shows the target deployment. Everything runs inside the hospital network, on an application server in Kazakhstan, as the national requirements demand [K3]:

- the MIS adapter receives HL7 messages or polls the MIS interface;
- a scheduler starts the hourly cycle;
- the FastAPI backend contains the core logic and the model;
- the Streamlit server delivers the dashboard to browsers at the nurse station and in the physicians' room over HTTPS.

The database would be PostgreSQL. SQLite is enough for one user on one laptop, but not for several workstations writing acknowledgements at the same time. The ORM (SQLAlchemy) was chosen so that this change does not touch the application code (technology comparison, decision 3).

Users log in with roles. Nurses see the list and acknowledge alerts; physicians also see the history of acknowledgements; an administrator sets thresholds and manages model versions. Every view of a patient and every acknowledgement is logged (NFR-10), as the national requirements expect for medical systems [K3].

### 6.2 Introduction in a hospital

A hospital would introduce the system in three steps, as recommended by the implementation literature [LIT-10] and as done for CHARTwatch [S-2]:

1. **Silent mode.** Predictions are computed and stored but not shown, for several weeks. This checks data completeness, alert frequency and agreement with real events.
2. **Pilot on one unit,** with staff training (R1 named training as a condition for use [T, R1-extra]).
3. **Review** of alert frequency, acknowledgement times, the share of unconfirmed alerts, uptime and model drift. The review is done first weekly, then monthly, before wider use.

### 6.3 In the diploma

In the diploma the same components run on one laptop. The replay adapter takes the place of the MIS adapter, SQLite takes the place of PostgreSQL, and a researcher plays the role of the administrator.

**Implemented in the diploma:**

- the data-source interface with the replay adapter;
- the hourly cycle;
- validation, features, models and explanations;
- all alert rules (threshold, suppression, re-alert, insufficient data);
- acknowledgement with an outcome and the "not acknowledged" marker;
- the API and the dashboard;
- storage of predictions and acknowledgements with an audit record.

**Designed but not implemented**, because they need a real hospital:

- the MIS or HL7 adapter;
- notifications to phones or through the MIS;
- hospital accounts and single sign-on;
- silent mode and the pilot in a hospital.

The live integration therefore stays out of the diploma's implementation (FR-17, Won't), but its place in the architecture is defined. A hospital would add one adapter, not change the system.

## 7. Figures

**Figure 1.** Clinical workflow with the system (activity diagram): [clinical-workflow.png](../../diagrams/export/clinical-workflow.png). The current workflow without the system is shown for comparison in [clinical-workflow-current.png](../../diagrams/export/clinical-workflow-current.png).

**Figure 2.** Hourly cycle and the response to one alert (sequence diagram): [alert-sequence.png](../../diagrams/export/alert-sequence.png).

**Figure 3.** Target deployment in a hospital and the diploma deployment (deployment diagram): [deployment.png](../../diagrams/export/deployment.png).

The sources are in [`diagrams/src`](../../diagrams/src).

## 8. Open questions for the next user discussions

1. Is the 30-minute limit for an unacknowledged alert right for an ICU, and who should see it first: the senior nurse or the duty physician?
2. Are the three acknowledgement outcomes enough, or is a free-text note needed?
3. Is a separate handover view useful — patients whose risk rose during the last shift and alerts still open — as R1 suggested [T, R1-FU4]? It is not in the requirements yet.
4. Do hourly charted values in the respondents' hospitals reach the MIS during the hour, or only at the end of a shift? If only at the end, the hourly cycle would see old data, and the insufficient-data state would fire too often.

## Sources

- [K1] Order of the Minister of Health of the Republic of Kazakhstan No. 78 of 26 April 2023 "On approval of the Standard for organising anaesthesiology and resuscitation care in the Republic of Kazakhstan" (reg. No. 32409), amended by Order No. 76 of 4 August 2025. https://zakon.uchet.kz/rus/docs/V2300032409
- [K2] Clinical protocol of diagnosis and treatment "Sepsis", Ministry of Health of the Republic of Kazakhstan, approved by the Joint Commission on the Quality of Medical Services, 1 April 2020, protocol No. 89. https://diseases.medelement.com/disease/сепсис-2020/16395
- [K3] Order of the acting Minister of Health No. 79 of 17 July 2026 amending the minimum requirements for medical digital systems; summary: https://pharmreviews.kz/novosti/novosti-kazahstana/v-kazakhstane-obnovili-trebovaniya-k-meditsinskim-tsifrovym-sistemam
- [K4] Prime Minister of the Republic of Kazakhstan, "Innovative technologies, electronic documentation and cost reduction: on development of digitalization in healthcare", 20 November 2020. https://primeminister.kz/en/news/reviews/innovative-technologies-electronic-documentation-and-cost-reduction-on-development-of-digitalization-in-healthcare
- [K5] Prime Minister of the Republic of Kazakhstan, "Economic Demonopolization Commission: Damumed database transferred to Ministry of Healthcare", 18 May 2023. https://primeminister.kz/en/news/komissiya-po-demonopolizatsii-ekonomiki-baza-dannykh-damumed-peredana-minzdravu-rk-24113
- [T] [Transcripts](../02-evidence/transcripts.md) of R1 and R2. Q = survey question, FU = follow-up question.
- [D] [Data analysis](../02-evidence/data-analysis.md) of the PhysioNet/CinC Challenge 2019 data.
- [LIT-7], [LIT-9], [LIT-10] Literature matrix sources #7 (Shashikumar 2021), #9 (Boussina 2024), #10 (van der Vegt 2024): [literature matrix](../03-literature/literature-matrix.md).
- [S-2], [S-4] Existing-system sources: CHARTwatch deployment (Pou-Prom et al. 2022) and TREWS adoption study (Henry et al.): [system architectures](../04-existing-systems/system-architectures.md).
