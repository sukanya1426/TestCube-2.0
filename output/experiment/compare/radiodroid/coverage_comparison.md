# Code coverage comparison

| Tool | Run | Tag | Actions | Methods hit | Total | Code cov. | Activities | Activity cov. | Feature cov. | Duration |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| TestCube | radiodroid | RADIODROID_SUPER_LOG | 154 | 12485 | 91188 | 13.69% | 1/1 | 100.00% | 0.00% (0/32) | 1618s |
| LLMDroid | radiodroid | RADIODROID_SUPER_LOG | 90 | 11438 | 91188 | 12.54% | 1/1 | 100.00%* | — | 589s |

\* activity coverage taken from `utg.js` (screens the explorer reached), not from AndroLog `ACTIVITY=` probes — LLMDroid's AndroLog monitor tracks methods only. The two count slightly differently, so treat a mixed-source activity comparison as indicative rather than exact.

Both tools were given the same 3600s budget. Durations below include each tool's own shutdown, so they differ slightly.

> **Feature coverage scored for TestCube only.** The evaluator is trace-based and works on either tool; score the other with scripts/evaluate_features.py to get a comparable number.

**Code coverage — TestCube 13.69% vs LLMDroid 12.54%: +1.15 pp (+9.2% relative).**

**Activity coverage — TestCube 100.00% vs LLMDroid 100.00% (+0.00 pp), but measured differently on each side (androlog, utg); compare like-for-like before quoting this.**

**Saturation** — TestCube reached 99% of its final coverage 100% of the way through (16/16 samples); LLMDroid reached 99% of its final coverage 63% of the way through (58/92 samples). A run that flattened early was not truncated by its budget.

