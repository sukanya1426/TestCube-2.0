"""
Feature-level coverage evaluation for TestCube 2.0.

This package is an evaluator. It consumes existing TestCube output
(events/, states/, utg.js) and a manually prepared features.json.
It does not change exploration, Gemini text input, or the screenshot oracle.

The unit of evaluation is an application feature, not a clicked widget
or a visited screen. UI discovery alone is not coverage. The default
judge is a VLM/Gemini semantic scorer; token overlap is ablation-only.
"""

from .evaluator import evaluate_feature_coverage
from .models import STATUS_COVERED, STATUS_NOT_COVERED, STATUS_PARTIAL

__all__ = [
    "evaluate_feature_coverage",
    "STATUS_COVERED",
    "STATUS_PARTIAL",
    "STATUS_NOT_COVERED",
]
