---
description: How skills are structured, how BOB routes requests to them, what skill
  metadata means for setup, and how quality is managed
title: BOB User Manual — 14. The Skills System
---

# 14. The Skills System

A skill is a written procedure. Not code, not a plugin — a structured document that tells BOB exactly what to do with a specific type of request: what inputs to gather, which steps to follow, which files to read or write, and what "done" looks like. Skills are the reason BOB produces consistent, repeatable work instead of improvising a fresh answer every time.

## Anatomy of a skill

Every skill lives at `{skills.root}/{name}/SKILL.md`. Open any of them and you will see the same structure:

`{skills.root}` and the other `{...}` names in this chapter are **context keys** — see
[chapter 21, Reference](21-reference.md) → "Top-level folder map" for how a key becomes a folder
on your workspace.


| Section | What it contains |
|---------|-----------------|
| **Inputs** | What BOB needs before it can start — context from the vault, parameters you supply, or files it will read |
| **Workflow** | Numbered steps; some skills have multiple routes depending on what you asked for |
| **Outputs** | Files created, paths used, or drafts returned for your review |
| **Verification** | How BOB checks its own work before handing it to you |
| **Done When** | Explicit acceptance criteria — the conditions that must be true for the skill to be considered complete |

The Done When criteria are the most important section for you as a user. If a skill's output does not satisfy them, the run is not finished.

## How BOB routes a request to a skill

When you send a message, BOB reads it and looks for the best-matching skill. Matching works in priority order:

1. **Explicit invocation** — you typed `/skill-name`, so BOB loads that skill directly.
2. **Keyword and intent match** — BOB compares your request against skill triggers and descriptions.
3. **Ambiguity prompt** — if two or more skills are plausible, BOB names them and asks which you meant.

When two or more skills are plausible, BOB is designed to name them and ask which you meant. It can still pick the wrong one, so check which skill ran. If it guesses wrong, correct it with the explicit name: `/proposal-writer`, `/win-loss-review`, and so on. The full list of installed, enabled skills is at [SKILLS](../../skills/index.md) in the vault root.

## Skill metadata that affects you

Each skill's frontmatter carries flags that determine whether it works out of the box or needs something from you first.

### The `requires` field

| Value | What it means | What you must do |
|-------|---------------|-----------------|
| `none` | Zero external dependencies | Nothing — the skill works immediately |
| `config` | Needs platform-specific configuration | Follow the skill's setup section; usually a path or toggle in the vault configuration note |
| `api-key` | Needs credentials for an external service | Add the key to the configuration note (never into the chat) |
| `mcp` | Needs an MCP server running | Install and configure the MCP server named in the skill |
| `install` | Needs a binary or tool installed on your machine | Install the tool; the skill's setup section lists the exact command |

If a skill's `requires` value is anything other than `none`, the skill will tell you what is missing when you invoke it. Fix the dependency and retry.

### Value chains

Each skill declares which value chains it belongs to — for example `lead-to-cash`, `deliver-to-satisfaction`, or `record-to-insight`. This is how BOB groups skills into business processes and how playbooks know which skills to call. You do not need to manage value chains directly; they are metadata for routing and reporting.

### Enabled vs disabled

A skill with `disable-model-invocation: true` is installed but not available for AI use — it is either under development or paused for quality reasons. Disabled skills do not appear in [SKILLS](../../skills/index.md). If you need a skill that is missing from the index, check its SKILL.md file for a status note.

## The SKILLS index

[SKILLS](../../skills/index.md) at the vault root is the authoritative list of every skill that is currently enabled in a full vault. In a starter vault it lists only the local skills; ask BOB (the skills server's `search_skills`) for the rest. It is a generated file — do not edit it by hand. When skills are added, updated, or disabled, regenerate it:

```
cd {skills.root}/skill-manager/scripts
uv run list_skills.py --generate
```

The index groups skills by category and shows their `requires` level and primary value chain. Use it to browse what is available before you ask BOB for something.

## Quality management of skills

BOB ships with a quality management system (QMS) that keeps skills accurate and reliable over time. You do not operate the QMS — that is a developer and administrator concern — but understanding its outputs helps you interpret skill quality signals.

| QMS artifact | Location | What it tells you |
|---|---|---|
| Quality standards | `{company.qms.standards}` | The scoring scale (1–4) and the tier thresholds |
| Skill scorecards | `{company.qms.scores}/{skill}.md` | Per-skill rubric scores and overall weighted result |
| Spec reviews | `{company.qms.spec-reviews}/individual/` | Five-layer specification audits per skill, with a pass/fail result |
| Rubrics | `{company.qms.rubrics}` | The criteria and weights used to score each skill category |
| Model cards | `{company.qms.model-cards}` | How a skill uses AI: intended use, risk profile, residual risk |

Skills are grouped into approval tiers based on their scorecard results. A higher tier means the skill has passed more rigorous review. Tier information appears in the scorecard note.

What this means in practice: if a skill produces output that surprises you, check its scorecard to see whether there are known limitations noted. Skills rated below the tier threshold are flagged for improvement.

## Where skills come from

A full vault stores every shipped skill locally: the v2.8.0 release has over 380. A starter vault stores only the skills that set up and operate the vault: `context-pack`, `vault-validator`, `tasknotes`, `personal-backlog`, `obsidian-ops`, `bob-workspace-bootstrap`, `bob-workspace-compose`, `bob-install`, `bob-doctor`, `acp-doctor`, `obsidian-plugin-manager`, `vault-setup`, `vault-upgrade` and `vault-preflight`. They stay local because the agent hooks, the BOB Workspace plugin and the templates call them by path. Every other skill, and all playbooks and value chains, are served by the **skills MCP server**, or added from the free skill packs (`pack-core` holds over 200 skills, plus nine more packs, mostly one per department; each pack bundles the helper skills it depends on, so one pack works on its own).

### Local first, then the server

BOB follows one rule when it needs a skill:

1. If `{skills.root}/<name>/SKILL.md` exists, BOB uses that local copy.
2. Otherwise it asks the skills server. The server's tools share a prefix (`bob_` when it serves one library). `search_skills` or `list_skills` finds a skill, `get_skill` reads its `SKILL.md`, and `read_skill_file` reads its references. `list_playbooks` and `get_playbook` serve playbooks, and `list_value_chains` and `get_value_chain` serve value chains. Playbooks are also offered to the agent as MCP prompts.
3. A skill can exist in both places (`tasknotes` is one). They are the same skill; the local copy is the one installed with your vault.

A playbook step that names a skill works the same way: run it locally if it is local, otherwise fetch it from the server. You do not do this yourself; you describe the job and BOB follows the rule. Registering the server is described in [chapter 3](03-getting-started.md).

### Running a served skill's scripts

Reading a served skill needs nothing else. To run its scripts, BOB copies the skill to a cache on your machine together with the skills it depends on (`skills-mcp pull --with-deps`), runs the commands from the skill folder, and hands them your vault with `--vault`. The host exports `VAULT_PATH` and `SKILLS_ROOT` so scripts find your workspace. A served skill runs outside your vault and so does not read the vault's `.env` file: set the API keys it needs in your environment (your shell profile, the agent host's settings, or the `env` of the server's configuration). `.env.example` in the vault root lists the keys and the skills that use them.

### Locations in skills: context keys

A skill never names your folders. It asks for a key such as `{company.clients}` and the context pack answers with the real folder, which is why the same skill works on a renamed workspace. See [chapter 21, The context pack](21-reference.md).

## The 2026-10-08 skill audit

Release v2.8.0 carries the results of a full audit of the vault's skills: over 400 skills were audited, and all of them pass the QMS gate when it is run in check mode (the run promotes nothing).

The gate is the check a skill must pass before it is treated as release-ready. It combines a passing specification review and quality scorecard with structure checks: required sections in the right order, referenced files present, and a current model card for the skills that need one. Passing means the skill's specification meets the standard; it does not guarantee any single output, so keep reading results as drafts (see [chapter 19](19-data-safety.md)). You can inspect the results: scorecards in `{company.qms.scores}`, spec reviews in `{company.qms.spec-reviews}`, and the audit's regeneration report under `{company.qms.audits}` (folder `skill-audit-2026-10-08`). In user terms the audit changed:

- Folder locations in skills are written as context keys, so a skill follows your workspace layout.
- Each skill's Output Locations block was regenerated, so it lists where the skill saves its results.
- The context-pack default key set now has over 350 keys; none was removed.

## How new skills are created and certified

New skills follow the **skillsmith** workflow — a governed path from initial brief through specification, draft, peer review, quality scoring, and release gate. A skill is not considered certified until it has a passing spec review, a completed scorecard, and approval from the relevant tier authority. The skillsmith process is designed to keep the skills library reliable; you benefit from this every time you invoke a skill and get predictable output without having to verify the procedure yourself.

