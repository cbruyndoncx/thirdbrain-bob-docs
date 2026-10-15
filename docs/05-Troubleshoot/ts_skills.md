---
title: Troubleshooting — Skills
---

# Troubleshooting — Skills

> **Folder names below are the default (numbered) layout that BOB ships with.** A workspace
> with its own context pack names the folders differently — `uv run 00-CORE/Agents/skills/context-pack/scripts/resolve_context.py --key skills.root`
> prints the real path for the key named in each case.

## BOB can't find skills / "I don't have a skill for that"

1. Verify the symlink exists: `ls -la .claude/skills` — should show `-> .../00-CORE/Agents/skills`
2. Restart your AI tool (it caches skill definitions at session start)
3. Ask directly: "What skills are available?" to confirm skills are loaded

For symlink check and recreate commands: [symlink_setup](../02-Setup/symlink_setup.md)

---

## AI ignores skills / picks wrong skill

- Be explicit: `/skill-name` to invoke a specific skill directly
- Check the skill exists: `ls .claude/skills/` — skill folder must be present
- Some skills are disabled — see `SKILLS.md` at vault root for enabled skills

---

## Skill runs but produces wrong output

- The skill may need vault context — point BOB at relevant files:
  `"Using 30-CLIENTS/acme-corp/, draft an upsell proposal"`
- Check the skill's `SKILL.md` for required inputs and routes

---

## Skills exist but symlink points to wrong path

```bash
# Check what the symlink points to
readlink -f .claude/skills

# Should end with: 00-CORE/Agents/skills
# If wrong, remove and recreate:
rm .claude/skills
ln -s $(pwd)/00-CORE/Agents/skills .claude/skills
```

---

## Related

- [symlink_setup](../02-Setup/symlink_setup.md) — Full symlink check and recreate guide
- [ts_agent_client](ts_agent_client.md) — Agent Client not starting
- [ts_install](ts_install.md) — Installation issues
