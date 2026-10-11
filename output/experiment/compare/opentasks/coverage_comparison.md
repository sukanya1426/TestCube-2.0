# Code coverage comparison

| Tool | Run | Tag | Actions | Methods hit | Total | Code cov. | Activities | Activity cov. | Feature cov. | Duration |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| TestCube | opentasks | OPENTASKS_SUPER_LOG | 160 | 3783 | 25768 | 14.68% | 3/8 | 37.50% | 0.00% (0/31) | 1770s |
| LLMDroid | opentasks | OPENTASKS_SUPER_LOG | 700 | 4820 | 25768 | 18.71% | 5/8 | 62.50%* | — | 3600s |

\* activity coverage taken from `utg.js` (screens the explorer reached), not from AndroLog `ACTIVITY=` probes — LLMDroid's AndroLog monitor tracks methods only. The two count slightly differently, so treat a mixed-source activity comparison as indicative rather than exact.

Both tools were given the same 3600s budget. Durations below include each tool's own shutdown, so they differ slightly.

> **Feature coverage scored for TestCube only.** The evaluator is trace-based and works on either tool; score the other with scripts/evaluate_features.py to get a comparable number.

**Code coverage — TestCube 14.68% vs LLMDroid 18.71%: -4.02 pp (-21.5% relative).**

**Activity coverage — TestCube 37.50% vs LLMDroid 62.50% (-25.00 pp), but measured differently on each side (androlog, utg); compare like-for-like before quoting this.**

**Saturation** — TestCube reached 99% of its final coverage 88% of the way through (15/17 samples); LLMDroid reached 99% of its final coverage 65% of the way through (458/700 samples). A run that flattened early was not truncated by its budget.

