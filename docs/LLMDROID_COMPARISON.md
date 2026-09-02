# TestCube vs. LLMDroid — architecture critique and what to borrow

This is an honest internal critique, written after running raw LLMDroid-Droidbot
as a baseline (see [`LLMDROID_SETUP.md`](../LLMDROID_SETUP.md) and
[`compare/LLMDroid/LLMDroid-Droidbot/TESTCUBE_INTEGRATION.md`](../compare/LLMDroid/LLMDroid-Droidbot/TESTCUBE_INTEGRATION.md)).
The observation that triggered it: LLMDroid felt **smoother and faster** in
practice. This document explains *why*, at the architecture level, or ideas
worth adapting, and what must **not** change about our own purpose.

**Ground rule for anything that comes out of this document**: nothing here
means "copy LLMDroid's code." We are publishing a paper about our own
architecture. Every idea below has to be re-derived and reimplemented in our
own terms, for our own purpose (feature-attribution, not raw exploration
throughput), and cited as inspiration from LLMDroid's published design where
it applies. `LLMDroid-Fastbot/` ships a `LICENSE`; `LLMDroid-Droidbot/` (the
variant we compared against) does not carry one in this checkout — treat that
as a reason for extra caution, not permission. Verbatim reuse of their code
in a paper's artifact is a problem regardless of license.

---

## 1. Why LLMDroid feels faster — architecture-level reasons

These are traced from source, not guessed (file:line references point at
`compare/LLMDroid/LLMDroid-Droidbot/`).

### 1.1 One narrow LLM choke point, not a heuristic-plus-fallback stack

LLMDroid routes every model call through a single class, `LLMAgent`
(`droidbot/policy/llm_agent.py`). One method, `__get_response`
(lines 383-431), does the entire job: build a prompt, call
`chat.completions.create(temperature=0, ...)` once, extract the substring
between the first `{` and the last `}`, `json.loads` it, retry up to 5 times
on failure. There is no separate heuristic-scoring pass ahead of it for the
guided path — when LLMDroid decides to ask, it asks once and takes the
answer.

TestCube's equivalent is spread across `droidbot/feature_tester/advisor.py`
(1345 lines) and `policy.py` (2499 lines). `advisor.decide()` runs
`_heuristic()` first (a large scored-candidate system —
`_score_event`, `_looks_like_fab`, `_looks_like_error_label`,
`_looks_like_result_row`, `_player_step_intent`, and a dozen more
special-purpose predicates), and only escalates to `_ask_llm()` /
`_visual_ground()` when heuristic confidence is low or the tester is stuck.
That escalation path itself has two branches (vision-preferred local VLM vs.
Gemini fallback, `advisor.py:803-826`).

**Why this matters for speed**: the heuristic layer is not free — it's a lot
of Python evaluated on every single state, and its size is a standing
maintenance and generality cost (see §3). LLMDroid's design accepts one
model round-trip per guided decision and keeps everything else in the fast
exploration path instead (§1.2).

### 1.2 Cheap exploration is the default; the LLM is the exception, not the norm

LLMDroid's default policy chain is `dfs_greedy` →
`UtgGreedySearchPolicy` → `UtgBasedInputPolicy`
(`droidbot/policy/utg_greedy_search_policy.py`,
`droidbot/policy/utg_based_policy.py:50-51`). In EXPLORE mode it falls
straight through to vanilla droidbot's own `generate_event_based_on_utg()`
(`utg_based_policy.py:423-458`) — no model call at all. The LLM is invoked
only when the policy's mode machine decides to switch to `ASK_GUIDANCE` /
`TEST_FUNCTION`, which (absent `-code_coverage time`) is driven by *code
coverage plateauing*, not by every state transition.

TestCube's advisor is consulted on effectively every decision inside a
feature (heuristic first, VLM/LLM as fallback) because the tester needs an
answer specific to the *current feature's remaining steps* at every step —
there's no equivalent "just wander for free until something interesting
happens" mode, because wandering doesn't advance a specific feature's
attribution.

### 1.3 Text-only state representation vs. screenshot + vision model

LLMDroid never sends an image. `DeviceState.to_dict()`
(`droidbot/desc/device_state.py:65-78`) serializes the UI as an HTML-ish
string (`to_html()`), and every prompt in `llm_agent.py` is built from that
string. A text-only chat completion against a 7B-class model is cheap and
fast compared to a vision-capable model processing a screenshot.

TestCube's fallback path (`advisor._visual_ground`, `advisor._ask_llm`) sends
screenshot bytes to a VLM (local Ollama `qwen2.5vl:7b` preferred,
`local_vlm.py`; Gemini multimodal otherwise). Vision inference is inherently
slower and more variable than text-only inference on comparable hardware,
and it's *necessary* for us in a way it isn't for LLMDroid — see §2.

### 1.4 State clustering avoids redundant work

LLMDroid groups structurally similar states via `StateCluster`
(`droidbot/desc/` — clustering keyed off content/activity), which limits how
often the same effective screen re-triggers exploration or a fresh LLM
decision. TestCube has no equivalent deduplication layer; `step_bank.py`
credits *completed steps* across features after the fact, but nothing
prevents the advisor from re-heuristicing (and potentially re-VLM-ing) two
states that are visually/structurally near-identical.

### 1.5 A structured mode machine narrows what each call has to reason about

LLMDroid's `QuestionMode` enum (OVERVIEW → GUIDE → TEST_FUNCTION →
REANALYSIS) gives each LLM call a single, narrow job: OVERVIEW summarizes
what's on screen once per state cluster, GUIDE picks a widget, TEST_FUNCTION
confirms an action actually satisfied the goal it was sent to satisfy. Each
prompt is short and its expected output shape is fixed, which is a big part
of why a small model at `temperature=0` with 5 retries is reliable enough to
run unattended.

TestCube's `advisor.decide()` is closer to "figure out everything about this
step in one call" when it does escalate to the model — feature context,
remaining steps, screen content, and the tap/type/scroll decision all in one
prompt. That's a heavier ask per call.

---

## 2. What must not change — this is not a speed contest

LLMDroid optimizes a fundamentally different objective: **maximize code
coverage growth**, using whatever exploration gets there fastest. It has no
concept of "feature," no ground truth, no notion of partial credit, and (per
`TESTCUBE_INTEGRATION.md`) produces no journal we can score online at all —
we could only bolt an *offline* judge onto its raw `states/`/`events/`
output. Speed and smoothness are real advantages, but they come from having
a simpler job.

TestCube's actual contribution is attribution, not raw exploration
throughput:

- **Feature-guided testing, not undirected exploration.** One feature at a
  time, from a fresh process, matched against a specific remaining-steps
  list (`docs/PROJECT.md` §"Restart the app between features"). LLMDroid has
  no analogue — it doesn't know what a "feature" is.
- **Cross-feature step-bank credit** (`step_bank.py`,
  `journal.apply_bank_credit`) — crediting a stuck feature when a later
  feature happens to complete its remaining steps. Nothing in LLMDroid does
  this; it isn't scored against anything, so there's nothing to credit.
- **Two honest, separated metrics** — `covered/total` and
  `mean(completion_ratio)`, deliberately not blending partial into "covered."
  LLMDroid has neither concept.
- **Online vs. offline separation** with different ID namespaces matched by
  name, not index — this is what let us score LLMDroid's raw output at all
  (offline only, since it has no live guided journal).

Any idea adopted from LLMDroid below has to slot into this attribution
layer, not replace it. If an efficiency change makes the tester faster but
degrades feature attribution accuracy, it's a net loss for our purpose even
if it would be a net win for LLMDroid's.

---

## 3. Self-critique — problems with our own architecture, independent of LLMDroid

Worth stating plainly, since a paper reviewer familiar with LLMDroid-style
single-agent designs will likely ask this directly:

- **Heuristic sprawl.** `advisor.py`'s dozen-plus `_looks_like_*` /
  `_is_*` predicates (`_looks_like_fab`, `_looks_like_error_label`,
  `_looks_like_result_row`, `_looks_like_search_placeholder`, …) read like
  they accreted per-app-observed edge cases even though the project's own
  rule is "no per-app hardcoding." The mechanism is generic (no app names in
  the code), but the *sheer number* of narrow pattern-match predicates is a
  smell worth auditing — some are likely dead weight on apps unlike the ones
  they were written against, and each one is a maintenance and latency cost
  paid on every state.
- **No state deduplication.** Every state the tester lands on re-runs the
  full heuristic stack from scratch, even if it's visited (or something
  near-identical to) that state before in the same feature attempt. This is
  the most directly transferable LLMDroid idea (§4.1).
- **VLM calls are more frequent than they need to be.** The heuristic-first
  design already gates *some* VLM usage, but there's no equivalent of
  LLMDroid's "just DFS for free until coverage plateaus" mode — every step
  inside a feature attempt goes through the heuristic (and potentially VLM)
  path, because every step needs to be attributed to that feature's steps.
  That coupling is arguably too tight — cheap, undirected navigation moves
  (e.g., dismissing a dialog, backing out of a dead end) don't need a
  feature-aware decision at all.
- **Restart cost is real and currently un-costed.** Force-stop + cold start
  between every feature is deliberate and necessary for attribution
  cleanliness (§2), but it's also a fixed wall-clock tax LLMDroid never
  pays, since it never segments by feature. Worth explicitly measuring
  (time-per-feature attributable to restart vs. exploration) so the paper
  can name this tradeoff rather than let a reviewer discover it.

---

## 4. Concrete ideas to adapt (reimplemented, not copied)

Ranked by how directly they map onto TestCube's existing modules.

### 4.1 State deduplication / clustering before the heuristic stack runs

**Idea, not LLMDroid's code**: hash or fingerprint each `DeviceState` (e.g.
activity + a normalized structural digest of visible widgets, independent of
LLMDroid's own `StateCluster` implementation) and cache the advisor's most
recent decision for states that collide with something already handled in
the current feature attempt. Skip straight to "already tried this, try
something untried" instead of re-running `_heuristic()` (and possibly a VLM
call) on a state that's structurally identical to one seen three steps ago.

- **Fits into**: `advisor.py`'s existing loop/backtrack handling
  (`backtrack` mechanism in `docs/PROJECT.md`) — this would make backtrack
  detection cheaper and more precise, not replace it.
- **Keeps our purpose intact**: still per-feature, still restarts between
  features; the cache would need to be scoped per-feature-attempt (or
  explicitly reset on restart) so it can't leak state across the restart
  boundary that §2's attribution model depends on.

### 4.2 A narrower, single-shot escalation call instead of a monolithic advisor prompt

**Idea**: when the heuristic layer *does* escalate, split "what should I do
next" into the same kind of narrow, single-purpose call LLMDroid uses
(§1.5) — e.g., a small OVERVIEW-style call to summarize what's on screen
relative to the current feature's remaining steps, separate from the GUIDE
call that picks the actual widget/action. Keep `temperature=0` and a small
fixed retry budget with the same "extract between first `{` and last `}`"
robustness trick LLMDroid uses in `__get_response` (this pattern is a
generic prompt-engineering idiom, not proprietary — safe to reimplement).

- **Fits into**: `advisor._ask_llm` / `_visual_ground` as an internal
  refactor; the feature-context/remaining-steps machinery around it doesn't
  change.
- **Keeps our purpose intact**: the model is still being asked "does this
  advance *this* feature's remaining steps," which LLMDroid's prompts never
  ask at all.

### 4.3 Gate expensive (vision) calls behind a cheaper progress signal, the way LLMDroid gates the LLM behind code-coverage growth

**Idea**: LLMDroid's mode switch triggers on code-coverage plateauing
(or elapsed time, with `-code_coverage time`). Our natural analogue isn't
code coverage — it's **remaining-steps stagnation**, which `stagnation` (in
`docs/PROJECT.md`'s "Older mechanisms" table) already tracks. Formalize it
as the explicit gate for the *vision* fallback specifically: use the
existing heuristic for ordinary navigation, and reserve the local VLM /
Gemini call for the case where remaining-steps progress has genuinely
stalled for N steps — rather than any time heuristic confidence dips below
threshold. This is a tightening of an existing mechanism, not new
machinery.

- **Fits into**: `advisor.decide()`'s escalation condition and the existing
  `stagnation` mechanism.
- **Keeps our purpose intact**: this reduces VLM call volume without
  touching what a covered/partial/dropped verdict means.

### 4.4 Audit and prune the `_looks_like_*` heuristic set

Not really "borrowed from LLMDroid" so much as motivated by the contrast —
LLMDroid gets comparable or better guided-decision quality out of *one*
narrow model call per decision, with no bespoke pattern library at all. That
suggests our large heuristic set should be measured (which predicates
actually fire and help, across all three test apps) rather than assumed
necessary, and either justified with data or trimmed. This is an
architecture-hygiene action item, not a feature.

### 4.5 Consider a cheap "free navigation" sub-mode for non-attributable moves

**Idea**: give the policy an explicit, LLM-free fast path for moves that
don't need feature attribution at all — dismissing a permission dialog,
backing out of an obvious dead end, closing a keyboard — mirroring the
spirit of LLMDroid's free EXPLORE mode, but scoped narrowly enough that it
never risks taking a step that should count toward a feature's remaining
steps. Anything ambiguous still goes through the full heuristic/advisor
path.

- **Keeps our purpose intact**: only applies where there is provably no
  feature-attribution content in the decision (dialog dismissal etc.) — the
  step_bank / journal never even needs to see these moves.

---

## 5. Summary for the paper

- LLMDroid is faster because it does less per decision (one narrow text-only
  call, gated behind cheap free exploration) and because it isn't trying to
  attribute every action to a specific feature.
- TestCube's slower path is largely the direct cost of the thing LLMDroid
  doesn't do at all: per-feature attribution, restart hygiene, cross-feature
  credit, and two honest coverage metrics instead of a raw code-coverage
  number.
- The adoptable ideas (§4) are efficiency techniques — state dedup, narrower
  prompts, tighter escalation gating, free-navigation fast path — that can
  cut latency and heuristic sprawl **without touching** what "covered,"
  "partial," or "weighted coverage" mean. That distinction (efficiency layer
  vs. attribution semantics) is the framing to use when writing this up: we
  are not converging toward LLMDroid's design, we are borrowing its
  performance techniques underneath an unchanged, and LLMDroid-absent,
  feature-coverage contribution.
