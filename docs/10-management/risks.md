# Risk Register

**Status:** initial version (DIP-16)  
**Last updated:** 22 Oct 2026  
Owner of every risk: Aman Baku. Probability and impact: Low / Medium / High. Reviewed at every milestone.

| ID | Risk | Probability | Impact | Trigger | Mitigation | Status |
|---|---|---|---|---|---|---|
| R-01 | Fewer than 3 user discussions before pre-defense 1 | High | High | Fewer than 2 completed by 22 Oct | Anonymous survey plus follow-up questions; data analysis as additional evidence; ask the supervisor for contacts and whether the survey is accepted (Q-03) | Open |
| R-02 | The supervisor does not accept early sepsis prediction as the concrete focus | Low | High | Negative answer to Q-01 | Fall back to Option A in ADR-001; the validation, feature, API and dashboard design stay reusable | Open |
| R-03 | Temporal leakage makes results look better than they are | Medium | High | Unusually high internal results; UT-02 fails | Patient-level split, forward fill only, preprocessing fitted on training data, dedicated leakage test (UT-02) | Open |
| R-04 | The main model does not beat logistic regression | Medium | Medium | Primary success criterion not met | Report the result honestly; the engineering contribution and the comparison remain valid | Open |
| R-05 | Large performance drop on the external test (set B) | High | Medium | External AUROC/AUPRC far below internal | Report the drop as a finding; discuss recalibration; make no claims beyond the evaluated data | Open |
| R-06 | Scope grows beyond what one student can finish | Medium | High | Could items started before all Must items are done | MoSCoW priorities; GRU and utility score only after M2; no deployment work | Open |
| R-07 | Time conflicts with other courses, exams and competitions | High | Medium | Two weeks in a row without merged work | Weekly planning in YouTrack; small pull requests; milestone dates with buffers | Open |
| R-08 | Laptop memory or speed is not enough for training | Low | Medium | Out-of-memory errors or training longer than one hour | float32 data, cached preprocessed data, LightGBM's memory-efficient training, sampling for tuning | Open |
| R-09 | I cannot explain or defend my own decisions | Medium | High | Hesitation on supervisor questions | Decisions recorded with reasons (ADRs, methodology); one-page summary of my reasoning; practice explaining the decisions before each pre-defense | Open |
| R-10 | Patient data or secrets committed to the public repository | Low | High | `git ls-files` finds `.psv`, `.zip` or `.env` | `.gitignore` rules; inspection IN-N02 before every submission | Open |
| R-11 | Wrong or unsupported claims in the literature review or system comparison | Medium | Medium | A claim cannot be found in the cited full text | Verify against full texts; remove press sources as evidence (DIP-17, DIP-18) | Open |
| R-12 | The dataset becomes unavailable or changes | Low | High | Download fails or a new version appears | Keep a local copy of version 1.0.0; cite the DOI and version | Open |
