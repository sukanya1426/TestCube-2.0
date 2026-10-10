# Code coverage comparison

| Tool | Run | Tag | Actions | Methods hit | Total | Code cov. | Activities | Activity cov. | Feature cov. | Duration |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| TestCube | newpipe | PIPE_SUPER_LOG | 241 | 12037 | 74478 | 16.16% | 3/12 | 25.00% | 17.65% (3/17) | 1639s |
| LLMDroid | newpipe | PIPE_SUPER_LOG | 130 | 10862 | 74478 | 14.58% | 3/12 | 25.00%* | 0.00% (0/17) | 599s |

\* activity coverage taken from `utg.js` (screens the explorer reached), not from AndroLog `ACTIVITY=` probes — LLMDroid's AndroLog monitor tracks methods only. The two count slightly differently, so treat a mixed-source activity comparison as indicative rather than exact.

> **Unequal run time:** TestCube 1639s, LLMDroid 599s. Coverage rises with time, so a delta between runs of different lengths is not a like-for-like result — check whether the shorter run stopped on its own or was cut short.

**Feature coverage — TestCube 17.65% vs LLMDroid 0.00%: +17.65 pp** (matcher: ai, same ground truth and evaluator on both traces).

**Code coverage — TestCube 16.16% vs LLMDroid 14.58%: +1.58 pp (+10.8% relative).**

**Activity coverage — TestCube 25.00% vs LLMDroid 25.00% (+0.00 pp), but measured differently on each side (androlog, utg); compare like-for-like before quoting this.**

**Saturation** — TestCube reached 99% of its final coverage 88% of the way through (14/16 samples); LLMDroid reached 99% of its final coverage 99% of the way through (129/130 samples). A run that flattened early was not truncated by its budget.

