# Data

This folder holds local data only. Its `raw/` and `processed/` subfolders are ignored by Git:
patient data must never be committed to this repository, even though the dataset is public and de-identified.

## Dataset

**Early Prediction of Sepsis from Clinical Data: the PhysioNet/Computing in Cardiology Challenge 2019**, version 1.0.0  
Page: https://physionet.org/content/challenge-2019/1.0.0/  
DOI: 10.13026/v64v-d857

## How to get it

1. Download the training data (sets A and B) from the dataset page above. Downloading the files one by one from the page is slow; the same files are available with the AWS command-line tool, without an account:

```
python3 -m pip install awscli
python3 -m awscli s3 sync --no-sign-request s3://physionet-open/challenge-2019/1.0.0/training/ data/raw/
```

2. The folders must look like this:

```
data/raw/training_setA/p000001.psv
data/raw/training_setA/...
data/raw/training_setB/p100001.psv
data/raw/training_setB/...
```

3. Check the counts: 20,336 files in `training_setA` and 20,000 in `training_setB` (set B files are named `p100001.psv` … `p120000.psv`).
4. Check that Git does not see the files: `git status` must not list anything under `data/raw/`.

Each `.psv` file is one ICU stay: one row per hour, pipe-separated columns, `SepsisLabel` in the last column.

## Licence and use

Use the data under the terms stated on the PhysioNet page. The data are used only for research and
demonstration in this diploma project.
