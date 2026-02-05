---
name: valantic-coding-standards
description: Enforces Valantic coding conventions for PHP, TypeScript, Java/Kotlin, and general best practices. Activates when writing or reviewing code.
---

# Valantic Coding Standards

## When to Use

This skill activates automatically when writing, editing, or reviewing code. Apply these standards to all code generated or modified in Valantic projects.

---

## PHP Standards

### General

- **PSR-12** compliance is mandatory
- Always declare `strict_types=1` at the top of every PHP file
- Use `readonly` properties where applicable (PHP 8.1+)
- Prefer named arguments for functions with >3 parameters

### Naming

- Classes: `PascalCase`
- Methods: `camelCase`
- Constants: `UPPER_SNAKE_CASE`
- Variables: `camelCase`
- Interfaces: `PascalCase` with `Interface` suffix (e.g., `OrderRepositoryInterface`)
- Abstract classes: `Abstract` prefix (e.g., `AbstractBaseController`)

### Spryker-Specific

- Follow the module structure: `src/Pyz/{Application}/{Module}/`
- Use transfer objects for data passing between layers
- Business logic belongs in the Business layer, never in Communication or Persistence
- Use dependency providers for cross-module dependencies
- Plugin architecture for extensibility

### Symfony-Specific

- Use attribute-based routing (`#[Route]`)
- Inject dependencies via constructor (no property injection)
- Use DTOs for request/response data, not arrays
- Repository pattern for database access
- Events for cross-cutting concerns

### Error Handling

- Use specific exception classes, not generic `\Exception`
- Log exceptions with context: `$logger->error('Order failed', ['orderId' => $id, 'exception' => $e])`
- Never catch and silently swallow exceptions

---

## TypeScript / React Standards

### General

- **Strict mode** enabled (`"strict": true` in tsconfig.json)
- Prefer `const` over `let`, never use `var`
- Use explicit return types on exported functions
- Prefer `interface` over `type` for object shapes (extendable)

### React

- **Functional components only** (no class components)
- Use hooks for state and side effects
- Component file naming: `PascalCase.tsx` (e.g., `OrderList.tsx`)
- One component per file
- Props interface: `ComponentNameProps` (e.g., `OrderListProps`)

### Naming

- Components: `PascalCase`
- Hooks: `camelCase` with `use` prefix (e.g., `useOrderData`)
- Utilities: `camelCase`
- Constants: `UPPER_SNAKE_CASE`
- Types/Interfaces: `PascalCase`
- Enums: `PascalCase` with `PascalCase` members

### State Management

- Local state: `useState` / `useReducer`
- Server state: React Query / SWR (not Redux for API data)
- Global state: Context API or Zustand (Redux only for complex flows)

### Error Handling

- Use Error Boundaries for component-level errors
- API errors: Handle in the calling hook, expose via return value
- Never use `try/catch` to silently ignore errors

---

## Java / Spring Boot Standards

### General

- Java 17+ or Kotlin
- Use Spring Boot starters for common functionality
- Prefer constructor injection (`@RequiredArgsConstructor` with Lombok)
- Use `@ConfigurationProperties` for externalized config

### Naming

- Classes: `PascalCase`
- Methods: `camelCase`
- Constants: `UPPER_SNAKE_CASE`
- Packages: `lowercase.dotted`
- Controllers: `*Controller`
- Services: `*Service`
- Repositories: `*Repository`

### Architecture

- Controller → Service → Repository layering
- DTOs for API request/response (never expose entities directly)
- Use `@Transactional` at the service layer
- Validate inputs with `@Valid` and Bean Validation annotations

### Error Handling

- Use `@ControllerAdvice` for global exception handling
- Define custom exception classes extending `RuntimeException`
- Return proper HTTP status codes (not always 200)
- Log with SLF4J: `log.error("Order processing failed", e)`

---

## General Best Practices (All Languages)

### Security

- Never hardcode secrets — use environment variables
- Validate all external input (user input, API responses, file content)
- Use parameterized queries (no string concatenation for SQL)
- Sanitize output to prevent XSS
- Use HTTPS for all external communication

### Logging

- Use structured logging (JSON format in production)
- Log levels: ERROR (failures), WARN (degraded), INFO (operations), DEBUG (development)
- Include correlation/trace IDs in log context
- Never log sensitive data (passwords, tokens, PII)

### Testing

- Unit tests for business logic (>80% coverage target)
- Integration tests for API endpoints and database queries
- Name tests descriptively: `should_returnError_when_orderNotFound`
- Arrange-Act-Assert pattern
- Use factories/builders for test data, not hardcoded values

### Git

- Branch naming: `feature/TICKET-123-short-description`, `bugfix/TICKET-456-fix-name`
- Commit messages: imperative mood, reference ticket number
- Keep commits atomic — one logical change per commit
- Squash fixup commits before merging
