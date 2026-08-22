"""Cross-feature shared-flow memory (action-chain registry)."""

import json
import os
import re


NON_IDEMPOTENT_LABELS = (
    "pay", "payment", "confirm", "submit order", "place order",
    "checkout", "buy now", "purchase", "redeem", "apply coupon",
    "delete", "remove account", "uninstall", "factory reset",
)


def chain_status(raw):
    """Map a journal feature status onto a chain terminal status."""
    value = (raw or "").lower().replace("-", "_")
    if value in ("covered", "completed"):
        return "completed"
    if value == "partial":
        return "partial"
    if value in ("in_progress", "pending"):
        return "in_progress"
    return "abandoned"


def is_non_idempotent(signature="", label=""):
    blob = ("%s %s" % (signature or "", label or "")).lower()
    return any(token in blob for token in NON_IDEMPOTENT_LABELS)


def lcs_length(left, right):
    if not left or not right:
        return 0
    prev = [0] * (len(right) + 1)
    for item in left:
        cur = [0]
        for j, other in enumerate(right):
            if item == other:
                cur.append(prev[j] + 1)
            else:
                cur.append(max(cur[-1], prev[j + 1]))
        prev = cur
    return prev[-1]


def similarity(left, right):
    if not left or not right:
        return 0.0
    shared = lcs_length(left, right)
    return float(shared) / float(max(len(left), len(right)))


def contiguous_prefix_match(current, prior, min_len=3, threshold=0.7):
    """True if the tail of `current` matches a contiguous window of `prior`."""
    if len(current) < min_len or len(prior) < min_len:
        return 0
    window = current[-min_len:]
    best = 0
    for start in range(0, len(prior) - min_len + 1):
        chunk = prior[start:start + min_len]
        same = sum(1 for a, b in zip(window, chunk) if a == b)
        ratio = float(same) / float(min_len)
        if ratio >= threshold:
            best = max(best, min_len)
            extra = 0
            while start + min_len + extra < len(prior) and min_len + extra < len(current):
                if current[-(min_len + extra + 1)] != prior[start + min_len + extra]:
                    break
                extra += 1
            best = max(best, min_len + extra)
    return best


class ChainMemory(object):
    def __init__(self):
        self.chains = []
        self.executed_non_idempotent = set()
        self.reuses = []

    def register(self, feature, signatures, terminal_state="", status=None):
        if not signatures:
            return None
        if status is not None:
            raw = status
        else:
            raw = (feature or {}).get("status") or "completed"
        entry = {
            "id": "C%03d" % (len(self.chains) + 1),
            "feature_id": (feature or {}).get("id"),
            "status": chain_status(raw),
            "signature": list(signatures),
            "terminal_state": terminal_state or "",
        }
        self.chains.append(entry)
        return entry

    def match_tail(self, current_sigs, k=3, threshold=0.7):
        best = None
        for chain in self.chains:
            if chain.get("status") not in ("completed", "covered"):
                continue
            length = contiguous_prefix_match(
                current_sigs, chain.get("signature") or [], min_len=k, threshold=threshold,
            )
            if length >= k and (best is None or length > best[0]):
                best = (length, chain)
        if best is None:
            return None
        return {"length": best[0], "chain": best[1]}

    def remaining_contained(self, remaining, prior_feature, prior_sigs=None):
        prior = set((prior_feature or {}).get("completed_actions") or [])
        prior.update((prior_feature or {}).get("actions") or [])
        blob = " ".join(str(item).lower() for item in prior)
        if prior_sigs:
            blob = blob + " " + " ".join(str(item).lower() for item in prior_sigs)
        if not remaining:
            return True
        hits = 0
        for action in remaining:
            tokens = set(re.findall(r"[a-z0-9]{3,}", (action or "").lower()))
            if tokens and any(token in blob for token in tokens):
                hits += 1
        return hits >= max(1, int(0.6 * len(remaining)))

    def note_reuse(self, feature_id, chain, skipped):
        self.reuses.append({
            "feature_id": feature_id,
            "reference_chain": (chain or {}).get("id"),
            "reference_feature": (chain or {}).get("feature_id"),
            "actions_skipped": skipped,
        })

    def save(self, path):
        folder = os.path.dirname(path)
        if folder:
            os.makedirs(folder, exist_ok=True)
        with open(path, "w", encoding="utf-8") as handle:
            json.dump({"chains": self.chains, "reuses": self.reuses}, handle, indent=2)
            handle.write("\n")


def decide_shared_flow(memory, current_sigs, remaining, prior_feature_lookup,
                       k=3, threshold=0.7):
    """Return reuse / diverge / None for the current feature trajectory."""
    match = memory.match_tail(current_sigs, k=k, threshold=threshold)
    if not match:
        return None
    chain = match["chain"]
    prior = None
    if callable(prior_feature_lookup):
        prior = prior_feature_lookup(chain.get("feature_id"))
    if memory.remaining_contained(remaining, prior, chain.get("signature")):
        return {
            "action": "reuse",
            "chain": chain,
            "skipped": len(remaining or []),
            "match_length": match["length"],
        }
    return {
        "action": "diverge",
        "chain": chain,
        "skipped": 0,
        "match_length": match["length"],
    }
