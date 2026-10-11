# Code coverage comparison

| Tool | Run | Tag | Actions | Methods hit | Total | Code cov. | Activities | Activity cov. | Feature cov. | Duration |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| TestCube | loophabits | LOOPHABITS_SUPER_LOG | 136 | 5896 | 41715 | 14.13% | 4/11 | 36.36% | 0.00% (0/38) | 1593s |
| LLMDroid | loophabits | LOOPHABITS_SUPER_LOG | 747 | 7902 | 41715 | 18.94% | 7/11 | 63.64%* | — | 3598s |

\* activity coverage taken from `utg.js` (screens the explorer reached), not from AndroLog `ACTIVITY=` probes — LLMDroid's AndroLog monitor tracks methods only. The two count slightly differently, so treat a mixed-source activity comparison as indicative rather than exact.

Both tools were given the same 3600s budget. Durations below include each tool's own shutdown, so they differ slightly.

> **Feature coverage scored for TestCube only.** The evaluator is trace-based and works on either tool; score the other with scripts/evaluate_features.py to get a comparable number.

**Code coverage — TestCube 14.13% vs LLMDroid 18.94%: -4.81 pp (-25.4% relative).**

**Activity coverage — TestCube 36.36% vs LLMDroid 63.64% (-27.28 pp), but measured differently on each side (androlog, utg); compare like-for-like before quoting this.**

**Saturation** — TestCube reached 99% of its final coverage 86% of the way through (12/14 samples); LLMDroid reached 99% of its final coverage 75% of the way through (558/747 samples). A run that flattened early was not truncated by its budget.

