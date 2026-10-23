# Project Management

**Status:** initial version (DIP-16), dependencies updated after the supervisor meeting of 23 Oct 2026  
**Last updated:** 23 Oct 2026

| | |
|---|---|
| YouTrack project | [DIP — issues](https://amanbaku-diploma.youtrack.cloud/issues?q=project:%20DIP) · [agile board](https://amanbaku-diploma.youtrack.cloud/agiles/204-1/218-1) |
| Repository | https://github.com/MarioAman07/health-indicator-analysis-system |
| Milestones | [milestones.md](milestones.md) |
| Risks | [risks.md](risks.md) |
| Supervisor feedback | [../11-feedback-log.md](../11-feedback-log.md) |

## 1. Responsibilities

The project is individual.

| Person | Role | Responsibilities |
|---|---|---|
| Aman Baku | Student, sole developer | Analysis, literature, requirements, architecture, implementation, testing, documentation, YouTrack planning; author of every commit and pull request |
| Altynbek Seitenov | Supervisor | Reviews key deliverables and decisions at agreed checkpoints (meetings, email); his feedback and my decisions are recorded in the feedback log |

## 2. How work is tracked

1. Every meaningful work item is a YouTrack task with assignee, priority, due date, expected outcome and acceptance criteria.
2. Board columns: Backlog → To do → In progress → Review → Done.
3. Each task gets its own branch from `main`, named `DIP-<n>-<short-name>`; commits start with `DIP-<n>:`.
4. Changes reach `main` only through a pull request that names the task, explains the change and says how it was checked (`main` is protected).
5. After merge, the task gets a comment with the pull-request link; it moves to Done only when its acceptance criteria are met.
6. Each pre-defense submission is tagged (`pre-defense-1`, `pre-defense-2`, `final-pre-defense`); tags are never moved.

## 3. Dependencies between work items

| Work item | Depends on | Why |
|---|---|---|
| Final requirements (DIP-12) | Supervisor confirmation of the direction (Q-01); user evidence (DIP-4, DIP-8) | Requirements change if the focus or the user needs change |
| ML methodology details (DIP-10) | Data analysis (DIP-9) | Variable selection, data-quality limit and class balance come from the data |
| Data analysis (DIP-9) | Dataset downloaded into `data/raw` | — |
| Architecture (DIP-13) | Requirements (DIP-12) | Components implement requirements |
| Prototype (DIP-14) | Architecture, requirements | Screens and API follow the use cases |
| Verification plan (DIP-15) | Requirements, ML methodology | Every Must requirement needs a test; metrics come from the methodology |
| Evidence synthesis (DIP-8) | User discussions (DIP-4) | — |
| Report (DIP-21) | All components 1–11 | — |
| Target system and ICU workflow (DIP-27) | Transcripts (DIP-26); national ICU standard and sepsis protocol | The workflow and the alert path are built on what the respondents and the regulations describe |
| Prototype update (DIP-30) | Requirements changed in DIP-27 | The screens show the adopted changes and the acknowledgement |
| Report v2 (DIP-29) | DIP-26, DIP-27, DIP-28, DIP-30 | The report summarises these documents |
| Implementation phases | Approved pre-defense 1 materials | The design must be agreed before coding starts |
