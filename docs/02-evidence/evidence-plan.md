# Evidence of Relevance: Plan

**Status:** DRAFT. The plan and interview guide are written. Outreach is the next step. **No discussions have been held and no findings are recorded.**
**Last updated:** 11 Oct 2026

## 1. Why I am doing this

The diploma requirements ask for evidence that the problem is real for the people who would use the system, normally 3–5 discussions with user representatives. I want to check my assumptions against what people with clinical experience actually say, instead of building the project around guesses.

The current direction is still a draft and has not been approved by my supervisor: a decision-support prototype that looks at repeated vital-sign and lab measurements and estimates how a patient's condition is developing, for clinical staff who review those measurements. It is not meant to diagnose, prescribe, or replace clinical judgement.

## 2. What I want to find out

| ID | Question | What it affects |
|---|---|---|
| E1 | How do clinical staff currently notice that a patient may be getting worse? | Problem statement, baseline |
| E2 | Which measurements do they look at, and where do they see them? | Requirements, prototype |
| E3 | How well does the current way of working function, and where does it struggle, if at all? | Problem statement, scope |
| E4 | Are scores, checklists or automated alerts already used? | Baseline, existing systems |
| E5 | What would they need next to a risk estimate to understand it? | Requirements, UX |
| E6 | Have they seen alerts that were ignored, and why? | Non-functional requirements, evaluation |
| E7 | What would stop them from using such a tool? | Risks, scope |
| E8 | What in my idea is unnecessary or missing? | Scope |

## 3. Who I want to talk to

Target: **3–5 completed discussions.** Nobody counts until the conversation has actually happened. Nobody is confirmed yet.

| Type | Why | How I will try to reach them |
|---|---|---|
| Practising doctor | Judges patient condition directly | Personal contacts, referrals |
| Nurse with ward experience | Takes and reviews vital signs daily | Personal contacts, referrals |
| Resident or intern | Recent ward experience, more reachable | University and personal contacts |
| Senior medical student with ward or clinical practice | Reachable, can describe training and ward routines | Medical university students |

People with real ward experience come first. A student with no clinical practice can give background, but I will not count them as strong user evidence unless my supervisor agrees.

Healthcare data or hospital IT people may be useful for technical questions, but they should not replace the user discussions.

## 4. How the discussions work

- Short and informal: about 15 minutes, by message, call or in person. Text is fine.
- 8–10 open questions. They talk about their own experience.
- I do not describe my solution until they have described their current way of working.
- No recording unless they explicitly agree.

After each discussion I write down: date, anonymous ID, general role, method, what they said (in my own words), and which of my assumptions or requirements it affects.

## 5. Privacy

- I do not ask about individual patients and I do not want any patient information. If it comes up by accident, I leave it out.
- Participation is voluntary. They can skip any question or stop.
- At the start I say that I will paraphrase and keep notes anonymous, and I ask permission before using any direct quote.
- Names, phone numbers and usernames **are not stored in the repository** and I do not commit chat screenshots or exports.
- I keep a private list of who I spoke to and when, outside the repository. If my supervisor or the committee asks for proof that the discussions took place, I can show it to them in person.
- Whether informal discussions like this need any university ethics step: [REQUIRES SUPERVISOR APPROVAL].

## 6. Questions for the discussion

I keep them open and neutral. I do not ask "would an ML system be useful?".

1. What is your role or level of training, and what clinical experience do you have?
2. When you need to know whether a patient is stable or getting worse, what do you look at?
3. Where does that information come from (monitors, lab results, records, something else)?
4. In practice, how is a possible deterioration usually noticed?
5. How well does that work? Where does it go wrong or become hard, if it does?
6. Have you used any scoring system, checklist or automated alert for patient condition? What was your experience?
7. If a system showed an estimated risk for a patient, what would you want to see next to it to understand it?
8. Have you seen alerts or warnings that got ignored? If so, why?
9. What would make you avoid or distrust a system that analyzes patient measurements automatically?
10. Is there anything important about this that I haven't asked?

Follow-ups when needed: "Can you give an example?", "What happened next?", "How often does that happen?", "Who usually sees that?". I do not force every follow-up.

## 7. How I separate evidence from guesses

- **USER-EVIDENCE:** something a real respondent told me in a discussion I held. Only this counts as evidence of relevance.
- **LITERATURE:** supported by a verified source in `docs/03-literature/literature-matrix.md`. It supports my reasoning but does not replace the discussions.
- **ASSUMPTION:** my own belief that nobody has confirmed. It is never presented as a finding.

### Evidence register

| ID | Date | Respondent | Role / experience | Method | What they said (paraphrased) | Effect on project | Type |
|---|---|---|---|---|---|---|---|
| EV-01 | | | | | *(empty: no discussion held yet)* | | |

### Assumptions to test

| ID | Assumption | Based on | How I will test it |
|---|---|---|---|
| AS-01 | Clinical staff reviewing patient indicators are a suitable primary user | My proposal draft | E1–E3 and supervisor |
| AS-02 | Trends in measurements are useful to see | My design reasoning | E2 |
| AS-03 | Users need some explanation next to a risk warning | Design reasoning and literature | E5 |
| AS-04 | Too many alerts reduce usefulness | Wong et al. (2021) found a large alert burden in one health system | E6 |
| AS-05 | A risk score alone is not enough | My design idea | E5 |
| AS-06 | Early deterioration monitoring is a suitable problem for this diploma | Literature review and scope analysis | User evidence and supervisor approval |

After the discussions I will mark each one as supported, partly supported, not supported or not tested.

## 8. Outreach

I plan to send **6–8 requests** to get 3 discussions. This is my own expectation that not everyone will reply, not a measured rate. Sending requests is not evidence; only completed discussions are.

**To a student or resident (informal):**

> Привет! Я делаю диплом в AITU по системе, которая помогает следить за показателями пациентов (давление, пульс, анализы). Мне нужно поговорить с несколькими людьми с клинической практикой: как вы вообще замечаете, что пациенту становится хуже. Это 8–10 коротких вопросов, можно прямо текстом, минут 15. Данные пациентов не нужны, всё анонимно. Если у тебя была практика в отделении, поможешь? Или подскажи, кого ещё можно спросить.

**To a doctor or nurse (formal):**

> Здравствуйте! Меня зовут Аман, я студент AITU, делаю дипломный проект по системе, которая помогает отслеживать показатели пациентов (жизненные признаки, анализы). Чтобы понять, нужна ли такая система на самом деле, хочу коротко поговорить с людьми, которые работают с пациентами. Нужно около 15 минут и 8–10 вопросов о том, как у Вас сейчас устроена эта работа. Никаких данных о пациентах не нужно, всё будет анонимно, можно ответить текстом. Если неудобно самому, подскажите, пожалуйста, коллегу. Спасибо!

## 9. Timeline

| Date | Action |
|---|---|
| 11 Oct | Send the first requests |
| 12 Oct | Call with supervisor: ask the questions in Section 10 |
| 13–20 Oct | Hold discussions as people reply; update the register right after each one |
| 21 Oct | Summarize what I learned and link it to requirements |
| 22–23 Oct | Buffer |

**If I have fewer than 3 valid discussions by about 21 Oct:** I will not pad the register. I will record exactly what I have and ask the supervisor which other evidence form is acceptable. The official text also lists observing relevant processes and analyzing available data, and an agreement with a real client.

## 10. Questions for my supervisor

1. Can he introduce anyone with clinical or hospital experience?
2. Is this short, anonymous discussion format acceptable, and is any extra approval needed?
3. Does a senior medical student without clinical practice count toward the 3–5?

## 11. Open items

| Item | Status |
|---|---|
| Whether 3–5 suitable respondents will be available | [NOT YET DETERMINED] |
| Final primary user | [REQUIRES SUPERVISOR APPROVAL] and user evidence |
| Final project direction (Option B) | [REQUIRES SUPERVISOR APPROVAL] |
| Whether any ethics step is required | [REQUIRES SUPERVISOR APPROVAL] |
| Whether students without clinical practice count | [REQUIRES SUPERVISOR APPROVAL] |
| Changes to requirements from the discussions | [WAITING FOR USER EVIDENCE] |

## 12. DIP-3 checklist

- [x] Plan, respondent types, questions and privacy rules written
- [x] Evidence register template prepared
- [ ] First requests sent
- [ ] Questions in Section 10 discussed with supervisor

*Collecting the discussions themselves and filling the register is tracked in DIP-4.*