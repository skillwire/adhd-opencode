# adhd-style for opencode

![License: AGPL-3.0](https://img.shields.io/badge/license-AGPL--3.0-blue.svg)
![Install](https://img.shields.io/badge/install-npx%20skills%20add%20skillwire%2Fadhd--opencode-lightgrey)
![Release](https://img.shields.io/github/v/release/skillwire/adhd-opencode)

ADHD-friendly output styling that actually survives the session: action-first, numbered steps, concrete next actions, time estimates, no preamble. No ADHD diagnosis needed — the style shapes how the agent *talks*, not what it does.

Battle-tested: the ruleset here survived six independent red-team audits against the opencode plugin/skill/gate mechanisms and came out simpler each time.

## Why this exists

- **Answer first.** The first line is the gist, the command, the path. Someone who reads only it has the answer.
- **Short by default.** Say the least that fully answers, then stop. Padding spends attention for nothing.
- **Scannable.** One idea per `**→**` block, bold carrying the whole answer, blank lines between points.
- **Numbers are sacred.** State thresholds exactly; never widen a scoped rule; a warning rides with the point it guards.
- **No fake off.** Safety exceptions (destructive-action confirm, debug spiral, ambiguity) are always on, even in "concise" mode.

## Before / after

The same question — *"how do I speed up my TypeScript build?"* — without and with the style.

| Default | adhd-style |
|---|---|
| A paragraph that opens with context, lists possibilities, buries the recommendation, and closes with "hope this helps" | `**→ Run npx tsc --noEmit and fix what it names.**` then a numbered 1-2-3, a caveat, and one next action. |

Measured on the upstream style this derives from: work unchanged (97%/97% hidden tests), output ~43% shorter, the answer lands in the first line 75% of the time vs 3%. (Self-reported by the upstream benchmark; reproduced in [attention-span](https://github.com/alexgreensh/attention-span).)

## Install (opencode)

### Always-on (recommended) — the style survives compaction, re-injected every turn

```bash
mkdir -p ~/.config/opencode
cp skills/adhd-style/output-style.md ~/.config/opencode/output-style.md
```

Then add to `~/.config/opencode/opencode.jsonc`:

```jsonc
{
  "$schema": "https://opencode.ai/config.json",
  "instructions": ["~/.config/opencode/output-style.md"]
}
```

Restart opencode. That's it — every session, every subagent, compaction-proof.

### On-demand (skill tool / npx skills)

```bash
npx skills add skillwire/adhd-opencode
```

Then load it in a session with the `skill` tool, or set a `/adhd-style` command:

```markdown
# ~/.config/opencode/commands/adhd-style.md
Use the `adhd-style` skill and apply its ruleset for the rest of this session.
```

> Note: on-demand loading applies for the current session only. On long sessions the ruleset can drift — for a persistent default use the always-on install above.

## Contents

| File | What |
|---|---|
| `skills/adhd-style/SKILL.md` | The skill (frontmatter + full ruleset) for the skill tool / `npx skills` |
| `skills/adhd-style/output-style.md` | The style body, no frontmatter — the single source; drop into `instructions` for always-on |
| `install/opencode.jsonc.example` | Minimal wiring example |

## Tune it

The style is a plain markdown body. Fork, edit `skills/adhd-style/output-style.md`, keep your copy. Zero dependencies.

## License & attribution

**AGPL-3.0.** This package is a compressed derivative of [attention-span](https://github.com/alexgreensh/attention-span)'s *Attention-kind* style (AGPL-3.0) folded together with rules from [i-have-adhd](https://github.com/ayghri/i-have-adhd) (MIT). See [NOTICE](NOTICE) and [LICENSE](LICENSE).

For personal use in your own config, nothing further is required. If you redistribute modified versions, AGPL share-alike applies.
