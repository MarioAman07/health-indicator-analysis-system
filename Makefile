# Common commands. Run from the repository root.
PYTHON ?= python3
DATA_DIR ?= data/raw

.PHONY: install eda test

install:  ## Install pinned dependencies
	$(PYTHON) -m pip install -r requirements.txt

eda:  ## Exploratory data analysis -> docs/02-evidence
	$(PYTHON) -m src.ml.eda --data-dir $(DATA_DIR) --out-dir docs/02-evidence

test:  ## Run automated tests
	$(PYTHON) -m pytest
