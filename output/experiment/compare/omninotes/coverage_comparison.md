# Code coverage comparison

| Tool | Run | Tag | Actions | Methods hit | Total | Code cov. | Activities | Activity cov. | Feature cov. | Duration |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| TestCube | omninotes | OMNINOTES_SUPER_LOG | 154 | 6188 | 33780 | 18.32% | 1/13 | 7.69% | 0.00% (0/48) | 1660s |
| LLMDroid | omninotes | OMNINOTES_SUPER_LOG | 749 | 7777 | 33780 | 23.02% | 3/13 | 23.08%* | — | 3587s |

\* activity coverage taken from `utg.js` (screens the explorer reached), not from AndroLog `ACTIVITY=` probes — LLMDroid's AndroLog monitor tracks methods only. The two count slightly differently, so treat a mixed-source activity comparison as indicative rather than exact.

Both tools were given the same 3600s budget. Durations below include each tool's own shutdown, so they differ slightly.

> **Feature coverage scored for TestCube only.** The evaluator is trace-based and works on either tool; score the other with scripts/evaluate_features.py to get a comparable number.

**Code coverage — TestCube 18.32% vs LLMDroid 23.02%: -4.70 pp (-20.4% relative).**

**Activity coverage — TestCube 7.69% vs LLMDroid 23.08% (-15.39 pp), but measured differently on each side (androlog, utg); compare like-for-like before quoting this.**

**Saturation** — TestCube reached 99% of its final coverage 81% of the way through (13/16 samples); LLMDroid reached 99% of its final coverage 53% of the way through (394/749 samples). A run that flattened early was not truncated by its budget.

