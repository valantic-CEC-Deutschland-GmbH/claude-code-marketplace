#!/usr/bin/env python3
"""
Valantic Dev Workflow - Permission Evaluator Hook

Pre-tool-use hook that evaluates Bash commands for safety.
Blocks dangerous operations and requires confirmation for risky ones.

Reads tool input from stdin as JSON:
  {"tool_name": "Bash", "tool_input": {"command": "..."}}

Outputs JSON to stdout:
  {"decision": "allow"} or {"decision": "block", "reason": "..."}
"""

import json
import re
import sys


# Commands that should always be blocked
BLOCKED_PATTERNS = [
    r"\brm\s+-rf\s+/(?!\S)",          # rm -rf / (root)
    r"\bmkfs\b",                        # filesystem formatting
    r"\bdd\s+.*of=/dev/",              # disk overwrite
    r">\s*/dev/sd[a-z]",               # redirect to disk device
    r"\bcurl\b.*\|\s*(?:ba)?sh",       # curl | bash (remote execution)
    r"\bwget\b.*\|\s*(?:ba)?sh",       # wget | bash
    r"--no-verify",                     # skipping git hooks
    r"\bgit\s+push\s+.*--force\s+.*(?:main|master)\b",  # force push to main
    r"\bgit\s+reset\s+--hard\b",       # hard reset
]

# Commands that should trigger a warning (allowed but flagged)
WARNING_PATTERNS = [
    r"\bgit\s+push\b",                 # any git push
    r"\bdocker\s+(?:rm|rmi|prune)\b",  # docker cleanup
    r"\bkubectl\s+delete\b",           # k8s resource deletion
    r"\bnpm\s+publish\b",              # publishing packages
    r"\bdropdb\b",                      # database deletion
    r"\bdrop\s+(?:table|database)\b",  # SQL drop statements
]


def evaluate_command(command: str) -> dict:
    """Evaluate a bash command for safety."""
    for pattern in BLOCKED_PATTERNS:
        if re.search(pattern, command, re.IGNORECASE):
            return {
                "decision": "block",
                "reason": f"Blocked by Valantic security policy: command matches dangerous pattern '{pattern}'"
            }

    for pattern in WARNING_PATTERNS:
        if re.search(pattern, command, re.IGNORECASE):
            return {
                "decision": "allow",
                "reason": f"Warning: this command matches a sensitive pattern. Proceed with caution."
            }

    return {"decision": "allow"}


def main():
    try:
        input_data = json.load(sys.stdin)
    except (json.JSONDecodeError, EOFError):
        # If we can't parse input, allow by default
        json.dump({"decision": "allow"}, sys.stdout)
        return

    tool_name = input_data.get("tool_name", "")
    tool_input = input_data.get("tool_input", {})

    if tool_name != "Bash":
        json.dump({"decision": "allow"}, sys.stdout)
        return

    command = tool_input.get("command", "")
    result = evaluate_command(command)
    json.dump(result, sys.stdout)


if __name__ == "__main__":
    main()
