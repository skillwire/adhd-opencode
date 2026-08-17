# SPDX-FileCopyrightText: 2026 Yuri Shubin
# SPDX-License-Identifier: AGPL-3.0-only
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
errors = []


def frontmatter(path: Path):
    text = path.read_text()
    m = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n", text, re.S)
    if not m:
        return None, text
    fm = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, _, v = line.partition(":")
            fm[k.strip()] = v.strip().strip("'\"")
    return fm, text[m.end() :]


# 1. SKILL.md frontmatter
skill = ROOT / "skills" / "adhd-style" / "SKILL.md"
if not skill.exists():
    errors.append("SKILL.md missing")
else:
    fm, _ = frontmatter(skill)
    if fm is None:
        errors.append("SKILL.md: no YAML frontmatter (--- ... ---)")
    else:
        for k in ("name", "description", "license"):
            if k not in fm:
                errors.append(f"SKILL.md: missing frontmatter '{k}'")
        if fm.get("name") != "adhd-style":
            errors.append(f"SKILL.md: name '{fm.get('name')}' != folder 'adhd-style'")

# 2. canonical style file: all required sections present
style = ROOT / "skills" / "adhd-style" / "output-style.md"
if not style.exists():
    errors.append("skills/adhd-style/output-style.md missing (single source)")
else:
    stext = style.read_text()
    for sec in (
        "## Delivery",
        "## Format",
        "## Multi-step work",
        "## Pre-send check",
        "## Safety exceptions",
    ):
        if sec not in stext:
            errors.append(f"output-style.md: missing section '{sec}'")
    # cross-harness: no YAML frontmatter (so it can be appended to any harness
    # rules file directly) and no harness-specific template syntax
    if re.match(r"^---\r?\n", stext):
        errors.append("output-style.md must NOT have YAML frontmatter (plain body for all harnesses)")
    if "{{" in stext or "}}" in stext:
        errors.append("output-style.md: contains harness template placeholders {{ }}")
    # strip test: first line is a comment, the rest must be plain markdown
    body = re.sub(r"^<!--.*?-->\s*\n", "", stext, count=1, flags=re.S)
    if not body.strip():
        errors.append("output-style.md: empty body after strip")

# 3. no duplicated root copy (single source of truth)
if (ROOT / "output-style.md").exists():
    errors.append("root output-style.md must be removed; single source lives in skills/adhd-style/")

# 4. LICENSE present
if not (ROOT / "LICENSE").exists():
    errors.append("LICENSE missing")
if not (ROOT / "NOTICE").exists():
    errors.append("NOTICE missing")

if errors:
    print("Validation FAILED:")
    print("\n".join("  - " + e for e in errors))
    sys.exit(1)
print("OK: skill valid, single source, license+notice present")
