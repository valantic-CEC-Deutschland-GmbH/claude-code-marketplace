#!/usr/bin/env python3
"""
Valantic Coding Standards - Pre-tool-use Hook

Checks Edit/Write operations against Valantic coding standards.
Provides warnings for common violations.

Reads tool input from stdin as JSON:
  {"tool_name": "Edit|Write", "tool_input": {"file_path": "...", "content|new_string": "..."}}

Outputs JSON to stdout:
  {"decision": "allow"} or {"decision": "allow", "reason": "warning message"}
"""

import json
import os
import re
import sys


def check_php_standards(content: str, file_path: str) -> list:
    """Check PHP-specific coding standards."""
    warnings = []

    # Check for strict_types declaration
    if "<?php" in content and "declare(strict_types=1)" not in content:
        if not file_path.endswith((".blade.php", ".tpl.php")):
            warnings.append("PHP file missing declare(strict_types=1)")

    # Check for generic Exception usage
    if re.search(r"throw\s+new\s+\\?Exception\(", content):
        warnings.append("Using generic \\Exception — prefer specific exception classes")

    # Check for var_dump/print_r debug statements
    if re.search(r"\b(?:var_dump|print_r|dd)\s*\(", content):
        warnings.append("Debug statement detected (var_dump/print_r/dd) — remove before committing")

    # Check for hardcoded credentials patterns
    if re.search(r"(?:password|secret|token|api_key)\s*=\s*['\"][^'\"]+['\"]", content, re.IGNORECASE):
        warnings.append("Possible hardcoded credential detected — use environment variables")

    return warnings


def check_typescript_standards(content: str, file_path: str) -> list:
    """Check TypeScript/React-specific coding standards."""
    warnings = []

    # Check for var usage
    if re.search(r"\bvar\s+\w+", content):
        warnings.append("Using 'var' — prefer 'const' or 'let'")

    # Check for class components in React
    if re.search(r"class\s+\w+\s+extends\s+(?:React\.)?Component", content):
        warnings.append("Class component detected — use functional components with hooks")

    # Check for console.log
    if re.search(r"\bconsole\.log\s*\(", content):
        warnings.append("console.log detected — use proper logging or remove before committing")

    # Check for any type
    if re.search(r":\s*any\b", content):
        warnings.append("Using 'any' type — prefer explicit types for type safety")

    return warnings


def check_java_standards(content: str, file_path: str) -> list:
    """Check Java/Kotlin-specific coding standards."""
    warnings = []

    # Check for System.out.println
    if "System.out.println" in content:
        warnings.append("System.out.println detected — use SLF4J logger instead")

    # Check for catching generic Exception
    if re.search(r"catch\s*\(\s*Exception\s+", content):
        warnings.append("Catching generic Exception — prefer specific exception types")

    # Check for exposed entity in controller
    if re.search(r"@(?:Get|Post|Put|Delete)Mapping", content) and "@Entity" in content:
        warnings.append("Entity annotation in controller file — use DTOs for API responses")

    return warnings


def check_general_standards(content: str, file_path: str) -> list:
    """Check language-agnostic standards."""
    warnings = []

    # Check for TODO/FIXME/HACK comments
    todos = re.findall(r"(?:TODO|FIXME|HACK|XXX)(?::?\s*(.{0,50}))?", content)
    if len(todos) > 3:
        warnings.append(f"Multiple TODO/FIXME comments found ({len(todos)}) — consider creating tickets")

    return warnings


def get_file_type(file_path: str) -> str:
    """Determine the file type from the extension."""
    ext = os.path.splitext(file_path)[1].lower()
    if ext == ".php":
        return "php"
    elif ext in (".ts", ".tsx", ".js", ".jsx"):
        return "typescript"
    elif ext in (".java", ".kt"):
        return "java"
    return "other"


def main():
    try:
        input_data = json.load(sys.stdin)
    except (json.JSONDecodeError, EOFError):
        json.dump({"decision": "allow"}, sys.stdout)
        return

    tool_input = input_data.get("tool_input", {})
    file_path = tool_input.get("file_path", "")

    # Get the content being written/edited
    content = tool_input.get("content", "") or tool_input.get("new_string", "")

    if not content or not file_path:
        json.dump({"decision": "allow"}, sys.stdout)
        return

    file_type = get_file_type(file_path)
    warnings = check_general_standards(content, file_path)

    if file_type == "php":
        warnings.extend(check_php_standards(content, file_path))
    elif file_type == "typescript":
        warnings.extend(check_typescript_standards(content, file_path))
    elif file_type == "java":
        warnings.extend(check_java_standards(content, file_path))

    if warnings:
        json.dump({
            "decision": "allow",
            "reason": "Coding standards warnings:\n- " + "\n- ".join(warnings)
        }, sys.stdout)
    else:
        json.dump({"decision": "allow"}, sys.stdout)


if __name__ == "__main__":
    main()
