# valantic-fast-tools

Makes every Claude Code agent use modern, fast CLI tools instead of the slow classics. Agents (especially the built-in exploration agents) habitually run `grep`, `find`, and `cat` - even when much faster alternatives are installed. This plugin enforces the fast tools deterministically.

## Why (the improvements)

| Slow default | Enforced alternative | Improvement |
|---|---|---|
| `grep -r pattern .` | `rg pattern` | ripgrep is typically 5-50x faster, respects `.gitignore`, skips binaries |
| `find . -name '*.ts'` | `fd -e ts` | parallel traversal, `.gitignore`-aware, simpler syntax |
| `cat file` (viewing) | `bat -n file` / Read tool | line numbers and syntax highlighting for the agent's context |
| `ls -R` | `tree -L 2` / `fd` | bounded, readable output instead of unbounded recursion |

Faster searches mean agents build up context in fewer, cheaper, quicker tool calls - most noticeable in plan mode and large repositories.

Background: the built-in `Explore` and `Plan` subagents skip your global `CLAUDE.md` by design ([docs](https://code.claude.com/docs/en/sub-agents)), so tool preferences written there never reach them. A PreToolUse hook runs at harness level and therefore applies to **all** agents - built-in, custom, and workflow subagents. This is the same mechanism as Anthropic's official [bash_command_validator example](https://github.com/anthropics/claude-code/blob/main/examples/hooks/bash_command_validator_example.py).

## What happens automatically (on install)

1. **PreToolUse hook on Bash** (`hooks/enforce-fast-tools.sh`): blocks slow commands and tells the agent what to use instead - the agent self-corrects and retries. Intercepted (only when the fast alternative is installed on your machine - the hook is binary-aware and degrades gracefully):
   - `grep` / `egrep` / `fgrep` / `git grep` -> `rg`
   - `find` -> `fd`
   - bare `cat <file>` (viewing) -> `bat -n` or the Read tool. `cat` in pipelines and heredocs stays allowed.
   - recursive `ls -R` -> `tree` / `fd`
2. **Three exploration agents** are registered (`code-explorer`, `code-architect`, `code-reviewer`): general-purpose codebase analysis/design/review agents that load your CLAUDE.md and prefer rg/fd/bat. They serve as replacements if you disable the built-in Explore/Plan agents (see manual steps).

Escape hatch: when classic semantics are genuinely needed (e.g. `grep -oP` extraction), append `# allow-slow-tools` to the command and the hook lets it through.

## What you need to do manually

**1. Install the fast tools** (the hook only enforces what is installed):

```bash
# Arch
sudo pacman -S ripgrep fd bat tree jq
# Debian / Ubuntu (fd binary is named fdfind - symlink it to fd)
sudo apt install ripgrep fd-find bat tree jq
# macOS
brew install ripgrep fd bat tree jq
```

`jq` is required by the hook itself (without it the hook allows everything).

**2. Optional but recommended - add to your `~/.claude/settings.json`** (plugins cannot change your personal permissions or environment):

```json
{
  "env": {
    "USE_BUILTIN_RIPGREP": "0"
  },
  "permissions": {
    "deny": ["Agent(Explore)", "Agent(Plan)"]
  }
}
```

- `USE_BUILTIN_RIPGREP=0`: the native Grep tool uses your system ripgrep instead of the bundled binary.
- `deny: Agent(Explore)/Agent(Plan)`: disables the built-in exploration agents (which ignore your CLAUDE.md); Claude then falls back to this plugin's `code-explorer`/`code-architect` and `general-purpose`, which all load your CLAUDE.md. Trade-off: somewhat more tokens per exploration. Remove the two entries to revert.

**3. Restart Claude Code** - hooks and settings are read at session start.

## Verify it works

Ask Claude to run `grep -r foo .` in any session. You should see the hook block it with a `Blocked (slow tool): use rg ...` message, and Claude retrying with `rg`.
