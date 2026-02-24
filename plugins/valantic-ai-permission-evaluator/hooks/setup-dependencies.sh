#!/bin/bash
# Auto-install npm dependencies for the permission evaluator plugin
# This runs on SessionStart to ensure node_modules are present

PLUGIN_DIR="$(cd "$(dirname "$0")/.." && pwd)"

if [ ! -d "$PLUGIN_DIR/node_modules" ] && [ -f "$PLUGIN_DIR/package.json" ]; then
  npm install --prefix "$PLUGIN_DIR" --silent 2>/dev/null
fi

# Check for required environment variable
if [ -z "$OPENAI_API_KEY" ]; then
  echo "[valantic-ai-permission-evaluator] WARNING: OPENAI_API_KEY is not set." >&2
  echo "  The LLM-powered permission evaluator requires an OpenAI API key." >&2
  echo "  Set it in your shell profile: export OPENAI_API_KEY=sk-proj-..." >&2
  echo "  Without it, the plugin will allow all tool uses without AI safety checks." >&2
fi
