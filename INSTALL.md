# Install

## Prerequisites

- [opencode](https://opencode.ai) 1.18.x or newer.

## Option 1 — Always-on (recommended)

The style is loaded as an instruction file: re-injected into the system prompt every turn, survives compaction, and applies to subagents too.

```bash
mkdir -p ~/.config/opencode
cp output-style.md ~/.config/opencode/output-style.md
```

Add the `instructions` key to `~/.config/opencode/opencode.jsonc` (create the file if missing):

```jsonc
{
  "$schema": "https://opencode.ai/config.json",
  "instructions": ["~/.config/opencode/output-style.md"]
}
```

Restart opencode. Verify in any session: ask the agent to quote the first line of its style instructions.

**To disable:** remove the `instructions` entry (or delete the file). The style is inert when not loaded.

## Option 2 — On-demand (skill tool)

```bash
npx skills add agentic-society/opencode-adhd-style
```

or copy manually:

```bash
mkdir -p ~/.config/opencode/skills/adhd-style
cp skills/adhd-style/SKILL.md ~/.config/opencode/skills/adhd-style/SKILL.md
```

Load it in a session via the `skill` tool, or add a convenience command:

```markdown
# ~/.config/opencode/commands/adhd-style.md
---
description: Apply the adhd-style output ruleset for the rest of this session
---
Use the `adhd-style` skill and apply its ruleset for the rest of this session, until the user says "stop adhd mode".
```

**Trade-off:** on-demand rulesets live in message history and can drift on long/compacted sessions. For a reliable default, prefer Option 1.

## Option 3 — Other harnesses

`output-style.md` is plain markdown with no opencode-specific syntax. Append it to your harness rules file:

- **Claude Code:** `~/.claude/CLAUDE.md` or `~/.claude/output-styles/*.md`
- **Codex / AGENTS.md harnesses:** append to `~/.codex/AGENTS.md` (or your global `AGENTS.md`) inside `<!-- adhd-style:start -->` / `<!-- adhd-style:end -->` fences
- **Gemini CLI:** append to `~/.gemini/GEMINI.md`

## Updating

```bash
curl -sfL https://raw.githubusercontent.com/shhubin/opencode-adhd-style/main/output-style.md \
  -o ~/.config/opencode/output-style.md
```

If you keep the config directory under git (`git init`), `git diff` shows exactly what changed — recommended, since instruction files fail silently if removed.

## Uninstall

- Option 1: remove the `instructions` entry and `~/.config/opencode/output-style.md`.
- Option 2: `npx skills remove adhd-style` or delete `~/.config/opencode/skills/adhd-style/`.
