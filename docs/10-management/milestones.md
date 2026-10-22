# Milestones

**Status:** initial version (DIP-16)  
**Last updated:** 21 Oct 2026

Dates after pre-defense 1 are my proposal. They will be aligned with the official dates of pre-defense 2, the final pre-defense and the defense once these are announced.

| ID | Milestone | Target date | Deliverables | Done when |
|---|---|---|---|---|
| M0 | Pre-defense 1 | 24 Oct 2026 | Proposal, evidence, literature, system and technology comparisons, requirements, architecture and diagrams, prototype, verification plan, project plan, feedback log; tag `pre-defense-1` | All 11 components in `main`; form submitted |
| M1 | Data pipeline and baselines | 20 Nov 2026 *(proposed)* | Validation, feature builder with leakage test, data split files, partial SIRS and logistic regression, first evaluation run | UT-01, UT-02, UT-05 and AT-03 pass |
| M2 | Main model and evaluation | 18 Dec 2026 *(proposed)* | LightGBM, threshold and alert logic, internal and external evaluation with confidence intervals, model card | AT-04 and AT-N01 pass; evaluation report in the repository |
| M3 | API and dashboard | 26 Feb 2027 *(proposed)* | FastAPI endpoints, SQLite storage, Streamlit dashboard connected to the API | AT-06 – AT-14 pass; user check on the real dashboard done |
| M4 | Testing and documentation | 26 Mar 2027 *(proposed)* | Coverage target, clean-setup demonstration, final README, diploma text draft | All Must acceptance tests pass; IN-N04, DM-N05 done |
| PD2 | Pre-defense 2 | *to be announced* | Working pipeline and evaluation results (M1–M2) | Tag `pre-defense-2` |
| FPD | Final pre-defense | *to be announced* | Complete system and documentation (M3–M4) | Tag `final-pre-defense` |

## Work until pre-defense 1

| Date | Work |
|---|---|
| 19 Oct 2026 | Supervisor feedback received; repository review; plan |
| 21 Oct 2026 | Repository hygiene, feedback log, ML methodology, proposal and ADR-001, requirements, architecture, prototype, verification plan, project plan; user survey started |
| 22 Oct 2026 | Data analysis, evidence synthesis, literature and comparison fixes, README, report v1 to the supervisor |
| 23 Oct 2026 | Meeting with the supervisor; changes from the meeting |
| 24 Oct 2026 | Final report, YouTrack screenshots, tag `pre-defense-1`, form submission |
