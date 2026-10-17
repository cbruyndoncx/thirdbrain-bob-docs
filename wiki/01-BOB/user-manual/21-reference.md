---
type: knowledge-base
title: "BOB User Manual — 21. Reference & Glossary"
description: "Folder map, entity quick-reference table, and plain-English glossary of BOB terms"
status: draft
created: 2026-08-07
modified: 2026-10-12
tags: [bob, user-manual, wiki]
---

# 21. Reference & Glossary

This chapter is a lookup resource. Come here when you need the location of something, want to check what fields a particular entity requires, or need a plain-English definition of a term used elsewhere in the manual.

## Top-level folder map

Locations are written as **context keys** — `{company.clients}` rather than a folder name. A key is
stable; the folder it points at is whatever your workspace calls it, and
`uv run {skills.root}/context-pack/scripts/resolve_context.py --key company.clients` prints it. On a
stock BOB install those folders are the numbered ones (`10-ME`, `20-COMPANY`, `30-CLIENTS` and the
rest), so a key and a folder name are the same thing until someone renames the tree.

| Key | Name | What belongs here |
|--------|------|-------------------|
| `{vault.core}` | System | Skills library, playbook recipes, vault templates, task notes, schemas, configuration. Do not store business content here. |
| `{me.root}` | Personal | Owner or operator profile, personal contacts, personal ideas and inbox, private comms threads. |
| `{company.root}` | Company | Everything that belongs to the company as a whole: profile, processes, HR, finance, sales, marketing, strategy, management. |
| `{company.clients}` | Client Work | One sub-folder per client, named by `client_id`. All client-scoped records live here: deals, invoices, projects, meetings, deliverables, comms. |
| `{resource.root}` | Knowledge | Reference and research material not tied to one client: market intelligence, legal references, research knowledge bases, general knowledge notes. |
| `{company.projects}` | Internal Projects | Internal product or initiative projects, structured like client projects but without a client. |
| `{output.tmp}` | Scratch | Temporary and in-progress work. Skipped by the validator and not included in Dataview indexes. Nothing here is permanent. |

### Key areas inside `{company.root}`

Each area is named by its context key. `resolve_context.py --key company.finance` prints the folder
your workspace actually uses for it.

| Key | Contents |
|-----|----------|
| `{company.profile-root}` | Company profile, brand guidelines |
| `{company.qms.root}` | Quality management: rubrics, scorecards, model cards, spec reviews |
| `{company.decisions}` | Logged decisions |
| `{company.processes}` | Process definitions, process runs, playbooks, audit records |
| `{company.legal}` | Contracts, legal rules, document retention |
| `{company.hr}` | People records (internal), recruiting, payroll (WPS) |
| `{company.finance}` | Full financial sub-tree: journals, invoices, AP, tax, close, bank, reports |
| `{company.suppliers}` | Supplier records and supplier invoices |
| `{company.partners}` | Partner records, certifications, commissions |
| `{company.products}` | Product catalogue |
| `{company.marketing}` | Marketing content by channel, campaigns, social channels, video, courseware |
| `{company.leads}` | Lead records pre-qualification |
| `{company.sales}` | Campaigns, sequences |
| `{company.operations}` | Surveys and operational records |
| `{company.management}` | Strategy, KPIs, management reports |

## Entity quick-reference

The table below covers the entities most users encounter. For deep finance and tax internals (journal entries, deferred tax, ECL, gratuity provisions, WPS), consult the schema files directly under `{vault.schemas}`.

| Entity | `type:` value | Default location | Key fields | Lifecycle |
|--------|--------------|------------------|------------|-----------|
| Lead | `lead` | `{lead.root}` | `company_name`, `contact_name`, `lead_date`, `source`, `status` | `new` → `qualified` → `nurture` / `disqualified` |
| Client | `client` | `{client.root}` | `client_id`, `client_name`, `profile_type`, `status` | `prospect` → `active` → `inactive` / `on-hold` → `completed` → `archived` |
| Person | `person` | `{me.people}` or `{client.people}` | `name` | No defined lifecycle |
| Deal | `deal` | `{client.deals}` | `client_id`, `title`, `stage` | `lead` → `qualified` → `proposal` → `negotiation` → `won` / `lost` |
| Invoice | `invoice` | `{client.invoices}` | `client_id`, `invoice_id`, `invoice_date`, `due_date`, `amount`, `currency`, `payment_status` | `draft` → `sent` → `paid` / `overdue`; `credited` when a credit note settles it in full (the corrected invoice is reissued, never deleted or renumbered) |
| Supplier Invoice | `supplier-invoice` | `{company.finance}/AP/INVOICES/` | `supplier_id`, `invoice_id`, `amount`, `currency`, `match_status`, `payment_status` | `received` → `matched` → `approved` → `paid` |
| Meeting | `meeting` | Any `*/20-MEETINGS/` folder | `context`, `date`, `attendees`, `status` | `scheduled` → `completed` / `cancelled` |
| Decision | `decision` | `{company.decisions}` or `{client.decisions}` | `status`, `created` | `proposed` → `decided` → `superseded` |
| Comms Thread | `comms-thread` | `{client.comms}` | `thread_id`, `channel`, `status`, `awaiting_reply`, `last_message_at` | `open` → `closed` |
| Project | `project` | `{client.projects}` | `project_id`, `project`, `title`, `status` | `planning` → `active` → `on-hold` → `completed` → `archived` |
| Deliverable | `deliverable` | `{client.projects}` | `status`, `created` | `draft` → `review` → `approved` → `delivered` |
| Task | `task` | `{output.tasks}` | `status` | `open` → `in-progress` ↔ `awaiting-input` → `done` |
| Research | `research` | `{client.root}` or `{resource.root}` | `research_type`, `research_date`, `status` | `draft` → `review` → `final` |
| Analysis | `analysis` | Same folder as related research | `analysis_type`, `based_on`, `status` | `draft` → `review` → `final` |
| Campaign | `campaign` | `{company.sales}/CAMPAIGNS/` | `campaign_name`, `campaign_type`, `status` | `draft` → `active` → `completed` |
| Marketing Content | `marketing-content` | `{company.marketing}/{channel}/` | `content_type`, `platform`, `title`, `status` | `draft` → `review` → `scheduled` → `published` |
| Product | `product` | `{company.products}/{product-id}/product.md`, or `{client.catalogue.products}` for a catalogue item imported from a supplier or client catalogue | `product_id`, `product_name`, `brand`, `category`, `pricing_model`, `status` | `draft` → `active` → `discontinued` |
| Supplier | `supplier` | `{company.suppliers}` | `supplier_id`, `supplier_name`, `status`, `spend_category` | `prospect` → `active` → `inactive` |
| Partner | `partner` | `{partner.root}` | `partner_id`, `partner_name`, `status`, `relationship_type` | `lead` → `qualified` → `active` → `inactive` → `archived` |
| Playbook | `playbook` | `{company.playbooks}` | `trigger`, `outcome`, `total-steps`, `status` | `draft` → `active` → `archived` |
| Skill | `skill` | `{skills.root}/{name}/SKILL.md` | `category`, `version`, `disable-model-invocation` | Managed by skillsmith |
| Feedback | `feedback` | `{client.feedback}`; a `discovery-debrief` (a prospect's post-call fit assessment, keyed by `lead_id`) is filed in the lead's folder under `{company.leads}` | `feedback_type`, `respondent`, `feedback_date`, `status` | `draft` → `review` → `final` |
| Issue | `issue` | `{client.issues}` for a client issue; `{company.qms.audits}` for a QMS audit issue | `issue_id`, `severity`, `status` (plus `client_id` and `sla_target` on a client issue) | Client issue: `open` → `investigating` → `resolved` → `verified` → `closed`. QMS audit issue: `Open` → `Resolved` |
| Testimonial | `testimonial` | `{client.root}/50-TESTIMONIALS` | `client_id`, `respondent_name`, `format`, `permission_level`, `status` | `draft` → `approved` → `published` |
| KPI | `kpi` | `{company.kpi-reports}` | `kpi_category`, `title`, `last_updated`, `update_frequency` | No defined lifecycle |
| Strategy | `strategy` | `{company.management}/STRATEGY/` | `title`, `status`, `created` | `draft` → `approved` → `archived` |
| Company | `company` | `{company.profile-root}` | `entity_id`, `title`, `status` | No defined lifecycle |
| Profile | `profile` | `{scope}/00-PROFILE/` | `profile_type`, `title`, `created` | No defined lifecycle |
| Report | `report` | `{company.root}/{division}/REPORTS/` | `report_type`, `title`, `status` | `draft` → `review` → `final` |
| Process Definition | `process-definition` | `{company.processes}/definitions/{id}/` | `process_id`, `apqc_id`, `value_chain`, `activities`, `status` | `draft` → `active` → `deprecated` |
| Purchase Order | `purchase-order` | `{company.finance}/AP/ORDERS/` | `po_id`, `supplier_id`, `total_amount`, `currency`, `approval_status` | `draft` → `approved` → `received` → `closed` |
| Credit Check | `credit-check` | `{client.deals}/credit-checks/` | `client_id`, `deal_ref`, `verdict`, `exposure_amount`, `status` | `draft` → `approved` |

## The context pack

Skills never carry your folder names. A skill asks for a **key** such as `{company.clients}`, and the **context pack** answers with the real folder in your workspace. This is what lets the same skill run on the stock numbered layout and on a layout you have renamed.

**What a pack holds.** A pack is a `context.yaml` file with four sections: `roots` (the named top-level folders), `keys` (each key's folder `path` and a one-line `summary` of what it holds), `routing` (where a new note of each entity type goes) and `conventions` (the workspace's filing rules). The default key set has over 350 keys.

**The default and `extends: default`.** The default pack is the stock numbered tree. A workspace that is that tree with a few folders named differently does not copy it; its `context.yaml` says `extends: default` and declares only the difference. For example, a workspace can keep its internal projects folder under its own name by overriding the one `projects` root. The rules:

| Section | What the child file does |
|---------|--------------------------|
| `roots` | Its entries win. Moving a root moves every inherited key and routing template under it |
| `keys` | A key you declare is merged field by field over the default (change `path`, keep `summary`); a new key is added |
| `routing` | Its entries win |
| `conventions` | Its lines are added to the default's |

**Which pack is used.** The first of these that exists wins: a pack given on the command line, the `CONTEXT_PACK` environment variable, a `context.yaml` found walking up from the current folder, a `context.yaml` at the workspace root, a single `context-*` pack under the skills folder, and last the framework default. Two installed packs with no explicit choice is an error, not a guess.

**See a key.** Run these commands (`{skills.root}/context-pack/scripts/`):

| Command | What it shows |
|---------|---------------|
| `resolve_context.py --show` | Which pack is active, where it was found, the workspace root and its roots |
| `resolve_context.py --key company.clients` | The folder a key resolves to |
| `resolve_context.py --list --scope company` | The keys of one scope, with their summaries |
| `resolve_context.py --route meeting` | Where a new note of that entity type is filed |

**A starter vault.** A starter vault ships the `context-pack` skill and the default key file but no workspace pack, so it uses the default layout until you create a pack with `init_context_pack.py` (see [[02-system-overview|chapter 2]] for the command). `resolve_context.py --show` reports "found by default" when no pack is installed.

**Override a key or rename a folder.** Edit your workspace's `context.yaml`: change a `roots` entry to move a whole area, or declare the key with a new `path`. Then move the folder yourself, because the resolver creates nothing. Skills follow the pack from then on. Two things do not follow it automatically: existing notes that already link to the old location, and Obsidian's own settings and the Bases, which Obsidian reads literally. `{skills.root}/bob-install/scripts/render_obsidian_paths.py` renders both from the active pack (it only reports unless told to write), and `bob-workspace-bootstrap` reports a disagreement as a high-priority finding.

**An unresolved key.** `Error: unknown key '<key>'` means neither your pack nor the default declares it: check the spelling and run `--list`. A key that is declared but whose folder is missing is reported and the command stops, unless the skill is writing to a destination that does not exist yet. See [[20-troubleshooting|chapter 20]].

## Glossary

**Agent**
A Claude Code process that reads the vault, selects skills, and executes tasks on your behalf. The agent is distinct from the AI model — it is the orchestrator, not the reasoner.

**ACP (Agent Client Panel)**
The Obsidian plugin panel where you type requests to BOB and read its responses. Your primary interface to the agent.

**Base**
An Obsidian view that queries vault notes by frontmatter fields and displays them as a filtered, sortable table. Used for pipeline views, task lists, and KPI dashboards.

**Cadence**
A recurring schedule of agent-driven tasks — weekly reviews, monthly close sequences, quarterly reports — defined in a playbook and triggered on a schedule or manually.

**Canvas**
An Obsidian feature that places notes and file nodes on a freeform board. BOB uses canvases for dashboards and relationship maps. Text nodes are not clickable; use file nodes for navigation.

**Draft-first**
BOB's default save behaviour: outputs are written as `status: draft` notes so you can review before treating them as authoritative. Change the status manually once you have approved the content.

**Frontmatter**
The block of structured key-value fields at the very top of a note, enclosed in `---` delimiters. Every typed note must have frontmatter. The validator checks it on every save.

**Grounding**
The process of connecting an AI response to specific vault content — notes, profiles, past decisions — rather than relying on the model's general knowledge alone. Grounding makes answers relevant to your business specifically.

**Inference**
A conclusion the AI draws from vault content. BOB can infer patterns, risks, and recommendations from your data — but inference is not fact. Always review inferred outputs before acting on them.

**Playbook**
A multi-step process recipe stored as a note in `{company.playbooks}`. Running a playbook creates a sequence of Task notes and coordinates skill invocations across steps, with checkpoints between them.

**QMS (Quality Management System)**
The set of rubrics, scorecards, model cards, and spec reviews stored under `{company.qms.root}`. The QMS scores every skill for output quality, risk level, and reliability. Skills below threshold are flagged or disabled.

**Skill**
A named, versioned capability that BOB can invoke. Each skill is a folder under `{skills.root}` containing a `SKILL.md` specification and scripts. Skills are the building blocks BOB assembles to answer a request.

**Vault**
The top-level folder on your machine that holds all BOB notes and configuration. In Obsidian terms, the vault is the root of your knowledge base. Your data lives here, in plain files, under your control.

**Value Chain**
One of BOB's core business process flows — lead-to-cash, hire-to-retire, procure-to-pay, and others. Skills are tagged to the value chain they serve, so BOB can choose the right skill for the stage of the process you are in.

**Wikilink**
A link written as `[[Note Name]]` that connects one vault note to another. Wikilinks are how entities reference each other without duplicating data. The validator checks that wikilinks resolve to real notes.

**Context Pack**
The file set that maps context keys such as `{company.clients}` to folders in your workspace. Skills name locations by key, never by a hard-coded path, so renaming a folder means changing one entry in the pack. A workspace pack can start from the framework default (`extends: default`) and declare only what differs. The default key set has over 350 keys. `resolve_context.py --key <key>` prints the folder a key resolves to.

**Model Card**
A governed document in `{company.qms.model-cards}` that describes how a skill uses AI: its intended use, risk profile, attributes tested, and residual risk. A process definition will not load a skill that lacks an active model card.

**Periodic Note**
A daily, weekly, or monthly note stored in `{vault.periodic-notes}`. Used for reviews, stand-ups, and time-series tracking. BOB can pre-fill these from vault data on a cadence.

**Dataview**
An Obsidian community plugin that lets you query frontmatter fields across all vault notes using a SQL-like syntax. BOB uses Dataview for live tables in dashboards. Base is the newer, lower-code alternative.

**Status**
A frontmatter field that records where a note sits in its lifecycle. Status values are controlled vocabularies — each entity type accepts only the values defined in [[07-data-model|chapter 7, The Data Model]]. The validator rejects unknown values.

**Scope**
The organisational level a piece of content belongs to: system (`{vault.core}`), personal (`{me.root}`), company (`{company.root}`), client (`{company.clients}`), or knowledge (`{resource.root}`). The top-level folder encodes the scope. BOB uses scope to route outputs to the right place.

**ThirdBrain**
The underlying platform on which BOB runs. ThirdBrain provides the agent framework, skill library, and vault conventions. BOB is BRNCX's configured and business-ready deployment of ThirdBrain.

**Process Run**
A single execution of a Process Definition. Each run produces a JSONL event log and a summary note under `{company.runs}`. The event log is authoritative; the note is a readable view.

**Comms Thread**
A note that tracks an ongoing external communication — email thread, WhatsApp exchange, or phone call series. When a communication produces a decision or deliverable, the thread links to it via `captured_in`.

**Credit Check**
A formal risk assessment note linked to a Deal, recording exposure amount, open and overdue receivables, and a verdict (`pass`, `refer`, or `block`). Required before a deal progresses past negotiation in some process definitions.

Previous: [[20-troubleshooting|20. Troubleshooting]]
