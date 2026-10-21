# ADR-001: Concrete project direction — early sepsis-risk prediction from ICU time series

**Status:** Proposed — on 21 Oct the supervisor asked for a research justification, which is prepared; confirmation expected at the meeting on 23 Oct (feedback log Q-01, FB-12)  
**Date:** 21 Oct 2026 (options first analysed on 10 Oct 2026, commit `0a757b5`)  
**Decision owner:** Aman Baku

## Context

The topic agreed with the supervisor, *Development of a Machine Learning-Based System for Analyzing Patient Health Indicators*, does not name a health problem, dataset or prediction target. A diploma project needs all three to define requirements, an evaluation and a realistic scope for one student. On 10 Oct I compared three possible directions.

## Options considered

| | A. Risk from structured indicators | B. Time-series early warning (sepsis) | C. ICU analysis on MIMIC-IV |
|---|---|---|---|
| Candidate data | NHANES (public); target not selected | PhysioNet/CinC Challenge 2019 (open, CC BY 4.0) | MIMIC-IV (credentialed access, training and data use agreement required) |
| Defined ML target | No — a condition still had to be chosen | Yes — `SepsisLabel`, defined by the data owners | No — task still to be chosen |
| Temporal data | Not required | Central | Available |
| Software-engineering depth | Mostly depends on what is built around one classifier | Ingestion, validation, missing-data handling, leakage-safe features, inference, alert logic, trend visualisation | High, but depends on the chosen task |
| Evaluation | Possible once a target is fixed | Objective, with a public label and two hospital systems for an external test | Possible, after access is granted |
| Schedule risk | Lower | Moderate | Higher: access is not immediate |

## Criteria

1. Legitimate data available now.
2. A clearly defined, objectively measurable prediction target.
3. Enough software-engineering work beyond a notebook.
4. Feasible for one student within the diploma schedule.
5. Support in the literature.
6. Privacy and medical-safety risk that can be managed.

## Decision

Choose **Option B**: a decision-support prototype that estimates early sepsis risk from hourly ICU measurements, built on the PhysioNet/CinC Challenge 2019 public data.

## Reasons

- It is the only option that meets criteria 1 and 2 at once: the data are open today and the label is already defined (Sepsis-3, 6 hours before onset).
- Time-series data force the engineering problems that make the project substantial: missing and irregular measurements, temporal leakage, alert thresholds and trend visualisation.
- The literature on this exact task is large and critical (#1, #2, #4, #8), so the evaluation can be designed around known weaknesses: AUROC-only reporting, poor transfer between hospitals, and alert burden.
- The two public hospital systems (sets A and B) allow an external test without restricted data.

The choice is based on project-design and engineering grounds. It is not a claim that sepsis is medically more important than other problems.

## Consequences and trade-offs

- The system becomes specific to one clinical problem instead of general "health analysis". The topic title stays as agreed with the supervisor (the official decision on the topic is expected after the pre-defense); the concrete focus is stated in the proposal.
- Time-series preprocessing is harder than a single tabular classifier. This is accepted as the main engineering challenge.
- The hidden Challenge test set (third hospital system) is not public, so results cannot be compared with the leaderboard.
- Option A remains the fallback if the supervisor considers B too specialised or too complex.
- Option C is not pursued because access would delay development without a demonstrated advantage for this diploma.

## Follow-up

- Confirm with the supervisor (Q-01 in the feedback log) and record the answer here.
- Relevance, research gap, research questions and hypotheses: [research justification](../01-research-justification.md).
- Methodological details: [ML methodology](../05-technology/ml-methodology.md).
