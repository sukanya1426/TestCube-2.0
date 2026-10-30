# Fixes applied to the LLMDroid baseline

The vendored baseline at `compare/LLMDroid/LLMDroid-Droidbot/` was modified. This
file records what changed, why, and what it means for the comparison, because a
paper that reports numbers from a modified baseline has to say so.

Every change here is a **liveness or parity fix**: it lets LLMDroid spend the
budget it was given, or gives it the same model configuration TestCube gets.
None of them touch how it chooses what to explore — the policy
(`utg_greedy_search_policy`), the prompts (`droidbot/policy/prompt.py`), the
state clustering and the coverage-growth gate are all untouched.

## The symptom

Four of fifteen LLMDroid runs produced far fewer actions than the other eleven:

| app | events span | actions | the other eleven |
|---|---|---|---|
| appmanager | 22.1 min | 190 | 59.6–60.0 min, 520–766 actions |
| money | 9.9 min | 138 | |
| newpipe | 10.0 min | 130 | |
| radiodroid | 9.6 min | 90 | |

Those four are also four of TestCube's largest wins, so the margin rested on
them. Dropping them took the code-coverage margin from +1.78 pp (9/15 wins) to
+1.53 pp with a **negative** median (5/11 wins), and the feature-coverage
confidence interval from [+1.25, +9.08] to [−1.54, +7.98]. The comparison could
not be published until the cause was known.

## Cause 1 — money and newpipe were given 600 s, not 3600 s

Not a bug. Both runs are from 2026-09-17, before the one-hour budget was
standardised, and the log shows the budget the runner actually passed:

```
[05:38:29] $ .../run_llmdroid.py --app money ... --timeout 600 ...
2026-09-17 05:48:32 | INFO | input_manager:start:227 - Finish sending events (138 actions in 600s)
```

TestCube's side of those two apps was 600 s as well, so the pair was internally
fair — but it cannot sit in a table whose other thirteen rows are 3600 s. The
fix is to re-run them. The original runs are preserved under
`output/experiment/_600s_baseline/llmdroid/`.

## Cause 2 — a failed question deadlocked the agent thread (appmanager)

```
2026-10-18 04:53:52 | ERROR | llm_agent:__work_loop:161 - Child thread error:
    'NoneType' object has no attribute 'has_untested_function'
2026-10-18 05:44:45 | ERROR | run_budget:_watch:121 - Run is still going 300s past
    its 3600s budget; writing reports and killing the process.
```

Between those two lines, 51 minutes, LLMDroid logged `Question remains: 2` every
three seconds and sent no events at all. It was alive and idle, not stopped
early — which is why the *events* spanned 22 minutes while the *process* used
its whole hour.

Three faults compounded:

1. `UTG.find_cluster_by_id()` returns `None` for a state id the model invented,
   and `__ask_for_overview` stored that `None` straight into
   `__top_valued_cluster`. The next overview call then invoked
   `has_untested_function()` on it. A 7B local model inventing a cluster id is
   routine; with GPT-4o, as in the original paper, it is presumably rare.
2. `__work_loop` decremented `__question_remained` only on the success path, so
   the raised exception left the counter above zero permanently and
   `wait_until_queue_empty()` spun for the rest of the budget.
3. `utg_based_policy` waits on `Future.result()` with no timeout, so a handler
   that raises before `set_result()` blocks the main thread just as effectively.

Fixes, in `droidbot/policy/llm_agent.py`:

- A `None` from `find_cluster_by_id` leaves the slot as it was and logs the
  hallucinated id, instead of being stored. Both `has_untested_function()` call
  sites and the `original_first5` loop also skip `None` defensively.
- `__question_remained` is decremented on the failure path too.
- A new `__resolve_pending_future()` settles a pending future with the value the
  policy already treats as "no guidance" (`(-1, func)`) or "no event" (`None`),
  so one lost question costs one question, not the run.

## Cause 3 — an unbounded retry on unparseable JSON (radiodroid)

```
2026-10-12 05:26:12 | WARNING | llm_agent:__get_response:432 - Exception(Expecting
    value: line 128 column 21 (char 3301)) occurred when transferring llm's
    response to json, try to get response again
```

repeated until the watchdog killed the run at 3900 s. `__get_response` ended
with `return self.__get_response(prompt)` — unbounded recursion — and the model
call uses `temperature=0`. A reply the model truncates mid-JSON is therefore
reproduced byte for byte on every retry: a guaranteed infinite loop, not a flaky
one. RadioDroid's station list has ~50 rows, each contributing a `"more
options": N` entry, so its "Function List" answer is the longest in the suite.

Fix: the retry is bounded by `LLMAgent.JSON_RETRIES = 3`. Past the cap the
question is abandoned with a `ValueError`, which cause 2's fixes now account for
and recover from.

## Cause 4 — LLMDroid was running at half TestCube's context window

The underlying reason radiodroid's answer was truncated at all.

Both tools use the same local model (`qwen2.5vl:7b` on Ollama), but by different
routes. TestCube posts to the native `/api/chat` with
`options.num_ctx = 8192` (`droidbot/local_vlm.py`). LLMDroid used the
OpenAI-compatible `/v1/chat/completions`, which **silently ignores `options`**,
so the model loaded at Ollama's own default of 4096. Measured with `ollama ps`
on this machine, Ollama 0.32.14:

```
/v1 + options num_ctx=8192   ->  CONTEXT 4096
/v1, no options              ->  CONTEXT 4096
/api/chat + options          ->  CONTEXT 8192
```

LLMDroid had half the context, and the baseline's longest prompts are the ones
that overflowed. This is a fairness defect in the baseline's disfavour, and it
would be the first thing a reviewer asked about.

Fix: `LLMAgent.__chat()` posts to `/api/chat` with `num_ctx = LLMAgent.NUM_CTX`
(8192, same env override as TestCube) when the configured `BaseUrl` is an Ollama
endpoint. Any other base URL keeps the original OpenAI client path untouched, so
an OpenAI-backed run behaves exactly as before. The server default is left
alone — the parity lives in the repo, where it can be audited, rather than in
machine state.

## What this means for the comparison

The four affected pairs were re-run at 3600 s on the fixed baseline. The eleven
unaffected pairs are untouched and need no re-run: their LLMDroid runs already
used 59.6–60.0 min and 520–766 actions, and none of the three bugs fired in
them.

Reporting requirement for the paper: state that the baseline was patched for
liveness and model-configuration parity, that the patches are in the repository,
and that its exploration policy and prompts are unmodified. The honest framing
is that the published LLMDroid implementation is not robust against a 7B local
model's malformed output — which is a finding about deploying it locally, not a
defect the original authors' GPT-4o results would have shown.
