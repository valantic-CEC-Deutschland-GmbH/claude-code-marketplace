# Contributing to Valantic Claude Code Marketplace

## Adding a New Plugin

1. Create a directory under `plugins/` with your plugin name
2. Add `.claude-plugin/plugin.json` with name, description, and author
3. Add your skills (`skills/<name>/SKILL.md`), commands (`commands/<name>.md`), or hooks (`hooks/`)
4. Register the plugin in the root `.claude-plugin/marketplace.json`
5. Submit a pull request for review

## Plugin Structure

```
plugins/your-plugin-name/
├── .claude-plugin/
│   └── plugin.json          # Required: plugin metadata
├── skills/                  # Optional: skill definitions
│   └── skill-name/
│       └── SKILL.md
├── commands/                # Optional: slash commands
│   └── command-name.md
└── hooks/                   # Optional: lifecycle hooks
    ├── hooks.json
    └── script.py
```

## Guidelines

- **SKILL.md** must have YAML frontmatter with `name` and `description`
- **Commands** must have YAML frontmatter with `description` and `allowed-tools`
- **Hook scripts** must use Python standard library only — no pip dependencies
- **Hook scripts** must reference paths using `${CLAUDE_PLUGIN_ROOT}`
- **No secrets** in the repository — use environment variables
- Use **Git LFS** for binary files larger than 1MB (templates, images)

## Testing

Before submitting:

1. Install the plugin locally and verify skills trigger correctly
2. Test all commands and verify `allowed-tools` restrictions
3. Run hook scripts manually to check for errors
4. Ensure no secrets or credentials are included

## Code Review

All changes require at least one review from the marketplace maintainers.
