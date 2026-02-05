---
name: valantic-project-templates
description: Reference templates for bootstrapping new Valantic projects (PHP, React, Spring Boot). Activates when creating new projects or discussing project structure.
---

# Valantic Project Templates

## When to Use

This skill provides reference templates for new project scaffolding. Use it when:
- Creating a new project from scratch
- Discussing project structure best practices
- Onboarding a developer to understand standard layouts

## Available Templates

See the `references/` directory for detailed templates:

- **php-template.md** — PHP project (Spryker/Symfony)
- **react-template.md** — React project (Next.js/Vite)
- **spring-template.md** — Spring Boot project (Java/Kotlin)

## Common Elements (All Projects)

Every Valantic project must include:

### Root Files

| File | Purpose |
|------|---------|
| `README.md` | Project overview, setup instructions, team contact |
| `CLAUDE.md` | Project-specific instructions for Claude Code |
| `.gitignore` | Language-appropriate ignore patterns |
| `.env.example` | Documented environment variables (no secrets) |
| `docker-compose.yml` | Local development environment |
| `.github/workflows/ci.yml` | CI/CD pipeline |

### README Sections

Every Valantic project README must contain:

1. **Project Name & Description**
2. **Team** — owning team and contact
3. **Prerequisites** — required tools and versions
4. **Getting Started** — step-by-step setup
5. **Development** — how to run, test, and debug
6. **Deployment** — environments and deployment process
7. **Architecture** — high-level overview with diagram if applicable

### CLAUDE.md Template

```markdown
# Project: {project-name}

## Tech Stack
- Language: {language}
- Framework: {framework}
- Database: {database}

## Coding Standards
- Follow Valantic coding standards (see valantic-coding-standards plugin)
- {language-specific rules}

## Commands
- Build: {build-command}
- Test: {test-command}
- Lint: {lint-command}
- Dev server: {dev-command}

## Architecture Notes
- {key architectural decisions}
```
