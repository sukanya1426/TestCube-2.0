# Code coverage comparison

| Tool | Run | Tag | Actions | Methods hit | Total | Code cov. | Activities | Activity cov. | Feature cov. | Duration |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| TestCube | fossifyvoicerecorder | FOSSIFYVOICE_SUPER_LOG | 161 | 3147 | 29941 | 10.51% | 2/13 | 15.38% | 4.35% (1/23) | 1815s |
| LLMDroid | fossifyvoicerecorder | FOSSIFYVOICE_SUPER_LOG | 740 | 8811 | 29941 | 29.43% | 8/13 | 61.54%* | — | 3596s |

\* activity coverage taken from `utg.js` (screens the explorer reached), not from AndroLog `ACTIVITY=` probes — LLMDroid's AndroLog monitor tracks methods only. The two count slightly differently, so treat a mixed-source activity comparison as indicative rather than exact.

Both tools were given the same 3600s budget. Durations below include each tool's own shutdown, so they differ slightly.

> **Feature coverage scored for TestCube only.** The evaluator is trace-based and works on either tool; score the other with scripts/evaluate_features.py to get a comparable number.

**Code coverage — TestCube 10.51% vs LLMDroid 29.43%: -18.92 pp (-64.3% relative).**

**Activity coverage — TestCube 15.38% vs LLMDroid 61.54% (-46.16 pp), but measured differently on each side (androlog, utg); compare like-for-like before quoting this.**

**Saturation** — TestCube reached 99% of its final coverage 88% of the way through (15/17 samples); LLMDroid reached 99% of its final coverage 82% of the way through (607/740 samples). A run that flattened early was not truncated by its budget.

