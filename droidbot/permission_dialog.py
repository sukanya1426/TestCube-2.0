"""Find and grant Android runtime permission dialogs.

System permission UI is often an overlay: the app activity stays in the
foreground, so activity-name checks miss it. The Allow *button* must be
tapped — not the message text that also starts with "Allow".
"""

import re
import time

from .input_event import TouchEvent


def normalize_label(text):
    raw = (text or "").lower()
    return raw.replace("’", "'").replace("‘", "'").replace("`", "'")


DENY_LABELS = (
    "don't allow",
    "dont allow",
    "deny",
    "don't send",
    "no thanks",
    "reject",
    "cancel",
)

ALLOW_EXACT = (
    "allow",
    "allow all",
    "allow always",
    "always allow",
    "while using the app",
    "only this time",
    "this time only",
    "always",
    "allow access",
)

ALLOW_ID_HINTS = (
    "permission_allow_button",
    "permission_allow_foreground_only_button",
    "permission_allow_always_button",
    "permission_allow_one_time_button",
    "permission_allow_all_button",
    "permission_allow",
)

PERMISSION_PACKAGES = (
    "permissioncontroller",
    "packageinstaller",
    "com.android.permissioncontroller",
    "com.google.android.permissioncontroller",
)

COMMON_RUNTIME_PERMS = (
    "android.permission.READ_EXTERNAL_STORAGE",
    "android.permission.WRITE_EXTERNAL_STORAGE",
    "android.permission.READ_MEDIA_AUDIO",
    "android.permission.READ_MEDIA_IMAGES",
    "android.permission.READ_MEDIA_VIDEO",
    "android.permission.READ_MEDIA_VISUAL_USER_SELECTED",
    "android.permission.POST_NOTIFICATIONS",
    "android.permission.RECORD_AUDIO",
    "android.permission.CAMERA",
    "android.permission.ACCESS_FINE_LOCATION",
    "android.permission.ACCESS_COARSE_LOCATION",
    "android.permission.READ_PHONE_STATE",
    "android.permission.BLUETOOTH_CONNECT",
    "android.permission.BLUETOOTH_SCAN",
    "android.permission.NEARBY_WIFI_DEVICES",
)


def is_permission_screen(state):
    if not state or not getattr(state, "views", None):
        return False
    activity = (getattr(state, "foreground_activity", None) or "").lower()
    if any(token in activity for token in PERMISSION_PACKAGES):
        return True
    for view in state.views:
        package = (view.get("package") or "").lower()
        resource_id = (view.get("resource_id") or "").lower()
        label = normalize_label(view.get("text") or view.get("content_description"))
        if any(token in package for token in PERMISSION_PACKAGES):
            return True
        if "permission_" in resource_id:
            return True
        if "allow " in label and " to " in label:
            return True
    return False


def is_deny_label(label):
    text = normalize_label(label)
    return any(token in text for token in DENY_LABELS)


def pick_allow_view(state):
    """Return the clickable Allow view, never the dialog title or Deny."""
    if not state or not getattr(state, "views", None):
        return None
    ranked = []
    for view in state.views:
        if not view.get("enabled") or view.get("visible") is False:
            continue
        resource_id = (view.get("resource_id") or "").lower()
        text = normalize_label(view.get("text"))
        desc = normalize_label(view.get("content_description"))
        label = (text or desc).strip()
        if is_deny_label(label) or "permission_deny" in resource_id:
            continue
        score = 0
        if any(hint in resource_id for hint in ALLOW_ID_HINTS):
            score = 100
        elif label in ALLOW_EXACT and view.get("clickable"):
            score = 90
        elif view.get("clickable") and label.startswith("allow") and len(label) <= 24:
            score = 80
        elif view.get("clickable") and label in ("while using the app", "only this time"):
            score = 90
        if score:
            ranked.append((score, view))
    if not ranked:
        return None
    ranked.sort(key=lambda item: -item[0])
    return ranked[0][1]


def make_allow_event(state):
    view = pick_allow_view(state)
    if not view:
        return None
    event = TouchEvent(view=view)
    event.skip_oracle = True
    return event


def grant_runtime_permissions(device, app):
    """Best-effort pm grant so the system dialog does not block exploration."""
    if device is None or app is None:
        return
    package = app.get_package_name()
    if not package:
        return
    perms = list(COMMON_RUNTIME_PERMS)
    requested = _requested_permissions(device, package)
    for perm in requested:
        if perm not in perms:
            perms.append(perm)
    granted = 0
    for perm in perms:
        try:
            device.adb.shell("pm grant %s %s" % (package, perm))
            granted += 1
        except Exception:
            continue
    print("Granted %d runtime permission slot(s) to %s" % (granted, package))


def wait_for_permission_dialog(device, seconds=1.5):
    time.sleep(seconds)
    return device.get_current_state() if device else None


def _requested_permissions(device, package):
    try:
        dump = device.adb.shell("dumpsys package %s" % package) or ""
    except Exception:
        return []
    found = []
    for match in re.finditer(r"(android\.permission\.[A-Z0-9_]+)", dump):
        perm = match.group(1)
        if perm not in found:
            found.append(perm)
    return found[:40]
