"""Load the manually prepared ground-truth feature list."""

import json
import os

from .models import Feature


class FeatureLoaderError(ValueError):
    pass


class FeatureLoader(object):
    """Load features.json. Feature discovery is out of scope."""

    def load(self, path):
        if not path or not os.path.isfile(path):
            raise FeatureLoaderError("Feature list not found: %s" % path)
        with open(path, "r", encoding="utf-8") as handle:
            try:
                payload = json.load(handle)
            except json.JSONDecodeError as exc:
                raise FeatureLoaderError("Invalid JSON in %s: %s" % (path, exc))

        if isinstance(payload, list):
            payload = {"app": None, "features": payload}

        if not isinstance(payload, dict):
            raise FeatureLoaderError("Feature list must be a JSON object or array.")

        raw_features = payload.get("features")
        if raw_features is None:
            raise FeatureLoaderError("Feature list is missing the 'features' array.")
        if not isinstance(raw_features, list):
            raise FeatureLoaderError("'features' must be an array.")

        features = []
        seen_ids = set()
        for index, item in enumerate(raw_features):
            feature = self._parse_feature(item, index)
            if feature.id in seen_ids:
                raise FeatureLoaderError("Duplicate feature id: %s" % feature.id)
            seen_ids.add(feature.id)
            features.append(feature)

        app_name = payload.get("app") or payload.get("application")
        package = payload.get("package")
        return {
            "app": app_name,
            "package": package,
            "features": features,
        }

    def _parse_feature(self, item, index):
        if not isinstance(item, dict):
            raise FeatureLoaderError("Feature at index %d is not an object." % index)
        feature_id = item.get("id")
        if not feature_id:
            raise FeatureLoaderError("Feature at index %d is missing a stable 'id'." % index)
        name = item.get("name") or str(feature_id)
        actions = item.get("actions") or []
        if not isinstance(actions, list):
            raise FeatureLoaderError("Feature %s: 'actions' must be a list of strings." % feature_id)
        valid_paths = item.get("valid_paths") or []
        if not isinstance(valid_paths, list):
            raise FeatureLoaderError("Feature %s: 'valid_paths' must be a list of lists." % feature_id)
        parsed_paths = []
        for path in valid_paths:
            if not isinstance(path, list):
                raise FeatureLoaderError("Feature %s: each valid path must be a list." % feature_id)
            parsed_paths.append([str(step) for step in path])
        keywords = item.get("keywords") or []
        if not isinstance(keywords, list):
            keywords = [str(keywords)]
        return Feature(
            id=str(feature_id),
            name=str(name),
            description=str(item.get("description") or ""),
            actions=[str(step) for step in actions],
            valid_paths=parsed_paths,
            keywords=[str(word) for word in keywords],
        )
