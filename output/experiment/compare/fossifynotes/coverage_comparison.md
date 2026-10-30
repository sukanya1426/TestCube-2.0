# Code coverage comparison

| Tool | Run | Tag | Actions | Methods hit | Total | Code cov. | Activities | Activity cov. | Feature cov. | Duration |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| TestCube | fossifynotes | FOSSIFYNOTES_SUPER_LOG | 297 | 6800 | 26609 | 25.56% | 6/12 | 50.00% | — | 3569s |
| LLMDroid | fossifynotes | FOSSIFYNOTES_SUPER_LOG | 757 | 7570 | 26609 | 28.45% | 8/12 | 66.67%* | — | 3600s |

\* activity coverage taken from `utg.js` (screens the explorer reached), not from AndroLog `ACTIVITY=` probes — LLMDroid's AndroLog monitor tracks methods only. The two count slightly differently, so treat a mixed-source activity comparison as indicative rather than exact.

Both tools were given the same 3600s budget. Durations below include each tool's own shutdown, so they differ slightly.

**Code coverage — TestCube 25.56% vs LLMDroid 28.45%: -2.89 pp (-10.2% relative).**

**Activity coverage — TestCube 50.00% vs LLMDroid 66.67% (-16.67 pp), but measured differently on each side (androlog, utg); compare like-for-like before quoting this.**

**Saturation** — TestCube reached 99% of its final coverage 67% of the way through (20/30 samples); LLMDroid reached 99% of its final coverage 48% of the way through (361/757 samples). A run that flattened early was not truncated by its budget.

