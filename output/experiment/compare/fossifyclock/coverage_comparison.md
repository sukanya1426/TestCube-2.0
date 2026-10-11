# Code coverage comparison

| Tool | Run | Tag | Actions | Methods hit | Total | Code cov. | Activities | Activity cov. | Feature cov. | Duration |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| TestCube | fossifyclock | FOSSIFYCLOCK_SUPER_LOG | 143 | 3926 | 27793 | 14.13% | 3/16 | 18.75% | 15.38% (4/26) | 1679s |
| LLMDroid | fossifyclock | FOSSIFYCLOCK_SUPER_LOG | 729 | 8210 | 27793 | 29.54% | 6/16 | 37.50%* | — | 3566s |

\* activity coverage taken from `utg.js` (screens the explorer reached), not from AndroLog `ACTIVITY=` probes — LLMDroid's AndroLog monitor tracks methods only. The two count slightly differently, so treat a mixed-source activity comparison as indicative rather than exact.

Both tools were given the same 3600s budget. Durations below include each tool's own shutdown, so they differ slightly.

> **Feature coverage scored for TestCube only.** The evaluator is trace-based and works on either tool; score the other with scripts/evaluate_features.py to get a comparable number.

**Code coverage — TestCube 14.13% vs LLMDroid 29.54%: -15.41 pp (-52.2% relative).**

**Activity coverage — TestCube 18.75% vs LLMDroid 37.50% (-18.75 pp), but measured differently on each side (androlog, utg); compare like-for-like before quoting this.**

**Saturation** — TestCube reached 99% of its final coverage 87% of the way through (13/15 samples); LLMDroid reached 99% of its final coverage 55% of the way through (402/731 samples). A run that flattened early was not truncated by its budget.

