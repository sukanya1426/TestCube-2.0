# Code coverage comparison

| Tool | Run | Tag | Actions | Methods hit | Total | Code cov. | Activities | Activity cov. | Feature cov. | Duration |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| TestCube | wikimediacommons | WIKIMEDIACOMMONS_SUPER_LOG | 238 | 7190 | 88193 | 8.15% | 2/26 | 7.69% | 0.00% (0/30) | 3642s |
| LLMDroid | wikimediacommons | WIKIMEDIACOMMONS_SUPER_LOG | 520 | 6183 | 88193 | 7.01% | 2/26 | 7.69%* | — | 3581s |

\* activity coverage taken from `utg.js` (screens the explorer reached), not from AndroLog `ACTIVITY=` probes — LLMDroid's AndroLog monitor tracks methods only. The two count slightly differently, so treat a mixed-source activity comparison as indicative rather than exact.

Both tools were given the same 3600s budget. Durations below include each tool's own shutdown, so they differ slightly.

> **Feature coverage scored for TestCube only.** The evaluator is trace-based and works on either tool; score the other with scripts/evaluate_features.py to get a comparable number.

**Code coverage — TestCube 8.15% vs LLMDroid 7.01%: +1.14 pp (+16.3% relative).**

**Activity coverage — TestCube 7.69% vs LLMDroid 7.69% (-0.00 pp), but measured differently on each side (androlog, utg); compare like-for-like before quoting this.**

**Saturation** — TestCube reached 99% of its final coverage 92% of the way through (22/24 samples); LLMDroid reached 99% of its final coverage 20% of the way through (102/520 samples). A run that flattened early was not truncated by its budget.

