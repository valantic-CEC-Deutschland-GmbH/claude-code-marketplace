# PHP Project Template (Spryker / Symfony)

## Project Structure

```
{project-name}/
├── .github/
│   └── workflows/
│       └── ci.yml
├── config/
│   ├── packages/
│   │   ├── doctrine.yaml
│   │   ├── framework.yaml
│   │   └── security.yaml
│   ├── routes.yaml
│   └── services.yaml
├── docker/
│   ├── php/
│   │   └── Dockerfile
│   ├── nginx/
│   │   └── default.conf
│   └── docker-compose.yml
├── migrations/
├── public/
│   └── index.php
├── src/
│   ├── Controller/
│   ├── DTO/
│   ├── Entity/
│   ├── Repository/
│   ├── Service/
│   ├── EventListener/
│   └── Kernel.php
├── tests/
│   ├── Unit/
│   ├── Integration/
│   └── bootstrap.php
├── .env.example
├── .gitignore
├── .php-cs-fixer.dist.php
├── CLAUDE.md
├── README.md
├── composer.json
├── phpstan.neon
└── phpunit.xml.dist
```

## Key Configuration Files

### composer.json

```json
{
  "require": {
    "php": ">=8.2",
    "symfony/framework-bundle": "^7.0",
    "symfony/orm-pack": "^2.0",
    "symfony/validator": "^7.0"
  },
  "require-dev": {
    "phpstan/phpstan": "^1.0",
    "friendsofphp/php-cs-fixer": "^3.0",
    "phpunit/phpunit": "^10.0",
    "symfony/test-pack": "^1.0"
  },
  "autoload": {
    "psr-4": {
      "App\\": "src/"
    }
  },
  "autoload-dev": {
    "psr-4": {
      "App\\Tests\\": "tests/"
    }
  }
}
```

### .php-cs-fixer.dist.php

```php
<?php

declare(strict_types=1);

$finder = PhpCsFixer\Finder::create()
    ->in(__DIR__ . '/src')
    ->in(__DIR__ . '/tests');

return (new PhpCsFixer\Config())
    ->setRules([
        '@PSR12' => true,
        'strict_param' => true,
        'declare_strict_types' => true,
        'array_syntax' => ['syntax' => 'short'],
        'no_unused_imports' => true,
        'ordered_imports' => ['sort_algorithm' => 'alpha'],
        'single_quote' => true,
    ])
    ->setFinder($finder)
    ->setRiskyAllowed(true);
```

### phpstan.neon

```neon
parameters:
    level: 8
    paths:
        - src
    checkGenericClassInNonGenericObjectType: false
```

### .env.example

```env
# Application
APP_ENV=dev
APP_SECRET=change-me-in-local-env
APP_DEBUG=1

# Database
DATABASE_URL="postgresql://user:password@localhost:5432/dbname?serverVersion=15"

# Redis (if applicable)
REDIS_URL=redis://localhost:6379

# External Services
# API_KEY=your-api-key-here
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
      - uses: shivammathur/setup-php@v2
        with:
          php-version: '8.2'
      - run: composer install --no-progress
      - run: vendor/bin/php-cs-fixer fix --dry-run --diff
      - run: vendor/bin/phpstan analyse
      - run: vendor/bin/phpunit
```
