# TestCube vs LLMDroid — batch experiment

One command runs the whole thing:

```bash
python scripts/run_experiment.py
```

That reads `experiment/config.json`, and for each app in turn does:
instrument → verify → **TestCube** → **LLMDroid** → compare → feature eval.
Each app is isolated: one failure is recorded and the next app starts.

## Before the first run

1. **Emulator up** (the runner refuses to start without one):

   ```bash
   cd ~/Library/Android/sdk/emulator && ./emulator -avd Pixel_5
   ```

2. **Ollama up**, since both tools use the local VLM:

   ```bash
   brew services start ollama
   python -m droidbot.local_vlm --check
   ```

3. **APKs in place.** Put each binary at `apks/<stem>.apk`, using the stems in
   `experiment/apps.json`. Only `money` and `newpipe` are present today; the
   other 28 have their specs generated but no binary.

4. **Specs generated** (already done for all 30; re-run after editing the dataset,
   which now lives in the repo at `docs/APK_DATASET.md`):

   ```bash
   python scripts/make_feature_specs.py --dataset docs/APK_DATASET.md
   ```

5. **Everything verified present:**

   ```bash
   python scripts/check_experiment_setup.py
   ```

## Changing what runs

**Which apps** is at the top of `scripts/run_experiment.py`, and nowhere else:

```python
APK_NAMES = ["money", "newpipe"]   # which APKs
NUM_APKS  = 5                      # how many
```

`APK_NAMES` wins; `NUM_APKS` applies only when `APK_NAMES` is `[]`. The script
prints which rule it used before doing anything.

**Everything else** is `experiment/config.json`:

| Want to change | Field | Or on the command line |
| --- | --- | --- |
| Which apps | `APK_NAMES` (in the script) | `--apps markor,aegis` |
| How many apps | `NUM_APKS` (in the script) | `--count 5` |
| The budget | `budget_seconds` | `--budget-seconds 1800` |
| Output folders | `testcube_output`, `llmdroid_output`, `compare_output`, `log_dir` | — |
| Skip LLMDroid | `run_llmdroid: false` | `--no-llmdroid` |

Useful:

```bash
python scripts/run_experiment.py --dry-run     # print the plan, run nothing
python scripts/run_experiment.py --count 5     # first pass
python scripts/run_experiment.py --resume      # continue, skipping finished apps
python scripts/run_experiment.py 2>&1 | tee run.log
```

## Where output lands

```
output/experiment/testcube/<stem>/    codecoverage.txt, code_coverage.json,
                                      feature_coverage/report.{txt,json}, utg.js
output/experiment/llmdroid/<stem>/    the same file names, LLMDroid's side
output/experiment/compare/<stem>/     coverage_comparison.{md,json}
output/experiment/compare/experiment_summary.md     one table for the whole batch
output/experiment/compare/experiment_results.json   machine-readable, rewritten per app
output/experiment/logs/<stem>.log     full stdout for that app
```

The summary and results files are rewritten after **every** app, so a batch
interrupted at app 17 still leaves 16 apps of usable results.

## The compatibility gate

An APK is only usable if it survives AndroLog instrumentation *and* the rewritten
dex verifies. That is not predictable from the app — `docs/CODE_COVERAGE.md`
records six of eight APKs failing, five on one Soot 4.6.0 bug, including the
least obfuscated APK measured. So the runner measures it:

1. `scripts/instrument_apk.py`, and the denominator is read back from the
   instrumented APK itself.
2. Install, launch, `grep VerifyError|FATAL EXCEPTION`, uninstall. `vinyl.apk`
   installs fine and is silently dead, which is what this step catches.

An app that fails either step is marked `skipped_instrumentation` /
`skipped_verify`, the reason is written into the summary, and the run moves on.
The outcome is written back into `experiment/apps.json` as
`instrumentation_status`, so the next run starts from evidence.

`experiment/apps.json` also carries a 12-app `reserve` pool to backfill failures.

## Fairness

- Both tools get the **same instrumented APK** and the **same wall-clock hour**.
  Different denominators make the numbers incomparable, and `compare_coverage.py`
  refuses a headline delta when tags or denominators differ.
- The runner never passes `-keep_app`, so each tool installs and uninstalls its
  own copy and LLMDroid cannot inherit TestCube's login state.
- `guide_features.json` and `ground_truth.json` are kept independent per app; if
  their name sets matched, the score would be guided-execution coverage rather
  than coverage. `scripts/make_feature_specs.py` guarantees this by construction.
- **Standing confound:** TestCube reads a per-app `guide_features.json`; LLMDroid
  gets only a prose `Description`. Part of any gap is *guided vs unguided*, not
  *better algorithm*. Add TestCube's own `dfs_greedy` as a third arm before
  claiming otherwise.
- Average ≥3 seeds. Coverage rises with time, so a single seed proves little.
