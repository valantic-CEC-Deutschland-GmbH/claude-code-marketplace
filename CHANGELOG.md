# Changelog

## 1.1.2 — 2026-02-23

### Added
- TweakCC install instructions and documentation section in README
- SessionStart hook for automatic dependency installation in ai-permission-evaluator plugin

## 1.1.1 — 2026-02-23

### Fixed
- Corrected marketplace add command in README to use `valantic-CEC-Deutschland-GmbH/claude-code-marketplace`

## 1.1.0 — 2026-02-23

### Added
- **valantic-ai-permission-evaluator** plugin: LLM-powered pre-tool-use hook using GPT-4.1-nano for contextual safety evaluation of all Claude Code tool calls. Requires `OPENAI_API_KEY` environment variable and `npm install` after plugin installation.

## 1.0.1 — 2026-02-18

### Added
- TweakCC configuration with custom themes, thinking verbs, and UI display settings

## 1.0.0 — 2026-02-05

### Added
- Initial marketplace structure with `.claude-plugin/marketplace.json` registry
- **valantic-brand-guidelines** plugin: Liquid Brand Design system (Routes A/B/C, colors, typography, CSS variables)
- **valantic-documents** plugin: Branded PPTX, PDF, and DOCX generation skills
- **valantic-dev-workflow** plugin: `/deploy`, `/review`, `/onboard` commands with permission evaluator hook
- **valantic-coding-standards** plugin: PHP/TypeScript/Java coding standards skill with pre-edit enforcement hook
- **valantic-project-setup** plugin: `/new-project` command with PHP, React, and Spring Boot templates
- README, CONTRIBUTING guide, and .gitignore
