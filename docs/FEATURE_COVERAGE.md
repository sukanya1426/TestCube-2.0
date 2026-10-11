# Feature coverage: what the number means and how far it can be trusted

Code coverage says how much of an app's bytecode a run reached. Feature coverage
is meant to say something different: how much of what the app is *for* a run
actually exercised. It is scored offline, after the run, against a hand-written
`feature/<app>/ground_truth.json`, and both tools are scored by the same code
with the same arguments.

Run it with:

    python scripts/score_features.py --matcher deterministic --trace-only

## The number we report is step coverage

    step coverage = mean over features of (matched steps / checkable steps)

Each ground-truth feature is a short path of steps ("Open the Alarm tab", "tap
Save"). Step coverage is the share of those steps a run demonstrably executed.

Strict feature coverage -- every step of a feature matched -- is also written to
the report, and at a one-hour budget it is close to zero for both tools. That is
not a measurement artefact: neither tool reliably drives a multi-step feature to
completion in an hour. It is reported, but it does not discriminate, so step
coverage is the headline.

### Checkable steps

A step is only counted when its wording contains something app-specific. "tap
the + button" names no app-specific thing -- every Button in the app matches it
equally well -- so no trace can confirm or deny it, and counting it as a failure
would make one unwritable step sink a whole feature for every tool. Checkability
is decided from the ground-truth wording alone, never from a trace, so the
excluded set is identical for both tools.

## What is admissible as evidence

Only events the tool actually sent, plus the destination screen of those events
for outcome steps ("the results appear"). A widget merely being present in a UI
dump is not coverage.

Within an action, only the widget it touched is matched against: visible text,
content description, the local part of the resource id, typed text, key name,
intent component. Explicitly **not** matched against:

- `event_str`, which embeds the state hash and the tap coordinates
- the fully-qualified resource id, which carries the package name
- the widget class and the event type

That last list is not pedantry. Scored against the full blob, the token `clock`
appears in 65% of all actions in a Fossify Clock trace and `touch` in 77%, so
any step mentioning either matched almost anything.

Further constraints, each of which removed a measured class of false positive:

| rule | what it stops |
|---|---|
| steps match in order, within `MAX_STEP_GAP` actions | step 1 at action 5 and step 2 at action 600 "covering" a feature |
| the step must explain `MIN_LABEL_COVERAGE` of the widget's own label | "Open Settings" matching a paragraph that happens to contain the word |
| operation words must not conflict (`VERB_GROUPS`) | "Open the habit list" matching `Button "Add habit"` |
| a long-press step requires a `long_touch` event | "long-press the habit" satisfied by an ordinary tap |
| a step naming only ubiquitous controls cannot anchor a feature | "Tap Save" scanning the whole run and settling on any Save button |
| actions on the launcher or status bar are ignored | "Open Settings" matching the launcher's own Settings label |

And, for recall, steps are split on "or" into alternatives, spelling and
inflection are folded (`stem`: British "Customise colours" has to reach
`settings_color_customization_holder`), and the number of key words a long
descriptive step must hit is capped.

## Fairness between the two tools

Anything derived from a single run's trace can favour the tool that produced it,
so the parameters that matter are fixed from shared inputs:

- **Ground truth, matcher, arguments**: the same for both, by construction.
- **`--trace-only` is the default.** TestCube keeps a journal of its own
  per-feature verdicts. Left in, the judge's context reads `Journal: covered`
  for TestCube and `Journal: none` for LLMDroid, which tells it the answer for
  one tool only. The journal and the exploration bank are dropped.
- **Non-discriminating words come from the ground truth, not the trace.** A
  per-trace frequency filter was tried and rejected: "contact" covers 35% of
  TestCube's actions but 7% of LLMDroid's, so it silently forbade TestCube from
  matching steps LLMDroid was allowed to match.
- **Scoring is whole-trace, not per session.** How a run is cut into sessions is
  a property of the tool: TestCube's median session is 4 actions, LLMDroid's 14.
  Ordering plus `MAX_STEP_GAP` carries "these steps happened together" instead.

## Validation

The matcher is token-based, so its error rate was measured by hand rather than
assumed. Samples were drawn at random across apps and both tools; the figures
below are from samples drawn *after* the last change, so they are not the
samples the rules were tuned on.

- **Precision** (is a reported match real?): **20/25** on the final sample.
  Two earlier independent samples gave 24/30 and 24/30. Before this work it was
  17/40.
- **Recall** (is an unmatched step really absent?): **12/12** correctly
  unmatched on the final sample. An earlier sample found 5 misses in 14, all
  from three causes since fixed ("or" read as "and", no spelling normalisation,
  long steps needing too many words).

So roughly **one reported match in five is spurious**, and step coverage should
be read as an estimate with that error attached, not as an exact quantity.
Residual error modes, in descending frequency: outcome steps matched through
destination screen text; "Open the X tab" matching a widget named X elsewhere;
and a step matching a widget that shares its noun but names another operation.

### Why the local LLM judge is not used

`--matcher ai` with the local `qwen2.5vl:7b` returned `0 covered, 0 partial` for
16 of 17 apps. On fossifyclock GT001, "View the current time on the clock tab",
it was shown the Clock tab opened eight times plus
`touch TextView "Fri, 25 Sep" rid=clock_date` and answered `not_covered`,
"No current time or date displayed", with confidence 0.0. The evidence was
sufficient and the judge was not. No Gemini key is available in this
environment, so a stronger judge has not been tried; the `ai` path is left in
place for when one is.

## Independent check on the result

Step coverage and code coverage share no inputs: one is token matching over
`events/`, the other is AndroLog bytecode probes read from logcat. On the six
apps where both tools have both metrics, the two pick **the same winner on all
six** (LLMDroid on fossifyclock, fossifycontacts, fossifyvoicerecorder and
loophabits; TestCube on money and newpipe). That is the main reason to believe
step coverage is measuring exploration and not noise.

## Caveat worth stating in any writeup

Trace-based feature coverage can only see actions that name the widget they
touched, and the two tools differ there: `actions_with_widget` over
`total_actions` runs at 47-89% for LLMDroid and 19-81% for TestCube, because
TestCube issues many coordinate-only taps. LLMDroid also issues around five
times more actions per hour (729 against 143 on fossifyclock). Both are real
properties of the tools rather than scoring bugs, but a reader should be told,
and both counts are in every `report.json`.
