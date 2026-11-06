---
type: knowledge-base
title: "BOB User Manual — 7. The Data Model"
description: "How BOB stores every business object as a structured note, how entities relate, and how the folder structure encodes scope"
status: draft
created: 2026-08-07
modified: 2026-10-12
tags: [bob, user-manual, wiki]
---

# 7. The Data Model

BOB keeps every piece of business information in the same place and in the same format: a plain text file, stored in your vault, with a small block of structured fields at the top. That block is called **frontmatter**. Everything else in the file is ordinary prose or tables — readable in any text editor, searchable, version-controllable, never locked in a proprietary database.

This chapter explains what that means in practice: what the entities are, how they connect, what happens to their status over time, and how the folder structure tells BOB where things belong.

## One fact, one home

The governing rule is simple. Each business object — a client, a deal, an invoice, a meeting — lives in exactly one note. When you need to refer to that object elsewhere, you link to it with a wikilink (`[[Note Name]]`). You do not copy data into a second note. You do not maintain parallel lists.

This matters because BOB reads the vault for context. If the same fact exists in two places and they disagree, BOB has no way to know which one is correct. One fact, one home eliminates that problem.

## What a typed note looks like

Every business object note begins with a frontmatter block:

```yaml
---
type: client
title: "Acme Manufacturing"
client_id: acme-manufacturing
client_name: Acme Manufacturing
status: active
created: 2026-03-01
tags: [client]
---
```

The `type:` field tells BOB — and the vault validator — what kind of object this is. The remaining fields are the structured data for that type. The body of the note holds meeting summaries, context, and anything that does not fit neatly into a field.

## The entities you work with daily

The vault recognises over 100 entity types, covering everything from journal entries to YouTube videos. Most users touch a much smaller set. The table below covers the entities that appear in everyday business work. The complete reference, including finance and tax internals, is in [[21-reference|chapter 21, Reference & Glossary]].

| Entity | What it represents | Where it lives |
|--------|--------------------|----------------|
| Lead | A prospective client before qualification | `{company.leads}` |
| Client | A qualified account you do business with | `{client.root}` |
| Person | A contact: employee, client contact, or partner contact | `{me.people}` or `{client.people}` |
| Deal | A sales opportunity linked to a client | `{client.deals}` |
| Invoice | A billable document linked to a client | `{client.invoices}` |
| Meeting | A recorded interaction with attendees and decisions | Any `*/20-MEETINGS/` folder |
| Decision | A logged decision, linked from a meeting or comms thread | `{company.decisions}` or `{client.decisions}` |
| Comms Thread | An ongoing email, WhatsApp, or call thread | `{client.comms}` |
| Project | A scoped body of work for a client or internally | `{client.projects}` |
| Deliverable | An output produced for a client or project | `{client.projects}` |
| Task | A single action item tracked through to done | `{output.tasks}` |
| Research | Market or account research feeding analysis | `{client.root}` or `{resource.root}` |
| Analysis | Structured conclusions drawn from research | Same folder as related research |
| Campaign | A marketing or sales outreach campaign | `{company.sales}/CAMPAIGNS/` |
| Playbook | A repeatable multi-step process recipe | `{company.playbooks}` |

## How entities relate

BOB's data model is relational — entities reference each other through fields and wikilinks, not by duplicating data. The core chain for client work runs like this:

```
Lead  ──promotes to──▶  Client  ──1:N──▶  Deal  ──1:N──▶  Invoice
                          │
                          ├──1:N──▶  Project  ──1:N──▶  Deliverable
                          │
                          ├──1:N──▶  Comms Thread  ──links──▶  Meeting / Decision
                          │
                          └──N:N──▶  Person  (via Meeting attendees)
```

A few specific connections to know:

- **Lead promotes to Client.** When a deal is won, the `create-client` skill converts the lead note into a full client record and moves it under `{company.clients}`. The lead note is not deleted; it becomes history.
- **Client ID links everything.** Every client-scoped note carries a `client_id` field matching the folder name. Remove that field and Dataview queries lose the record.
- **Meetings link People and Decisions.** A meeting note lists `attendees` as wikilinks to Person notes, and its `captured_in` field links out to any Decision or Deliverable the meeting produced.
- **Tasks link to Playbooks.** When a playbook runs, it creates Task notes. Each task carries a `playbook` wikilink back to the recipe that generated it.
- **Analysis builds on Research.** An Analysis note's `based_on` field lists the Research notes it drew from. Its `feeds_into` field points to the Deliverable it supports. This chain is how BOB knows where evidence came from.

## Status lifecycles

Every entity has a defined lifecycle. Status fields are not free text — they accept only the values in the table below. The validator rejects anything else.

| Entity | Status progression |
|--------|--------------------|
| Lead | `new` → `qualified` → `nurture` or `disqualified` |
| Deal | `lead` → `qualified` → `proposal` → `negotiation` → `won` or `lost` |
| Client | `prospect` → `active` → `inactive` or `on-hold` → `completed` → `archived` |
| Project | `planning` → `active` → `on-hold` → `completed` → `archived` |
| Task | `open` → `in-progress` ↔ `awaiting-input` → `done` |
| Meeting | `scheduled` → `completed` or `cancelled` |
| Deliverable | `draft` → `review` → `approved` → `delivered` |
| Research / Analysis | `draft` → `review` → `final` |
| Marketing Content | `draft` → `review` → `scheduled` → `published` |
| Accounting Period | `open` → `soft-closed` → `hard-closed` |

Lifecycle rules are enforced across parent-child relationships. You cannot mark a Project `completed` while it still has Deliverables in `draft`. You cannot archive a Client with active Projects. BOB will tell you which records are blocking a status change.

## How the folder structure encodes scope

The top-level folder is not cosmetic — it tells BOB (and you) whose data this is and what kind of content it contains. Each row names a context key; `resolve_context.py --key company.root` prints the folder your workspace uses for it.

| Key | Scope | What lives here |
|--------|-------|-----------------|
| `{vault.core}` | System | Skills, playbooks, templates, tasks, schemas, vault configuration |
| `{me.root}` | Personal | Owner profile, personal contacts, ideas, inbox, personal comms |
| `{company.root}` | Company | Company profile, processes, HR, finance, sales, marketing, management |
| `{company.clients}` | Client work | One sub-folder per client: deals, invoices, projects, meetings, comms |
| `{resource.root}` | Knowledge | Research knowledge base, legal reference, market intelligence |
| `{output.tmp}` | Scratch | Temporary work — skipped by the validator, not indexed |

The scope encoded in the path determines where BOB saves outputs. A deliverable for a client goes under `{company.clients}`. A blog post goes under `{company.marketing}`. BOB will not cross these boundaries without telling you.

## How validation works

A validator runs automatically every time an agent (Claude Code, Codex, Antigravity) writes a note inside the vault (outside the skip list: `{skills.root}`, `{vault.templates}`, `{output.tmp}`), once the hooks are installed on that machine — see [[install-agent-hooks|Install the frontmatter hooks]]. It checks:

- **Type and required fields.** Every `type:` has a defined set of required fields. A missing field blocks the save and tells you exactly what is absent.
- **Referential integrity.** Links in `attendees`, `based_on`, `feeds_into`, and `blockedBy` must resolve to real notes. A broken link is flagged.
- **Lifecycle consistency.** Parent-child status rules are checked on save — not just when you manually request a check.
- **Location.** A `client` note must live under `{company.clients}`. A `task` must live under `{output.tasks}`. File in the wrong place and validation will tell you.
- **Uniqueness.** `client_id` values must be unique. Person emails must be unique. Circular task dependencies are rejected.

Validation errors go back to the agent that wrote the note, and it fixes the flagged field in the same turn. Edits you make by hand in Obsidian are not seen by a hook. For those, run the foreground `frontmatter_watcher.py` from the vault-validator skill, or run the validator on the file.

If you need to do rough draft work without validation firing, use `{output.tmp}`. When the note is ready, move it to its correct location and complete the frontmatter.

