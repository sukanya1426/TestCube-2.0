# Code coverage comparison

| Tool | Run | Tag | Actions | Methods hit | Total | Code cov. | Activities | Activity cov. | Feature cov. | Duration |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| TestCube | materialfiles | MATERIALFILE_SUPER_LOG | 348 | 6263 | 33328 | 18.79% | 4/28 | 14.29% | 0.00% (0/42) | 3900s |
| LLMDroid | materialfiles | MATERIALFILE_SUPER_LOG | 731 | 6177 | 33328 | 18.53% | 4/28 | 14.29%* | 0.00% (0/42) | 3600s |

\* activity coverage taken from `utg.js` (screens the explorer reached), not from AndroLog `ACTIVITY=` probes — LLMDroid's AndroLog monitor tracks methods only. The two count slightly differently, so treat a mixed-source activity comparison as indicative rather than exact.

Both tools were given the same 3600s budget. Durations below include each tool's own shutdown, so they differ slightly.

**Feature coverage — TestCube 0.00% vs LLMDroid 0.00%: +0.00 pp** (matcher: deterministic, same ground truth and evaluator on both traces).

**Code coverage — TestCube 18.79% vs LLMDroid 18.53%: +0.26 pp (+1.4% relative).**

**Activity coverage — TestCube 14.29% vs LLMDroid 14.29% (+0.00 pp), but measured differently on each side (androlog, utg); compare like-for-like before quoting this.**

**Saturation** — TestCube reached 99% of its final coverage 91% of the way through (32/35 samples); LLMDroid reached 99% of its final coverage 91% of the way through (665/731 samples). A run that flattened early was not truncated by its budget.

