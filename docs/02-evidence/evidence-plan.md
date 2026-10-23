# Evidence of Relevance

**Status:** Collection in progress since 21 Oct 2026 (anonymous survey plus follow-up discussions). No response is entered as evidence until it has actually been received. Results so far: [user-evidence.md](user-evidence.md) — 2 respondents, both with a survey answer and a follow-up exchange (2 discussions); their full anonymised answers are in [transcripts.md](transcripts.md) (added on 23 Oct at the supervisor's request, FB-15). Data analysis: [data-analysis.md](data-analysis.md).

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

Two formats are used (from 21 Oct 2026):

1. **Anonymous online survey** (Google Forms) covering the questions of §6 in 13 survey questions. The form was designed with an optional page showing a prototype screen; the version sent on 21 Oct did not include it because the screens were not yet published in the repository. No login and no email collection. Respondents may leave a contact for 1–2 follow-up questions; a survey answer with a follow-up exchange is recorded as a discussion, a survey answer without one is recorded as a survey response.
2. **Short text or voice discussion** (Telegram or call) with the same questions and follow-ups.

The supervisor was asked on 21 Oct 2026 whether the survey together with the dataset analysis is acceptable evidence (feedback log Q-03).

Common rules for both formats:

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
- the full answers as a transcript (original language and translation), if the respondent agrees to publication; otherwise paraphrased findings;
- which assumption or requirement the finding affects.

Until 23 Oct only paraphrased findings were recorded. After the supervisor asked for transcripts (FB-15), both respondents were asked again and agreed to the publication of their anonymised answers in full.

Names, phone numbers, usernames, private chat screenshots, and patient data must not be committed to the repository.

## 5. Introductory statement

> I am collecting short anonymous feedback for my university diploma project about how clinical staff monitor patient condition. I do not need any patient information. Your answers may be published in the project without your name or contacts, together with your general role. You can skip any question or stop at any time.

This wording is used from 23 Oct 2026. Before that date the statement promised only a short summary, so the first two respondents were asked separately before their transcripts were published.

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

- **USER-EVIDENCE:** a finding from a real discussion held for this project, backed by its transcript.
- **LITERATURE:** a finding supported by a publication in the literature matrix.
- **ASSUMPTION:** project reasoning that has not yet been confirmed by users.

Only completed discussions count as user evidence.

## 8. Evidence register

The respondents and the register of real findings are kept in [user-evidence.md](user-evidence.md) (§1–§2). A row is added only for an answer actually received.

## 9. Assumptions to test

| ID | Assumption | Test |
|---|---|---|
| AS-01 | Clinical staff who review patient measurements are the right primary user | E1–E3 |
| AS-02 | Trends in repeated measurements are useful to see | E2 |
| AS-03 | A risk warning needs supporting context | E5 |
| AS-04 | Excessive or poorly targeted alerts reduce usefulness | E6 |
| AS-05 | A risk value alone is insufficient for interpretation | E5 |
| AS-06 | Early monitoring of deterioration is a suitable concrete problem for the proposed system | E1–E3, E8, supervisor feedback |

After the discussions, mark each assumption as supported, partly supported, not supported, or not tested. Current statuses: [user-evidence.md](user-evidence.md) §3.

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

A preliminary synthesis of the first two respondents is in [user-evidence.md](user-evidence.md) §4. The full synthesis is written after at least three valid discussions.

The synthesis should explain:

- where respondents agreed;
- where they disagreed;
- which assumptions were wrong or incomplete;
- which requirements or scope decisions changed;
- what remains uncertain.

## 12. Evidence-to-requirement traceability

See [user-evidence.md](user-evidence.md) §5.

## 13. Outreach messages

### Informal message to a student or resident

> Привет! Я делаю диплом в AITU по системе, которая помогает анализировать показатели пациентов и замечать возможное ухудшение состояния. Мне нужно коротко поговорить с несколькими людьми с клинической практикой о том, как вы обычно следите за состоянием пациента. Это 8–10 вопросов, можно ответить прямо текстом, примерно 10–15 минут. Данные пациентов не нужны, ответы будут анонимными. Если у тебя была практика в отделении, сможешь помочь? Если нет, может, подскажешь кого-нибудь с такой практикой?

### Formal message to a doctor or nurse

> Здравствуйте! Меня зовут Аман, я студент AITU и делаю дипломный проект по системе анализа показателей пациентов. Для проекта мне нужно понять, как в реальной работе отслеживают возможное ухудшение состояния пациента. Хотел бы задать 8–10 коротких вопросов, это займёт около 10–15 минут и можно ответить текстом. Никакие данные пациентов не нужны, ответы будут использоваться только в анонимном виде. Если Вам будет удобно, буду очень благодарен за помощь. Если неудобно самому, подскажите, пожалуйста, коллегу.

Outreach messages are not evidence; only completed discussions and received survey responses are recorded.

## 14. Questions for the supervisor

1. Is the anonymous survey with short follow-up discussions an acceptable format? Asked on 21 Oct (Q-03). Discussed on 23 Oct: the supervisor asked to record the answers as transcripts (FB-15).
2. Is any ethics or university approval needed for the survey and the discussions? Not reached at the meeting on 23 Oct; still to be asked.
3. Does a senior medical student count as a respondent only with actual clinical or ward experience? Not asked yet.
4. Can the supervisor suggest suitable respondents? Not asked yet.
5. If fewer than three discussions can be completed, which other evidence is acceptable? Not asked yet.

Answers are recorded in the [feedback log](../11-feedback-log.md).

## 15. Timeline

| Date | Action |
|---|---|
| 13–14 Oct | First outreach planned (not sent) |
| 21 Oct | Survey created; outreach to 8–10 people with clinical experience |
| 21 Oct | First 2 survey answers received; follow-up held with R2 ([user-evidence.md](user-evidence.md)) |
| 22 Oct | Follow-up held with R1 |
| 21–22 Oct | Collect survey answers and hold follow-up discussions; update the register after each one |
| 22 Oct | Write synthesis and map findings to requirements (DIP-8) |
| 23 Oct | Supervisor meeting; transcripts published with the respondents' agreement; the five proposed changes adopted in the requirements |
| From 24 Oct | Further respondents and the user check of the prototype screens |

If fewer than three valid discussions are obtained, the actual number is reported and the supervisor is asked which other evidence is acceptable.

## 16. Completion criteria

This component is complete when:

- at least 3 valid discussions with suitable representatives have been completed, or another evidence form has been explicitly accepted by the supervisor;
- every completed discussion has an anonymous entry;
- the assumptions have been evaluated against the evidence;
- a cross-interview synthesis has been written;
- findings have been linked to affected requirements or scope decisions;
- private proof of participation can be shown to the supervisor if requested without committing private information to Git.

## 17. Current open items

- 2 discussions so far; at least one more is needed.
- The primary user is supported by the first answers (AS-01), but on two respondents only.
- The supervisor called the sepsis direction a good idea on 23 Oct, provided it is planned in depth (feedback log Q-01).
- Whether the survey and the short discussions need any ethics or university approval has not been asked yet.
- The proposed requirement changes ([user-evidence.md](user-evidence.md) §5) were adopted on 23 Oct; the first values of the new workflow (30-minute acknowledgement limit, 10-point re-alert margin) still have to be checked with respondents.
