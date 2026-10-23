# Health Indicator Analysis System

Diploma project: **Development of a Machine Learning-Based System for Analyzing Patient Health Indicators**.  
A research prototype that analyses hourly ICU measurements, estimates the risk of sepsis about six hours before onset, and shows the clinician why a warning appears.

> **Research prototype — not a diagnosis.** The system uses public, de-identified data only. It is not a medical device and must not be used for clinical decisions.

## Problem

ICU patients are monitored through dozens of vital signs and laboratory values, recorded at different times and often missing. Sepsis can develop within hours, and its early signs are easy to miss. Published machine-learning models are hard to compare, often perform worse at a new hospital and can produce many false alerts; deployed tools are mostly proprietary. This project builds an **open, tested system** that turns ICU time-series data into a transparent early-warning result, evaluates it honestly against simple baselines and on a second hospital system, and explains each warning. Details: [proposal](docs/01-proposal.md).

## How it would work in a hospital

In a Kazakh ICU the system would read the hourly measurements from the hospital information system, compute each patient's risk once an hour and show it at the nurse station. When the risk crosses the threshold, the nurse sees an alert with the reasons and one fixed prompt — re-check the measurements and inform the responsible physician — and records the outcome; the physician then acts under the national sepsis protocol. In this diploma the hospital system is replaced by a replay of the public PhysioNet data through the same data-source interface, so the rest of the system is built and tested as it would run. Details: [target system](docs/07-architecture/target-system.md).

## Target users

| User | Need |
|---|---|
| ICU nurse or physician (primary; supported by the first user evidence, checking continues) | See which patients need attention first, how their measurements changed and why the risk is high, without too many alerts |
| Clinical-informatics researcher or ML engineer (secondary) | A reproducible pipeline, fair baselines, honest metrics and an external test |

## Expected outcomes

1. Leakage-safe preprocessing pipeline for clinical time series.
2. Early-sepsis model (LightGBM) with two baselines: partial SIRS rule and logistic regression.
3. Evaluation report: internal test and external test on a second hospital system, with confidence intervals and alert metrics.
4. REST API for inference (FastAPI, OpenAPI).
5. Dashboard with patient list, patient trends and risk, explanations and model comparison (Streamlit).
6. Automated tests and full reproduction instructions.

## Team

| Person | Role |
|---|---|
| Aman Baku (Баку Аман Сағынғалиұлы), SE-2422 — GitHub [@MarioAman07](https://github.com/MarioAman07) | Individual project: analysis, design, implementation, testing, documentation |
| Altynbek Seitenov (Сейтенов Алтынбек Серикович) | Supervisor |

## Scope

**In scope:** ingestion and validation of the PhysioNet/CinC Challenge 2019 data; temporal preprocessing; model training and baseline comparison; alert logic and explanations; REST API; dashboard; automated tests; evaluation report.  
**Out of scope:** diagnosis or treatment advice; use on real patients; a working connection to a hospital information system (designed as a replaceable data source, not built); clinical validation.

## Current status — pre-defense 1 (24 Oct 2026)

Analysis, design and planning are done; implementation starts after pre-defense 1. The clickable prototype and the data-analysis script already run.

| # | Component | Document | Status |
|---|---|---|---|
| 1 | Project proposal and scope | [docs/01-proposal.md](docs/01-proposal.md), [research justification](docs/01-research-justification.md), [ADR-001](docs/decisions/ADR-001-scope.md) | Revised; research justification discussed with the supervisor on 23 Oct |
| 2 | Evidence of relevance | [docs/02-evidence/](docs/02-evidence/) | 2 discussions so far (survey + follow-up), published as [transcripts](docs/02-evidence/transcripts.md); data analysis of 40,336 ICU stays done (DIP-9) |
| 3 | Literature review | [docs/03-literature/literature-matrix.md](docs/03-literature/literature-matrix.md) | 12 peer-reviewed sources, critical synthesis |
| 4 | Existing system comparison | [docs/04-existing-systems/system-comparison.md](docs/04-existing-systems/system-comparison.md), [how they are built](docs/04-existing-systems/system-architectures.md) | 5 systems × 9 criteria; architectures of 4 systems reconstructed from publications |
| 5 | Technology comparison | [docs/05-technology/technology-comparison.md](docs/05-technology/technology-comparison.md), [ML methodology](docs/05-technology/ml-methodology.md) | 6 decisions linked to requirements |
| 6 | Requirements | [docs/06-requirements.md](docs/06-requirements.md) | 19 functional (10 Must, 7 Should, 2 Could) + 2 Won't, 10 non-functional, with acceptance criteria |
| 7 | Architecture and diagrams | [docs/07-architecture/architecture.md](docs/07-architecture/architecture.md), [target system](docs/07-architecture/target-system.md), [diagrams/](diagrams/) | Context, use case, component, ICU workflow, alert sequence, deployment and data-model diagrams (PlantUML + PNG) |
| 8 | UX / prototype | [docs/08-prototype/](docs/08-prototype/) | Clickable prototype on synthetic data with alert acknowledgement; API examples |
| 9 | Verification and evaluation plan | [docs/09-verification.md](docs/09-verification.md) | Requirement → test traceability, metrics, baselines |
| 10 | Project management and risks | [docs/10-management/](docs/10-management/) | Milestones, 14 risks, dependencies |
| 11 | Supervisor feedback | [docs/11-feedback-log.md](docs/11-feedback-log.md) | Feedback of 19, 21 and 23 Oct recorded with decisions |

## Technologies

Python 3.10–3.12 · pandas, NumPy · scikit-learn, LightGBM, SHAP · FastAPI, Pydantic · SQLite via SQLAlchemy · Streamlit, Plotly · pytest · PlantUML for diagrams. Reasons: [technology comparison](docs/05-technology/technology-comparison.md).

## Links

- YouTrack: [DIP issues](https://amanbaku-diploma.youtrack.cloud/issues?q=project:%20DIP) · [agile board](https://amanbaku-diploma.youtrack.cloud/agiles/204-1/218-1)
- Documentation: [docs/](docs/)
- Dataset: [PhysioNet/CinC Challenge 2019, v1.0.0](https://physionet.org/content/challenge-2019/1.0.0/) (CC BY 4.0, DOI 10.13026/v64v-d857)

## Getting started

Requirements: Python 3.10–3.12 (the pinned NumPy and SHAP versions do not install on 3.13+) and Git. On macOS, LightGBM also needs OpenMP: `brew install libomp`.

```bash
git clone https://github.com/MarioAman07/health-indicator-analysis-system.git
cd health-indicator-analysis-system
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

### Run the prototype (synthetic data, no download needed)

```bash
streamlit run src/frontend/prototype_app.py
```

### Run the data analysis

1. Download the training data as described in [data/README.md](data/README.md) into `data/raw/`.
2. Run:

```bash
make eda        # or: python -m src.ml.eda --data-dir data/raw --out-dir docs/02-evidence
```

Results: `docs/02-evidence/eda-summary.json` and figures in `docs/02-evidence/figures/`.

### Run the tests

```bash
make test       # or: python -m pytest
```

Training (`make train`), evaluation (`make evaluate`), the API and the connected dashboard are planned for the next milestones ([milestones](docs/10-management/milestones.md)).

## Repository structure

```
config/              configuration files (seed, features, threshold)
data/                local data only; raw/ and processed/ are ignored by Git
diagrams/src/        PlantUML sources;  diagrams/export/  PNG exports
docs/                proposal, evidence, literature, comparisons, requirements,
                     architecture, prototype, verification, management, feedback
evaluation/          evaluation scripts and summary results
src/ml/              core package: validation, features, models, evaluation
src/backend/         FastAPI application (planned)
src/frontend/        Streamlit prototype and dashboard
tests/               automated tests
```

## How work is tracked

Every task is a YouTrack issue `DIP-<n>`; each task has its own branch `DIP-<n>-<name>` and a pull request into `main`; commits start with `DIP-<n>:`. Details: [project management](docs/10-management/README.md).

## Data and licence notes

The PhysioNet/CinC Challenge 2019 data are used under CC BY 4.0 and are never committed to this repository. User-discussion transcripts are published with the respondents' agreement; they contain no names, contacts or patient data.
