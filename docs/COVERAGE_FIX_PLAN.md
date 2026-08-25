# Fixing TestCube coverage, termination, and whole-app exploration

## Context

The user made the changes documented in `docs/PROJECT.md` (restart between features,
exploration bank, weighted metric, LLM judge), but feature coverage is still poor and runs
"get into a loop and run for a long time" without terminating cleanly.

I analysed `output/money-2` (Money Manager Ex, 28 features, 2026-08-22 — the latest run).
Everything below is measured from that run's `events/`, `feature_test/log.md`,
`report.json`, and the source. Verified, not inferred.

### What the run actually did

| Measure | Value |
| --- | --- |
| Wall clock | **1h 29m**, 246 events, ~20s/event |
| Online coverage | 13/28 = **46%** |
| Offline (LLM judge) | 2/28 = **7.14%** |
| Overlap of the two "covered" sets | **zero** |
| Actions that matched a listed step | **11 of 203 (5.4%)** |
| Features never attempted | **6** (GT023–GT028, `attempts: 0`) |
| Run end | died mid-GT022 after a ~4-min hang |

Two features consumed **53 of 88 minutes** (GT017 29.7m, GT009 23.4m); both ended at
`completion_ratio: 0.0`.

### Root causes (all verified)

**1. Loop detectors are state-hash based; the loop is action-based.**
`nextDayButton` (a date stepper) was tapped **68 times** — 40% of all taps — in 10 streaks
up to 14 long, recurring *after* restarts. Each tap changes the date text, so the state hash
changes: I measured **all 67 adjacent state pairs as different**. So `_no_progress`
(`policy.py:831-845`, `MAX_NO_PROGRESS=12`) resets every tap, `_in_state_cycle`
(`policy.py:1417-1423`) never sees a repeat, and `_maybe_stagnation` (`policy.py:1943-1948`)
keeps novelty at 1.0. All three are blind by construction.
`widget_signature` and `self._feature_sigs` **already exist** (`policy.py:60`, `768-773`)
and would have caught 33 identical consecutive signatures — they are wired only to
`shared_flow`, never to loop detection.

**2. The heuristic scorer is inert, so everything takes the slow VLM path.**
`confidence = min(0.95, best_score/8.0)` (`advisor.py:409`) vs `HEURISTIC_TRUST = 0.55`
(`advisor.py:22`) needs `best_score >= 4.4`. Money scored 0.00–0.06 throughout, so
**136 of 138 decisions** took the 30–40s VLM fallback. This is the direct cause of the
"runs for a long time" symptom — latency, not step count.

**3. The guide list is a tenth of the gold list's depth.** This correlates with score:

| App | guide steps | gold steps | offline coverage |
| --- | --- | --- | --- |
| vinyl | 16 (avg 1.8) | 18 (avg 2.0) | **22%** |
| spotube | 30 (avg 1.0) | 90 (avg 3.1) | — |
| money | 29 (avg 1.0) | 139 (avg 5.0) | **7%** |

27 of money's 28 guide features have exactly ONE vague action ("Add a transaction") vs
gold's 9 concrete steps. One matched tap empties `remaining_actions` → `STATUS_COVERED`
("Listed steps are done" ×11). Vinyl, the only app whose guide matches gold depth, scores best.

**4. No global budget; per-feature caps never fire.** `MAX_STEPS_PER_FEATURE=60` was never
hit (max observed 47). droidbot defaults are `DEFAULT_EVENT_COUNT=100000000` /
`DEFAULT_TIMEOUT=-1` (`input_manager.py:19-20`), so the policy raising
`InputInterruptedException` is the only realistic terminator. Early features starve later ones.

**5. Non-termination hazards.**
- `policy.py:230-234` — bare `except: continue` that does **not** increment `action_count`
  (incremented at `:235`, after the try): a persistently-throwing `generate_event` spins forever.
- `policy.py:948` + `:860-861` — `_feature_switch_restart=True` suppresses `_restarts += 1`
  and `_advance_feature_restart` has no attempt counter, so `MAX_RESTARTS` can never fire.
- `policy.py:851` — `_restarts = 0` on every foregrounding defeats the crash cap.
- `policy.py:966-969` — `_continue_next_feature` recursion writes `_switch_depth`, never guards on it.
- `MAX_OUTSIDE_STEPS=6` (`policy.py:90`) is dead code, never read.

**6. Online metric over-credits.** GT002 is `covered` at ratio 1.00 with **zero** completed
actions. `policy.py:842-843` also marks `STATUS_COVERED` purely because a screen stopped changing.

**7. Leaked prompt template.** 3 log entries store the literal placeholder
`"why this action advances the remaining step"` from `advisor.py:771` as the decision reason.

### Ruled out — do not "fix"

`money-2` has no top-level `states/` or `utg.js`, but both exist under `.droidbot/`
(204 states), and `trace_loader._first_dir/_first_file` probe `.droidbot` **first**. All 246
events resolve their start/stop states. The low offline score is **not** missing trace data.

---

## Plan

Sequenced so the run always terminates first, then stops wasting taps, then improves quality.

### P0 — Clean termination (do first)

**P0.1 Always-increment the action counter.** `policy.py:230-235`: move
`self.action_count += 1` into a `finally` so the swallow-and-`continue` path cannot freeze the
global counter. Add `_consecutive_errors`; abort after 5 with `stop_reason="repeated_errors"`.
Without this, no budget below is reliable.

**P0.2 Global budget.** Add to `FeatureTesterConfig` (`config.py:36`): `max_run_events=400`,
`max_run_seconds=2700`, plus CLI flags via the existing `add_cli_flags` (`config.py:75`).
In `start()` (`policy.py:210-219`) use `min(input_manager.event_count, cfg.max_run_events)`
and check elapsed wall clock each iteration. A run with no flags must now terminate.

**P0.3 Bound the restart loop.** Add a lifetime `_restart_attempts` (never reset) incremented
in `_start_app_event` **unconditionally**, capped independently of `MAX_RESTARTS`. Give
`_advance_feature_restart` (`policy.py:930-948`) a per-switch try counter (~3) that gives up
and proceeds rather than re-issuing start intents forever.

**P0.4 Guard recursion.** `policy.py:966`: stop recursing past depth 5, reset `_switch_depth`
in `_begin_feature`.

**P0.5 Per-feature attempts cap.** `feature["attempts"]` (`policy.py:583`) is incremented but
never compared — add `cfg.max_feature_attempts=2`. Wire the dead `MAX_OUTSIDE_STEPS` into the
hardcoded `4`/`7` at `policy.py:333-335`.

### P1 — Stop the wasted taps (the 68-tap loop)

**P1.1 Per-widget tap ceiling — the load-bearing fix.** `_tap_counts` is keyed by
`(state_str, view_str)` so it is useless when the hash churns. Add `self._widget_taps` keyed by
the **state-free** `self._widget_try_key(event)` (`policy.py:1433-1435`, already
`widget_signature`-based), incremented in `_emit` (`policy.py:745-749`), reset in
`_begin_feature`. In `_filter_banned` (`policy.py:1447-1460`) drop any widget past
`cfg.max_widget_taps=6` (never BACK). `_filter_banned` already has a safe fallback chain, so
this cannot dead-end. This alone caps the 68 taps at 6.

**P1.2 Count revisits, not adjacent equality.** In `_note_progress` (`policy.py:834-843`),
only reset `_no_progress` when the state is genuinely **new to this feature** (consult the
already-populated `_feature_seen_states`, `policy.py:839`); a revisit is not progress. Apply
the same change to `is_new` in `_maybe_stagnation` (`policy.py:1946`).

**P1.3 Remove the "stuck = covered" path.** `policy.py:842-843`: mark `STATUS_PARTIAL` when
some steps completed, else `STATUS_DROPPED` — never `STATUS_COVERED` for a frozen screen.

### P2 — Whole-app exploration

**P2.1 Fair-share per-feature budget.** Once the feature count is known (`policy.py:~555`):
`per_feature = max(8, min(cfg.max_steps_per_feature, cfg.max_run_events // n))`. For 28
features / 400 events → ~14 steps each, guaranteeing all 28 are *reached* (money-2 reached 22).
Use it in place of the constant at `policy.py:285`. On the retry pass, recompute from the
remaining budget so unspent steps flow to hard features.

**P2.2 Bound hybrid discovery.** `discovery.py:64-81` appends every LLM-proposed feature
unbounded — slice to the existing `cfg.discovery_budget` (12). Set `_discovery_done` in a
`finally` in `_commit_discovery` so every exit path marks it, and have `_hybrid_still_pending`
(`policy.py:1994-2000`) stop vetoing termination (`policy.py:281`) once the budget is ~90% spent.

### P3 — Coverage quality

**P3.1 Auto-enrich thin guide features (chosen approach).** `refine_granularity`
(`granularity.py`) already exists and calls an LLM, but it **splits coarse** features and runs
**only** on the `local_readme` fallback (`policy.py:2379-2385`) — the guide path never touches it.
Add the mirror operation in the same module: for a guide feature whose `actions` are below a
floor (< 3), expand it into 3–6 concrete behavioral steps using the README + `nav_hints`, and
call it on the guide branch of `_load_feature_payload` (`policy.py:2343`). Cache the enriched
list to `output/<run>/feature_test/features.json` (already written) so a re-run is cheap.

Keyed on step count only — no per-app strings, works for a new APK. Gold stays eval-only
(`PROJECT.md:30`): enrichment reads README/guide, never `ground_truth.json`. Add a test
asserting enriched guide actions are **not** identical to gold, preserving independence.

**P3.2 Fix step matching (5.4% match rate).** In `_match_remaining_action`
(`journal.py:820-849`): replace the hard `len(overlap) >= 2` cutoff with a containment ratio
`len(overlap)/min(len(needle),len(hay))` against a new `cfg.step_match_threshold` (~0.5), so a
1-token needle still matches a 9-token gold step; add an empty-token fallback so `"Tap OK"`
(currently tokenizes to `{}` — literally unmatchable) works; drop `button`/`icon` from the
stopword set (`journal.py:884-890`); lower the 4-char floor to 2.

**Do not** weaken `_event_compatible_with_step` (`journal.py:852-865`) — it is the precision
backstop with ~8 existing tests. **Leave** `_followup_submit_step` returning `None`; its
docstring records a real regression and `test_followup_submit_after_typing` pins it.

**P3.3 Fix the leaked template.** Add a module-level `PROMPT_PLACEHOLDERS` tuple beside the
prompt skeleton (`advisor.py:771`, `:627`) and blank any reason matching it, falling back to
`heuristic.reason` — same treatment `matched` already gets.

**P3.4 Cut blind VLM calls.** In `advisor.decide` (`advisor.py:102-207`), when
`heuristic.confidence == 0.0` and steps remain, try the existing
`mechanisms.find_affordance_event` and `pick_untried_plausible` **before** spending a VLM call.
A reordering, not new machinery; gate behind the existing `afford_search` flag. Add a
per-feature VLM budget so one feature cannot burn 30 minutes.

### P4 — Metric honesty

**P4.1** Lead the online report with the already-implemented weighted coverage
(`journal.py:812-819`); label the strict number "features with all guide steps matched".

**P4.2** Emit an online-vs-offline agreement block (covered counts, set **overlap**,
disagreement list), reusing `confusion._best_journal_match` (`confusion.py:47-54`) to match by
name rather than `GT0NN` IDs (which collide for money but will not for other apps). The zero
overlap becomes a tracked metric instead of a manual discovery.

**P4.3** Record `journal.session["stop_reason"]` on every termination path
(`all_features_done` / `budget_events` / `budget_time` / `restart_loop` / `repeated_errors`) so
a budget-truncated run is never compared against a natural one.

---

## Verification

**Tier 1 — existing tests must stay green.** `pytest tests/` (`test_feature_guided.py`,
`test_feature_upgrade.py`, `test_feature_eval.py`, `test_layout_paths.py`). P3.2 is the
highest regression risk; the `_event_compatible_with_step` tests are the guardrail.

**Tier 2 — new unit tests.**
- Churning-hash loop: 20 all-different states sharing one `widget_signature` → widget dropped
  after 6 taps, feature terminates. (Directly reproduces the 68-tap bug.)
- Always-raising `generate_event` → `start()` returns within 6 iterations with a stop reason.
- Fair-share budget: 28 stub features / 400 events → 14 each, all reach `attempts >= 1`.
- Match-quality table: `"Tap OK"`/`"Tap Play"` match; `("Tap Save", ["Enter a file name"])` does not.
- Guide enrichment produces ≥3 actions and is **not** identical to gold.

**Tier 3 — offline replay, no device.** Re-run `scripts/evaluate_features.py` against the
existing `output/money-2` trace (complete on disk) to validate P3.2/P4 before spending a live run.

**Tier 4 — full live re-run of all three apps** (user's choice), default flags, no
`-count`/`-timeout`, to prove unattended termination:

```bash
source .venv/bin/activate && adb devices
droidbot -a apks/vinyl.apk   -o output/vinyl-fix1   -is_emulator
droidbot -a apks/money.apk   -o output/money-fix1   -is_emulator
droidbot -a apks/spotube.apk -o output/spotube-fix1 -is_emulator

LLM_BACKEND=local python scripts/evaluate_features.py \
  --results output/money-fix1 --features feature/money/ground_truth.json \
  --readme feature/money/README.md --matcher ai
```

Pin `LLM_BACKEND=local` — the `.env` `GEMINI_API_KEY` would otherwise let `auto` pick a
different judge than the baseline. I verified local Ollama reproduces the stored vinyl-2
result exactly (2/9, 22.22%), so local is a valid baseline-matched judge.

**Success criteria:** run ends on `all_features_done` or a budget in well under 45 min; all 28
money features `attempts >= 1`; **zero** widget signatures with >6 taps; step match rate well
above 5.4%; and online/offline covered-set overlap materially above zero — criterion (iv) is
the one proving the coverage work is real rather than re-tuned optimism.

## Expected outcome, stated honestly

P3.1 (enrichment) should raise real coverage. But P1.3 + P3.1's step-count guard + P4 will make
the **reported online number drop** from 46% toward the offline number. That is the correct
outcome — 7% was always the truth, and 46% was measuring one tap per feature. Judge this work
by the offline number and the online/offline overlap, not by the online headline.

## Cross-check note (separate from this plan)

`money-1`'s stored 14.29% used the old `(COVERED+PARTIAL)/Total` formula and has 2 partials;
under the current `COVERED/Total` it is 7.14%. `vinyl-2` is unaffected (0 partials). Worth
re-scoring money-1 before putting old and new runs in one table.
