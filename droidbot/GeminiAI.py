# GeminiAI.py (fixed for current google-generativeai library + your new key)
import os
import pathlib
import json
import re
import ssl
import threading
import time

# Campus/proxy SSL inspection breaks gRPC (boringssl). Use REST over Python SSL
# and do not hang forever if the certificate chain is still untrusted.
os.environ.setdefault("GRPC_VERBOSITY", "ERROR")
os.environ.setdefault("GLOG_minloglevel", "2")
ssl._create_default_https_context = ssl._create_unverified_context
try:
    import httplib2
    _Http = httplib2.Http

    def _InsecureHttp(*args, **kwargs):
        kwargs["disable_ssl_certificate_validation"] = True
        return _Http(*args, **kwargs)

    httplib2.Http = _InsecureHttp
except Exception:
    pass

import google.generativeai as genai  # correct import

media = pathlib.Path(__file__).parents[1] / "droidbot"
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY") or ""
GEMINI_MODEL_NAMES = (
    "gemini-3.5-flash",
    "gemini-2.5-flash",
    "gemini-2.0-flash",
    "gemini-1.5-flash",
)


def _configure_genai():
    if not GEMINI_API_KEY:
        return
    genai.configure(api_key=GEMINI_API_KEY, transport="rest")


_configure_genai()


def _looks_like_network_failure(exc):
    text = str(exc).lower()
    return any(token in text for token in (
        "ssl",
        "certificate",
        "certverify",
        "certificate_verify_failed",
        "timed out",
        "timeout",
        "handshake",
        "connection reset",
        "failed to establish",
    ))


class GeminiAi:
    _chat = None
    _input = None
    _readme = ""
    _credentials = ""
    _app_name = None
    _configured = False
    _disabled = False
    __model = None
    _request_lock = threading.Lock()
    _last_request_monotonic = 0.0
    _field_cache = {}
    _backend = os.environ.get("LLM_BACKEND", "auto")
    MIN_REQUEST_INTERVAL = float(os.environ.get("GEMINI_MIN_INTERVAL", "25"))

    @classmethod
    def set_backend(cls, backend=None, ollama_host=None, ollama_model=None, warmup=True):
        if backend:
            cls._backend = backend
            os.environ["LLM_BACKEND"] = backend
        from .local_vlm import LocalVLM
        LocalVLM.configure(host=ollama_host, model=ollama_model)
        if cls._backend in ("auto", "local") and warmup:
            if LocalVLM.is_available(force=True):
                LocalVLM.warmup()
            elif cls._backend == "local":
                print("Local VLM requested but Ollama is not ready at %s" % LocalVLM.host())

    @classmethod
    def is_disabled(cls):
        """True only when no LLM backend can answer."""
        if cls._backend == "local":
            from .local_vlm import LocalVLM
            return not LocalVLM.is_available()
        if cls._backend == "gemini":
            return bool(cls._disabled)
        from .local_vlm import LocalVLM
        if LocalVLM.is_available():
            return False
        return bool(cls._disabled)

    @classmethod
    def disable(cls, reason=""):
        if not cls._disabled:
            cls._disabled = True
            print("Gemini disabled after failure: %s" % reason)

    @classmethod
    def _ensure_model(cls):
        if cls.__model is not None:
            return cls.__model
        _configure_genai()
        last_error = None
        for name in GEMINI_MODEL_NAMES:
            try:
                cls.__model = genai.GenerativeModel(name)
                print("Using Gemini model: %s (REST)" % name)
                return cls.__model
            except Exception as exc:
                last_error = exc
                cls.__model = None
        raise RuntimeError("Could not create a Gemini model: %s" % last_error)

    @classmethod
    def parse_json(cls, json_string: str):
        try:
            json_string = json_string.strip()
            json_lines = json_string.split('\n')
            json_string = '\n'.join(json_lines[1:-1])
            json_data = json.loads(json_string)
            return json_data
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return None

    @classmethod
    def get_chat(cls):
        if cls._chat is None:
            _system_prompt = f'You are an android input test case generator tool called Testcube. Your work is to find best input for a input field.I have some existing credential input. Here is the credentials i have. Credentials: \n{cls._input}. Now after every input field found i will give you a prompt. The prompt will look like "Enter your email" / "Enter Password" / "Username" etc also there can be an optional event_str look like "SetTextEvent(state=471db0b34dd4b9be2ac8f0917d8e947a, view=23945eb0f968dd6ba05de8382ade54e1(Login)/EditText-Enter your), text=)". From the event_str you can get knowledge about what page are you in now so use credential accordingly. Your work is to find for this prompt what existing credential i should use. My credentials are in key value format. You have to give me the key name only with proper case maintained. If you found something that that is not your prompt type like if you encounter a prompt example@gmail.com then you have to be smart and send response as email because this value belong to an email.Also if you found **** then it must be a password so respond pass. So finally just dont look for the key name if you found something that matches any value in the existing credential then also repond the corresponding key name.\nExample:\nCredentials:\nemail: saimon@gmail.com\npass: 12345678\nprompt: Enter your email\nresponse: email\nprompt: Enter Password\nresponse: pass\nprompt: Bhuiyan\nresponse: l_name.\nAlso use credentials that are actual_... only for Login page any type of login page for first time, otherwise use random credentials. Like if i ask for email then one time give me email5 then next time give me email7. Use randomize value.'
            cls._chat = cls._ensure_model().start_chat(history=[{"role": "user", "parts": [_system_prompt]}])
        return cls._chat

    @classmethod
    def generate_random_input(cls):
        if cls._input is None:
            credential_content = ""
            with open(media / "credential.txt", "r") as f:
                credential_content += f.read()
            _system_prompt = f'You are an android input test case generator tool called Testcube. Your work is to simulate mock data to test an android app. I have some existing credentials input for testing. Here is the credentials i have. Credentials:\n{credential_content}. Now you need to create exactly 10 copy of this credentials in json format and return me a json. For each variation consider empty string, variatiion in gmail format, variation in password length, variation in upper case lower case etc but try to be real. Also create variation in all of the field. Finally return me a json where my given credentials key should be named "actual_email": "example@gmail.com", "actual_pass": "12345678" etc. And the 10 variation should be like "email1": "something@gmail.com" and so on and all the key and value should properly double quoted.'
            chat = cls._ensure_model().start_chat(history=[{"role": "user", "parts": [_system_prompt]}])
            response = chat.send_message("Generate now")
            cls._input = cls.parse_json(response.text)
            print(cls._input)
        return cls._input

    @classmethod
    def generate_content(cls, prompt, timeout=45):
        """Complete a prompt via local VLM and/or Gemini.

        ``prompt`` may be a string or a Gemini-style list of text + PIL images.
        """
        backend = (cls._backend or "auto").lower()
        errors = []
        if backend in ("auto", "local"):
            try:
                from .local_vlm import LocalVLM
                if LocalVLM.is_available():
                    local_timeout = max(timeout, 90) if backend == "local" else max(timeout, 60)
                    text = LocalVLM.generate(prompt, timeout=local_timeout)
                    if text:
                        return text
            except Exception as exc:
                errors.append("local: %s" % exc)
                print("Local VLM failed: %s" % exc)
                if backend == "local":
                    raise RuntimeError("Local VLM request failed: %s" % exc)
        if backend in ("auto", "gemini"):
            try:
                return cls._generate_gemini(prompt, timeout=timeout)
            except Exception as exc:
                errors.append("gemini: %s" % exc)
                if backend == "gemini":
                    raise
        raise RuntimeError("LLM request failed (%s)" % ("; ".join(errors) or "no backend"))

    @classmethod
    def _generate_gemini(cls, prompt, timeout=45):
        """One-shot Gemini completion. Rate-limited; retries 429 on the same model."""
        if cls._disabled:
            raise RuntimeError("Gemini is disabled")
        last_error = None
        for name in GEMINI_MODEL_NAMES:
            model_usable = False
            for attempt in range(3):
                cls._wait_for_slot()
                try:
                    _configure_genai()
                    model = genai.GenerativeModel(name)
                    response = model.generate_content(
                        prompt, request_options={"timeout": timeout}
                    )
                    cls.__model = model
                    return response.text
                except Exception as exc:
                    last_error = exc
                    print("Gemini model %s failed: %s" % (name, exc))
                    if _looks_like_network_failure(exc):
                        cls.disable(str(exc))
                        raise RuntimeError("Gemini request failed: %s" % last_error)
                    if cls._is_not_found(exc):
                        break
                    delay = cls._retry_delay(exc)
                    if delay is not None:
                        if cls._is_daily_quota(exc) and attempt >= 1:
                            cls.disable("daily quota exceeded")
                            raise RuntimeError("Gemini request failed: %s" % last_error)
                        print("Gemini rate-limited, waiting %.1fs before retry." % delay)
                        time.sleep(delay)
                        model_usable = True
                        continue
                    break
            if model_usable:
                continue
        raise RuntimeError("Gemini request failed: %s" % last_error)

    @classmethod
    def _wait_for_slot(cls):
        with cls._request_lock:
            gap = cls.MIN_REQUEST_INTERVAL - (time.monotonic() - cls._last_request_monotonic)
            if gap > 0:
                print("Gemini cooldown: waiting %.1fs to stay under quota." % gap)
                time.sleep(gap)
            cls._last_request_monotonic = time.monotonic()

    @staticmethod
    def _retry_delay(exc):
        text = str(exc)
        if "429" not in text and "RESOURCE_EXHAUSTED" not in text and "quota" not in text.lower():
            return None
        match = re.search(r"retry in ([\d.]+)s", text, re.IGNORECASE)
        if match:
            return min(90.0, max(5.0, float(match.group(1)) + 1.0))
        match = re.search(r"'retryDelay': '(\d+)s'", text)
        if match:
            return min(90.0, max(5.0, float(match.group(1)) + 1.0))
        return 25.0

    @staticmethod
    def _is_daily_quota(exc):
        text = str(exc)
        return "PerDay" in text or "per day" in text.lower()

    @staticmethod
    def _is_not_found(exc):
        text = str(exc).lower()
        return "404" in text or "not found" in text or "no longer available" in text

    @classmethod
    def set_context(cls, readme_path=None, credential_path=None, app_name=None):
        """Load README + optional credentials for traversal-time input."""
        cls._app_name = app_name
        if readme_path and os.path.isfile(readme_path):
            with open(readme_path, "r", encoding="utf-8") as handle:
                cls._readme = handle.read()
            print("Loaded app README for Gemini input: %s" % readme_path)
        credential_file = credential_path
        if not credential_file:
            from .feature_tester.specs import discover_credentials
            credential_file = discover_credentials(readme_path=readme_path)
        if not credential_file:
            candidate = media / "credential.txt"
            if candidate.is_file():
                credential_file = str(candidate)
        if credential_file and os.path.isfile(credential_file):
            with open(credential_file, "r", encoding="utf-8") as handle:
                cls._credentials = handle.read()
            print("Loaded credentials: %s" % credential_file)

    @classmethod
    def suggest_field_input(cls, view, state=None):
        """Return the exact string to type into an input field."""
        view = view or {}
        label = view.get("text") or view.get("content_description") or ""
        resource_id = view.get("resource_id") or ""
        view_class = view.get("class") or ""
        is_password = bool(view.get("is_password"))
        cache_key = "%s|%s|%s" % (label, resource_id, is_password)
        if cache_key in cls._field_cache:
            return cls._field_cache[cache_key]
        if cls.is_disabled():
            value = cls._fallback_field_input(label, resource_id, is_password)
            cls._field_cache[cache_key] = value
            return value
        activity = ""
        event_hint = ""
        if state is not None:
            activity = getattr(state, "foreground_activity", "") or ""
            try:
                from .input_event import SetTextEvent
                event_hint = SetTextEvent(view=view, text="").get_event_str(state)
            except Exception:
                event_hint = activity

        prompt = (
            "You are TestCube, an Android GUI tester. Type a realistic value into "
            "the current input field so exploration can continue.\n"
            "Return ONLY JSON: {\"text\": \"the exact string to type\"}\n"
            "Rules:\n"
            "- Return the value itself, never a credential key name.\n"
            "- If this is login/email/password and known credentials are provided, use them.\n"
            "- If this is search, use a real query from the README domain (e.g. an artist or song).\n"
            "- If this is a name/playlist/comment field, invent a short realistic value.\n"
            "- Do not include quotes inside the JSON value unless they belong in the typed text.\n"
            "- If the field already contains a usable value and should be kept, return that same value.\n\n"
            "Application: %s\n"
            "README:\n%s\n\n"
            "Known credentials (optional):\n%s\n\n"
            "Current activity: %s\n"
            "Field text/hint: %s\n"
            "resource_id: %s\n"
            "class: %s\n"
            "is_password: %s\n"
            "event: %s\n"
        ) % (
            cls._app_name or "unknown",
            (cls._readme or "(none)")[:8000],
            cls._credentials or "(none)",
            activity,
            label,
            resource_id,
            view_class,
            is_password,
            event_hint,
        )
        try:
            raw = cls.generate_content(prompt)
            parsed = cls._parse_object(raw)
            if parsed and "text" in parsed:
                value = "" if parsed["text"] is None else str(parsed["text"])
                cls._field_cache[cache_key] = value
                return value
        except Exception as exc:
            print("Gemini field input failed: %s" % exc)
        value = cls._fallback_field_input(label, resource_id, is_password)
        cls._field_cache[cache_key] = value
        return value

    @classmethod
    def suggest_field_input_for_step(cls, view, remaining, feature=None):
        """Two-stage field fill: reason about role, then emit the string to type."""
        view = view or {}
        label = view.get("text") or view.get("content_description") or ""
        resource_id = view.get("resource_id") or ""
        view_class = view.get("class") or ""
        is_password = bool(view.get("is_password"))
        feat = feature or {}
        step = (remaining or [""])[0]
        cache_key = "step|%s|%s|%s" % (label, resource_id, step)
        if cache_key in cls._field_cache:
            return cls._field_cache[cache_key]
        if cls.is_disabled():
            value = cls._fallback_field_input(label, resource_id, is_password)
            cls._field_cache[cache_key] = value
            return value
        prompt = (
            "You are TestCube filling one Android text field.\n"
            "First reason about (1) the app's functionality and (2) this field's role "
            "given the remaining test step. Then emit the exact string to type.\n"
            "Return ONLY JSON: "
            "{\"role\":\"search query|playlist name|email|other\","
            "\"reasoning\":\"one sentence\","
            "\"text\":\"the exact string to type\"}\n"
            "Rules:\n"
            "- Prefer a known credential (search_query, playlist_name, email, pwd) when it fits.\n"
            "- Never return HTML, widget dumps, placeholders, or error strings.\n"
            "- Keep the value short and realistic for this app domain.\n\n"
            "Application: %s\nFeature: %s\nRemaining steps: %s\n"
            "README excerpt:\n%s\n\nKnown credentials:\n%s\n\n"
            "Field text/hint: %s\nresource_id: %s\nclass: %s\nis_password: %s\n"
        ) % (
            cls._app_name or "unknown",
            feat.get("name") or "",
            remaining or [],
            (cls._readme or "(none)")[:4000],
            cls._credentials or "(none)",
            label,
            resource_id,
            view_class,
            is_password,
        )
        try:
            raw = cls.generate_content(prompt)
            parsed = cls._parse_object(raw)
            if parsed and "text" in parsed:
                value = "" if parsed["text"] is None else str(parsed["text"])
                cls._field_cache[cache_key] = value
                return value
        except Exception as exc:
            print("Gemini staged field input failed: %s" % exc)
        value = cls._fallback_field_input(label, resource_id, is_password)
        cls._field_cache[cache_key] = value
        return value

    @classmethod
    def extract_features_from_readme(cls, readme_text, app_name=None):
        prompt = (
            "You write a GUI test plan for an Android app from its README or notes.\n"
            "FEATURE DEFINITION: a feature is a finite ordered sequence of user operations "
            "where (a) each operation is necessary — removing it changes or breaks the outcome, "
            "and (b) the sequence ends in a visibly different, checkable app state.\n"
            "Do NOT bundle multiple distinct outcomes or toggles into one feature just because "
            "they live on the same screen. Playback controls, shuffle/repeat, sleep timer, "
            "volume, and equalizer are separate features if the README names them separately. "
            "Each feature should usually have 2-6 actions.\n"
            "Each feature is a user-facing flow a tester can tap/type through on a phone, "
            "NOT a marketing bullet (skip cross-platform, open source, telemetry, install methods).\n"
            "Do NOT invent features the text does not describe. "
            "Do not add login/sign-up, games, reports, or social-account creation "
            "unless those words actually appear as user-facing capabilities. "
            "Always start with first-run setup (welcome, skip/guest, create database/account) "
            "when a first-run flow is mentioned or typical. "
            "Then cover only primary objects named in the docs.\n"
            "Actions must be ordered, concrete, and imperative: Tap / Enter / Select / Long-press / Save.\n"
            "8-20 features is typical. Return ONLY JSON:\n"
            "{\n"
            '  "app": "AppName",\n'
            '  "features": [\n'
            "    {\n"
            '      "id": "F001",\n'
            '      "name": "Complete first-run setup",\n'
            '      "description": "...",\n'
            '      "actions": ["Tap Get Started or Skip", "Reach the home screen"],\n'
            '      "valid_paths": [],\n'
            '      "keywords": ["onboarding", "skip"],\n'
            '      "nav_hints": ["skip", "get started"]\n'
            "    }\n"
            "  ]\n"
            "}\n"
            "Use IDs F001, F002, ...\n\n"
            "Application name: %s\n\n"
            "README / notes:\n%s\n"
        ) % (app_name or cls._app_name or "unknown", (readme_text or "")[:14000])
        raw = cls.generate_content(prompt)
        parsed = cls._parse_object(raw)
        return parsed

    @classmethod
    def _parse_object(cls, text):
        if not text:
            return None
        text = text.strip()
        fenced = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", text, re.DOTALL)
        candidates = []
        if fenced:
            candidates.append(fenced.group(1))
        braced = re.search(r"\{.*\}", text, re.DOTALL)
        if braced:
            candidates.append(braced.group(0))
        candidates.append(text)
        for candidate in candidates:
            try:
                parsed = json.loads(candidate)
            except ValueError:
                continue
            if isinstance(parsed, dict):
                return parsed
        return cls.parse_json(text)

    @classmethod
    def _fallback_field_input(cls, label, resource_id, is_password):
        blob = ("%s %s" % (label or "", resource_id or "")).lower()
        creds = cls._credentials or ""
        mapping = {
            "email": "email",
            "user": "uid",
            "login": "email",
            "pass": "pwd",
            "pwd": "pwd",
            "search": "search_query",
            "query": "search_query",
            "playlist": "playlist_name",
            "phone": "phone",
            "payee": "f_name",
            "category": "comment",
            "note": "comment",
            "memo": "comment",
            "city": "city",
            "amount": "rating",
            "balance": "rating",
            "price": "rating",
            "year": None,
            "account": "f_name",
            "filename": None,
            "database": None,
            "file name": None,
            "mmb": None,
        }
        if any(token in blob for token in ("file name", "filename", "database", ".mmb", "mmb")):
            return "testcube.mmb"
        if "year" in blob:
            return "2026"
        if any(token in blob for token in ("amount", "balance", "price", "share")):
            return cls._credential_value(creds, "rating") or "100"
        if any(token in blob for token in ("leave blank", "optional password")):
            return ""
        for needle, key in mapping.items():
            if not key:
                continue
            if needle in blob:
                value = cls._credential_value(creds, key)
                if value:
                    return value
        if is_password:
            return cls._credential_value(creds, "pwd") or "TestPass123"
        if any(token in blob for token in ("name", "title")):
            return cls._credential_value(creds, "f_name") or "TestCube"
        return cls._credential_value(creds, "search_query") or "test"

    @classmethod
    def _credential_value(cls, creds, key):
        if not creds:
            return None
        prefix = key.lower() + ":"
        for line in creds.splitlines():
            stripped = line.strip()
            if stripped.lower().startswith(prefix):
                return stripped.split(":", 1)[1].strip()
        return None