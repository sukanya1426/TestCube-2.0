# Handoff: running TestCube vs LLMDroid

Paste this into a fresh chat for context.

## The goal

Compare two LLM-driven Android GUI explorers on the same APKs:

- **TestCube** — this repo. Policy `feature_guided`.
- **LLMDroid** — vendored at `compare/LLMDroid/LLMDroid-Droidbot/`. Policy `dfs_greedy`.

Two things are measured per run:

- **Code coverage** (the comparable metric) — AndroLog bytecode probes emit one
  logcat line per executed method. Both tools run the **same instrumented APK**
  so the denominator is identical.
- **Feature coverage** (TestCube only) — scored offline against
  `feature/<app>/ground_truth.json`. LLMDroid has no feature list, so this is
  supplementary, not a comparison.

Protocol: **1 hour of wall clock per tool per app**, same instrumented APK,
app reinstalled between runs. Coverage rises with time, so unequal budgets
invalidate any delta.

## What to run

Everything is one command. Each script checks its prerequisites *before*
starting anything long, because a missing dependency previously wasted a
6-hour batch.

```bash
bash scripts/setup_tools.sh           # ONE TIME after cloning. ~5 min.
bash scripts/run_one_llmdroid.sh      # 1 app, LLMDroid only, ~1h
bash scripts/run_one_app.sh           # 1 app, BOTH tools, ~2h10m
python scripts/run_experiment.py --all --usable-only --resume   # full batch, ~43h
```

Both `run_one_*.sh` scripts have `APP` and `BUDGET_SECONDS` at the top. Set
`BUDGET_SECONDS=600` for a 10-minute smoke test before committing to an hour.

Which apps run in the batch is set by `APK_NAMES` / `NUM_APKS` at the top of
`scripts/run_experiment.py`. **`APK_NAMES` wins; `NUM_APKS` applies only when
`APK_NAMES` is empty.** Everything else (budget, output paths, policy) is in
`experiment/config.json`.

## Checks, so a run does not go to waste

Verify before starting:

```bash
python scripts/check_experiment_setup.py     # instant: specs + compatibility for all 30 apps
python scripts/run_experiment.py --dry-run --all --usable-only   # the plan, runs nothing
```

`run_experiment.py` refuses to start unless all of these hold, and says exactly
what to fix:

| check | why it exists |
| --- | --- |
| AndroLog jar + `tools/android-platforms` | `tools/` is gitignored, so a fresh clone has neither. Without them **every** APK fails to instrument, which looks like broken APKs. |
| `openai` and `jpype` importable | LLMDroid imports both at module load. Missing either makes LLMDroid exit 1 for **every** app while TestCube succeeds — a batch that looks half-working and yields no comparison. This is what actually happened. |
| a device on `adb` | fails in 0.2s instead of hanging |
| single-instance lock | two runners on one emulator interleave taps and uninstall each other's app; the symptom is an idle screen and flat coverage |
| APK prefetch | all APKs downloaded up front, so a broken download surfaces in minute one, not hour eighteen |

Also needed, not auto-checked: **Ollama running** with `qwen2.5vl:7b` (both
tools use it), and `caffeinate -i` on macOS so the machine does not sleep
through a long batch.

## Traps that already cost time

1. **A wrong AndroLog tag gives a clean run reporting 0.00000% coverage** — app
   installs, launches, verifies, explores, every artifact written, no error
   anywhere. The runner now reads the tag out of the APK's dex rather than
   trusting the catalogue. If coverage reads 0%, suspect the tag or dead dex,
   not the explorer. `nononsensenotes` did this: 139 actions, zero probes.
2. **`verified_ok` is environment-specific.** Soot's type assigner behaves
   differently per JDK: `money` and `vlc` instrument on **Java 21** and fail on
   **Java 17**. Yield was 20/30 on 21 and 16/30 on 17. Use Java 21.
3. **Never pass `-keep_app`.** droidbot installs only when the package is absent
   and uninstalls at teardown. Keeping the app lets the second tool inherit the
   first tool's login state, and `-grant_perm` silently does nothing.
4. **Always launch LLMDroid through `scripts/run_llmdroid.py`.** It swaps
   `config.json.<app>` into `config.json` and restores it afterwards. Killed
   mid-run, it leaves `config.json` mid-swap and the next run uses the wrong app.
5. **Run budgets are flags now** (`--max-run-seconds`), not only env vars.
6. **`apks/` is not in git** (1.3 GB, and four APKs exceed GitHub's 100 MB
   limit). Rebuild with `python scripts/fetch_apks.py`; exact pinned builds are
   in `docs/APK_SOURCES.md`. newpipe is pinned to 0.27.0 because F-Droid's
   current 0.29.1 fails instrumentation.

## State as of 2026-10-02

- 30 candidate apps, specs complete and valid for all 30
  (`feature/<app>/` × 4 files + `compare/.../config.json.<app>`).
- `experiment/apps.json` currently records **16 usable / 14 failing**. These
  verdicts were measured on **Java 17**; on Java 21 the same APKs gave 20/30,
  with `money`, `vlc`, `fossifynotes` and `fossifymusic` usable. Re-measure with
  `python scripts/survey_instrumentation.py --redo` after changing JDK.
- One 16-app TestCube batch exists under `output/experiment/`. **LLMDroid ran
  zero times in it** (missing `openai`/`jpype`), so there is **no
  TestCube-vs-LLMDroid comparison yet** — that is the open task.
- TestCube-only results from that batch: median code coverage 12.8%, best
  omninotes 18.3%, weakest markor 5.1%. Feature coverage was near zero (7 of 16
  at exactly 0.0%), which is worth investigating separately — the generated
  ground truths may be too demanding.

## Known confound for any writeup

TestCube reads a human-authored `guide_features.json`; LLMDroid gets only a
prose `Description`. Part of any gap is *guided vs unguided*, not *better
algorithm*. Supporting "feature guidance improves coverage" is fine; claiming
"TestCube's explorer beats LLMDroid's" needs TestCube's own `dfs_greedy` as a
third arm. Also average ≥3 seeds — both tools are stochastic.
