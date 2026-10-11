# Code coverage comparison

| Tool | Run | Tag | Actions | Methods hit | Total | Code cov. | Activities | Activity cov. | Feature cov. | Duration |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| TestCube | nononsensenotes | NONONSENSENO_SUPER_LOG | 139 | 0 | 15514 | 0.00% | 0/8 | 0.00% | 0.00% (0/34) | 1632s |
| LLMDroid | nononsensenotes | NONONSENSENO_SUPER_LOG | 675 | 2602 | 15514 | 16.77% | 1/8 | 12.50%* | — | 3600s |

\* activity coverage taken from `utg.js` (screens the explorer reached), not from AndroLog `ACTIVITY=` probes — LLMDroid's AndroLog monitor tracks methods only. The two count slightly differently, so treat a mixed-source activity comparison as indicative rather than exact.

Both tools were given the same 3600s budget. Durations below include each tool's own shutdown, so they differ slightly.

> **Feature coverage scored for TestCube only.** The evaluator is trace-based and works on either tool; score the other with scripts/evaluate_features.py to get a comparable number.

**Code coverage — TestCube 0.00% vs LLMDroid 16.77%: -16.77 pp (-100.0% relative).**

**Activity coverage — TestCube 0.00% vs LLMDroid 12.50% (-12.50 pp), but measured differently on each side (androlog, utg); compare like-for-like before quoting this.**

**Saturation** — LLMDroid reached 99% of its final coverage 93% of the way through (627/675 samples). A run that flattened early was not truncated by its budget.

