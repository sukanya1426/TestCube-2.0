#!/usr/bin/env bash
# Install Ollama (if needed), start it, pull qwen2.5-vl:7b, and keep it resident.
set -euo pipefail

MODEL="${OLLAMA_MODEL:-qwen2.5vl:7b}"

if ! command -v ollama >/dev/null 2>&1; then
  echo "Installing Ollama via Homebrew..."
  brew install ollama
fi

echo "Starting Ollama service..."
brew services start ollama >/dev/null 2>&1 || true
# Fallback if brew services is unavailable
if ! curl -sf --max-time 2 http://127.0.0.1:11434/api/tags >/dev/null; then
  OLLAMA_FLASH_ATTENTION=1 ollama serve >/tmp/ollama-serve.log 2>&1 &
  sleep 2
fi

echo "Pulling ${MODEL} (Metal / Apple Silicon)..."
ollama pull "${MODEL}"

echo "Warming the model so weights stay in unified memory..."
curl -sS http://127.0.0.1:11434/api/chat \
  -H "Content-Type: application/json" \
  -d "{\"model\":\"${MODEL}\",\"messages\":[{\"role\":\"user\",\"content\":\"Reply with OK.\"}],\"stream\":false,\"keep_alive\":-1,\"options\":{\"num_predict\":8}}" \
  >/dev/null

echo
echo "Local VLM is ready."
curl -sS http://127.0.0.1:11434/api/tags
echo
python3 -m droidbot.local_vlm --check || true
