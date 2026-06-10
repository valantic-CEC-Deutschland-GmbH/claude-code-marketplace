#!/usr/bin/env bash
# PreToolUse hook for the Bash tool: blocks slow CLI commands when a faster
# alternative is installed and tells the agent what to use instead.
#
# Contract: tool-call JSON on stdin; exit 0 allows the command, exit 2 blocks
# it and feeds the stderr message back to the agent so it can retry.
# Applies to every agent (built-in Plan/Explore, custom, workflow subagents).
#
# Escape hatch: append "# allow-slow-tools" to the command.

set -u

deny() {
	printf '%s\n' "$1" >&2
	exit 2
}

command -v jq > /dev/null || exit 0

cmd=$(jq -r '.tool_input.command // empty' 2> /dev/null) || exit 0
[[ -n $cmd ]] || exit 0
[[ $cmd == *'# allow-slow-tools'* ]] && exit 0

# command position: string start, or after | ; & ` ( or newline
pos=$'(^|[|;&`(\n])[[:space:]]*'

if command -v rg > /dev/null; then
	if [[ $cmd =~ ${pos}(grep|egrep|fgrep)[[:space:]] ]] ||
		[[ $cmd =~ ${pos}git[[:space:]]+grep[[:space:]] ]]; then
		deny "Blocked (slow tool): use rg (ripgrep) instead of grep. Examples: rg -n 'pattern' --glob '!node_modules/*' | rg -i 'pattern' (case-insensitive) | rg -l 'pattern' (list files). Bulk edits: rg -l 'old' | parallel -j16 sed -i 's/old/new/g' {}. If grep semantics are truly required, append: # allow-slow-tools"
	fi
fi

if command -v fd > /dev/null && [[ $cmd =~ ${pos}find[[:space:]] ]]; then
	deny "Blocked (slow tool): use fd instead of find. Examples: fd 'name' | fd -e ts src/ | fd -e ts -x wc -l {}. fd respects .gitignore and is much faster. If find semantics are truly required, append: # allow-slow-tools"
fi

if command -v bat > /dev/null &&
	[[ $cmd =~ ^[[:space:]]*cat[[:space:]] ]] &&
	[[ $cmd != *'|'* ]] && [[ $cmd != *'<<'* ]]; then
	deny "Blocked (slow tool): use bat -n <file> or the Read tool instead of bare cat for viewing files. cat in pipelines (cat f | sed ... | sponge f) and heredocs are allowed."
fi

ls_recursive=$pos'ls[[:space:]]+[^|;&]*-[a-zA-Z]*R'
if command -v tree > /dev/null && [[ $cmd =~ $ls_recursive ]]; then
	deny "Blocked (slow tool): use tree -L 2 -I 'node_modules' or fd instead of recursive ls -R."
fi

exit 0
