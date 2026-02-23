#!/bin/bash
# Auto-install npm dependencies for the permission evaluator plugin
# This runs on SessionStart to ensure node_modules are present

PLUGIN_DIR="$(cd "$(dirname "$0")/.." && pwd)"

if [ ! -d "$PLUGIN_DIR/node_modules" ] && [ -f "$PLUGIN_DIR/package.json" ]; then
  npm install --prefix "$PLUGIN_DIR" --silent 2>/dev/null
fi
