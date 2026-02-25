# Changelog

## 1.2.2 — 2026-02-25

### Changed
- Extracted GitHub Agents documentation into dedicated `github-agents.md` with centralization rationale and links to additional autonomous agent resources

## 1.2.1 — 2026-02-24

### Fixed
- Updater Agent now installs required language runtimes (PHP, Python, etc.) before checking for outdated packages — fixes false "all up to date" results on projects using non-Node.js stacks
- Updater Agent now handles missing lock files (e.g., composer.lock) by running a full dependency resolution first
- Updater Agent documents that updating workflow files requires a PAT with `workflow` scope
- Updater Agent with `major: true` now actually attempts major version bumps instead of preemptively skipping them as "too complex"

## 1.2.0 — 2026-02-24

### Added
- **Updater Agent**: Reusable GitHub Actions workflow for autonomous dependency updates (package managers, Docker images, GitHub Actions). Configurable major/minor control.

## 1.1.3 — 2026-02-24

### Improved
- ai-permission-evaluator: Graceful handling when `OPENAI_API_KEY` is missing — allows all tool uses with info message instead of throwing errors
- ai-permission-evaluator: SessionStart hook now warns user if `OPENAI_API_KEY` is not set
- ai-permission-evaluator: Plugin description mentions required env var

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
