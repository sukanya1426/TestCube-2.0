"""Compute unique-feature coverage.

Feature Coverage = COVERED / Total (only fully covered features).
Weighted Feature Coverage = mean(completion_ratio) so partial gold
steps still contribute (0, k/n, or 1).
"""

from .models import STATUS_COVERED, STATUS_NOT_COVERED, STATUS_PARTIAL, CoverageReport

COVERAGE_FORMULA = "covered / total"
WEIGHTED_COVERAGE_FORMULA = "mean(completion_ratio)"


def completion_ratio_for(item):
    if getattr(item, "completion_ratio", None) is not None:
        try:
            return max(0.0, min(1.0, float(item.completion_ratio)))
        except (TypeError, ValueError):
            pass
    if item.status == STATUS_COVERED:
        return 1.0
    if item.status == STATUS_PARTIAL:
        return 0.5
    return 0.0


class CoverageCalculator(object):
    def calculate(self, application, feature_results, results_dir=None,
                  readme_path=None, features_path=None):
        total = len(feature_results)
        covered = sum(1 for item in feature_results if item.status == STATUS_COVERED)
        partial = sum(1 for item in feature_results if item.status == STATUS_PARTIAL)
        uncovered = sum(1 for item in feature_results if item.status == STATUS_NOT_COVERED)
        exercised = covered + partial
        coverage = (float(covered) / float(total)) if total else 0.0
        weighted = (
            sum(completion_ratio_for(item) for item in feature_results) / float(total)
            if total else 0.0
        )
        return CoverageReport(
            application=application or "unknown",
            total_features=total,
            covered_features=covered,
            uncovered_features=uncovered,
            partial_features=partial,
            coverage=coverage,
            coverage_percentage=round(coverage * 100.0, 2),
            features=list(feature_results),
            results_dir=results_dir,
            readme_path=readme_path,
            features_path=features_path,
            exercised_features=exercised,
            coverage_formula=COVERAGE_FORMULA,
            weighted_coverage=weighted,
            weighted_coverage_percentage=round(weighted * 100.0, 2),
            weighted_coverage_formula=WEIGHTED_COVERAGE_FORMULA,
        )
