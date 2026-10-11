# Code coverage comparison

| Tool | Run | Tag | Actions | Methods hit | Total | Code cov. | Activities | Activity cov. | Feature cov. | Duration |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| TestCube | markor | MARKOR_SUPER_LOG | 41 | 3125 | 61884 | 5.05% | 2/11 | 18.18% | 0.00% (0/46) | 473s |
| LLMDroid | markor | MARKOR_SUPER_LOG | 759 | 3222 | 61884 | 5.21% | 2/11 | 18.18%* | 0.00% (0/46) | 3597s |

\* activity coverage taken from `utg.js` (screens the explorer reached), not from AndroLog `ACTIVITY=` probes — LLMDroid's AndroLog monitor tracks methods only. The two count slightly differently, so treat a mixed-source activity comparison as indicative rather than exact.

Both tools were given the same 3600s budget. Durations below include each tool's own shutdown, so they differ slightly.

**Feature coverage — TestCube 0.00% vs LLMDroid 0.00%: +0.00 pp** (matcher: deterministic, same ground truth and evaluator on both traces).

**Code coverage — TestCube 5.05% vs LLMDroid 5.21%: -0.16 pp (-3.0% relative).**

**Activity coverage — TestCube 18.18% vs LLMDroid 18.18% (-0.00 pp), but measured differently on each side (androlog, utg); compare like-for-like before quoting this.**

**Saturation** — TestCube reached 99% of its final coverage 20% of the way through (1/5 samples); LLMDroid reached 99% of its final coverage 3% of the way through (24/759 samples). A run that flattened early was not truncated by its budget.

