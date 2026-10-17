---
type: knowledge-base
title: "BOB User Manual — 18. Administration & Configuration"
description: "AI model selection, configuration surfaces, validation, generated artifacts, backups, health checks, releases, and housekeeping cadence"
status: draft
created: 2026-08-07
modified: 2026-10-12
tags: [bob, user-manual, wiki]
---

# 18. Administration & Configuration

This chapter covers the surfaces you touch to keep BOB running correctly — model selection, configuration, validation, and housekeeping. Most of this needs no technical expertise, and a few maintenance steps run a command in a terminal; all of it needs doing on a regular cadence.

## Choosing and switching AI models

BOB works with multiple AI providers. You set the active model in the Agent Client plugin settings inside Obsidian. The vault itself is model-agnostic: your notes, skills, and playbooks work the same regardless of which model is selected.

| Provider | When to choose it |
|----------|------------------|
| Claude (Anthropic) | Default recommendation; strong at structured reasoning and document tasks |
| OpenAI | Solid alternative; useful if you already have an OpenAI account. Model names and tiers change frequently — see the provider's current documentation. |
| Gemini (Google) | Option for users with Google Workspace integration |
| Local model | Air-gapped or maximum-privacy environments for the AI processing itself; slower, lower capability. Skills that call outside services, and fetching skills from the skills server, still use the network |

To switch: open Obsidian Settings → Agent Client → change the active agent. The switch takes effect on the next conversation. Your vault data is not affected.

Keep your AI subscription active and your API key current. An expired key produces an authentication error at the start of a run, not mid-way through — BOB checks before it starts.

## Configuration surfaces

There are three places where configuration lives. Do not use the chat window for any of them.

| Surface | Location | What goes here |
|---------|----------|----------------|
| Vault configuration note | `{vault.core}/vault-configuration.md` | Plugin settings, folder routing, export paths, Obsidian app settings |
| Brand theme files | `{company.assets-brand-guidelines}/`, `{company.brand}/`, or `{product.brand}/` for a product's own brand | Colours, fonts, logo paths, tone-of-voice rules used by content skills |
| Credentials and API keys | Configuration note or a dedicated secrets note | External API keys, service credentials, integration tokens |

**Never paste credentials into the chat.** The Agent Client sends chat content to the AI provider. Credentials belong in configuration files that stay on your machine. The vault configuration note has a section for this; skills that need a key tell you exactly which field to populate.

Brand theme files are referenced by marketing and content skills automatically. If BOB produces content with the wrong tone or wrong logo path, check the brand theme file first.

## Automatic validation

BOB validates two things continuously.

### Frontmatter validation

Every note you create through BOB, and any note you create manually using a vault template, has its frontmatter checked when it is saved. The validator confirms that required fields are present, that `type:` values match the data model, and that status values are in the allowed lifecycle. If validation fails, Obsidian surfaces a warning on the note.

### Vault referential integrity

The `vault-validator` skill checks the whole vault for broken links and structural inconsistencies. Run it after bulk imports, after moving files, or whenever the graph view shows unexpected orphans:

```
uv run vault-validator/scripts/vault_validator.py --vault /path/to/vault
```

The validator checks:

| Check | What it catches |
|-------|----------------|
| Referential links | `attendees[]`, `based_on[]`, `blockedBy[]`, and `client_id` that point to notes that do not exist |
| Completeness | Deliverables with no linked research; clients with no profile note |
| Lifecycle consistency | Completed projects with draft deliverables; won deals with no invoice |
| Location | Client files outside their `{client.root}` folder |
| Uniqueness | Duplicate person emails; circular task dependencies |

Fix issues before they accumulate. A vault with many broken references produces noisy, unreliable context for BOB.

## Generated artifacts — the regeneration principle

Several files in the vault are generated outputs, not source-of-truth documents. The rule is simple: **never hand-edit a generated file**. Edit its source and regenerate.

| Generated artifact | How to regenerate |
|---|---|
| [[SKILLS]] — the skills index | `uv run {skills.root}/skill-manager/scripts/list_skills.py --generate` |
| [[AGENTS.md]] files — directory manifests | `uv run {skills.root}/obsidian-ops/scripts/index_generator.py --vault . --emit-agents` |
| [[PLAYBOOKS]] — the playbooks index | Regenerated by the same index generator script |
| Schema files | Regenerated from source YAML by the schema build script |

The commands above use **context keys**; see [[21-reference|chapter 21, Reference]] →
"Top-level folder map" for how a key becomes a folder on your workspace.

If a generated file looks wrong, do not fix it directly — the fix will be overwritten on the next regeneration. Find the source note or script configuration, fix it there, and regenerate.

## Backup responsibility

The vault is plain files — Markdown, JSON, YAML, and a small number of binary assets. Any backup tool that copies files works: Time Machine, rsync, a cloud sync folder, or a Git repository.

BOB does not manage backups. That is your responsibility. The recommended minimum:

- A cloud sync (Dropbox, OneDrive, iCloud) running continuously for file-level recovery
- A weekly snapshot to a separate location in case the sync itself is corrupted

Because the vault is plain text, restoring a single note is as simple as copying the file back.

## Health checks

Two commands check whether BOB's environment is healthy.

### `bob-doctor`

Checks the Agent Client connection, the active model, plugin status, and key configuration fields. Run it any time BOB behaves unexpectedly:

```
run bob-doctor
```

BOB reports each check as pass or fail and tells you what to fix.

### `vault-preflight`

A lighter check run before a playbook or process that touches external services — confirms API keys are present, MCP servers are reachable, and required binaries are installed. Some playbooks run preflight automatically at step one.

## Updates and releases

BOB is distributed as a **vault release** — a packaged set of skills, playbooks, schemas, templates, and configuration. When a new release is available, it is applied to your vault by the installation process.

Releases follow an additive principle: upgrades add new skills and update existing ones; they do not delete your notes, client data, or personal playbooks. Your content is never touched by a release. If a skill you rely on changes behaviour in a release, the release notes will describe what changed.

After a release, regenerate the SKILLS index and run `bob-doctor` to confirm the environment is healthy. In a starter vault the skills server serves the library, so the server's own pack is what a release updates for served skills.

A release ships as separate artifacts: the vault ZIP (with its SHA-256 checksum file), plus this manual and the Getting Started Guide as PDFs. The PDFs are not inside the ZIP. Release v2.8.0 is a depth release: four skills added to the full vault (`doodle`, `prepare-application`, `review-job`, `skill-gap-learning-path`), the skill audit described in [[14-skills-system|chapter 14]], a fix to the Belgian chart-of-accounts seeder in `coa-account` (deduction accounts take the opposite normal balance; classes 15 and 19 are typed as equity), and changed data-model entities (issue, feedback, invoice, product) listed in [[21-reference|chapter 21]].

## Housekeeping cadence

Small, regular maintenance keeps the vault reliable. The table below is a suggested minimum cadence.

| Task | Frequency | How |
|------|-----------|-----|
| Review the inbox | Weekly | Process `{me.inbox}` — file, delete, or act on new notes |
| Regenerate SKILLS index | After any skill add, update, or disable | Run `list_skills.py --generate` |
| Regenerate AGENTS manifests | After adding folders or skills | Run the index generator |
| Run vault-validator | Monthly, or after bulk file operations | Run `vault_validator.py` |
| Check credentials | When a skill reports an auth error | Update the relevant field in the configuration note |
| Back up the vault | Continuous (cloud sync) + weekly snapshot | Your choice of tool |

Housekeeping is not optional maintenance — it is what keeps BOB's context accurate. A stale SKILLS index means BOB cannot route to new skills. An inbox full of unprocessed notes adds noise to every context read. Spend fifteen minutes a week on this and the vault will stay clean.

