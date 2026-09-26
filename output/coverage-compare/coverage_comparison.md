# Code coverage comparison

| Tool | Run | Tag | Actions | Methods hit | Total | Code cov. | Activities | Activity cov. | Duration |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| TestCube | money | MONEY_SUPER_LOG | 306 | 10339 | 147371 | 7.02% | 14/51 | 27.45% | 3643s |
| LLMDroid | money | MONEY_SUPER_LOG | 400 | 6121 | 147371 | 4.15% | 4/51 | 7.84%* | 1738s |

\* activity coverage taken from `utg.js` (screens the explorer reached), not from AndroLog `ACTIVITY=` probes — LLMDroid's AndroLog monitor tracks methods only. The two count slightly differently, so treat a mixed-source activity comparison as indicative rather than exact.

**Code coverage — TestCube 7.02% vs LLMDroid 4.15%: +2.86 pp (+68.9% relative).**

**Activity coverage — TestCube 27.45% vs LLMDroid 7.84% (+19.61 pp), but measured differently on each side (androlog, utg); compare like-for-like before quoting this.**

**Saturation** — TestCube reached 99% of its final coverage 90% of the way through (28/31 samples); LLMDroid reached 99% of its final coverage 22% of the way through (86/399 samples). A run that flattened early was not truncated by its budget.
