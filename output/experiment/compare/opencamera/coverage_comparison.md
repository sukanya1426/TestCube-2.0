# Code coverage comparison

| Tool | Run | Tag | Actions | Methods hit | Total | Code cov. | Activities | Activity cov. | Feature cov. | Duration |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| TestCube | opencamera | OPENCAMERA_SUPER_LOG | 194 | 2888 | 36079 | 8.00% | 1/3 | 33.33% | 0.00% (0/55) | 2227s |
| LLMDroid | opencamera | OPENCAMERA_SUPER_LOG | 450 | 3029 | 36079 | 8.40% | 1/3 | 33.33%* | — | 2296s |

\* activity coverage taken from `utg.js` (screens the explorer reached), not from AndroLog `ACTIVITY=` probes — LLMDroid's AndroLog monitor tracks methods only. The two count slightly differently, so treat a mixed-source activity comparison as indicative rather than exact.

Both tools were given the same 3600s budget. Durations below include each tool's own shutdown, so they differ slightly.

> **Feature coverage scored for TestCube only.** The evaluator is trace-based and works on either tool; score the other with scripts/evaluate_features.py to get a comparable number.

**Code coverage — TestCube 8.00% vs LLMDroid 8.40%: -0.39 pp (-4.7% relative).**

**Activity coverage — TestCube 33.33% vs LLMDroid 33.33% (-0.00 pp), but measured differently on each side (androlog, utg); compare like-for-like before quoting this.**

**Saturation** — TestCube reached 99% of its final coverage 45% of the way through (9/20 samples); LLMDroid reached 99% of its final coverage 64% of the way through (290/452 samples). A run that flattened early was not truncated by its budget.

