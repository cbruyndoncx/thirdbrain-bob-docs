---
type: knowledge-base
title: "Symlink Setup — Skills Access for AI Tools"
status: final
created: 2026-04-28
modified: 2026-09-01
tags: [setup, symlinks, skills, troubleshooting]
---

# Symlink Setup — Skills Access for AI Tools

> **Folder names below are the default (numbered) layout that BOB ships with.** A workspace
> with its own context pack names the folders differently — `uv run 00-CORE/Agents/skills/context-pack/scripts/resolve_context.py --key skills.root`
> prints the real path for the key named in each case.

For AI assistants (Claude Code, Codex, Gemini CLI) to discover vault skills, each tool's skill
directory must be a link pointing to `00-CORE/Agents/skills/`.

*   **Claude Code:** `.claude/skills`
*   **Gemini CLI:** `.gemini/skills`
*   **Codex:** `.codex/skills`

**This vault comes pre-configured**, and `bob-install`'s `setup.sh` creates these links for you.
Use this guide only if skills aren't loading.

> [!important] Windows: use a junction, not a symlink
> If you are on Windows — especially running **Claude Cowork** or any Windows-native client — the
> link must be a **junction**. A WSL `ln -s` symlink is followable only by WSL; Windows reads it as
> an empty directory, so the client loads **zero skills and reports no error**.
>
> [[SYMLINK-SETUP.md|SYMLINK-SETUP]] is the canonical reference — filesystem matrix, the WSL/Win32
> explanation, and how to verify a link from the Windows side. Read it before troubleshooting a
> Windows install.

---

## Quick Check

```bash
# From vault root — check AI platform links
ls -la .claude/skills .gemini/skills .codex/skills 2>/dev/null

# Should show something like:
# .claude/skills -> 00-CORE/Agents/skills
```

If you see the skills folder contents, you're done. If not, recreate the links below.

**On Windows, a passing `ls` under WSL proves nothing** — it only shows that WSL can follow the
link. Verify from Windows as described in [[SYMLINK-SETUP.md|SYMLINK-SETUP]].

---

## Create the Links

`bob-install`'s `setup.sh` creates these for you. To do it by hand, the commands for every
platform live in **one place** — [[SYMLINK-SETUP.md|SYMLINK-SETUP]].

They are not repeated here on purpose. This page had its own copy until 2026-09-01, and that copy
had fallen a full revision behind: it never mentioned junctions, told Windows users they needed
Administrator rights, and named a directory the tooling does not read.

**The one thing to know before you go there:** on Windows use a **junction** (`mklink /J`). It
needs no elevation and resolves from both WSL and Windows. A WSL `ln -s` symlink is invisible to
Windows-native clients, which then load zero skills without erroring.

---

## Verify Skills Are Working

1. **List available skills:**
   ```bash
   ls .claude/skills/
   ```
   Should show folders like `business-baseline/`, `copywriting/`, etc.

2. **Restart your AI tool** (Claude Code, Codex, or Gemini CLI)

3. **Ask the AI:** "What skills are available?" — should list skills from `00-CORE/Agents/skills/`

4. **Try a skill:** "Run a business baseline" — the AI should recognise and activate it

---

## Troubleshooting

| Symptom | Fix |
|---------|-----|
| `ls: cannot access .claude/skills` | Link missing — run Create the Links above |
| Link exists but skills don't load | Check the target: `readlink -f .claude/skills` — must point to `00-CORE/Agents/skills` |
| Skills load but AI ignores them | Restart the AI tool; it caches skill definitions at session start |
| **Windows client sees zero skills, no error** | The link is a WSL symlink, not a junction. Recreate with `mklink /J` — see [[SYMLINK-SETUP.md\|SYMLINK-SETUP]] |
| Permission denied creating a link on Windows | You are creating a symlink, not a junction. `mklink /J` needs no elevation |

## Related

- [[SYMLINK-SETUP.md|SYMLINK-SETUP]] — canonical reference: filesystem matrix, WSL/Win32 behaviour, Windows-side verification
- [[bob-doctor]] — checks these links as part of environment readiness
