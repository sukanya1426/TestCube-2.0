# Code coverage comparison

| Tool | Run | Tag | Actions | Methods hit | Total | Code cov. | Activities | Activity cov. | Feature cov. | Duration |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| TestCube | newpipe | PIPE_SUPER_LOG | 325 | 14453 | 74478 | 19.41% | 5/12 | 41.67% | 0.00% (0/17) | 3528s |
| LLMDroid | newpipe | PIPE_SUPER_LOG | 534 | 18017 | 74478 | 24.19% | 5/12 | 41.67%* | — | 3587s |

\* activity coverage taken from `utg.js` (screens the explorer reached), not from AndroLog `ACTIVITY=` probes — LLMDroid's AndroLog monitor tracks methods only. The two count slightly differently, so treat a mixed-source activity comparison as indicative rather than exact.

Both tools were given the same 3600s budget. Durations below include each tool's own shutdown, so they differ slightly.

> **Feature coverage scored for TestCube only.** The evaluator is trace-based and works on either tool; score the other with scripts/evaluate_features.py to get a comparable number.

**Code coverage — TestCube 19.41% vs LLMDroid 24.19%: -4.79 pp (-19.8% relative).**

**Activity coverage — TestCube 41.67% vs LLMDroid 41.67% (+0.00 pp), but measured differently on each side (androlog, utg); compare like-for-like before quoting this.**

**Saturation** — TestCube reached 99% of its final coverage 88% of the way through (29/33 samples); LLMDroid reached 99% of its final coverage 65% of the way through (348/534 samples). A run that flattened early was not truncated by its budget.

