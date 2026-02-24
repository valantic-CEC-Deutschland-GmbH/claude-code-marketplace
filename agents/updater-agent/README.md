# Updater Agent

Reusable GitHub Actions workflow that uses Claude Code CLI to autonomously update all project dependencies — package managers, Docker images, and GitHub Actions — and create a PR with the results.

## Features

- **Stack-agnostic**: Automatically detects and updates composer, npm, yarn, pnpm, pip, go, cargo, gradle, maven, bundler, and more
- **Docker-aware**: Updates Dockerfile base images, compose service images, and checks downstream effects (e.g., PHP constraint in composer.json after base image bump)
- **GitHub Actions**: Updates action version pins in workflow files
- **Major/minor control**: Configurable flag to include or exclude major version bumps
- **Autonomous verification**: Discovers and runs linters, tests, and build checks — reverts updates that break them
- **Migration-aware**: Uses Context7 MCP to look up migration guides for major version bumps
- **Technical debt tracking**: Records skipped dependencies in CLAUDE.md or DEPENDENCY_DEBT.md

## Quick Start

Create a workflow in your repository at `.github/workflows/updater-agent.yml`:

```yaml
name: Updater Agent

on:
  workflow_dispatch:
    inputs:
      major:
        description: 'Include major version updates'
        type: boolean
        default: false

jobs:
  update-dependencies:
    uses: valantic-CEC-Deutschland-GmbH/claude-code-marketplace/.github/workflows/updater-agent.yml@main
    with:
      major: ${{ inputs.major }}
    secrets:
      CLAUDE_CODE_OAUTH_TOKEN: ${{ secrets.CLAUDE_CODE_OAUTH_TOKEN }}
```

## Inputs

| Input | Type | Default | Description |
|-------|------|---------|-------------|
| `major` | boolean | `false` | When true, include major version updates. When false, only minor/patch. |
| `branch_name` | string | `ai/dependency-updates` | Branch name for the update PR. |

## Secrets

| Secret | Required | Description |
|--------|----------|-------------|
| `CLAUDE_CODE_OAUTH_TOKEN` | Yes | Claude Code OAuth token for CLI authentication. |

## Permissions

The calling workflow needs:

```yaml
permissions:
  contents: write
  pull-requests: write
```

## How It Works

1. **Branch setup** — Checks for an existing PR on the update branch. Continues from it if found, or creates a fresh branch from main.
2. **Stack discovery** — Scans the repo for all package managers, Dockerfiles, compose files, and GitHub Actions workflows.
3. **Outdated detection** — Runs outdated commands for each package manager, checks Docker Hub for newer image tags, checks GitHub for newer action versions.
4. **Updates** — Applies updates one by one, using Context7 for migration guides on major bumps. Updates all files referencing the same Docker image for consistency.
5. **Verification** — Discovers project checks from CLAUDE.md, package.json scripts, composer.json scripts, Makefile, and CI configs. Runs them and reverts updates that fail.
6. **Technical debt** — Records any skipped dependencies so future runs know to skip them.
7. **Commit & push** — Creates a dated commit and pushes.
8. **PR** — Creates or updates a PR with structured tables grouping changes by type.

## Major Version Filtering

When `major: false` (default):
- Package managers: skips updates where the major version changes (3.x to 4.x)
- Docker: uses judgment — `php:8.4` to `8.5` is minor, `node:20` to `22` is major
- GitHub Actions: skips major bumps (`@v4` to `@v5`)

When `major: true`: includes everything and uses Context7 to look up migration guides.
