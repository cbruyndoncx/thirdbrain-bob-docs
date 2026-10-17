---
type: knowledge-base
title: "Invoking skills — per agent"
status: final
created: 2026-05-02
modified: 2026-05-02
tags: [reference, skills, claude-code, codex, goose, kilo, kiro, invocation]
---

# Invoking skills — per agent

How a user explicitly triggers an Agent Skill differs across agents. All of these tools read the same open Agent Skills standard (`SKILL.md` with frontmatter `name` + `description`), but the user-facing call syntax is not portable.

## Claude Code

- Skills with `user-invocable: true` in their `SKILL.md` frontmatter become available as **slash commands**.
- Trigger by typing `/skill-name` — same syntax as built-in slash commands.
- Without `user-invocable: true`, the skill can still auto-activate based on its description, but the user cannot call it explicitly with a slash.

```yaml
# SKILL.md frontmatter
---
name: ad-creative
user-invocable: true
---
```

User types: `/ad-creative`

## Codex

- Skills are invoked explicitly with the **`$skill-name`** prefix, not `/`.
- `/command` in Codex only triggers true Codex commands (built-ins and configured slash commands) — it does **not** route to skills.
- The `user-invocable` frontmatter field is a Claude Code concept; Codex resolves `$skill-name` against the skills directory directly.

User types: `$ad-creative`

## Goose CLI (Block)

- Skills live in `~/.agents/skills/` (global) or `.agents/skills/` (per-project).
- Explicit invocation today is via the **`/skills` meta-command**, which lists skills and lets you load one or more by name:
  - `/skills` — list available skills
  - `/skills code-review edge-case-finder` — load named skills into the session
- Natural-language explicit calls also work ("use the code-review skill to review this PR").
- A `$skill-name` inline-prefix syntax is a community feature request, not currently shipped.

## Kilo Code CLI

- Skills follow the open Agent Skills format (YAML frontmatter `name` + `description`, then Markdown).
- No dedicated slash-prefix or `$`-prefix invocation — the agent matches your request against skill descriptions and activates when a skill "clearly and unambiguously applies".
- Explicit invocation is by **naming the skill in the prompt**: e.g. "use the api-design skill". Because the agent sees the literal skill name, this guarantees activation.
- Discovery is metadata-only at startup (progressive disclosure); full instructions are loaded on demand.

## Kiro (IDE vs CLI)

Kiro's two surfaces behave differently — the IDE supports explicit slash invocation, the CLI does not.

- **Kiro IDE**: type `/` in the chat input to browse available skills as slash commands. A skill named `pr-review` becomes `/pr-review`. Selecting it loads the full skill instructions. Manage skills in the *Agent Steering & Skills* panel; inspect with `/context show`.
- **Kiro CLI**: explicit `/<skill-name>` invocation is **not** supported (open feature request). Skills currently activate via description matching only — invoke by naming the skill in the prompt, same as Kilo Code.
- Naming rule for Kiro slash commands: lowercase, numbers and hyphens only, max 64 chars, folder name must match the slash command exactly.

## Summary table

| Agent | Explicit skill call | What `/foo` does | Notes |
|---|---|---|---|
| Claude Code | `/skill-name` | Runs the skill as a slash command | Requires `user-invocable: true` in SKILL.md frontmatter |
| Codex | `$skill-name` | Runs a true command only — never a skill | `$` is the skill-only prefix |
| Goose CLI | `/skills <name> [<name>…]` or name in prompt | `/skills` lists/loads skills (meta-command) | No per-skill `/name` shortcut; `$name` is a feature request |
| Kilo Code CLI | Name the skill in the prompt | No skill-specific slash routing | Auto-activates on description match |
| Kiro IDE | `/skill-name` (slash menu) | Runs the skill | Folder name must equal slash name |
| Kiro CLI | Name the skill in the prompt | No skill routing (CLI gap) | `/skill-name` is IDE-only today |

## Why this matters

When writing playbooks, onboarding docs, or worker instructions that reference skills, do not assume a single invocation syntax. Either show the syntax for each target agent, or scope the instruction to one. The only universally portable form is **"name the skill in the prompt"** — every agent above respects an explicit name reference even when the slash/`$` shortcut is unavailable.
