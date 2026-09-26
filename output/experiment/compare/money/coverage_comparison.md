# Code coverage comparison

| Tool | Run | Tag | Actions | Methods hit | Total | Code cov. | Activities | Activity cov. | Duration |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| TestCube | money | MONEY_SUPER_LOG | 47 | 9489 | 147371 | 6.44% | 7/51 | 13.73% | 765s |
| LLMDroid | money | MONEY_SUPER_LOG | 138 | 6087 | 147371 | 4.13% | 4/51 | 7.84%* | 598s |

\* activity coverage taken from `utg.js` (screens the explorer reached), not from AndroLog `ACTIVITY=` probes — LLMDroid's AndroLog monitor tracks methods only. The two count slightly differently, so treat a mixed-source activity comparison as indicative rather than exact.

Both tools were given the same 600s budget. Durations below include each tool's own shutdown, so they differ slightly.

**Code coverage — TestCube 6.44% vs LLMDroid 4.13%: +2.31 pp (+55.9% relative).**

**Activity coverage — TestCube 13.73% vs LLMDroid 7.84% (+5.89 pp), but measured differently on each side (androlog, utg); compare like-for-like before quoting this.**

**Saturation** — TestCube reached 99% of its final coverage 80% of the way through (4/5 samples); LLMDroid reached 99% of its final coverage 62% of the way through (86/138 samples). A run that flattened early was not truncated by its budget.

