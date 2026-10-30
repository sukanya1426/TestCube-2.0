# Code coverage comparison

| Tool | Run | Tag | Actions | Methods hit | Total | Code cov. | Activities | Activity cov. | Feature cov. | Duration |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| TestCube | appmanager | APPMANAGER_SUPER_LOG | 223 | 15179 | 207143 | 7.33% | 3/39 | 7.69% | 0.00% (0/40) | 3516s |
| LLMDroid | appmanager | APPMANAGER_SUPER_LOG | 190 | 14079 | 207143 | 6.80% | 5/39 | 12.82%* | — | 1336s |

\* activity coverage taken from `utg.js` (screens the explorer reached), not from AndroLog `ACTIVITY=` probes — LLMDroid's AndroLog monitor tracks methods only. The two count slightly differently, so treat a mixed-source activity comparison as indicative rather than exact.

Both tools were given the same 3600s budget. Durations below include each tool's own shutdown, so they differ slightly.

> **Feature coverage scored for TestCube only.** The evaluator is trace-based and works on either tool; score the other with scripts/evaluate_features.py to get a comparable number.

**Code coverage — TestCube 7.33% vs LLMDroid 6.80%: +0.53 pp (+7.8% relative).**

**Activity coverage — TestCube 7.69% vs LLMDroid 12.82% (-5.13 pp), but measured differently on each side (androlog, utg); compare like-for-like before quoting this.**

**Saturation** — TestCube reached 99% of its final coverage 100% of the way through (23/23 samples); LLMDroid reached 99% of its final coverage 58% of the way through (111/192 samples). A run that flattened early was not truncated by its budget.

