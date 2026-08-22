"""Infer a ground-truth feature list from an application README via Gemini."""

import json
import os

from .llm_matcher import extract_json


class FeatureExtractor(object):
    def extract(self, readme_path, app_name=None, output_path=None,
                allow_numbered_spec=True):
        if not readme_path or not os.path.isfile(readme_path):
            raise ValueError("README not found: %s" % readme_path)
        with open(readme_path, "r", encoding="utf-8") as handle:
            readme = handle.read()
        from droidbot.GeminiAI import GeminiAi
        payload = None
        extra_notes = ""
        try:
            from droidbot.feature_tester.specs import extra_spec_texts, parse_numbered_features
            numbered = None
            if allow_numbered_spec:
                numbered = parse_numbered_features(readme, app_name=app_name)
            if numbered and numbered.get("features"):
                payload = numbered
            else:
                chunks = [readme]
                for path, body in extra_spec_texts(readme_path=readme_path):
                    chunks.append("\n\nAdditional notes from %s:\n%s" % (path, body))
                extra_notes = "\n".join(chunks)
        except Exception:
            extra_notes = readme
        if not payload or not payload.get("features"):
            try:
                payload = GeminiAi.extract_features_from_readme(
                    extra_notes or readme, app_name=app_name,
                )
            except Exception as exc:
                print("Gemini feature extract failed, using local README parser: %s" % exc)
        payload = _drop_features_not_in_readme(payload, extra_notes or readme)
        if not payload or not payload.get("features"):
            from droidbot.feature_tester.fallback_features import extract_features_locally
            payload = extract_features_locally(
                extra_notes or readme,
                app_name=app_name,
                allow_numbered_spec=allow_numbered_spec,
            )
        payload = _drop_features_not_in_readme(payload, extra_notes or readme) or payload
        try:
            from droidbot.feature_tester.granularity import refine_granularity
            payload = refine_granularity(payload, app_name=app_name)
            flags = payload.get("granularity_flags") or []
            if flags:
                print("Granularity review (candidate splits): %s" % ", ".join(flags))
        except Exception as exc:
            print("Granularity check skipped: %s" % exc)
        if output_path:
            directory = os.path.dirname(output_path)
            if directory and not os.path.isdir(directory):
                os.makedirs(directory)
            with open(output_path, "w", encoding="utf-8") as handle:
                json.dump(payload, handle, indent=2)
                handle.write("\n")
        return payload


def _drop_features_not_in_readme(payload, readme):
    if not payload or not payload.get("features"):
        return payload
    if payload.get("source") == "numbered_spec":
        return payload
    blob = (readme or "").lower()
    kept = []
    for item in payload["features"]:
        name = (item.get("name") or "").lower()
        if any(token in name for token in ("first-run", "onboard", "setup", "get started", "welcome")):
            kept.append(item)
            continue
        required = None
        if "login" in name or "sign in" in name or "sign-up" in name or "sign up" in name:
            required = ("log in", "login", "sign in", "oauth")
        elif "game" in name:
            required = ("game", "quiz")
        elif "report" in name:
            required = ("report",)
        elif "import" in name:
            required = ("import", "qif", "csv")
        elif "export" in name:
            required = ("export",)
        if required and not any(token in blob for token in required):
            print("Dropping inferred feature not supported by README: %s" % item.get("name"))
            continue
        kept.append(item)
    if len(kept) < 2:
        return None
    for index, item in enumerate(kept, start=1):
        item["id"] = "F%03d" % index
    payload = dict(payload)
    payload["features"] = kept
    return payload
