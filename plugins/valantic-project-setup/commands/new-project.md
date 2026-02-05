---
description: Bootstrap a new project with Valantic templates — supports PHP, React, and Spring Boot
argument-hint: <project-name> [--type php|react|spring]
allowed-tools: [Bash(git:*), Bash(mkdir:*), Bash(composer:*), Bash(npm:*), Bash(npx:*), Bash(mvn:*), Bash(gradle:*), Read, Write, Glob, Grep]
---

## Your task

You are scaffolding a new Valantic project. Follow this workflow:

### 1. Gather Project Information

If not provided via arguments, ask the user:

- **Project name**: lowercase-kebab-case (e.g., `order-management-api`)
- **Project type**: PHP (Spryker/Symfony), React (Next.js/Vite), or Spring Boot (Java/Kotlin)
- **Description**: One-line project description
- **Team**: Which Valantic team owns this project

### 2. Create Project Structure

Based on the selected type, scaffold the project using the reference templates:

- **PHP**: Read `references/php-template.md` for the project structure
- **React**: Read `references/react-template.md` for the project structure
- **Spring Boot**: Read `references/spring-template.md` for the project structure

### 3. Initialize the Project

- Create the directory structure
- Initialize git repository
- Create initial files (README, .gitignore, .env.example, CLAUDE.md)
- Set up linting and formatting configuration
- Create a basic CI/CD pipeline configuration

### 4. Apply Valantic Standards

- Set up coding standards configuration (reference `valantic-coding-standards` plugin)
- Configure pre-commit hooks where applicable
- Add Valantic-specific README sections (team, deployment, contact)

### 5. Final Steps

- Show the created project structure
- Provide next steps for the developer:
  1. Install dependencies
  2. Configure environment variables
  3. Run the development server
  4. Create the first feature branch

### Important Rules

- Always use the Valantic project structure templates
- Include `.env.example` with documented variables (no actual secrets)
- Include a `CLAUDE.md` with project-specific instructions for Claude
- Set up `.gitignore` appropriate for the project type
