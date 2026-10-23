# Risk Register

**Status:** initial version (DIP-16), reviewed after the supervisor meeting of 23 Oct 2026  
**Last updated:** 23 Oct 2026  
Owner of every risk: Aman Baku. Probability and impact: Low / Medium / High. Reviewed at every milestone.

| ID | Risk | Probability | Impact | Trigger | Mitigation | Status |
|---|---|---|---|---|---|---|
| R-01 | Fewer than 3 user discussions before pre-defense 1 | High | High | Fewer than 2 completed by 22 Oct | Anonymous survey plus follow-up questions; data analysis as additional evidence; ask the supervisor for contacts and whether the survey is accepted (Q-03). 23 Oct: two respondents with follow-up answers, published as transcripts at the supervisor's request; further respondents are needed for the user check | Open |
| R-02 | The supervisor does not accept early sepsis prediction as the concrete focus | Low | High | Negative answer to Q-01 | Fall back to Option A in ADR-001; the validation, feature, API and dashboard design stay reusable. 23 Oct: the supervisor called the focus a good idea; the official topic decision is still expected after the pre-defense | Open (probability reduced) |
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
| R-13 | The workflow of the target system does not match real ICU practice in Kazakhstan | Medium | High | Respondents reject the alert path, the 30-minute limit or the re-alert margin | Workflow based on the national standard, the sepsis protocol and the transcripts; open values marked as first values; checked in the user check and the next discussions; silent mode first in the introduction plan | Open |
| R-14 | No access to a hospital information system for integration | High | Medium | No hospital contact or no test interface by M3 | The data-source interface keeps the system independent of the source; the diploma uses the replay adapter; the MIS adapter is designed but not claimed as built | Open |
