#TestCube-2.0/droidbot/custom_input_event.py
from .input_event import TouchEvent, UIEvent, SetTextEvent
from .image_comparer import ImageComparer


CTA_TAP_PHRASES = (
    "let's get started",
    "lets get started",
    "get started",
    "continue",
    "next",
    "got it",
)


def _normalize_label(text):
    return (text or "").lower().replace("’", "'").replace("‘", "'")


def _tap_xy(view, x, y):
    """Tap the visual CTA, not the center of a Flutter merged semantics node."""
    if x and y:
        return x, y
    if not view:
        return UIEvent.get_xy(x=x, y=y, view=view)
    bounds = view.get("bounds")
    if not bounds:
        return UIEvent.get_xy(x=x, y=y, view=view)
    left, top = bounds[0]
    right, bottom = bounds[1]
    height = bottom - top
    cx = (left + right) / 2.0
    cy = (top + bottom) / 2.0
    label = _normalize_label("%s %s" % (
        view.get("content_description") or "",
        view.get("text") or "",
    ))
    if height > 600 and any(phrase in label for phrase in CTA_TAP_PHRASES):
        # Full-screen Flutter node: the button sits at the bottom of a
        # centered card (~74% down), not at the screen center or bottom.
        cy = top + height * 0.74
        print("Tapping lower CTA on large Flutter view at (%s, %s) label=%s" % (cx, cy, label[:80]))
    return cx, cy


def _tap_oracle_enabled():
    """Whether to run the screenshot-comparison oracle around each Button tap."""
    import os
    return os.environ.get("TESTCUBE_TAP_ORACLE", "") not in ("", "0", "false", "False")


class CustomTouchEvent(TouchEvent):

    def send(self, device):
        x, y = _tap_xy(self.view, self.x, self.y)
        view_class = ""
        if self.view:
            view_class = self.view.get("class") or ""

        from .GeminiAI import GeminiAi
        # The oracle only prints what it finds: the tap is sent either way and
        # the comparison never reaches the policy or the return value. What it
        # does cost is two screenshots, a 1.5s sleep and an image-comparison
        # VLM call on every clickable Button -- at least 90s each on the local
        # backend. Open Camera managed 3 actions in its 63-minute budget
        # because of it, and its feature coverage fell from 29.97% to 0.
        # Opt in with TESTCUBE_TAP_ORACLE=1.
        use_oracle = (
            _tap_oracle_enabled()
            and self.view
            and "Button" in view_class
            and self.view.get("clickable")
            and not GeminiAi.is_disabled()
            and not getattr(self, "skip_oracle", False)
        )

        if use_oracle:
            before = device.take_screenshot()
            print(f'Before Image: {before}')
            device.view_long_touch(x=x, y=y, duration=200)
            import time
            time.sleep(1.5)
            after = device.take_screenshot()
            print(f'After Image: {after}')
            result = ImageComparer.compareImage(before, after)
            if not result:
                return True

            import json
            import re

            match = re.search(r'\{.*\}', result, re.DOTALL)
            if match:
                json_str = match.group(0)
                parsed_data = json.loads(json_str)
                print('\n\n\n')
                print(f'Verdict = {parsed_data.get("verdict")}')
                print(f'Response = {parsed_data.get("response")}')
                print('\n\n\n')
            else:
                print("No JSON found in the text.")
        else:
            device.view_long_touch(x=x, y=y, duration=200)
        return True


class CustomSetTextEvent(SetTextEvent):

    def send(self, device):
        x, y = UIEvent.get_xy(x=self.x, y=self.y, view=self.view)
        touch_event = TouchEvent(x=x, y=y)
        touch_event.send(device)

        from .GeminiAI import GeminiAi

        text = self.text
        if text is None or text == "":
            state = device.get_last_known_state()
            text = GeminiAi.suggest_field_input(self.view, state)
        if text is None:
            text = ""
        self.text = text
        device.view_set_text(text)
        return True
