# Evidence of Relevance

**Status:** Plan ready; real user evidence is not yet complete. No discussion should be entered as evidence until it actually happens.

## 1. Purpose

The purpose of this activity is to test whether the proposed problem, users, and planned features match real clinical work instead of relying only on literature and design assumptions.

The target is **3–5 completed discussions with relevant user representatives**, in line with the diploma requirement.

The current proposed system is a research decision-support prototype that analyzes repeated patient measurements and estimates possible deterioration risk. It is not intended to diagnose, prescribe, or replace clinical judgement.

## 2. Questions the evidence should answer

| ID | Question | Project area affected |
|---|---|---|
| E1 | How do clinical staff currently notice that a patient may be getting worse? | Problem statement, baseline |
| E2 | Which measurements do they use and where do they see them? | Requirements, prototype |
| E3 | Where does the current monitoring process become difficult or fail? | Problem statement, scope |
| E4 | Are scoring systems, checklists, or automated alerts used? | Existing-system comparison, baseline |
| E5 | What context is needed next to a risk estimate for it to be understandable? | Requirements, UX |
| E6 | When are alerts or warnings ignored, and why? | Non-functional requirements, evaluation |
| E7 | What would make a user distrust or avoid an automated analytical tool? | Risks, requirements |
| E8 | What is missing or unnecessary in the proposed idea? | Scope |

## 3. Intended respondents

Priority is given to people with real ward or clinical experience:

| Respondent type | Reason |
|---|---|
| Practising doctor | Directly reviews patient condition and deterioration |
| Nurse with ward experience | Regularly observes and records vital signs |
| Resident or intern | Recent practical experience with monitoring and escalation |
| Senior medical student with ward/clinical practice | Can describe recent clinical routines |

Hospital IT or health-data specialists may provide useful technical background, but they should not replace the user discussions.

## 4. Discussion format

- About 10–15 minutes.
- Text, call, online meeting, or in person.
- Open and neutral questions.
- The respondent first describes the current process before the proposed solution is explained in detail.
- No patient information is requested.
- No recording unless the respondent explicitly agrees.

After each discussion, record only:

- date;
- anonymous respondent ID;
- general role and relevant experience;
- method;
- paraphrased findings;
- which assumption or requirement the finding affects.

Names, phone numbers, usernames, private chat screenshots, and patient data must not be committed to the repository.

## 5. Introductory statement

> I am collecting short anonymous feedback for my university diploma project about how clinical staff monitor patient condition. I do not need any patient information. I will only keep a short summary in my own words and your general role. You can skip any question or stop at any time.

## 6. Interview questions

1. What is your role or level of training, and what clinical experience do you have?
2. When you need to know whether a patient is stable or getting worse, what do you usually look at?
3. Where does that information come from: monitors, laboratory results, records, or somewhere else?
4. In practice, how is possible deterioration usually noticed?
5. How well does the current process work? Where does it get difficult or fail?
6. Have you used any scoring system, checklist, or automated alert for patient condition? What was your experience?
7. If a system showed an estimated risk for a patient, what would you need next to the value to understand it?
8. Have you seen alerts or warnings that were ignored? If so, why?
9. What would make you avoid or distrust a system that automatically analyzes patient measurements?
10. Is there anything important that I have not asked?

Optional follow-ups: “Can you give an example?”, “What happened next?”, “How often does that happen?”, “Who normally reacts to that?”

## 7. Evidence categories

- **USER-EVIDENCE:** a finding paraphrased from a real discussion held for this project.
- **LITERATURE:** a finding supported by a publication in the literature matrix.
- **ASSUMPTION:** project reasoning that has not yet been confirmed by users.

Only completed discussions count as user evidence.

## 8. Evidence register

Fill this table only after real discussions.

| ID | Date | Role / experience | Method | Paraphrased finding | Effect on project | Evidence type |
|---|---|---|---|---|---|---|
| EV-01 |  |  |  |  |  | USER-EVIDENCE |

Add EV-02, EV-03, and further rows only when the discussions have actually happened.

## 9. Assumptions to test

| ID | Assumption | Test |
|---|---|---|
| AS-01 | Clinical staff who review patient measurements are the right primary user | E1–E3 |
| AS-02 | Trends in repeated measurements are useful to see | E2 |
| AS-03 | A risk warning needs supporting context | E5 |
| AS-04 | Excessive or poorly targeted alerts reduce usefulness | E6 |
| AS-05 | A risk value alone is insufficient for interpretation | E5 |
| AS-06 | Early monitoring of deterioration is a suitable concrete problem for the proposed system | E1–E3, E8, supervisor feedback |

After the discussions, mark each assumption as supported, partly supported, not supported, or not tested.

## 10. Per-discussion summary template

### EV-XX — anonymous respondent

- Date:
- General role and experience:
- Method:
- Questions covered:
- Key points:
- What this confirms or challenges:
- Project change, if any:
- Evidence strength: strong / moderate / background only

## 11. Cross-interview synthesis

Complete this only after at least three valid discussions.

| Finding | Respondents supporting/challenging it | Agreement or disagreement | Project decision |
|---|---|---|---|
|  |  |  |  |

The synthesis should explain:

- where respondents agreed;
- where they disagreed;
- which assumptions were wrong or incomplete;
- which requirements or scope decisions changed;
- what remains uncertain.

## 12. Evidence-to-requirement traceability

Complete this after the discussions.

| Evidence ID | Finding | Requirement affected | Decision |
|---|---|---|---|
|  |  |  |  |

## 13. Outreach messages

### Informal message to a student or resident

> Привет! Я делаю диплом в AITU по системе, которая помогает анализировать показатели пациентов и замечать возможное ухудшение состояния. Мне нужно коротко поговорить с несколькими людьми с клинической практикой о том, как вы обычно следите за состоянием пациента. Это 8–10 вопросов, можно ответить прямо текстом, примерно 10–15 минут. Данные пациентов не нужны, ответы будут анонимными. Если у тебя была практика в отделении, сможешь помочь? Если нет, может, подскажешь кого-нибудь с такой практикой?

### Formal message to a doctor or nurse

> Здравствуйте! Меня зовут Аман, я студент AITU и делаю дипломный проект по системе анализа показателей пациентов. Для проекта мне нужно понять, как в реальной работе отслеживают возможное ухудшение состояния пациента. Хотел бы задать 8–10 коротких вопросов, это займёт около 10–15 минут и можно ответить текстом. Никакие данные пациентов не нужны, ответы будут использоваться только в анонимном виде. Если Вам будет удобно, буду очень благодарен за помощь. Если неудобно самому, подскажите, пожалуйста, коллегу.

Sending messages is not evidence by itself; only completed discussions count.

## 14. Supervisor questions

Ask the supervisor:

1. Is this short anonymous discussion format acceptable for the diploma?
2. Is any additional ethics or university approval needed for these discussions?
3. Does a senior medical student count only when they have actual clinical/ward experience?
4. Can the supervisor suggest or introduce suitable respondents?
5. If fewer than three valid discussions can be completed, which alternative form of relevance evidence is acceptable?

Record the actual answers in the supervisor-feedback log without adding assumptions.

## 15. Timeline

| Date | Action |
|---|---|
| 13–14 Oct | Send first outreach messages |
| 13–20 Oct | Hold discussions and update the register immediately after each one |
| 18–20 Oct | Follow up and contact additional respondents if fewer than 3 are complete |
| 21 Oct | Write synthesis and map findings to requirements |
| 22–23 Oct | Apply confirmed changes to proposal, requirements, and prototype |

If fewer than three valid discussions are obtained, record the true number and ask the supervisor which alternative evidence is acceptable. Do not create or pad responses.

## 16. Completion criteria

This component is complete when:

- at least 3 valid discussions with suitable representatives have been completed, or another evidence form has been explicitly accepted by the supervisor;
- every completed discussion has an anonymous entry;
- the assumptions have been evaluated against the evidence;
- a cross-interview synthesis has been written;
- findings have been linked to affected requirements or scope decisions;
- private proof of participation can be shown to the supervisor if requested without committing private information to Git.

## 17. Current open items

- Respondents are not yet confirmed in this document.
- The primary user remains a working definition until evidence is collected.
- The concrete sepsis direction remains subject to supervisor review.
- The ethics/approval procedure for the short discussions should be confirmed with the supervisor.
- Requirement changes cannot be written until real evidence exists.
