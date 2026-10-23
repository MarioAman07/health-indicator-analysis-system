# User Evidence: Results

**Status:** Collection in progress. 2 respondents so far, both with a survey answer and a follow-up exchange, so 2 discussions. The target is 3–5 discussions ([evidence plan](evidence-plan.md) §1).  
**Last updated:** 23 Oct 2026  
**Method:** [evidence plan](evidence-plan.md) §4 — anonymous Google Forms survey, followed by a round of follow-up questions in a messenger.  
**Full answers:** [transcripts.md](transcripts.md) (original Russian text with an English translation).

The findings below are paraphrased in my own words; the full anonymised answers are in [transcripts.md](transcripts.md). Names, contacts, chat screenshots and the raw answer table are kept privately and are not committed.

## 1. Respondents

| ID | Date | Role | Setting | Clinical experience | Format | Counts as |
|---|---|---|---|---|---|---|
| R1 | 21 Oct 2026 (survey), 22 Oct 2026 (follow-up) | Nurse | General medical or surgical ward | More than 5 years | Survey + follow-up in a messenger (5 answers) | Discussion |
| R2 | 21 Oct 2026 | Resident / intern | ICU; urology-nephrology; operating theatre | 1–3 years | Survey + follow-up in a messenger (5 answers) | Discussion |

The survey ran without the page with the prototype screen (questions 14–15), because the screens were not yet published in the repository. The user check of the screen (NFR-07, H3) has therefore **not been done yet**.

## 2. Evidence register

| ID | Finding (paraphrased) | Source | Affects |
|---|---|---|---|
| EV-01 | A change in a patient's state is usually noticed first by the nurse during routine measurement of vital signs. The nurse checks the patient and informs the physician; in critical situations staff act within their competence. | R1, R2 | AS-01, users |
| EV-02 | How old data may be. R2: in the ICU vital signs are recorded every hour (on wards every 4–8 hours, for stable patients 12 hours), and measurements not updated every hour are out of date, with nuances: severity, mechanical ventilation, surgery. R1: the system should draw attention when values have not been updated for 4–6 hours, earlier for patients whose values can change quickly. | R2 (survey Q5, follow-up 1), R1 (follow-up 1) | FR-11, data choice |
| EV-03 | Deterioration is missed when early signs such as fast breathing or unusual drowsiness are taken as minor, when information is lost at shift handover, at night, with many patients, and when a physician is not available. | R1 (Q7), R2 (follow-up 4) | AS-06, FR-08 |
| EV-04 | There is no "red flag" system for early deterioration. Only emergency codes such as code blue exist. | R2 (Q7) | AS-06 |
| EV-05 | Scores and alerts are already in use: qSOFA, SOFA and SIRS in R2's ICU, and automatic alerts in the hospital information system on R1's ward. Their value depends on accurate and timely data entry and on staff response. Scores are general, and patient-specific factors (age, comorbidities) are judged by the physician. | R1 (Q8–9), R2 (Q8–9, Q13) | Baselines, C-04, NFR-06 |
| EV-06 | Alerts can be missed or ignored under high workload, staff shortage and frequent false alarms (R1, general opinion). In R2's unit alerts are not ignored. | R1 (Q9–10), R2 (Q10) | AS-04, FR-07 |
| EV-07 | A risk number alone is not enough. Users want to see why the risk rose: which measurements changed (for example, falling oxygen saturation or changes in pulse and blood pressure), when they were measured, and the clinical dynamics. | R1 (Q11, follow-up 5), R2 (Q11) | AS-03, AS-05, FR-09, FR-10 |
| EV-08 | Features chosen as useful by both respondents: which measurements influenced the risk, a warning when data are missing or out of date, and a patient list sorted by risk. R2 also chose charts over time and a limit on repeated alerts. | R1, R2 (Q12) | FR-08 – FR-11, FR-07 |
| EV-09 | How to show the risk. R2 finds a percentage clearest. R1 prefers a colour together with a short label, for example "High risk" in red, because it is faster to read under workload. | R2 (follow-up 3), R1 (follow-up 3) | Dashboard, FR-08 |
| EV-10 | Repeated alerts. R1: identical notifications should not be repeated constantly; repeat when the problem persists or the patient's state changes, and repeat at once in a dangerous situation. R2: alert on every change (but also ticked "limit on how often alerts repeat" in the survey). Both support a new alert when the state changes. | R1 (follow-up 2), R2 (follow-up 2, Q12) | AS-04, FR-07 |
| EV-11 | Reasons to distrust a tool: frequent errors, unclear results, data not updated in time, high risk without explanation. The tool must be simple and fast, staff need training, and it must not replace professional judgement. | R1 (Q13, final question) | NFR-06, NFR-07, FR-10, FR-11 |
| EV-12 | R1 would like the system to suggest what to do next. In the follow-up she specified: highlight the changed values and prompt to re-check them and to inform the responsible medical worker. | R1 (Q11, follow-up 5) | FR-18 (Won't), FR-10 |
| EV-13 | Asked which indicators are missing besides the five vital signs (HR, Temp, Resp, MAP, SpO₂), R2 answered that the monitors already provide everything and nothing is superfluous. | R2 (follow-up 5) | FR-09 |
| EV-14 | At shift handover, important changes from the night and which patients need closer watching can be missed. A view with the latest values, their changes and a separate list of patients who need special attention would help. | R1 (follow-up 4) | AS-06, FR-08, FR-09 |

## 3. Assumptions after the first answers

| ID | Assumption | Status | Basis |
|---|---|---|---|
| AS-01 | Clinical staff who review patient measurements are the right primary user | **Supported** | EV-01 |
| AS-02 | Trends in repeated measurements are useful to see | **Supported** — both ask to see how values changed; R2 chose charts, R1 asked for the latest values and their changes; the preferred form is not settled | EV-07, EV-08, EV-14 |
| AS-03 | A risk warning needs supporting context | **Supported** | EV-07, EV-11 |
| AS-04 | Excessive or poorly targeted alerts reduce usefulness | **Partly supported** — R1 sees false alarms and identical repeats as a problem; R2 reports that alerts are not ignored | EV-06, EV-10 |
| AS-05 | A risk value alone is insufficient for interpretation | **Supported** | EV-07 |
| AS-06 | Early monitoring of deterioration is a suitable concrete problem | **Supported** | EV-03, EV-04, EV-14 |

These statuses rest on two people, one of whom works on a ward rather than in the ICU. They are preliminary until at least three discussions are completed.

## 4. Preliminary synthesis

- **Agreement.**
  - Both respondents describe nurses as the first to notice a change.
  - Both ask to see why the risk is high and which values changed, and both want a warning about missing or outdated data.
  - Both want a list of patients who need attention.
  - Both support a new alert when the patient's state changes.
  
  This supports the current design: risk with contributing measurements, trends, an "insufficient data" state, a sorted list and a suppression window.
- **Disagreement.**
  - *How old data may be:* 1 hour (R2, ICU) versus 4–6 hours (R1, ward). The data analysis gives 4 hours as a data-based candidate.
  - *How to show the risk:* a percentage (R2) versus colour and a short label (R1). Showing the percentage together with a colour-coded level label would meet both.
  - *Alert fatigue:* R1 sees false alarms and identical repeats as a problem; R2 says alerts are not ignored.
- **New or changed points.**
  - Re-alert when the risk rises further instead of only after a fixed window (EV-10).
  - Show when each measurement was taken (EV-07).
  - Help at shift handover with recent changes and a list of patients to watch (EV-14).
- **Kept out of scope.** Treatment and medication recommendations stay out of scope (FR-18, C-04). R1's request (EV-12) is limited to highlighting changed values and prompting to re-check and inform the responsible clinician. A fixed, non-clinical prompt of this kind fits the scope and was adopted on 23 Oct (§5).
- **Still uncertain.**
  - Whether users understand the patient screen (user check not done).
  - Whether the findings hold for an ICU nurse and for more respondents.

## 5. Evidence → requirements

| Evidence | Requirement | Decision |
|---|---|---|
| EV-01 | Users (proposal §2), FR-08 | Keep: nurse or physician as primary user |
| EV-03, EV-04, EV-08, EV-14 | FR-08 patient list | Keep (patients with an active alert first, then by risk) |
| EV-07, EV-08, EV-13, EV-14 | FR-09 trends with the five vital signs | Keep; no extra signals needed |
| EV-07, EV-08, EV-11 | FR-10 contributing measurements | Keep |
| EV-02, EV-08, EV-11 | FR-11 insufficient-data state | Keep configurable. **Adopted 23 Oct:** default 4 h (data analysis; within R1's 4–6 h). R2's 1 h for the ICU stays possible as a setting |
| EV-06, EV-10 | FR-07 alert suppression | Keep the suppression window. **Adopted 23 Oct:** a new alert inside the window when the risk rises further (FR-07) |
| EV-09 | FR-08 / dashboard | **Adopted 23 Oct:** risk shown as a percentage together with a colour-coded level label (FR-08); the API keeps a value in [0, 1] and the level |
| EV-07 | FR-09 | **Adopted 23 Oct:** time since the last measurement next to each vital sign (FR-09) |
| EV-12 | FR-18 (Won't), FR-10 | No treatment advice. **Adopted 23 Oct:** a fixed prompt "re-check the measurements and inform the responsible clinician" next to an alert (FR-19) |
| EV-05, EV-11 | NFR-06, C-04 | Keep: "research prototype — not a diagnosis" on every screen |

The five proposals were presented at the meeting with the supervisor on 23 Oct and adopted by me the same day; they are recorded in the [requirements](../06-requirements.md) and the [target system description](../07-architecture/target-system.md).

## 6. Next steps

1. Get at least one more discussion. A third person with ICU experience would be best.
2. Run the user check of the prototype screen (questions 14–15) with 2–3 respondents once the screens are on GitHub.
3. Ask the next respondents about the limit for outdated data and about the form of the risk display, where the first two disagree.
