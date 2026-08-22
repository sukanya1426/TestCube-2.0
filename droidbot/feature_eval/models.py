"""Data objects for feature-coverage evaluation."""

from dataclasses import dataclass, field
from typing import Dict, List, Optional


STATUS_COVERED = "covered"
STATUS_PARTIAL = "partial"
STATUS_NOT_COVERED = "not_covered"

STATUS_RANK = {
    STATUS_NOT_COVERED: 0,
    STATUS_PARTIAL: 1,
    STATUS_COVERED: 2,
}


@dataclass
class Feature:
    """One ground-truth application feature.

    `id` is unique within one feature list. Live README extraction and
    hand-authored ground truth may reuse F001/F002 for different features;
    evaluation matches by name/description, not by ID.

    `actions` is the default expected action chain.
    `valid_paths` lists alternative chains; any one fully executed path
    is enough to mark the feature COVERED.
    """

    id: str
    name: str
    description: str = ""
    actions: List[str] = field(default_factory=list)
    valid_paths: List[List[str]] = field(default_factory=list)
    keywords: List[str] = field(default_factory=list)

    def paths(self) -> List[List[str]]:
        if self.valid_paths:
            return [list(path) for path in self.valid_paths if path]
        if self.actions:
            return [list(self.actions)]
        if self.name:
            return [[self.name]]
        return []


@dataclass
class ObservedAction:
    """One executed TestCube event, reconstructed from events/*.json.

    Screens and widgets are evidence. This object represents an action
    that was actually sent, not a widget that merely appeared in a dump.
    """

    index: int
    tag: str
    test_case: str
    event_type: str
    event_str: str = ""
    view_text: Optional[str] = None
    content_description: Optional[str] = None
    resource_id: Optional[str] = None
    view_class: Optional[str] = None
    text_input: Optional[str] = None
    key_name: Optional[str] = None
    intent: Optional[str] = None
    start_state: Optional[str] = None
    stop_state: Optional[str] = None
    start_activity: Optional[str] = None
    stop_activity: Optional[str] = None
    stop_texts: List[str] = field(default_factory=list)
    screenshot: Optional[str] = None
    state_changed: bool = False

    def summary(self) -> str:
        parts = [self.event_type]
        if self.view_class:
            parts.append(self.view_class.split(".")[-1])
        label = self.content_description or self.view_text
        if label:
            parts.append('"%s"' % _clip(label, 60))
        if self.resource_id:
            parts.append("rid=%s" % self.resource_id.split("/")[-1])
        if self.text_input:
            parts.append("text=%s" % _clip(self.text_input, 40))
        if self.key_name:
            parts.append("key=%s" % self.key_name)
        if self.intent:
            parts.append("intent=%s" % _clip(self.intent, 80))
        if self.stop_activity:
            parts.append("activity=%s" % self.stop_activity.split(".")[-1])
        if self.state_changed:
            parts.append("state_changed")
        return " ".join(parts)

    def token_blob(self) -> str:
        # Destination-state texts are intentionally excluded. A label that
        # merely appears on screen is not evidence that this action exercised
        # that feature. Outcome matching uses stop_texts separately.
        pieces = [
            self.event_type,
            self.event_str or "",
            self.view_text or "",
            self.content_description or "",
            self.resource_id or "",
            self.view_class or "",
            self.text_input or "",
            self.key_name or "",
            self.intent or "",
            _short_activity(self.start_activity),
            _short_activity(self.stop_activity),
        ]
        return " ".join(pieces)


@dataclass
class TestCaseTrace:
    """A contiguous executed session, usually bounded by kill_app / start."""

    id: str
    actions: List[ObservedAction] = field(default_factory=list)


@dataclass
class ExecutionTrace:
    app_package: Optional[str] = None
    app_name: Optional[str] = None
    actions: List[ObservedAction] = field(default_factory=list)
    test_cases: List[TestCaseTrace] = field(default_factory=list)
    states: Dict[str, dict] = field(default_factory=dict)


@dataclass
class FeatureResult:
    id: str
    name: str
    status: str
    test_cases: List[str] = field(default_factory=list)
    confidence: float = 0.0
    evidence: List[str] = field(default_factory=list)
    matched_path: Optional[List[str]] = None
    matcher: str = "deterministic"
    completion_ratio: Optional[float] = None


@dataclass
class CoverageReport:
    application: str
    total_features: int
    covered_features: int
    uncovered_features: int
    partial_features: int
    coverage: float
    coverage_percentage: float
    features: List[FeatureResult] = field(default_factory=list)
    results_dir: Optional[str] = None
    readme_path: Optional[str] = None
    features_path: Optional[str] = None

    confusion: Optional[list] = None
    feature_inference: Optional[dict] = None
    matcher_min_confidence: Optional[float] = None
    matcher_mode: Optional[str] = None
    ground_truth_source: Optional[str] = None
    exercised_features: Optional[int] = None
    coverage_formula: Optional[str] = None
    weighted_coverage: Optional[float] = None
    weighted_coverage_percentage: Optional[float] = None
    weighted_coverage_formula: Optional[str] = None

    def to_dict(self) -> dict:
        payload = {
            "application": self.application,
            "total_features": self.total_features,
            "covered_features": self.covered_features,
            "uncovered_features": self.uncovered_features,
            "partial_features": self.partial_features,
            "coverage": self.coverage,
            "coverage_percentage": self.coverage_percentage,
            "results_dir": self.results_dir,
            "readme_path": self.readme_path,
            "features_path": self.features_path,
            "features": [
                {
                    "id": item.id,
                    "name": item.name,
                    "status": item.status,
                    "test_cases": item.test_cases,
                    "confidence": item.confidence,
                    "evidence": item.evidence,
                    "matched_path": item.matched_path,
                    "matcher": item.matcher,
                    "completion_ratio": item.completion_ratio,
                }
                for item in self.features
            ],
        }
        if self.confusion is not None:
            payload["confusion"] = self.confusion
        if self.feature_inference is not None:
            payload["feature_inference"] = self.feature_inference
        if self.matcher_min_confidence is not None:
            payload["matcher_min_confidence"] = self.matcher_min_confidence
        if self.matcher_mode is not None:
            payload["matcher_mode"] = self.matcher_mode
        if self.ground_truth_source is not None:
            payload["ground_truth_source"] = self.ground_truth_source
        if self.exercised_features is not None:
            payload["exercised_features"] = self.exercised_features
        if self.coverage_formula is not None:
            payload["coverage_formula"] = self.coverage_formula
        if self.weighted_coverage is not None:
            payload["weighted_coverage"] = self.weighted_coverage
        if self.weighted_coverage_percentage is not None:
            payload["weighted_coverage_percentage"] = self.weighted_coverage_percentage
        if self.weighted_coverage_formula is not None:
            payload["weighted_coverage_formula"] = self.weighted_coverage_formula
        return payload


def better_status(left: str, right: str) -> str:
    if STATUS_RANK.get(right, 0) > STATUS_RANK.get(left, 0):
        return right
    return left


def _clip(text, length):
    text = " ".join(str(text).split())
    if len(text) <= length:
        return text
    return text[: length - 3] + "..."


def _short_activity(name):
    if not name:
        return ""
    return name.replace("/", ".").split(".")[-1]
