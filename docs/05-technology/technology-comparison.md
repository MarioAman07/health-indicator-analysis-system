# Technology Comparison

**Status:** DRAFT. The choices below are proposals. Not yet reviewed by my supervisor [REQUIRES SUPERVISOR APPROVAL].
**Last updated:** 13 Oct 2026

## 1. How I did this

I compared technologies for five decisions. Each has three alternatives and the same eight criteria, chosen because they matter for a one-person Software Engineering project: development complexity, ML integration, performance, maintainability, testing, documentation, deployment, and suitability for an individual student.

Two kinds of statements appear in the tables:

- **Facts from documentation or literature**, with a source. A fact that I have not opened in the official docs is marked [MUST VERIFY].
- **My judgment** about how well an option fits my project (marked "my judgment"). These are planning opinions, not measurements. I used the words "good", "medium" and "weak".

The requirements file (`docs/06-requirements.md`) is written after this one. I will link each decision to requirement IDs once they exist.

I am not choosing by popularity. Where an option is popular but does not fit my project, I say so.

## 2. Decision 1: Backend and API framework

All three alternatives are Python frameworks. I did not consider Java or JavaScript backends, because the machine-learning code is Python, and a second language would force a separate model-serving service. That adds a component with no benefit for a project this size.

| Criterion | FastAPI | Flask | Django with Django REST Framework |
|---|---|---|---|
| Development complexity | Low to medium. Fact: a small app is a few lines, and request models are declared with Python type hints [MUST VERIFY on docs] | Low. Minimal core, I add validation and docs myself (my judgment) | Higher. A full framework with many conventions (my judgment) |
| ML integration | Good. Same Python process can load a model file (my judgment) | Good (my judgment) | Good, but more machinery around a model service (my judgment) |
| Performance | Described by its project as high-performance, built on Starlette and Pydantic [README, vendor claim]. For my load this is not decisive | Adequate for a prototype (my judgment) | Adequate for a prototype (my judgment) |
| Maintainability | Good. Typed request and response models act as a contract (my judgment) | Medium. Structure is left to me (my judgment) | Good structure, heavier than I need (my judgment) |
| Testing | Fact: provides a TestClient for pytest [README] | Has a test client [MUST VERIFY] | Has a built-in test framework [MUST VERIFY] |
| Documentation | Fact: generates interactive OpenAPI documentation (Swagger UI and ReDoc) automatically [README] | Needs extensions (my judgment) [MUST VERIFY] | DRF has schema and docs options [MUST VERIFY] |
| Deployment | Runs on an ASGI server such as Uvicorn [MUST VERIFY] | Runs on common WSGI servers [MUST VERIFY] | Runs on common servers [MUST VERIFY] |
| Fit for an individual student | Good: small, one clear way to validate input (my judgment) | Good, but more design decisions on my own (my judgment) | Weaker: more to learn than the project needs (my judgment) |

Official documentation (not opened by me): https://fastapi.tiangolo.com, https://flask.palletsprojects.com, https://docs.djangoproject.com, https://www.django-rest-framework.org. The FastAPI facts above come from its project README, which I saw through repository copies.

**Selected: FastAPI.** My project needs strict input validation (clinical measurements with ranges and types), a documented API that I can show in the package, and easy API tests. FastAPI covers all three with little code. The cost is that I must be careful with async code; I will use plain synchronous endpoints unless there is a reason not to.

Component interaction: the dashboard will talk to the API over HTTP with JSON, described by OpenAPI. I considered gRPC and a message queue and rejected both. A single backend with one client does not need them, and they would add complexity without helping any requirement.

## 3. Decision 2: Data storage

Raw dataset files stay on disk and are never committed. This decision is about the application database that holds demo patient data, stored predictions and model metadata.

| Criterion | SQLite | PostgreSQL | Files only (CSV / Parquet) |
|---|---|---|---|
| Development complexity | Low. No server to run [MUST VERIFY on sqlite.org] | Medium. Needs a database server and configuration | Low to start, but I must write my own query and update logic (my judgment) |
| ML integration | Fine through a Python library or an ORM (my judgment) | Fine (my judgment) | Very direct for training data (my judgment) |
| Performance | Enough for one user and demo-size data (my judgment, [MUST VERIFY] limits) | Better for many users and heavy queries (my judgment) | Fast for whole-file reads, weak for lookups of one patient (my judgment) |
| Maintainability | Good with a schema and migrations (my judgment) | Good, mature tooling (my judgment) | Weak: no schema enforcement, hard to keep predictions and audit data consistent (my judgment) |
| Testing | Easy. In-memory or temporary file databases (my judgment) | Needs a test instance or container (my judgment) | Easy for small fixtures (my judgment) |
| Documentation | Good [MUST VERIFY] | Good [MUST VERIFY] | Format docs only |
| Deployment | Single file, nothing to install (my judgment) | Container or server needed | Nothing to deploy |
| Fit for an individual student | Good | Medium: more setup | Good for the ML pipeline only |

Official documentation (not opened by me): https://www.sqlite.org, https://www.postgresql.org/docs/.

**Selected: SQLite, accessed through an ORM layer such as SQLAlchemy [MUST VERIFY compatibility], with the training data kept as files.** Why: I need a small store for patients, predictions and model versions, which supports the auditable requirement (every prediction can be traced to a model version). A single file keeps setup, tests and reproduction simple for one person. If I ever needed many users, switching to PostgreSQL would be a configuration change instead of a rewrite. I am not choosing PostgreSQL now, even though it is more common in production, because I would pay setup cost for concurrency my prototype does not need.

## 4. Decision 3: Machine-learning approach

| Criterion | Regularized logistic regression | Gradient-boosted trees (e.g. XGBoost or LightGBM) | Recurrent or temporal neural network (e.g. GRU, LSTM) |
|---|---|---|---|
| Development complexity | Low | Medium | High: sequence handling, padding, tuning (my judgment) |
| Handling missing values | Needs imputation (my judgment) | Fact: XGBoost can handle missing values natively [MUST VERIFY on docs] | Needs imputation or masking (my judgment) |
| Use of time information | Only through features I build (window summaries, changes) | Same, through features I build (my judgment) | Uses sequences directly (my judgment) |
| Explainability | Coefficients are readable | Feature importance, and SHAP was used in Lashen et al. 2023 [S: literature matrix #3] | Harder (my judgment) |
| Evidence in the literature I reviewed | Weak against NEWS in one study: AUROC 0.654 vs 0.682 (Lashen 2023) | XGBoost AUROC 0.778 vs neural network 0.756 and NEWS 0.682 (Lashen 2023). Decision trees and neural networks performed best in a network meta-analysis (Yadgarov 2024), with low certainty | Reported in many sepsis studies (Moor 2021 lists LSTM, GRU, CNN and temporal convolutional networks) |
| Training cost and reproducibility | Very cheap, easy to reproduce | Cheap on a laptop, reproducible with fixed seeds (my judgment) | More expensive, harder to reproduce exactly (my judgment) |
| Testing | Easy | Easy | Harder: more moving parts (my judgment) |
| Fit for an individual student | Good as a baseline | Good as the main model | Risky as the only model (my judgment) |

Official documentation (not opened by me): https://scikit-learn.org, https://xgboost.readthedocs.io, https://shap.readthedocs.io.

**Selected: gradient-boosted trees on time-window features as the main model, with logistic regression as the required simple baseline.** The evidence is mixed and these studies are not directly comparable, so I am not choosing on a leaderboard number. I choose boosted trees because they handle missing values and tabular window features, are explainable, are cheap to train and reproduce, and fit a one-person project. A recurrent network stays an optional extension only if time remains. A NEWS-style score may be a second reference, but only if it can be built fairly from the dataset (see the proposal).

All of this depends on the dataset and the supervisor's decisions (horizon, baseline) [REQUIRES SUPERVISOR APPROVAL].

## 5. Decision 4: Dashboard (frontend)

| Criterion | Streamlit | React with a charting library | Server-rendered templates (Jinja2 with Plotly) |
|---|---|---|---|
| Development complexity | Low. Python only (my judgment) | High: a second language, a build tool and state handling (my judgment) | Medium (my judgment) |
| Integration with the API | Calls the FastAPI endpoints over HTTP | Calls the same endpoints | Rendered by the backend itself, which blurs the API boundary |
| Time-series charts | Supported through charting libraries [MUST VERIFY] | Very flexible | Supported through Plotly [MUST VERIFY] |
| Maintainability | Good for a small app, limited for custom layouts (my judgment) | Good, with more code to maintain | Medium |
| Testing | Test the API; UI tests are limited (my judgment) | Mature UI testing tools exist (my judgment) | Backend tests cover most of it |
| Deployment | One more Python process | Static build, or a dev server | Same process as the backend |
| Fit for an individual student | Good | Depends on my JavaScript experience: [REQUIRES USER INPUT] | Medium |

Official documentation (not opened by me): https://docs.streamlit.io, https://react.dev, https://plotly.com/python/.

**Selected: Streamlit, calling the FastAPI backend over HTTP.** My scope says "minimal dashboard". I want the dashboard to be a client of the public API, so the layers stay separate (UI, API, model). That also means the main logic can be tested without the UI. React would give more control, but costs time I would rather spend on pipeline, evaluation and tests. If I turn out to be comfortable with JavaScript, I can swap the frontend without touching the backend.

## 6. Decision 5: Packaging and deployment

| Criterion | Docker Compose (API, dashboard) | Python virtual environment with a Makefile | Cloud platform service |
|---|---|---|---|
| Development complexity | Medium. Needs Docker installed and a few config files | Low | Medium to high: accounts, configuration, costs |
| Reproducibility | Good: same environment for everyone (my judgment) | Medium: depends on the local Python and system libraries (my judgment) | Good, but ties results to a provider |
| Testing | Can run tests in a container | Easy | Harder to reproduce locally |
| Documentation | One command to run, easy to explain | Short instructions | Provider specific |
| Fit for an individual student | Good | Good | Weak: not needed for a prototype without real users |

Official documentation (not opened by me): https://docs.docker.com/compose/.

**Selected: a pinned Python environment with a Makefile as the main way to run and test, and a Docker Compose file as the one-command option.** Reproducibility is one of my stated goals, and a container is the simplest way to show it. The virtual environment stays documented because Docker may not be available on every machine. I am not using a cloud service, because the prototype has no real users and no need to be online.

## 7. Summary of proposed choices

| Decision | Selected | Main reason |
|---|---|---|
| Backend and API | FastAPI | Typed validation, automatic API documentation and easy tests |
| Data storage | SQLite (through an ORM) | Simple setup, easy tests, traceable predictions |
| ML approach | Gradient-boosted trees, logistic regression baseline | Missing values, explainability, cheap and reproducible |
| Dashboard | Streamlit as an API client | Fast to build and keeps the layers separate |
| Packaging | Pinned environment with Makefile, plus Docker Compose | Reproducibility for one person |

## 8. Still to check

| Item | Status |
|---|---|
| Open the official documentation for every [MUST VERIFY] fact above | [MUST VERIFY] |
| SQLAlchemy compatibility with SQLite for my schema | [MUST VERIFY] |
| My comfort with JavaScript (affects the dashboard decision) | [REQUIRES USER INPUT] |
| Whether the supervisor accepts these choices | [REQUIRES SUPERVISOR APPROVAL] |