"""Local Vision-Language Model client (Ollama + Metal on Apple Silicon).

Used alongside Gemini. In auto mode, TestCube prefers this backend when the
Ollama server is reachable so screenshot analysis does not burn API quota.
"""

import base64
import io
import json
import os
import urllib.error
import urllib.request


DEFAULT_HOST = os.environ.get("OLLAMA_HOST", "http://127.0.0.1:11434").rstrip("/")
DEFAULT_MODEL = os.environ.get("OLLAMA_MODEL", "qwen2.5vl:7b")
DEFAULT_KEEP_ALIVE = os.environ.get("OLLAMA_KEEP_ALIVE", "-1")
DEFAULT_NUM_CTX = int(os.environ.get("OLLAMA_NUM_CTX", "8192"))
DEFAULT_TEMPERATURE = float(os.environ.get("OLLAMA_TEMPERATURE", "0.2"))


class LocalVLM(object):
    _available = None
    _last_error = None

    @classmethod
    def configure(cls, host=None, model=None):
        if host:
            os.environ["OLLAMA_HOST"] = host.rstrip("/")
        if model:
            os.environ["OLLAMA_MODEL"] = model
        cls._available = None

    @classmethod
    def host(cls):
        return os.environ.get("OLLAMA_HOST", DEFAULT_HOST).rstrip("/")

    @classmethod
    def model(cls):
        return os.environ.get("OLLAMA_MODEL", DEFAULT_MODEL)

    @classmethod
    def is_available(cls, force=False):
        if cls._available is not None and not force:
            return cls._available
        try:
            payload = cls._get("/api/tags", timeout=2)
            models = [
                item.get("name") or item.get("model") or ""
                for item in (payload.get("models") or [])
            ]
            wanted = cls.model()
            cls._available = any(_model_matches(wanted, name) for name in models)
            if cls._available:
                print("Local VLM ready: %s at %s" % (wanted, cls.host()))
            elif models:
                print("Local VLM: Ollama is up but %s is not pulled. Have: %s" % (
                    wanted, ", ".join(models),
                ))
        except Exception as exc:
            cls._last_error = exc
            cls._available = False
        return bool(cls._available)

    @classmethod
    def generate(cls, prompt, timeout=120):
        """Complete a text prompt, optionally with PIL images or file paths."""
        text, images = _split_prompt(prompt)
        if not text:
            text = "Describe this Android UI screenshot and the obvious next tap."
        payload = {
            "model": cls.model(),
            "messages": [
                {
                    "role": "user",
                    "content": text,
                    "images": images,
                }
            ],
            "stream": False,
            "keep_alive": _keep_alive_value(),
            "options": {
                "temperature": DEFAULT_TEMPERATURE,
                "num_ctx": DEFAULT_NUM_CTX,
            },
        }
        num_predict = os.environ.get("OLLAMA_NUM_PREDICT")
        if num_predict:
            try:
                payload["options"]["num_predict"] = int(num_predict)
            except ValueError:
                pass
        if not images:
            payload["messages"][0].pop("images", None)
        data = cls._post("/api/chat", payload, timeout=timeout)
        message = data.get("message") or {}
        content = message.get("content")
        if content:
            return content
        raise RuntimeError("Local VLM returned no content: %s" % data)

    @classmethod
    def analyze_screen(cls, image_path, prompt, state_history=None, timeout=120):
        history = "\n".join(state_history or [])
        full = prompt
        if history:
            full = "State & Event History:\n%s\n\nTask: %s" % (history, prompt)
        return cls.generate([full, image_path], timeout=timeout)

    @classmethod
    def warmup(cls):
        if not cls.is_available(force=True):
            return False
        try:
            running = cls._get("/api/ps", timeout=5)
            names = [
                (item.get("name") or item.get("model") or "")
                for item in (running.get("models") or [])
            ]
            if any(_model_matches(cls.model(), name) for name in names):
                print("Local VLM already resident: %s" % cls.model())
                return True
        except Exception:
            pass
        try:
            cls._post("/api/chat", {
                "model": cls.model(),
                "messages": [{"role": "user", "content": "Reply with OK."}],
                "stream": False,
                "keep_alive": _keep_alive_value(),
                "options": {"temperature": 0, "num_predict": 8},
            }, timeout=180)
            print("Local VLM warmed and kept resident: %s" % cls.model())
            return True
        except Exception as exc:
            print("Local VLM warmup failed: %s" % exc)
            return False

    @classmethod
    def _get(cls, path, timeout=5):
        url = cls.host() + path
        request = urllib.request.Request(url, method="GET")
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return json.loads(response.read().decode("utf-8"))

    @classmethod
    def _post(cls, path, payload, timeout=120):
        url = cls.host() + path
        body = json.dumps(payload).encode("utf-8")
        request = urllib.request.Request(
            url,
            data=body,
            method="POST",
            headers={"Content-Type": "application/json"},
        )
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                return json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")
            raise RuntimeError("Ollama HTTP %s: %s" % (exc.code, detail[:500]))


def _keep_alive_value():
    raw = os.environ.get("OLLAMA_KEEP_ALIVE", DEFAULT_KEEP_ALIVE)
    if raw in ("-1", "forever"):
        return -1
    try:
        return int(raw)
    except ValueError:
        return raw


def _model_matches(wanted, installed):
    if not wanted or not installed:
        return False
    if wanted == installed:
        return True
    def _norm(name):
        return name.lower().replace("-", "").replace("_", "")
    return _norm(wanted) == _norm(installed) or _norm(wanted).split(":")[0] == _norm(installed).split(":")[0]


def _split_prompt(prompt):
    if prompt is None:
        return "", []
    if isinstance(prompt, str):
        return prompt, []
    texts = []
    images = []
    for part in prompt:
        encoded = _encode_image(part)
        if encoded is not None:
            images.append(encoded)
        elif isinstance(part, str):
            texts.append(part)
        else:
            texts.append(str(part))
    return "\n".join(texts).strip(), images


def _encode_image(part):
    if part is None:
        return None
    if isinstance(part, str):
        if os.path.isfile(part) and _looks_like_image_path(part):
            with open(part, "rb") as handle:
                return base64.b64encode(handle.read()).decode("utf-8")
        return None
    if hasattr(part, "save") and hasattr(part, "mode"):
        image = part
        if image.mode not in ("RGB", "L"):
            image = image.convert("RGB")
        buffer = io.BytesIO()
        image.save(buffer, format="PNG")
        return base64.b64encode(buffer.getvalue()).decode("utf-8")
    return None


def _looks_like_image_path(path):
    lower = path.lower()
    return lower.endswith((".png", ".jpg", ".jpeg", ".webp", ".bmp"))


def main(argv=None):
    import argparse
    parser = argparse.ArgumentParser(description="Check or warm the local Ollama VLM.")
    parser.add_argument("--check", action="store_true", help="Probe Ollama and list models.")
    parser.add_argument("--warmup", action="store_true", help="Load the model into unified memory.")
    parser.add_argument("--host", default=None)
    parser.add_argument("--model", default=None)
    args = parser.parse_args(argv)
    if args.host or args.model:
        LocalVLM.configure(host=args.host, model=args.model)
    if args.check or not args.warmup:
        try:
            tags = LocalVLM._get("/api/tags", timeout=5)
        except Exception as exc:
            print("Ollama is not reachable at %s (%s)" % (LocalVLM.host(), exc))
            print("Start it with: brew services start ollama")
            return 1
        names = [item.get("name") for item in tags.get("models") or []]
        print("Ollama: %s" % LocalVLM.host())
        print("Wanted model: %s" % LocalVLM.model())
        print("Installed: %s" % (", ".join(names) or "(none)"))
        print("Available: %s" % LocalVLM.is_available(force=True))
    if args.warmup:
        ok = LocalVLM.warmup()
        return 0 if ok else 1
    return 0 if LocalVLM.is_available() else 1


if __name__ == "__main__":
    raise SystemExit(main())
