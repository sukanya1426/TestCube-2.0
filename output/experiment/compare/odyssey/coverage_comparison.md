# Code coverage comparison

| Tool | Run | Tag | Actions | Methods hit | Total | Code cov. | Activities | Activity cov. | Feature cov. | Duration |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| TestCube | odyssey | ODYSSEY_SUPER_LOG | 218 | 5646 | 55027 | 10.26% | 1/3 | 33.33% | 0.00% (0/33) | 2274s |
| LLMDroid | odyssey | ODYSSEY_SUPER_LOG | 766 | 6680 | 55027 | 12.14% | 1/3 | 33.33%* | — | 3599s |

\* activity coverage taken from `utg.js` (screens the explorer reached), not from AndroLog `ACTIVITY=` probes — LLMDroid's AndroLog monitor tracks methods only. The two count slightly differently, so treat a mixed-source activity comparison as indicative rather than exact.

Both tools were given the same 3600s budget. Durations below include each tool's own shutdown, so they differ slightly.

> **Feature coverage scored for TestCube only.** The evaluator is trace-based and works on either tool; score the other with scripts/evaluate_features.py to get a comparable number.

**Code coverage — TestCube 10.26% vs LLMDroid 12.14%: -1.88 pp (-15.5% relative).**

**Activity coverage — TestCube 33.33% vs LLMDroid 33.33% (-0.00 pp), but measured differently on each side (androlog, utg); compare like-for-like before quoting this.**

**Saturation** — TestCube reached 99% of its final coverage 82% of the way through (18/22 samples); LLMDroid reached 99% of its final coverage 34% of the way through (261/765 samples). A run that flattened early was not truncated by its budget.

