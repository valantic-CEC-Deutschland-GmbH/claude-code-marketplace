# Valantic GitHub Agents

Centralized collection of autonomous GitHub Actions agents powered by Claude Code CLI.

## Purpose

This repository serves as the **single source of truth** for reusable AI-powered GitHub Actions workflows at Valantic. Instead of duplicating agent logic across dozens of repositories, each project only needs a thin caller workflow (3-5 lines of YAML) that references the reusable workflow hosted here.

**Why centralize?**

- **One update, all repos benefit** — Fix a bug or improve an agent prompt once, and every consuming repository picks it up automatically (or pins to a tag for stability).
- **Consistent behavior** — All teams get the same agent capabilities, prompt engineering, and MCP tool configurations.
- **Lower maintenance** — No need to copy-paste workflows, keep forks in sync, or debug drift between repo-local copies.
- **Easier auditing** — Security reviews, permission scoping, and prompt changes happen in one place.

## Available Agents

| Agent | Workflow | Description |
|-------|----------|-------------|
| [Updater Agent](agents/updater-agent/) | `updater-agent.yml` | Autonomous dependency updates for package managers, Docker images, and GitHub Actions |

### Updater Agent

Reusable GitHub Actions workflow that uses Claude Code CLI to autonomously update all project dependencies — package managers, Docker images, and GitHub Actions — and create a PR with the results.

**Highlights:**
- Stack-agnostic: composer, npm, yarn, pnpm, pip, go, cargo, gradle, maven, bundler, and more
- Docker-aware: updates Dockerfile base images and compose service images
- GitHub Actions: updates action version pins in workflow files
- Autonomous verification: discovers and runs linters, tests, and build checks — reverts updates that break them
- Migration-aware: uses Context7 MCP to look up migration guides for major version bumps

**Quick start** — add this to `.github/workflows/updater-agent.yml` in your repository:

```yaml
name: Updater Agent

on:
  workflow_dispatch:
    inputs:
      major:
        description: 'Include major version updates'
        type: boolean
        default: false

permissions:
  contents: write
  pull-requests: write

jobs:
  update-dependencies:
    uses: valantic-CEC-Deutschland-GmbH/claude-code-marketplace/.github/workflows/updater-agent.yml@main
    with:
      major: ${{ inputs.major }}
    secrets:
      CLAUDE_CODE_OAUTH_TOKEN: ${{ secrets.CLAUDE_CODE_OAUTH_TOKEN }}
```

See [agents/updater-agent/README.md](agents/updater-agent/README.md) for full documentation (inputs, secrets, permissions, how it works).

## Adding More Agents

This collection will grow over time. New agents follow the same pattern:

1. Create `agents/<agent-name>/` with a `PROMPT.md`, `README.md`, and optional `mcp-config.json`
2. Add a reusable workflow in `.github/workflows/<agent-name>.yml`
3. Consuming repos add a thin caller workflow referencing the reusable one

## Additional Resources

For more examples of autonomous GitHub-integrated agents, see the **GitHub AW workflows** collection:

- [github/gh-aw — .github/workflows](https://github.com/github/gh-aw/tree/main/.github/workflows)

These workflows demonstrate additional patterns for AI-powered automation running directly in GitHub Actions.
