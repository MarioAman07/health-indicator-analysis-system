# Technology Comparison

**Status:** DRAFT for supervisor review. The technology choices below are preliminary and may be revised after the requirements are finalized and supervisor feedback is received.  
**Last updated:** 13 Oct 2026

## 1. Comparison approach

Five key technical decisions were analyzed for the proposed system.

For each decision, three reasonable alternatives were compared using project-relevant criteria such as:

- development complexity;
- machine-learning integration;
- performance;
- maintainability;
- testing;
- documentation;
- deployment complexity;
- suitability for an individual Software Engineering diploma project.

The technologies are not selected based only on popularity. The main criterion is how well each option fits the requirements and scope of this project.

The current choices are preliminary and will later be linked to the corresponding requirement IDs.

---

## 2. Decision 1: Backend and API framework

The machine-learning pipeline will be implemented in Python. Therefore, using a Python backend avoids introducing an additional programming language or a separate model-serving component.

| Criterion | FastAPI | Flask | Django + Django REST Framework |
|---|---|---|---|
| Development complexity | Low to medium. Uses Python type hints and structured request models | Low. Minimal framework, but more project structure must be defined manually | Higher. Full framework with more conventions and built-in components |
| ML integration | Good. The ML model can be loaded and called directly from Python | Good. Same Python environment can be used | Good, although the framework adds more infrastructure than this prototype requires |
| Performance | Suitable for API-based applications and more than sufficient for the planned prototype | Sufficient for prototype-scale workloads | Sufficient for prototype-scale workloads |
| Maintainability | Good. Typed request and response models provide a clear API contract | Medium. More architectural decisions must be defined manually | Good structure, but heavier than required for this project |
| Testing | Provides API testing utilities and works well with pytest | Includes a testing client and supports pytest-based testing | Provides an established testing framework |
| Documentation | Automatic OpenAPI schema and interactive API documentation | API documentation usually requires additional configuration or extensions | API schemas and documentation can be provided through DRF tooling |
| Deployment | Supports ASGI deployment | Commonly deployed through WSGI servers | Supports both WSGI and ASGI deployment |
| Fit for this project | High | High | Medium |

### Selected option: FastAPI

FastAPI is currently the preferred backend framework.

The project requires:

- validation of structured clinical measurements;
- a clearly documented API;
- straightforward integration with Python ML code;
- convenient automated API testing.

FastAPI provides these capabilities while keeping the backend relatively small and understandable for an individual project.

The backend will initially use simple synchronous endpoints unless asynchronous processing becomes necessary.

### Component interaction

The dashboard will communicate with the backend through HTTP using JSON.

The API contract will be described through OpenAPI.

gRPC and message queues were considered but are not selected because the planned prototype has one backend and one client. Introducing additional communication infrastructure would increase complexity without solving a current requirement.

---

## 3. Decision 2: Data storage

The public clinical dataset used for model development will remain as dataset files and will not be committed to the repository.

The application database is intended only for prototype-related information such as:

- demonstration patient records;
- stored predictions;
- model metadata;
- model version information;
- evaluation or audit metadata where required.

| Criterion | SQLite | PostgreSQL | Files only (CSV / Parquet) |
|---|---|---|---|
| Development complexity | Low. Serverless database stored in a local file | Medium. Requires a running database service and configuration | Low initially, but application logic for updates and queries must be implemented manually |
| Python / ML integration | Good through Python libraries and ORM tools | Good through mature Python database libraries and ORM tools | Very direct for training and analytical datasets |
| Performance | Suitable for a single-user prototype and small application database | Better suited to concurrent users and larger production workloads | Efficient for analytical file reads but less convenient for application-level queries |
| Maintainability | Good when a defined schema and ORM are used | Good, with mature schema and migration tooling | Lower for application state because schema and relationships are not enforced centrally |
| Testing | Simple temporary databases can be created for tests | Usually requires a dedicated test database or container | Simple for analytical fixtures |
| Deployment | No separate database server required | Requires a database service | No database service required |
| Fit for this project | High | Medium | High for ML data, lower for application state |

### Selected option: SQLite with an ORM

SQLite is currently preferred for the application database.

The prototype does not require high concurrency or a production-scale database server. SQLite provides a simple and reproducible setup while still allowing structured storage of predictions, metadata, and model versions.

An ORM such as SQLAlchemy will reduce coupling between application logic and the database implementation.

If the project later requires PostgreSQL, using an ORM should simplify migration, although database-specific schema or query changes may still be necessary.

The ML training dataset itself will remain file-based.

---

## 4. Decision 3: Machine-learning approach

Three model families were considered.

| Criterion | Regularized Logistic Regression | Gradient-Boosted Trees | Recurrent / Temporal Neural Network |
|---|---|---|---|
| Development complexity | Low | Medium | High |
| Missing-data handling | Normally requires an explicit imputation strategy | Some implementations such as XGBoost can handle missing values directly | Usually requires imputation, masking, or another explicit missing-data strategy |
| Use of temporal information | Requires engineered temporal features such as changes and window summaries | Uses engineered temporal features | Can operate directly on ordered sequences |
| Explainability | Model coefficients are relatively easy to interpret | Feature importance and SHAP-style explanations can be used | Generally more difficult to interpret |
| Evidence from reviewed literature | Useful as a simple baseline, but did not outperform NEWS in one reviewed study | Strong results in several reviewed studies and suitable for tabular clinical data | Widely studied for sequential clinical prediction |
| Training cost | Low | Low to medium | Higher |
| Reproducibility | High | High when versions, seeds, and settings are controlled | More difficult because of greater training complexity |
| Testing complexity | Low | Low to medium | Higher |
| Fit for an individual project | High as baseline | High as main model | Medium / higher project risk |

### Selected approach

The proposed configuration is:

**Main model:** gradient-boosted trees  
**Baseline:** regularized logistic regression

The main model will use temporal features derived from measurements available up to each prediction time.

Gradient-boosted trees are preferred because they:

- work well with structured tabular data;
- can support missing-data handling;
- are relatively inexpensive to train;
- support feature-level interpretation;
- are practical to reproduce and test.

Logistic regression remains important as a transparent and reproducible baseline.

A recurrent neural model such as GRU or LSTM may be considered as an optional extension if time and project scope permit.

The final prediction horizon and baseline configuration will be discussed with the supervisor.

---

## 5. Decision 4: Dashboard / frontend

The prototype requires a minimal interface rather than a production hospital user interface.

| Criterion | Streamlit | React + charting library | Server-rendered templates |
|---|---|---|---|
| Development complexity | Low. Python-based | Higher. Requires JavaScript/TypeScript tooling and client-side state management | Medium |
| Backend integration | Can call FastAPI endpoints over HTTP | Can call the same REST API | Can be integrated directly with the backend |
| Time-series visualization | Supports built-in charts and external charting libraries | Highly flexible | Can use libraries such as Plotly |
| Maintainability | Good for a small research prototype | Strong for larger custom applications but requires more frontend code | Medium |
| Testing | Supports automated application testing; backend API remains independently testable | Mature frontend testing ecosystem | Much of the behaviour can be covered by backend tests |
| Deployment | Runs as a separate Python application | Requires frontend build/deployment | Can run with the backend |
| UI flexibility | Medium | High | Medium |
| Fit for this project | High | Medium | Medium |

### Selected option: Streamlit

Streamlit is currently preferred for the prototype dashboard.

The project scope requires a minimal interface that can show:

- patient measurements over time;
- risk results;
- warning states;
- model and context information.

Using Streamlit allows more project time to be spent on the data pipeline, temporal correctness, model evaluation, API design, and automated testing.

The dashboard will call the FastAPI backend rather than contain the main analytical logic itself.

This keeps the architecture separated into:

**UI → API → preprocessing / model inference**

and allows the backend to be tested independently.

---

## 6. Decision 5: Local execution and deployment approach

The project does not currently require public cloud deployment because it is a research prototype without real production users.

Three execution approaches were considered.

| Criterion | Docker Compose | Python virtual environment + Makefile | Cloud platform |
|---|---|---|---|
| Development complexity | Medium | Low | Medium to high |
| Reproducibility | High because services and dependencies can be defined explicitly | Good when dependency versions are pinned | High, but environment becomes provider-dependent |
| Testing | Tests can run inside containers | Straightforward local testing | Requires additional remote configuration |
| Setup | Requires Docker | Requires Python and dependency installation | Requires account, deployment configuration and possibly cost management |
| Demonstration | Convenient one-command startup can be provided | Simple for development | Accessible remotely |
| Fit for the current project | High | High | Low to medium |

### Selected approach

The main development workflow will use:

**Pinned Python environment + Makefile**

A **Docker Compose** configuration will also be provided as a reproducible one-command execution option.

This provides two useful paths:

1. simple local development through Python;
2. reproducible demonstration through containers.

A cloud deployment is not currently required because the diploma prototype is not intended for production use.

---

## 7. Summary of proposed technology choices

| Decision | Proposed choice | Main reason |
|---|---|---|
| Backend and API | FastAPI | Structured validation, automatic API documentation, Python ML integration, convenient testing |
| Data storage | SQLite through an ORM | Simple setup, reproducibility, sufficient for a single-user prototype |
| ML approach | Gradient-boosted trees + logistic regression baseline | Suitable for structured clinical data, explainability, reasonable complexity and reproducibility |
| Dashboard | Streamlit as an API client | Fast development of a minimal analytical interface while preserving layer separation |
| Execution / deployment | Pinned Python environment + Makefile, with Docker Compose | Simple development plus reproducible demonstration |

---

## 8. Open Decisions

The technology stack is currently a proposal rather than a final architectural decision.

The following points will be reviewed after the requirements are finalized and discussed with the supervisor:

- whether the proposed stack provides sufficient engineering complexity for the diploma;
- whether gradient-boosted trees are appropriate as the main model;
- whether logistic regression is sufficient as the primary baseline;
- whether an additional clinical baseline should be included;
- whether SQLite is sufficient for the final prototype or PostgreSQL is more appropriate;
- whether Streamlit provides enough UI functionality for the required prototype.

Any decisions changed after supervisor feedback will be recorded in the project documentation and Git history.