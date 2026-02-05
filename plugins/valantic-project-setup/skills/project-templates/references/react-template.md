# React Project Template (Next.js / Vite)

## Project Structure

```
{project-name}/
├── .github/
│   └── workflows/
│       └── ci.yml
├── public/
│   └── favicon.ico
├── src/
│   ├── components/
│   │   ├── ui/              # Reusable UI components
│   │   └── layout/          # Layout components (Header, Footer, Sidebar)
│   ├── hooks/               # Custom React hooks
│   ├── lib/                 # Utility functions and helpers
│   ├── pages/               # Page components (or app/ for Next.js App Router)
│   ├── services/            # API client and service functions
│   ├── stores/              # State management (Zustand/Context)
│   ├── types/               # TypeScript type definitions
│   ├── styles/              # Global styles and theme
│   │   └── globals.css
│   └── App.tsx              # Root component (Vite) or layout.tsx (Next.js)
├── tests/
│   ├── components/
│   ├── hooks/
│   └── setup.ts
├── .env.example
├── .eslintrc.json
├── .gitignore
├── .prettierrc
├── CLAUDE.md
├── Dockerfile
├── README.md
├── docker-compose.yml
├── package.json
├── tsconfig.json
└── vitest.config.ts
```

## Key Configuration Files

### package.json

```json
{
  "name": "{project-name}",
  "private": true,
  "version": "0.1.0",
  "scripts": {
    "dev": "vite",
    "build": "tsc && vite build",
    "preview": "vite preview",
    "test": "vitest",
    "test:coverage": "vitest --coverage",
    "lint": "eslint src --ext .ts,.tsx",
    "lint:fix": "eslint src --ext .ts,.tsx --fix",
    "format": "prettier --write 'src/**/*.{ts,tsx,css,json}'"
  },
  "dependencies": {
    "react": "^18.0.0",
    "react-dom": "^18.0.0",
    "react-router-dom": "^6.0.0",
    "@tanstack/react-query": "^5.0.0",
    "zustand": "^4.0.0"
  },
  "devDependencies": {
    "@types/react": "^18.0.0",
    "@types/react-dom": "^18.0.0",
    "@typescript-eslint/eslint-plugin": "^7.0.0",
    "@typescript-eslint/parser": "^7.0.0",
    "@testing-library/react": "^14.0.0",
    "@testing-library/jest-dom": "^6.0.0",
    "eslint": "^8.0.0",
    "eslint-plugin-react-hooks": "^4.0.0",
    "prettier": "^3.0.0",
    "typescript": "^5.0.0",
    "vite": "^5.0.0",
    "vitest": "^1.0.0"
  }
}
```

### tsconfig.json

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "module": "ESNext",
    "skipLibCheck": true,
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "jsx": "react-jsx",
    "strict": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noFallthroughCasesInSwitch": true,
    "paths": {
      "@/*": ["./src/*"]
    }
  },
  "include": ["src"]
}
```

### .eslintrc.json

```json
{
  "extends": [
    "eslint:recommended",
    "plugin:@typescript-eslint/recommended",
    "plugin:react-hooks/recommended"
  ],
  "parser": "@typescript-eslint/parser",
  "plugins": ["@typescript-eslint"],
  "rules": {
    "no-console": "warn",
    "@typescript-eslint/no-explicit-any": "error",
    "@typescript-eslint/explicit-function-return-type": ["warn", {
      "allowExpressions": true,
      "allowTypedFunctionExpressions": true
    }],
    "react-hooks/exhaustive-deps": "warn"
  }
}
```

### .env.example

```env
# API
VITE_API_BASE_URL=http://localhost:3000/api

# Feature Flags
VITE_ENABLE_ANALYTICS=false

# Auth (if applicable)
# VITE_AUTH_PROVIDER_URL=https://auth.example.com
```

### CI Pipeline (.github/workflows/ci.yml)

```yaml
name: CI
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'
      - run: npm ci
      - run: npm run lint
      - run: npm run build
      - run: npm run test -- --run
```
