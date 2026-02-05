---
description: Guided deployment with environment checks, pre-flight validation, and rollback support
argument-hint: [environment] (e.g., staging, production)
allowed-tools: [Bash(git:*), Bash(docker:*), Bash(kubectl:*), Bash(ssh:*), Read, Glob, Grep]
---

## Your task

You are helping a developer deploy their application. Follow this structured deployment workflow:

### 1. Pre-flight Checks

- Verify the current branch and git status (no uncommitted changes)
- Check that the target environment argument is valid (staging, production, or custom)
- Look for deployment configuration files (e.g., `docker-compose.yml`, `Dockerfile`, `k8s/`, `.github/workflows/`, `deploy/`)
- Verify the latest CI/CD pipeline status if applicable

### 2. Environment Validation

- Confirm the target environment with the user before proceeding
- For **production** deployments, require explicit confirmation: "You are about to deploy to PRODUCTION. Please confirm by typing 'yes'."
- Check for environment-specific configuration files
- Verify required environment variables are documented (do NOT display secret values)

### 3. Deployment Execution

- Show the deployment command that will be executed
- Execute the deployment step by step, providing status updates
- If using Docker: build, tag, and push the image
- If using Kubernetes: apply manifests with `--dry-run=client` first
- If using git-based deployment: push to the appropriate branch

### 4. Post-deployment Verification

- Check deployment status (container health, pod status, etc.)
- Verify the application is responding (health check endpoint if available)
- Show relevant logs from the deployment

### 5. Rollback Plan

- If anything fails, present the rollback options:
  - Git: revert to previous commit
  - Docker: retag previous image
  - Kubernetes: `kubectl rollout undo`
- Do NOT execute rollback without user confirmation

### Important Rules

- NEVER deploy to production without explicit user confirmation
- NEVER expose secrets, tokens, or passwords in output
- Always show a dry-run or preview before executing destructive commands
- Log all deployment steps for audit trail
