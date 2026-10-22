# Supervisor Feedback Log

**Supervisor:** Altynbek Seitenov (Сейтенов Алтынбек Серикович)  
**Purpose:** record every piece of supervisor feedback, the decision I took on it, and the change it led to, so that the review → revision trail can be traced in Git and YouTrack.  
**Last updated:** 22 Oct 2026

Status values: **Open** (not started) · **In progress** · **Done** (change merged into `main`, or the requested action completed) · **Answered** (a question that needed only a reply).

IDs follow the order in which entries were recorded; rows are listed by date.

## 1. Feedback register

| ID | Date | Channel | Feedback (quoted or paraphrased) | My decision | Resulting change | Status |
|---|---|---|---|---|---|---|
| FB-01 | 30 Sep 2026 | Discussion | The topic was agreed with the supervisor; the supervisor offered to adapt the topic for me. The application for topic approval was submitted on 1 Oct 2026; the official decision is expected after the pre-defense. | Keep the agreed topic. Make it concrete as early sepsis-risk prediction from ICU time-series data, pending supervisor confirmation (see Q-01). | `docs/decisions/ADR-001-scope.md` (DIP-11) | In progress |
| FB-13 | 12 Oct 2026 | Discussion | The supervisor asked me to send the materials that were ready; his written feedback on them came on 19 Oct (FB-02 – FB-09). | Send the available materials. | Materials sent; feedback recorded as FB-02 – FB-09 | Done |
| FB-02 | 19 Oct 2026 | Email | "The project has a starting structure, but the documentation, particularly README, needs substantial improvement." | Rewrite the README to cover every item of Git Step 3 and add a component status table. | `README.md` (DIP-20) | Done |
| FB-03 | 19 Oct 2026 | Email | Problem statement and relevance: explain what problem the system addresses, who the intended users are, and why the solution is necessary. | Rewrite the problem statement and users; define primary and secondary users; back relevance with user discussions and an analysis of the dataset. | `docs/01-proposal.md` (DIP-11), `docs/02-evidence/` (DIP-8, DIP-9) | In progress |
| FB-04 | 19 Oct 2026 | Email | Proposed solution: present my own vision of how the system should work — main functions, architecture, expected outcomes. | Add a "My proposed solution" section; specify requirements, architecture diagrams and prototype screens. | `docs/01-proposal.md`, `docs/06-requirements.md`, `docs/07-architecture/`, `docs/08-prototype/` (DIP-11 – DIP-14) | Done |
| FB-05 | 19 Oct 2026 | Email | Machine-learning methodology: justify the algorithms, explain the data, describe how model performance will be evaluated. | Fix the prediction task, label interpretation, split strategy, features, models, baselines, metrics and success criterion in one document, each with a rationale. | `docs/05-technology/ml-methodology.md` (DIP-10), `docs/09-verification.md` (DIP-15) | Done |
| FB-06 | 19 Oct 2026 | Email | Literature and existing systems: critical comparison; explain which limitations the project addresses. | Add a "limitation → project response" table; correct inconsistencies between the system comparison and the literature matrix; restore the search log. | `docs/03-literature/`, `docs/04-existing-systems/` (DIP-17, DIP-18) | Done |
| FB-07 | 19 Oct 2026 | Email | Complete the required documents, diagrams, requirements, evaluation plan and README according to the pre-defense guidelines. | Fill components 6–11, which were empty on 19 Oct. | DIP-7, DIP-12 – DIP-16 | Done |
| FB-08 | 19 Oct 2026 | Email | "I would particularly like to hear your own reasoning and justification for the proposed technical decisions, rather than simply reviewing formal documentation." | Write a one-page summary of my reasoning for the main technical decisions. | `docs/00-my-reasoning.md` (DIP-22) | Open |
| FB-09 | 19 Oct 2026 | Email | Send the revised materials and report by 22 October; a Teams meeting will follow before the pre-defense on 24 October. | Send report v1 on 22 Oct; address meeting feedback through separate pull requests. | Report v1 (DIP-21) | In progress |
| FB-10 | 19 Oct 2026 | Email | Professional communication: begin messages with an appropriate greeting, particularly when addressing the supervisor. | Every message to the supervisor starts with a greeting. | Applied from 21 Oct 2026 | Done |
| FB-11 | 19 Oct 2026 | Email (forwarded announcement) | Approbation-period form: one PDF with YouTrack board and task screenshots, one unified PDF report with all required sections, access for supervisor and committee before submission; deadline 18:00, 24 Oct 2026. | Prepare both PDFs and check access from a logged-out browser before submitting. | DIP-22 | Open |
| FB-12 | 21 Oct 2026 | Email | Reply to the clarification of Q-01: "I see. Please prepare as research justification and we will see [it on] 23." "Good idea." | Prepare a short research justification of the sepsis focus: relevance, evidence from the literature, research gap, research questions and hypotheses, data and feasibility. Present it at the meeting on 23 Oct. | `docs/01-research-justification.md` (DIP-24) | Done |

## 2. Questions sent to the supervisor

| ID | Date sent | Question | Answer | Recorded on |
|---|---|---|---|---|
| Q-01 | 21 Oct 2026 | Is early sepsis prediction from ICU time-series data (PhysioNet 2019) an acceptable concrete focus for the agreed topic? | 21 Oct: the supervisor did not understand the question. Clarification sent on 21 Oct: the broad topic is narrowed to predicting sepsis risk about 6 hours before onset from hourly ICU vital signs and lab values (PhysioNet 2019), with trends and reasons shown for each warning. Supervisor's reply on 21 Oct: "I see. Please prepare as research justification and we will see [it on] 23." "Good idea." Research justification prepared (FB-12, DIP-24); final confirmation expected at the meeting on 23 Oct. | 21 Oct 2026 |
| Q-02 | 21 Oct 2026 | Is 23 October suitable for the Teams meeting? | Yes — meeting on 23 Oct; time to be agreed. | 21 Oct 2026 |
| Q-03 | 21 Oct 2026 | Are questionary forms together with an analysis of the PhysioNet dataset acceptable as relevance evidence? | To be discussed at the meeting on 23 Oct. | 21 Oct 2026 |

## 3. Process issues found in self-review

| Date found | Issue | Correction |
|---|---|---|
| 19 Oct 2026 | Up to 13 Oct, pull requests #1, #2, #3 and #5 were merged by me without review, #2/#3/#5 targeted feature branches instead of `main`, and several commits reached `main` directly. | Rule adopted on 21 Oct: every task gets its own branch from `main` and its own pull request, and `main` is protected so that changes arrive only through pull requests (protection is set up in DIP-6); key changes are reviewed with the supervisor at agreed checkpoints (meetings), and that review is recorded in this log and in the pull request. History is not rewritten. |
| 19 Oct 2026 | The literature search log for sources #1–#6 was removed from `literature-matrix.md` in commit `0151e06`. | Restore it from commit `ca0d2d5` and add a dated log for #7–#12 (DIP-17). |
