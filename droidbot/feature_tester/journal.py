"""Persist feature-test progress as JSON + Markdown so a run can resume."""

import json
import os
import re
from datetime import datetime


STATUS_PENDING = "pending"
STATUS_IN_PROGRESS = "in_progress"
STATUS_COVERED = "covered"
STATUS_PARTIAL = "partial"
STATUS_DROPPED = "dropped"
STATUS_NOT_PRESENT = "not_present"
STATUS_BLOCKED = "blocked"


class FeatureJournal(object):
    def __init__(self, output_dir, app_name=None):
        self.root = os.path.join(output_dir or ".", "feature_test")
        self.session_path = os.path.join(self.root, "session.json")
        self.log_path = os.path.join(self.root, "log.md")
        self.report_md_path = os.path.join(self.root, "report.md")
        self.report_json_path = os.path.join(self.root, "report.json")
        self.session = {
            "app": app_name or "unknown",
            "status": "running",
            "started_at": _now(),
            "updated_at": _now(),
            "current_feature_id": None,
            "features_path": None,
            "features": [],
        }

    def load_or_create(self, feature_payload):
        os.makedirs(self.root, exist_ok=True)
        if os.path.isfile(self.session_path):
            with open(self.session_path, "r", encoding="utf-8") as handle:
                saved = json.load(handle)
            if saved.get("features") and saved.get("status") == "running":
                self.session = saved
                self.session["status"] = "running"
                self.session["updated_at"] = _now()
                self._append_log("Resumed existing feature-test session.")
                self.save()
                return self.session
        payload = feature_payload or {}
        records = []
        for item in payload.get("features") or []:
            records.append({
                "id": item.get("id"),
                "name": item.get("name"),
                "description": item.get("description") or "",
                "actions": list(item.get("actions") or []),
                "valid_paths": item.get("valid_paths") or [],
                "keywords": item.get("keywords") or [],
                "nav_hints": item.get("nav_hints") or [],
                "source": item.get("source") or "readme",
                "status": STATUS_PENDING,
                "reason": "",
                "attempts": 0,
                "completed_actions": [],
                "remaining_actions": list(item.get("actions") or []),
                "steps": [],
            })
        self.session["app"] = payload.get("app") or self.session.get("app")
        self.session["features"] = records
        self.session["started_at"] = _now()
        if not os.path.isfile(self.log_path):
            with open(self.log_path, "w", encoding="utf-8") as handle:
                handle.write("# Feature test log: %s\n\n" % self.session["app"])
        self._append_log("Started with %d features." % len(records))
        self.save()
        return self.session

    def save(self):
        os.makedirs(self.root, exist_ok=True)
        self.session["updated_at"] = _now()
        with open(self.session_path, "w", encoding="utf-8") as handle:
            json.dump(self.session, handle, indent=2)
            handle.write("\n")

    def features(self):
        return self.session.get("features") or []

    def get_feature(self, feature_id):
        for item in self.features():
            if item.get("id") == feature_id:
                return item
        return None

    def next_pending(self):
        current_id = self.session.get("current_feature_id")
        if current_id:
            current = self.get_feature(current_id)
            if current and current.get("status") in (STATUS_PENDING, STATUS_IN_PROGRESS):
                return current
        for item in self.features():
            if item.get("status") in (STATUS_PENDING, STATUS_IN_PROGRESS):
                return item
        return None

    def start_feature(self, feature):
        feature["status"] = STATUS_IN_PROGRESS
        self.session["current_feature_id"] = feature["id"]
        self._append_log("## %s %s\n\nStarting feature." % (feature["id"], feature["name"]))
        self.save()

    def record_step(self, feature, step):
        feature.setdefault("steps", []).append(step)
        matched = step.get("matched_step")
        remaining = feature.get("remaining_actions") or []
        activity = (step.get("activity") or "").lower()
        event_str = step.get("event") or ""
        event_type = (step.get("event_type") or "").lower()
        if any(token in activity for token in ("documentsui", "picker")):
            if not _is_file_related_matched(matched, remaining):
                matched = ""
        target = _match_remaining_action(
            remaining, matched, event_str=event_str, event_type=event_type,
        )
        if target:
            completed = feature.setdefault("completed_actions", [])
            if target not in completed:
                completed.append(target)
            feature["remaining_actions"] = [
                action for action in remaining if action != target
            ]
            follow = _followup_submit_step(
                feature.get("remaining_actions") or [], event_str, event_type,
            )
            if follow:
                if follow not in completed:
                    completed.append(follow)
                feature["remaining_actions"] = [
                    action for action in feature["remaining_actions"] if action != follow
                ]
        self._append_log(
            "- **%s** `%s` → %s\n  - reason: %s\n  - matched: %s"
            % (
                step.get("decision") or "act",
                step.get("event") or "(none)",
                step.get("activity") or "",
                step.get("reason") or "",
                matched or "-",
            )
        )
        self.save()

    def finish_feature(self, feature, status, reason="", **extra):
        feature["status"] = status
        feature["reason"] = reason
        for key, value in extra.items():
            if value is not None:
                feature[key] = value
        if not feature.get("completion_source"):
            feature["completion_source"] = "executed"
        if self.session.get("current_feature_id") == feature.get("id"):
            self.session["current_feature_id"] = None
        self._append_log(
            "Finished **%s** as `%s`. %s\n" % (feature.get("id"), status, reason)
        )
        set_completion_ratio(feature)
        try:
            from .test_cases import write_feature_test_case
            write_feature_test_case(self.root, feature, source_run=self.root)
        except Exception:
            pass
        self.save()

    def credit_from_bank(self, bank):
        """Apply later actions from other features to incomplete gold steps."""
        upgraded = apply_bank_credit(self.features(), bank)
        for feature in upgraded:
            self._append_log(
                "Cross-feature credit: **%s** → %s (from %s)"
                % (
                    feature.get("id"),
                    feature.get("status"),
                    ", ".join(feature.get("credited_from") or []) or "later actions",
                )
            )
        if upgraded:
            self.save()
        return upgraded

    def append_features(self, items):
        """Merge extra features (e.g. action-inferred) into the live session."""
        existing_ids = {item.get("id") for item in self.features()}
        existing_names = set()
        for item in self.features():
            existing_names.update(re.findall(r"[a-z0-9]{4,}", (item.get("name") or "").lower()))
        added = []
        next_index = len(self.features()) + 1
        for item in items or []:
            name = (item.get("name") or "").strip()
            if not name:
                continue
            name_tokens = set(re.findall(r"[a-z0-9]{4,}", name.lower()))
            if name_tokens and name_tokens <= existing_names:
                self._append_log("Hybrid discovery discarded (deduped): %s" % name)
                continue
            feature_id = item.get("id")
            if not feature_id or feature_id in existing_ids:
                feature_id = "F%03d" % next_index
                next_index += 1
            record = {
                "id": feature_id,
                "name": name,
                "description": item.get("description") or "",
                "actions": list(item.get("actions") or []),
                "valid_paths": item.get("valid_paths") or [],
                "keywords": item.get("keywords") or [],
                "nav_hints": item.get("nav_hints") or [],
                "source": item.get("source") or "action_inferred",
                "status": STATUS_PENDING,
                "reason": "",
                "attempts": 0,
                "completed_actions": [],
                "remaining_actions": list(item.get("actions") or []),
                "steps": [],
            }
            self.session.setdefault("features", []).append(record)
            existing_ids.add(feature_id)
            existing_names.update(name_tokens)
            added.append(record)
            self._append_log("Hybrid discovery merged: %s as %s" % (name, feature_id))
        if added:
            self._append_log("Hybrid discovery added %d feature(s): %s" % (
                len(added),
                ", ".join(item.get("id") for item in added),
            ))
            self.save()
        return added

    def all_done(self):
        if self.next_pending() is not None:
            return False
        for item in self.features():
            if item.get("status") == STATUS_BLOCKED and not item.get("retry_attempted"):
                return False
        return True

    def complete_step(self, feature, step_text):
        if not feature or not step_text:
            return False
        remaining = list(feature.get("remaining_actions") or [])
        if step_text not in remaining:
            return False
        remaining.remove(step_text)
        feature["remaining_actions"] = remaining
        completed = list(feature.get("completed_actions") or [])
        if step_text not in completed:
            completed.append(step_text)
        feature["completed_actions"] = completed
        self._append_log("Verified step complete: %s" % step_text)
        self.save()
        return True

    def finalize(self, extra=None):
        extra = extra or {}
        bank = extra.get("exploration_bank")
        if bank is not None:
            from .step_bank import ExplorationBank
            if not hasattr(bank, "events_from_other_features"):
                bank = ExplorationBank(bank)
            self.credit_from_bank(bank)
            self.session["exploration_bank"] = bank.to_list()
        for item in self.features():
            set_completion_ratio(item)
        counts = {
            STATUS_COVERED: 0,
            STATUS_PARTIAL: 0,
            STATUS_DROPPED: 0,
            STATUS_NOT_PRESENT: 0,
            STATUS_IN_PROGRESS: 0,
            STATUS_PENDING: 0,
            STATUS_BLOCKED: 0,
        }
        for item in self.features():
            status = item.get("status") or STATUS_PENDING
            counts[status] = counts.get(status, 0) + 1
            if status == STATUS_IN_PROGRESS:
                if item.get("completed_actions"):
                    item["status"] = STATUS_PARTIAL
                    counts[STATUS_PARTIAL] += 1
                else:
                    item["status"] = STATUS_DROPPED
                    item["reason"] = item.get("reason") or "Run ended before the feature completed."
                    counts[STATUS_DROPPED] += 1
                counts[STATUS_IN_PROGRESS] -= 1
            elif status == STATUS_BLOCKED:
                item["status"] = STATUS_DROPPED
                item["blocked_still"] = True
                item["reason"] = item.get("reason") or "blocked_no_progress"
                counts[STATUS_DROPPED] += 1
                counts[STATUS_BLOCKED] -= 1
        self.session["status"] = "finished"
        self.session["counts"] = counts
        self.save()
        report = self._build_report(counts)
        self._attach_extensions(report, extra or {})
        try:
            from .test_cases import write_all_test_cases
            write_all_test_cases(self, source_run=self.root)
        except Exception as exc:
            self._append_log("Could not write replayable test cases: %s" % exc)
        with open(self.report_json_path, "w", encoding="utf-8") as handle:
            json.dump(report, handle, indent=2)
            handle.write("\n")
        with open(self.report_md_path, "w", encoding="utf-8") as handle:
            handle.write(self._render_markdown(report))
        self._append_log("Wrote final report: %s" % self.report_md_path)
        return report

    def _scored_features(self):
        """Features the run actually had a chance to test.

        An LLM-discovered feature that was never attempted is a proposal, not
        a tested capability; counting it only dilutes the denominator.
        Guide/README features always count, attempted or not.
        """
        kept = []
        for item in self.features():
            if (
                item.get("source") == "action_inferred"
                and not item.get("attempts")
                and not item.get("steps")
            ):
                continue
            kept.append(item)
        return kept or self.features()

    def _build_report(self, counts):
        scored = self._scored_features()
        total = len(scored)
        counts = {}
        for item in scored:
            counts[item.get("status")] = counts.get(item.get("status"), 0) + 1
        covered = counts.get(STATUS_COVERED, 0)
        return {
            "app": self.session.get("app"),
            "started_at": self.session.get("started_at"),
            "finished_at": _now(),
            "total_features": total,
            "covered": covered,
            "partial": counts.get(STATUS_PARTIAL, 0),
            "dropped": counts.get(STATUS_DROPPED, 0),
            "not_present": counts.get(STATUS_NOT_PRESENT, 0),
            "blocked": counts.get(STATUS_BLOCKED, 0),
            "coverage": (float(covered) / total) if total else 0.0,
            "weighted_coverage": _weighted_coverage(scored),
            "unscored_discovered": len(self.features()) - total,
            "feature_source": self.session.get("feature_source"),
            "guide_vs_readme": self.session.get("guide_vs_readme"),
            "guide_features_path": self.session.get("guide_features_path"),
            "features": self.features(),
            "session_path": self.session_path,
            "log_path": self.log_path,
            "exploration_bank": self.session.get("exploration_bank") or [],
        }

    def _attach_extensions(self, report, extra):
        total = report.get("total_features") or 0
        covered = report.get("covered") or 0
        report["online_coverage"] = {
            "covered": covered,
            "total": total,
            "coverage": report.get("coverage") or 0.0,
            "partial": report.get("partial") or 0,
            "weighted_coverage": report.get("weighted_coverage") or 0.0,
            "dropped": report.get("dropped") or 0,
            "not_present": report.get("not_present") or 0,
            "explanation": (
                "Feature coverage is fully covered / total. Weighted coverage is "
                "the mean per-feature completion ratio so partial gold steps count."
            ),
        }
        report["shared_flow_reuses"] = extra.get("shared_flow_reuses") or []
        try:
            from .run_stats import STATS
            report["run_cost"] = extra.get("run_cost") or STATS.to_dict()
            for state_str in STATS.sparse_screens:
                self._append_log(
                    "**sparse/ambiguous screen**: repeated low-confidence VLM "
                    "fallbacks on state `%s`" % state_str
                )
        except Exception:
            report["run_cost"] = extra.get("run_cost") or {}
        report["offline_coverage"] = extra.get("offline_coverage")
        if report["offline_coverage"] is None:
            report["offline_coverage"] = self._compute_offline_coverage()
        report["attempt_summary"] = self._attempt_summary()
        report["ground_truth_source"] = self._ground_truth_source_label()
        report["feature_source"] = self.session.get("feature_source")
        report["guide_vs_readme"] = self.session.get("guide_vs_readme")
        report["ground_truth_addendum"] = self._score_addendum()

    def _attempt_summary(self):
        attempted = 0
        never = 0
        recovered = 0
        blocked_still = 0
        for item in self.features():
            if item.get("source") == "action_inferred":
                continue
            steps = item.get("steps") or []
            attempts = int(item.get("attempts") or 0)
            if attempts or steps:
                attempted += 1
            else:
                never += 1
            if item.get("completed_on_retry"):
                recovered += 1
            if item.get("blocked_still") or (
                item.get("retry_attempted") and item.get("status") in (STATUS_DROPPED, STATUS_BLOCKED)
            ):
                blocked_still += 1
        return {
            "attempted": attempted,
            "never_attempted": never,
            "blocked_then_recovered": recovered,
            "blocked_still": blocked_still,
        }

    def _ground_truth_source_label(self):
        try:
            from .config import get_config
            from .guide import classify_ground_truth_source
            cfg = get_config()
            guide = self.session.get("guide_features_path") or cfg.guide_features_path
            gt = cfg.ground_truth_path
            return classify_ground_truth_source(guide, gt)
        except Exception:
            return None

    def _score_addendum(self):
        try:
            from .guide import discover_ground_truth_addendum, load_feature_json
            from droidbot.feature_eval.confusion import name_similarity
            apk = self.session.get("apk_path")
            path = discover_ground_truth_addendum(apk)
            if not path:
                stem = None
                guide = self.session.get("guide_features_path") or ""
                if "feature" in guide.replace("\\", "/"):
                    parts = os.path.abspath(guide).replace("\\", "/").split("/")
                    if "feature" in parts:
                        idx = parts.index("feature")
                        if idx + 1 < len(parts):
                            stem = parts[idx + 1]
                if stem:
                    candidate = os.path.join(os.getcwd(), "feature", stem, "ground_truth_addendum.json")
                    if os.path.isfile(candidate):
                        path = candidate
            payload = load_feature_json(path) if path else None
            if not payload:
                return None
            matched = []
            missed = []
            journal = self.features()
            for item in payload.get("features") or []:
                best, best_sim = None, 0.0
                for live in journal:
                    sim = name_similarity(item, live)
                    if sim > best_sim:
                        best, best_sim = live, sim
                if best is not None and best_sim >= 0.3:
                    matched.append({
                        "addendum_name": item.get("name"),
                        "journal_id": best.get("id"),
                        "journal_name": best.get("name"),
                        "journal_source": best.get("source"),
                        "name_similarity": round(best_sim, 3),
                    })
                else:
                    missed.append(item.get("name"))
            return {
                "path": path,
                "total": len(payload.get("features") or []),
                "matched": len(matched),
                "pairs": matched,
                "missed": missed,
                "explanation": (
                    "Independent features not in the guide list. "
                    "matched = live journal features with name similarity >= 0.3 "
                    "(hybrid discovery is the expected source)."
                ),
            }
        except Exception as exc:
            return {"error": str(exc)}

    def _resolve_coverage_features_path(self):
        from .config import get_config
        cfg = get_config()
        candidates = [
            cfg.ground_truth_path,
            self.session.get("features_path"),
        ]
        guide = self.session.get("guide_features_path") or cfg.guide_features_path or ""
        if guide:
            candidates.append(os.path.join(os.path.dirname(guide), "ground_truth.json"))
        results_dir = os.path.dirname(self.root)
        for path in candidates:
            if path and os.path.isfile(path):
                return path
        live = os.path.join(self.root, "features.json")
        if os.path.isfile(live):
            return live
        return None

    def _compute_offline_coverage(self):
        try:
            gt = self._resolve_coverage_features_path()
            if not gt:
                return {"error": "no ground_truth.json or live features.json to score"}
            results_dir = os.path.dirname(self.root)
            from droidbot.feature_eval.evaluator import evaluate_feature_coverage
            offline, _paths = evaluate_feature_coverage(
                results_dir=results_dir,
                features_path=gt,
                use_llm=True,
                matcher_mode="ai",
                output_dir=os.path.join(results_dir, "feature_coverage"),
                journal_features=self.features(),
            )
            payload = offline.to_dict()
            return {
                "covered": payload.get("covered_features"),
                "total": payload.get("total_features"),
                "coverage": payload.get("coverage"),
                "partial": payload.get("partial_features"),
                "exercised": payload.get("exercised_features"),
                "coverage_formula": payload.get("coverage_formula"),
                "weighted_coverage": payload.get("weighted_coverage"),
                "weighted_coverage_percentage": payload.get("weighted_coverage_percentage"),
                "explanation": (
                    "Offline coverage is an LLM/VLM semantic judge vs ground-truth "
                    "JSON. Feature Coverage = COVERED / Total. Weighted Coverage = "
                    "mean(completion_ratio) so partial gold steps still count. "
                    "Step order is not required. Later exploration can complete "
                    "an earlier partial feature."
                ),
                "features": payload.get("features"),
                "confusion": payload.get("confusion"),
                "feature_inference": payload.get("feature_inference"),
            }
        except Exception as exc:
            return {"error": str(exc)}

    def _render_markdown(self, report):
        lines = [
            "# Feature test report: %s" % report.get("app"),
            "",
            "- Started: %s" % report.get("started_at"),
            "- Finished: %s" % report.get("finished_at"),
            "- Features: %s" % report.get("total_features"),
            "- Covered: %s" % report.get("covered"),
            "- Partial: %s" % report.get("partial"),
            "- Dropped (blocked / stuck): %s" % report.get("dropped"),
            "- Not present in the app: %s" % report.get("not_present"),
            "- Weighted coverage: %.0f%% (mean completion ratio; the headline number)"
            % (100.0 * (report.get("weighted_coverage") or 0.0)),
            "- Coverage: %.0f%% (features with every guide step matched)"
            % (100.0 * (report.get("coverage") or 0.0)),
            "- Stop reason: %s" % (self.session.get("stop_reason") or "not recorded"),
        ]
        gt_source = report.get("ground_truth_source")
        if gt_source == "same_as_guide_list":
            lines.append(
                "- Scoring: **guided-execution coverage** "
                "(ground_truth_source=same_as_guide_list — the scorer uses the same list that drove exploration)."
            )
        elif gt_source == "independent_labeled_set":
            lines.append(
                "- Scoring: **feature coverage** vs an independent labeled set "
                "(ground_truth_source=independent_labeled_set)."
            )
        elif gt_source:
            lines.append("- ground_truth_source: %s" % gt_source)
        summary = report.get("attempt_summary") or {}
        if summary:
            lines.extend([
                "",
                "## Attempt summary",
                "",
                "- Attempted: %s" % summary.get("attempted"),
                "- Never attempted: %s" % summary.get("never_attempted"),
                "- Blocked then recovered on retry: %s" % summary.get("blocked_then_recovered"),
                "- Blocked still: %s" % summary.get("blocked_still"),
            ])
        diff = report.get("guide_vs_readme")
        if isinstance(diff, dict) and (diff.get("guide_only") or diff.get("readme_only") or diff.get("both")):
            lines.extend([
                "",
                "## Guide vs README-extracted",
                "",
                "- Guide features: %s" % diff.get("guide_count"),
                "- README-extracted features: %s" % diff.get("readme_count"),
                "- In both: %s" % len(diff.get("both") or []),
                "- Guide-only: %s" % len(diff.get("guide_only") or []),
                "- README-only: %s" % len(diff.get("readme_only") or []),
            ])
            for row in (diff.get("guide_only") or [])[:12]:
                lines.append("  - guide-only: %s %s" % (row.get("id"), row.get("name")))
            for row in (diff.get("readme_only") or [])[:12]:
                lines.append("  - README-only: %s %s" % (row.get("id"), row.get("name")))
        addendum = report.get("ground_truth_addendum")
        if isinstance(addendum, dict) and addendum.get("total"):
            lines.extend([
                "",
                "## Independent ground-truth addendum",
                "",
                "- Features not in the guide list: %s" % addendum.get("total"),
                "- Matched in this run: %s" % addendum.get("matched"),
                "- Missed: %s" % len(addendum.get("missed") or []),
            ])
            if addendum.get("explanation"):
                lines.append("- %s" % addendum.get("explanation"))
        cost = report.get("run_cost") or {}
        fills = cost.get("field_fills") or {}
        if fills:
            lines.extend([
                "",
                "## Text-field resolution",
                "",
                "- Filled via credential.txt: %s" % fills.get("credential", 0),
                "- Filled via VLM/Gemini: %s" % fills.get("vlm", 0),
                "- Unresolved: %s" % fills.get("unresolved", 0),
            ])
        online = report.get("online_coverage") or {}
        offline = report.get("offline_coverage")
        lines.extend([
            "- Online coverage: %.0f%% (%s/%s) — live journal self-report (covered / extracted features)."
            % (
                100.0 * (online.get("coverage") or 0.0),
                online.get("covered") if online.get("covered") is not None else report.get("covered"),
                online.get("total") if online.get("total") is not None else report.get("total_features"),
            ),
        ])
        if isinstance(offline, dict) and offline.get("coverage") is not None:
            partial = offline.get("partial") or 0
            covered = offline.get("covered")
            total = offline.get("total")
            weighted = offline.get("weighted_coverage")
            if weighted is None:
                weighted = offline.get("weighted_coverage_percentage")
                if weighted is not None:
                    weighted = float(weighted) / 100.0
            lines.append(
                "- Offline coverage: %.0f%% (%s covered / %s; %s partial) — "
                "LLM judge vs ground-truth JSON, not the live journal."
                % (
                    100.0 * (offline.get("coverage") or 0.0),
                    covered,
                    total,
                    partial,
                )
            )
            if weighted is not None:
                lines.append(
                    "- Offline weighted coverage: %.0f%% (mean completion ratio)."
                    % (100.0 * float(weighted))
                )
        elif isinstance(offline, dict) and offline.get("error"):
            lines.append("- Offline coverage: unavailable (%s)" % offline.get("error"))
        else:
            lines.append("- Offline coverage: not computed (no ground-truth JSON).")
        lines.extend([
            "",
            "## Findings",
            "",
        ])
        for item in report.get("features") or []:
            lines.append("### %s %s" % (item.get("id"), item.get("name")))
            lines.append("")
            lines.append("- Status: **%s**" % item.get("status"))
            if item.get("reason"):
                lines.append("- Reason: %s" % item.get("reason"))
            if item.get("completion_source") and item.get("completion_source") != "executed":
                lines.append("- Completion source: %s" % item.get("completion_source"))
            if item.get("source") and item.get("source") != "readme":
                lines.append("- Feature source: %s" % item.get("source"))
            completed = item.get("completed_actions") or []
            remaining = item.get("remaining_actions") or []
            if completed:
                lines.append("- Completed steps: %s" % "; ".join(completed))
            if remaining:
                lines.append("- Remaining steps: %s" % "; ".join(remaining))
            if item.get("completion_ratio") is not None:
                lines.append("- Completion ratio: %.2f" % float(item.get("completion_ratio") or 0.0))
            credited = item.get("credited_from") or []
            if credited:
                lines.append("- Credited from later features: %s" % ", ".join(credited))
            steps = item.get("steps") or []
            if steps:
                lines.append("- Actions taken: %d" % len(steps))
                for step in steps[-8:]:
                    lines.append(
                        "  - %s: %s (%s)"
                        % (
                            step.get("decision"),
                            step.get("event") or step.get("reason"),
                            step.get("source") or "",
                        )
                    )
            lines.append("")
        lines.extend(_render_shared_flows(report))
        lines.append("See `session.json` and `log.md` in this folder for the full trace.")
        lines.append("")
        return "\n".join(lines)

    def _append_log(self, text):
        os.makedirs(self.root, exist_ok=True)
        with open(self.log_path, "a", encoding="utf-8") as handle:
            handle.write("%s  \n%s\n\n" % (_now(), text))


def _now():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def _render_shared_flows(report):
    reuses = report.get("shared_flow_reuses") or []
    lines = [
        "## Shared flows detected",
        "",
    ]
    if not reuses:
        lines.append("None this run.")
        lines.append("")
        return lines
    saved = sum(item.get("actions_skipped") or 0 for item in reuses)
    lines.append(
        "%d reuse(s); %d action(s) skipped by not re-executing a known terminal flow."
        % (len(reuses), saved)
    )
    lines.append("")
    for item in reuses:
        lines.append(
            "- `%s` reused `%s` (from %s), skipped %s action(s)"
            % (
                item.get("feature_id"),
                item.get("reference_chain"),
                item.get("reference_feature"),
                item.get("actions_skipped"),
            )
        )
    lines.append("")
    return lines


def apply_bank_credit(features, bank):
    """Credit leftover steps of earlier features from later exploration.

    Mutates ``features``. Returns those whose status changed.
    """
    if bank is None:
        return []
    if not hasattr(bank, "events_from_other_features"):
        from .step_bank import ExplorationBank
        bank = ExplorationBank(bank)
    upgraded = []
    for feature in features or []:
        status = feature.get("status") or STATUS_PENDING
        if status in (STATUS_PENDING, STATUS_IN_PROGRESS, STATUS_COVERED):
            set_completion_ratio(feature)
            continue
        remaining = list(feature.get("remaining_actions") or [])
        gold = list(feature.get("actions") or [])
        completed = list(feature.get("completed_actions") or [])
        if not remaining and gold:
            remaining = [item for item in gold if item not in completed]
        fid = feature.get("id")
        for entry in bank.events_from_other_features(fid):
            if not remaining:
                break
            target = _match_remaining_action(
                remaining,
                entry.get("matched_step") or entry.get("event") or "",
                event_str=entry.get("blob") or entry.get("event") or "",
                event_type=entry.get("event_type") or "",
            )
            if not target:
                continue
            if target not in completed:
                completed.append(target)
            remaining = [item for item in remaining if item != target]
            credited = feature.setdefault("credited_from", [])
            src = entry.get("feature_id")
            if src and src not in credited:
                credited.append(src)
            steps = feature.setdefault("credited_steps", [])
            steps.append({
                "from_feature": src,
                "matched_step": target,
                "event": entry.get("event") or "",
            })
        feature["completed_actions"] = completed
        feature["remaining_actions"] = remaining
        old_status = status
        if gold and not remaining and completed:
            feature["status"] = STATUS_COVERED
            feature["completion_source"] = "cross_feature"
            extra = " Later exploration completed remaining steps."
            if extra not in (feature.get("reason") or ""):
                feature["reason"] = (feature.get("reason") or "").rstrip() + extra
        elif completed and old_status in (
            STATUS_DROPPED, STATUS_NOT_PRESENT, STATUS_BLOCKED,
        ):
            feature["status"] = STATUS_PARTIAL
        set_completion_ratio(feature)
        if feature.get("status") != old_status:
            upgraded.append(feature)
    return upgraded


def set_completion_ratio(feature):
    if not feature:
        return 0.0
    if (feature.get("status") or "") == STATUS_COVERED:
        feature["completion_ratio"] = 1.0
        return 1.0
    gold = list(feature.get("actions") or [])
    done = list(feature.get("completed_actions") or [])
    if not gold:
        ratio = 1.0 if (feature.get("status") or "") == STATUS_COVERED else 0.0
        feature["completion_ratio"] = ratio
        return ratio
    ratio = min(1.0, float(len(done)) / float(len(gold)))
    feature["completion_ratio"] = ratio
    return ratio


def _weighted_coverage(features):
    items = list(features or [])
    if not items:
        return 0.0
    total = 0.0
    for item in items:
        total += float(item.get("completion_ratio") if item.get("completion_ratio") is not None else set_completion_ratio(item))
    return total / float(len(items))


def _match_remaining_action(remaining, matched, event_str="", event_type=""):
    if not matched:
        return None
    needle = matched.strip().lower()
    if not needle or len(needle) < 2:
        return None
    if "expected step" in needle or needle in ("empty", "or empty", "none"):
        return None
    if "bottom navigation" in needle or re.search(r"tab \d+ of \d+", needle):
        return None
    needle_tokens = _action_tokens(needle)
    if not needle_tokens:
        # Every token was a stopword ("Tap OK" -> {}). Fall back to normalized
        # containment so short confirm steps are not permanently unmatchable.
        bare = re.sub(r"[^a-z0-9]+", " ", needle).strip()
        if not bare:
            return None
        for action in remaining:
            hay = action.strip().lower()
            hay_bare = re.sub(r"[^a-z0-9]+", " ", hay).strip()
            if bare and (bare == hay_bare or bare in hay_bare):
                event_l = ("%s %s" % (event_str or "", event_type or "")).lower()
                if not _event_compatible_with_step(
                    hay,
                    "set_text" in event_l or "settext" in event_l,
                    "scroll" in event_l,
                    "bottom navigation" in event_l or "nav tab" in event_l,
                ):
                    continue
                return action
        return None
    event_l = ("%s %s" % (event_str or "", event_type or "")).lower()
    is_set_text = "set_text" in event_l or "settext" in event_l
    is_scroll = "scroll" in event_l
    is_nav_tab = "bottom navigation" in event_l or "nav tab" in event_l
    for action in remaining:
        hay = action.strip().lower()
        if hay == needle:
            if not _event_compatible_with_step(hay, is_set_text, is_scroll, is_nav_tab):
                continue
            return action
        hay_tokens = _action_tokens(hay)
        overlap = needle_tokens & hay_tokens
        if not overlap:
            continue
        # Containment, not Jaccard: a short needle ("Tap Save") should still
        # match a long gold step that contains it. A flat "two shared tokens"
        # cutoff made short steps effectively unmatchable and held the live
        # match rate at ~5%.
        ratio = len(overlap) / float(min(len(needle_tokens), len(hay_tokens)))
        if ratio >= _step_match_threshold():
            if not _event_compatible_with_step(hay, is_set_text, is_scroll, is_nav_tab):
                continue
            return action
    return None


def _step_match_threshold():
    try:
        from .config import get_config
        return float(get_config().step_match_threshold)
    except Exception:
        return 0.5


def _event_compatible_with_step(step, is_set_text, is_scroll, is_nav_tab):
    typing = any(word in step for word in ("enter", "type", "input", "query"))
    if typing and not is_set_text:
        return False
    if is_set_text and not typing:
        return False
    if is_scroll and not any(word in step for word in ("scroll", "browse", "swipe")):
        return False
    if is_nav_tab and any(word in step for word in (
        "select", "create", "enter", "play", "adjust", "save", "edit", "sync", "manage", "bar", "field",
    )):
        return False
    return True


def _followup_submit_step(remaining, event_str, event_type):
    """Do not auto-complete a Search/submit tap after typing.

    Flutter and many search bars still need an explicit Search/IME tap;
    skipping it marks Search covered with no results, so Play never starts.
    """
    return None


def _action_tokens(text):
    # "button"/"icon" were dropped from the stop set: they are weak but not
    # noise, and removing them emptied short steps such as "Tap Save button".
    stop = {
        "the", "a", "an", "to", "for", "or", "and", "of", "on", "in", "if",
        "shown", "tap", "step",
    }
    return {word for word in re.findall(r"[a-z0-9]{2,}", text or "") if word not in stop}


def _is_file_related_matched(matched, remaining):
    blob = ("%s %s" % (matched or "", " ".join(remaining or []))).lower()
    return any(token in blob for token in (
        "file", "database", "import", "export", "csv", "qif", "mmb",
        "save", "filename", "open database", "create database",
    ))
