"""Write feature-coverage reports without changing existing TestCube output."""

import json
import os

from .models import STATUS_COVERED, STATUS_NOT_COVERED, STATUS_PARTIAL


STATUS_LABEL = {
    STATUS_COVERED: "COVERED",
    STATUS_PARTIAL: "PARTIAL",
    STATUS_NOT_COVERED: "NOT COVERED",
}


class ReportGenerator(object):
    def write(self, report, output_dir):
        if not os.path.isdir(output_dir):
            os.makedirs(output_dir)
        json_path = os.path.join(output_dir, "report.json")
        txt_path = os.path.join(output_dir, "report.txt")
        with open(json_path, "w", encoding="utf-8") as handle:
            json.dump(report.to_dict(), handle, indent=2)
            handle.write("\n")
        text = self.render_text(report)
        with open(txt_path, "w", encoding="utf-8") as handle:
            handle.write(text)
            if not text.endswith("\n"):
                handle.write("\n")
        return {"json": json_path, "txt": txt_path}

    def render_text(self, report):
        lines = [
            "========================================",
            "TestCube Feature Coverage Report",
            "========================================",
            "",
            "Application: %s" % report.application,
            "",
            "Total Features   : %d" % report.total_features,
            "Covered Features : %d" % report.covered_features,
            "Partial          : %d" % report.partial_features,
            "Uncovered        : %d" % report.uncovered_features,
            "",
            "Feature Coverage : %.2f%%" % report.coverage_percentage,
            "",
        ]
        formula = getattr(report, "coverage_formula", None)
        if formula:
            lines.append("Coverage formula : COVERED / Total")
        weighted = getattr(report, "weighted_coverage_percentage", None)
        if weighted is not None:
            lines.append(
                "Weighted Coverage: %.2f%%  (mean completion ratio; partial steps count)"
                % weighted
            )
        exercised = getattr(report, "exercised_features", None)
        if exercised is not None:
            lines.append(
                "Exercised        : %d  (covered %d + partial %d)"
                % (exercised, report.covered_features, report.partial_features)
            )
        if formula or weighted is not None or exercised is not None:
            lines.append("")
        gt_source = getattr(report, "ground_truth_source", None)
        if gt_source == "same_as_guide_list":
            lines.append("ground_truth_source: same_as_guide_list")
            lines.append("This number is guided-execution coverage (same list drove exploration).")
            lines.append("")
        elif gt_source:
            lines.append("ground_truth_source: %s" % gt_source)
            lines.append("")
        matcher_mode = getattr(report, "matcher_mode", None)
        if matcher_mode == "ai":
            lines.append("Matcher: VLM/Gemini semantic judge (not token overlap).")
            lines.append("")
        elif matcher_mode:
            lines.append("Matcher: %s" % matcher_mode)
            lines.append("")
        if getattr(report, "matcher_min_confidence", None) is not None and matcher_mode == "deterministic":
            lines.append("Matcher min-confidence: %.2f" % report.matcher_min_confidence)
            lines.append("")
        lines.extend([
            "----------------------------------------",
            "FEATURE DETAILS",
            "----------------------------------------",
            "",
        ])
        if not report.features:
            lines.append("(no features)")
        for item in report.features:
            lines.append("[%s] %s" % (item.id, item.name))
            lines.append("Status     : %s" % STATUS_LABEL.get(item.status, item.status.upper()))
            if item.test_cases:
                lines.append("Test Cases : %s" % ", ".join(item.test_cases))
            if item.status != STATUS_NOT_COVERED:
                lines.append("Confidence : %.2f" % item.confidence)
            if item.matcher:
                lines.append("Matcher    : %s" % item.matcher)
            if getattr(item, "completion_ratio", None) is not None:
                lines.append("Completion : %.0f%% of gold steps" % (100.0 * float(item.completion_ratio)))
            if item.evidence:
                lines.append("Evidence   :")
                for evidence in item.evidence[:8]:
                    lines.append("  - %s" % evidence)
            lines.append("")
        lines.extend([
            "----------------------------------------",
            "SUMMARY",
            "----------------------------------------",
            "",
            "%d / %d features covered" % (report.covered_features, report.total_features),
            "%d / %d features partial" % (report.partial_features, report.total_features),
            "Feature Coverage = COVERED / Total = %.2f%%" % report.coverage_percentage,
            "Weighted Feature Coverage = mean(completion_ratio) = %.2f%%"
            % (getattr(report, "weighted_coverage_percentage", 0.0) or 0.0),
            "",
            "Only fully COVERED features count toward Feature Coverage.",
            "Weighted coverage also credits PARTIAL gold-step fractions.",
            "Gold steps need not occur in listed order. Later exploration can",
            "complete an earlier partial feature. The coverage judge is an",
            "LLM/VLM semantic verdict, not string or token overlap.",
            "",
        ])
        if report.confusion:
            lines.extend([
                "----------------------------------------",
                "JOURNAL VS GROUND TRUTH",
                "----------------------------------------",
                "",
            ])
            inf = report.feature_inference or {}
            extracted_n = inf.get("extracted_count")
            gt_n = inf.get("ground_truth_count")
            ratio = inf.get("feature_completeness_ratio")
            if gt_n:
                lines.append(
                    "Extracted vs ground truth: %s / %s (completeness ratio %s)"
                    % (extracted_n if extracted_n is not None else "?", gt_n, ratio)
                )
                lines.append("")
            if inf.get("prf1_withheld"):
                lines.append(
                    "Feature-inference P/R/F1: withheld — ground truth and live "
                    "feature lists reuse the same IDs for different features. "
                    "Matching is by name similarity (not ID). Do not cite P/R/F1 "
                    "until a re-run confirms the confusion table below is name-aligned."
                )
                lines.append("")
            elif inf:
                lines.append(
                    "Feature-inference P/R/F1: %.2f / %.2f / %.2f (false not_present=%s)"
                    % (
                        inf.get("precision") or 0.0,
                        inf.get("recall") or 0.0,
                        inf.get("f1") or 0.0,
                        inf.get("false_not_present") or 0,
                    )
                )
                lines.append("")
            for row in report.confusion:
                journal_name = row.get("journal_name")
                if journal_name:
                    journal_bit = "%s %r (sim=%s, %s)" % (
                        row.get("journal_id") or "missing",
                        journal_name,
                        row.get("name_similarity"),
                        row.get("matched_by") or "none",
                    )
                else:
                    journal_bit = "missing (no name match)"
                lines.append(
                    "GT %s %r | journal=%s status=%s | offline=%s"
                    % (
                        row.get("ground_truth_id"),
                        row.get("ground_truth_name"),
                        journal_bit,
                        row.get("journal_status"),
                        row.get("offline_status"),
                    )
                )
            lines.append("")
        return "\n".join(lines)
