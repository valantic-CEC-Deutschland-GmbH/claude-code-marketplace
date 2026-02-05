---
description: New developer onboarding checklist — guides through project setup, tools, and conventions
argument-hint: [project-name]
allowed-tools: [Bash(git:*), Bash(docker:*), Bash(npm:*), Bash(composer:*), Bash(mvn:*), Bash(gradle:*), Read, Glob, Grep]
---

## Your task

You are onboarding a new developer to a Valantic project. Walk them through the following checklist interactively.

### 1. Project Discovery

- Identify the project type by examining the root directory:
  - `composer.json` → PHP (Spryker/Symfony)
  - `package.json` → JavaScript/TypeScript (React/Next.js)
  - `pom.xml` or `build.gradle` → Java/Kotlin (Spring Boot)
- Read the project README if it exists
- Check for existing documentation in `docs/`, `CONTRIBUTING.md`, or `CLAUDE.md`

### 2. Environment Setup Checklist

Present this checklist and help the developer complete each step:

#### General
- [ ] Git configured (name, email, SSH keys)
- [ ] Access to the GitHub/GitLab repository
- [ ] IDE installed and configured (PHPStorm / VS Code / IntelliJ)
- [ ] Docker and Docker Compose installed

#### PHP Projects
- [ ] PHP 8.1+ installed
- [ ] Composer installed
- [ ] `composer install` runs successfully
- [ ] Database migrations applied
- [ ] `.env` file created from `.env.example`

#### TypeScript/React Projects
- [ ] Node.js 18+ installed (via nvm recommended)
- [ ] `npm install` or `yarn install` runs successfully
- [ ] `.env.local` created from `.env.example`
- [ ] Development server starts (`npm run dev`)

#### Java/Spring Projects
- [ ] JDK 17+ installed
- [ ] Maven/Gradle build succeeds
- [ ] `application-local.yml` configured
- [ ] Application starts locally

### 3. Coding Standards Orientation

- Explain the project's coding standards (reference `valantic-coding-standards` plugin)
- Show linting/formatting configuration
- Explain the git branching model used
- Show how to run tests

### 4. Key Architecture Walkthrough

- Identify and explain the main directory structure
- Point out key configuration files
- Explain the deployment pipeline
- List important external services and how to access them (without sharing secrets)

### 5. First Task Suggestion

- Suggest a good "first issue" or starter task
- Walk through the development → PR → review → merge cycle

### Important Rules

- Never share or display actual secrets, tokens, or passwords
- If `.env.example` is missing, flag it as a project improvement opportunity
- Be patient and thorough — this is someone's first day
