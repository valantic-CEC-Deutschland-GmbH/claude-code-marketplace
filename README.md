# Valantic Claude Code Marketplace

Company-internal Claude Code marketplace providing branded tools, workflows, and coding standards for Valantic developers.

## Installation

```bash
# Add the Valantic marketplace
/plugin marketplace add valantic/claude-code-marketplace

# Browse available plugins
/plugins

# Install individual plugins
/plugin install valantic-brand-guidelines@valantic-claude-code-marketplace
/plugin install valantic-documents@valantic-claude-code-marketplace
/plugin install valantic-dev-workflow@valantic-claude-code-marketplace
/plugin install valantic-coding-standards@valantic-claude-code-marketplace
/plugin install valantic-project-setup@valantic-claude-code-marketplace
```

## Available Plugins

| Plugin | Type | Description |
|--------|------|-------------|
| `valantic-brand-guidelines` | Skill | Liquid Brand Design system (Routes A/B/C, colors, typography) |
| `valantic-documents` | Skill | Branded PPTX/PDF/DOCX generation with Valantic templates |
| `valantic-dev-workflow` | Commands + Hooks | Deployment, review, onboarding commands + permission hooks |
| `valantic-coding-standards` | Skill + Hooks | Enforce company coding conventions automatically |
| `valantic-project-setup` | Skill + Commands | Bootstrap new projects with Valantic templates (PHP, React, Spring) |

## Plugin Details

### valantic-brand-guidelines

Applies Valantic's official **Liquid Brand Design** system. Includes:
- Visual Routes A (Restrained), B (Standard), C (Dynamic)
- Official color palette (Coral `#FF5757`, Purple Heart `#4C26B7`, Peach `#FFCCAA`)
- Typography system (Calibre/Segoe UI)
- CSS variables and design tokens

### valantic-documents

Generate branded documents:
- **PPTX**: Presentations with Valantic slide layouts and styling
- **PDF**: Reports and whitepapers with brand colors and typography
- **DOCX**: Business documents with proper formatting

### valantic-dev-workflow

Development workflow commands:
- `/deploy` — Guided deployment with environment checks and rollback support
- `/review` — Structured code review against Valantic standards
- `/onboard` — New developer onboarding checklist

Includes a permission evaluator hook that enforces safe tool usage policies.

### valantic-coding-standards

Automatic enforcement of Valantic coding conventions:
- PHP: PSR-12, strict types, Spryker/Symfony patterns
- TypeScript/React: functional components, strict mode, naming conventions
- Java/Spring: standard patterns, proper annotations
- General: error handling, logging, security practices

Pre-tool-use hook checks edits against standards.

### valantic-project-setup

Bootstrap new projects:
- `/new-project` — Interactive project scaffolding
- PHP (Spryker/Symfony) template
- React (Next.js/Vite) template
- Spring Boot (Kotlin/Java) template

## Security

- **No secrets**: API keys, tokens, and passwords must stay in local environment variables
- **Private repo**: Developers need GitHub access via SSH or HTTPS
- **Hook scripts**: Use Python standard library only (no pip dependencies)
- **MCP configs**: Use `${ENV_VAR}` patterns for credentials

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on adding or updating plugins.
