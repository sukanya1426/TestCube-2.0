# Code coverage comparison

| Tool | Run | Tag | Actions | Methods hit | Total | Code cov. | Activities | Activity cov. | Feature cov. | Duration |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| TestCube | fossifycontacts | FOSSIFYCONTA_SUPER_LOG | 167 | 7266 | 62716 | 11.59% | 3/15 | 20.00% | 0.00% (0/38) | 1762s |
| LLMDroid | fossifycontacts | FOSSIFYCONTA_SUPER_LOG | 762 | 19859 | 62716 | 31.66% | 8/15 | 53.33%* | — | 3600s |

\* activity coverage taken from `utg.js` (screens the explorer reached), not from AndroLog `ACTIVITY=` probes — LLMDroid's AndroLog monitor tracks methods only. The two count slightly differently, so treat a mixed-source activity comparison as indicative rather than exact.

Both tools were given the same 3600s budget. Durations below include each tool's own shutdown, so they differ slightly.

> **Feature coverage scored for TestCube only.** The evaluator is trace-based and works on either tool; score the other with scripts/evaluate_features.py to get a comparable number.

**Code coverage — TestCube 11.59% vs LLMDroid 31.66%: -20.08 pp (-63.4% relative).**

**Activity coverage — TestCube 20.00% vs LLMDroid 53.33% (-33.33 pp), but measured differently on each side (androlog, utg); compare like-for-like before quoting this.**

**Saturation** — TestCube reached 99% of its final coverage 71% of the way through (12/17 samples); LLMDroid reached 99% of its final coverage 66% of the way through (503/762 samples). A run that flattened early was not truncated by its budget.

