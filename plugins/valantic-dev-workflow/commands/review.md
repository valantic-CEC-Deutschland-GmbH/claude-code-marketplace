---
description: Structured code review against Valantic coding standards and best practices
argument-hint: [file or PR number]
allowed-tools: [Bash(git diff:*), Bash(git log:*), Bash(gh pr:*), Read, Glob, Grep]
---

## Your task

You are performing a structured code review. Follow this checklist:

### 1. Gather Context

- If a PR number is provided, fetch the PR details with `gh pr view`
- If a file path is provided, read the file and its recent git history
- If no argument, review the current staged/unstaged changes via `git diff`
- Identify the programming language and applicable standards

### 2. Review Checklist

Evaluate the code against these categories:

#### Correctness
- [ ] Logic errors or edge cases
- [ ] Null/undefined handling
- [ ] Error handling completeness
- [ ] Resource cleanup (connections, file handles)

#### Security
- [ ] No hardcoded secrets or credentials
- [ ] Input validation at system boundaries
- [ ] SQL injection, XSS, or command injection risks
- [ ] Proper authentication/authorization checks

#### Code Quality
- [ ] Naming conventions (per language standards)
- [ ] Function/method length (max ~30 lines recommended)
- [ ] Single responsibility principle
- [ ] No unnecessary complexity or premature abstractions
- [ ] Dead code or unused imports

#### Testing
- [ ] Test coverage for new/changed code
- [ ] Edge cases tested
- [ ] Test names describe the behavior being tested

#### Valantic Standards
- [ ] PHP: PSR-12, strict types, proper Spryker/Symfony patterns
- [ ] TypeScript: Strict mode, functional components, proper typing
- [ ] Java: Spring Boot conventions, proper annotations
- [ ] General: Consistent error handling, structured logging

### 3. Output Format

Present findings as:

```
## Review Summary

**Files reviewed**: [count]
**Overall**: [APPROVE / REQUEST CHANGES / COMMENT]

### Issues Found

#### Critical (must fix)
- [file:line] Description

#### Suggestions (nice to have)
- [file:line] Description

### Positive Highlights
- What's done well
```

### Important Rules

- Be constructive, not nitpicky
- Focus on issues that matter (bugs, security, maintainability)
- Don't suggest style changes that contradict existing project patterns
- Praise good practices when you see them
