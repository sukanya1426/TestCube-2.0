# Code coverage comparison

| Tool | Run | Tag | Actions | Methods hit | Total | Code cov. | Activities | Activity cov. | Feature cov. | Duration |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| TestCube | vlc | VLC_SUPER_LOG | 266 | 10367 | 205862 | 5.04% | 3/40 | 7.50% | — | 3601s |
| LLMDroid | vlc | VLC_SUPER_LOG | 731 | 16566 | 205862 | 8.05% | 5/40 | 12.50%* | — | 3597s |

\* activity coverage taken from `utg.js` (screens the explorer reached), not from AndroLog `ACTIVITY=` probes — LLMDroid's AndroLog monitor tracks methods only. The two count slightly differently, so treat a mixed-source activity comparison as indicative rather than exact.

Both tools were given the same 3600s budget. Durations below include each tool's own shutdown, so they differ slightly.

**Code coverage — TestCube 5.04% vs LLMDroid 8.05%: -3.01 pp (-37.4% relative).**

**Activity coverage — TestCube 7.50% vs LLMDroid 12.50% (-5.00 pp), but measured differently on each side (androlog, utg); compare like-for-like before quoting this.**

**Saturation** — TestCube reached 99% of its final coverage 11% of the way through (3/27 samples); LLMDroid reached 99% of its final coverage 90% of the way through (656/731 samples). A run that flattened early was not truncated by its budget.

