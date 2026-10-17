---
type: knowledge-base
title: "BOB User Manual — 6. The Workspace"
description: "A reference guide to every area of the BOB Workspace plugin — what it shows, what data feeds it, and what you can do from each view"
status: draft
created: 2026-08-07
modified: 2026-10-12
tags: [bob, user-manual, wiki]
---

# 6. The Workspace

The BOB Workspace is an Obsidian plugin. It lives as a panel inside Obsidian and gives you structured views over the plain markdown files in your vault. All data is stored in those files — the plugin reads them, renders them as tables, boards, dashboards, and forms, and writes back to them when you make changes. Close the plugin and the data is still there, fully readable in any text editor.

This chapter covers every area of the workspace: how to navigate between them, what each view shows, what data feeds it, and what actions are available.

## The Obsidian Window

When you open Obsidian you see three zones:

| Zone | What it is |
|------|------------|
| Left sidebar | File explorer, search, bookmarks — standard Obsidian navigation |
| Editor pane | Opens when you click a note; shows and edits the file directly |
| BOB Workspace panel | The plugin panel — your structured business interface |

The plugin panel opens in a sidebar or as a full pane, depending on how you've pinned it. If the panel is not visible, run the **Open BOB Workspace** command from the Obsidian command palette (`Ctrl+P`).

The Agent Client panel (ACP) — where you type requests to BOB — is a separate panel. It can be open alongside the Workspace at the same time. You do not have to choose between them: use the Workspace to navigate and view data, and the ACP to run skills and playbooks. See [[04-daily-use|chapter 3, Working with BOB Day to Day]] for detail on the ACP.

## Navigation

The left nav of the Workspace lists every active module. Clicking a nav item loads that area in the main pane. Modules you have disabled in Settings do not appear.

| Nav item | Module | What it covers |
|----------|--------|----------------|
| Home | Always on | Command-centre dashboard |
| Team | Always on | Filtered people view for employees, freelancers, contractors |
| Planner | Planner | Inbox, today's note, calendar, TaskNotes, projects |
| CRM | CRM | Pipeline, contacts, clients, leads, campaigns, activities |
| PRM | PRM | Partner overview, registrations, commissions, certifications |
| Client Work | Always on | Delivery workspace scoped by client and project |
| Finance | Always on | Invoices, general ledger, finance setup, tax |
| Suppliers | Always on | Supplier records, purchase requisitions, purchase orders |
| Reports | Always on | Aggregated pipeline, sales, partner, activity, productivity views |
| AI Workspace | Always on | Playbooks browser and skills library |
| Base Links | Always on | Direct links to every `.base` file |
| Settings | Always on | Plugin configuration |

## Home

Home is the default screen when you launch the plugin (configurable in **Settings → App → Default tab**). It is a two-column read-only dashboard.

**Left column:** today's tasks, tickable inline. Ticking a task writes back to the source daily note or TaskNote immediately. Also shows this week's progress and upcoming deadlines.

**Right column:** top active projects with milestone progress bars, pipeline summary by stage, partners due for follow-up, recent activity feed.

Home gives you the state of the business at a glance. Nothing on Home is entered here — it is all drawn from records you have already created elsewhere in the vault.

## Team

Team is not a separate entity type. It is a filtered view of `type: person` records whose `person_category` field matches the categories configured in **Settings → BOB Workspace → Team person categories**. The defaults are `employee`, `freelancer`, and `contractor`.

To add a team member, use **+ New Person** and set `person_category` to one of the configured values. To include a new category such as `advisor`, add it to the setting — no schema change is needed.

## The Bases Dropdown

Most list screens in the Workspace show a **dropdown in the top-right corner**. This lets you switch between named views defined in the corresponding `.base` file in `{vault.bases}`. Each named view can have its own filters, column order, sort, and groupBy.

To add or change a view, open the relevant `.base` file and edit the `views:` block. The dropdown updates immediately on save — no Obsidian restart required.

Inline field editing is available in native Obsidian Base views (open the `.base` file directly). The plugin grid rows open the source note for editing instead.

## Planner

The Planner module covers your personal operational loop. Toggle it on or off under **Settings → Modules**.

### Inbox

The Inbox is the universal capture surface. Items land here from anywhere in the vault and are grouped by urgency:

| Group | Items shown |
|-------|-------------|
| Now / Overdue | Past due, shown in red |
| Due Today | Due later today |
| This Week | Due within the current week |
| Later | Everything else |

Each item has quick-action buttons: snooze (+15 min, +1 hour, Tomorrow), mark Done, or Edit. The nav badge on the Inbox item shows the live count of overdue and due-now items.

**Quick capture** is available from anywhere in Obsidian via `Ctrl+Shift+I`. A modal appears; type a title, optionally set a datetime and repeat cadence (daily/weekly). The captured item writes to a markdown file in the configured reminders folder.

### Today

Today shows your current daily note in a live-editable surface. The journal textarea autosaves as you type. The **+ Quick task** button appends a new checkbox task to the configured tasks heading in today's note.

If today's daily note does not yet exist, Today creates it from your configured template. The daily note folder and heading names are set in **Settings → App**.

### Calendar

Calendar is a Mon-to-Sun week grid of your daily notes. Each day column shows the tasks from that day's note, tickable inline. Clicking a day heading opens the note. The week start day is configurable in **Settings → App → Week starts on**.

### TaskNotes

TaskNotes lists active task notes from `{output.tasks}` (configurable). Each row is a single TaskNote file; status, priority, due date, and project link come from the file's frontmatter.

The archive folder (also configurable) feeds the Productivity report — historical completions remain visible even after tasks are archived.

The Bases dropdown reflects named views in `{vault.bases}/Tasks.base`. Useful views: open tasks, in-progress tasks, tasks grouped by project.

### Projects

Projects shows a card grid of all `type: project` notes, grouped by status. Each card displays the project name, client, priority, deadline, and a colour-banded milestone progress bar.

Clicking a card opens the Project Detail surface:

| Area | What you see |
|------|-------------|
| Top bar | Status, priority, owner, and due date pills |
| Left column | Tickable milestones and task list, with + Add buttons |
| Right column | Brief, Scope, Risks, Stakeholders, Notes — autosaving textareas |
| Footer | Open as note button — edits the full markdown body |

The textareas write back to the H2 sections of the underlying project note as you type.

## CRM

The CRM module covers the revenue-facing side of the business, from first lead through active client activities. Toggle under **Settings → Modules**.

### CRM Dashboard

A read-only summary of pipeline health and recent activity. Shows: pipeline by stage (bar chart), hot deals by value, stale deals (no edits in 14+ days), recent activity, and customer base stats. Use this as a daily check-in before working individual records.

### Pipeline

A kanban board of all `type: deal` notes, grouped by the `stage` frontmatter field. Drag a card to a new column to update its stage — the write-back is immediate. Won deals are tinted green; lost deals are shown at reduced opacity.

Use **+ New Deal** to open the capture modal. Required field: title. Key fields: stage, deal value, expected close date, client.

### Contacts

A sortable list of all `type: person` notes not in the Team view. Each row shows name, company, role, email, and last-contact date. Click a row to open the source note.

### Clients

Lists all `type: client` notes. Status lifecycle: `prospect → active → inactive → completed → archived`. The Bases dropdown on `{vault.bases}/Clients.base` supports views such as *Active only* or *By region*.

### Leads

Lists all `type: lead` notes. Status lifecycle: `new → qualified → nurture / disqualified`. When a lead converts, run the `create-client` skill to promote it to a Client record.

### Campaigns

A tabbed screen grouping three entity types:

| Tab | Shows |
|-----|-------|
| Overview | Active campaign count, recent sequence touches, lead counts by source |
| Campaigns | All `type: campaign` notes — name, type, status, launch date, target persona |
| Sequences | All `type: sequence` notes — name, campaign reference, total touches, duration, status |

### Activities

Lists all `type: activity` notes — calls, emails, meetings, and other touchpoints against contacts or deals. Key fields: title, channel, direction (inbound/outbound), contact reference, date. Use the Bases dropdown to add views by channel, by contact, or filtered to the current week.

## PRM — Partner Relationships

The PRM module manages co-sell, co-delivery, referral, and certification partners. Partner records live under `{partner.root}`. Toggle under **Settings → Modules**.

| Tab | Shows |
|-----|-------|
| Overview | Active partner count, open registrations, pending commissions, certifications expiring soon |
| Partners | All `type: partner` notes — name, relationship type, agreement, status |
| Registrations | Deal registrations submitted to partner portals — submitted date, expiry, value, status |
| Commissions | `type: commission` notes per partner per period — amount, earned date, status (pending/paid) |
| Certifications | Vendor/programme certifications held — issued date, expiry date, status |
| Analytics | Read-only: deals influenced, revenue attributed, commission paid, registration conversion rates |

The Certifications tab is most useful when you add a view in `{vault.bases}/Partner-Certifications.base` filtered to `status: active` and sorted by expiry date ascending — it surfaces renewals before they lapse.

## Client Work

Client Work is the delivery workspace. It is scoped: you pick a client from the selector at top-left, optionally narrow to a project, and all tabs filter accordingly. Selectors match on both `client_id` and `end_client_id`, which covers sub-contracting scenarios.

| Tab | Entity type | Key fields |
|-----|-------------|------------|
| Overview | — | Summary of open deliverables, comms, meetings, feedback, surveys for the selected scope |
| Meetings | `meeting` | Date, attendees, context, status (scheduled / completed / cancelled) |
| Comms | `comms-thread` | Channel, subject, status, last message date, awaiting reply flag |
| Deliverables | `deliverable` | Status: draft → review → approved → delivered |
| Feedback | `feedback` | Type (NPS/CSAT/interview), respondent, score, themes, sentiment |
| Surveys | `survey` | Title, type, target audience, tool, response count, response rate |
| Testimonials | `testimonial` | Respondent, format, permission level (public/attributed/anonymous) |
| Decisions | `decision` | What was decided, by whom, and why — for audit and handoff |

The `awaiting_reply` flag on comms threads surfaces threads that need a response. The permission level on testimonials controls what can be shared externally — add a Base view filtered to `permission_level: public` to find usable social proof quickly.

## Finance

Finance covers the full accounting and tax stack. Each area is a separate nav item with its own tab strip.

### Customer Invoices

Lists all `type: invoice` notes. Status lifecycle: `draft → sent → paid / overdue / cancelled`. Use **+ New Invoice** to create one. The currency default is set in **Settings → Currency**.

Useful Bases views on `{vault.bases}/Supplier-Invoices.base`: *Outstanding* (sent, unpaid), *Overdue*, *By client*, *This month*.

### General Ledger

A tabbed surface covering the full double-entry accounting stack:

| Tab | Shows |
|-----|-------|
| Overview | Current-period GL health: debits/credits, recent journal entries, unusual balances, open reconciliation items |
| Chart of Accounts | All `type: chart-of-accounts` notes — account code, name, type, normal balance |
| Journal Entries | All `type: journal-entry` notes — JE ID, period, type (manual/system/accrual), status (draft/posted) |
| Bank Reconciliations | Per-account, per-period reconciliations — bank balance vs. GL balance; difference must be zero before period close |
| Trial Balances | Per-period trial balances — total debits must equal total credits before generating statements |
| Statements | P&L, Balance Sheet, Cash Flow, Changes in Equity — each linked to a signed-off trial balance |
| FS Notes | Narrative notes accompanying each set of financial statements — accounting policies, going concern, per-line disclosures |

### Finance Setup

Reference data that underpins the GL:

| Tab | Shows |
|-----|-------|
| Overview | Setup completeness: periods configured, bank accounts linked, FX rates loaded, inventory items |
| Accounting Periods | Start/end date, type (monthly/quarterly/annual), status (open/soft-closed/hard-closed) — hard-closed periods cannot be edited |
| Bank Accounts | Account ID, bank, IBAN, currency, mapped GL account code |
| FX Rates | Per-period exchange rate tables by currency pair — used for invoice revaluation and foreign-currency postings |
| Inventory | SKU, cost method (FIFO/weighted average), quantities, net realisable value, write-down |

### Tax

All compliance filings under one tabbed surface:

| Tab | Shows |
|-----|-------|
| Overview | Upcoming deadlines: VAT returns, corporate tax filings, retention deadlines, free zone validity |
| VAT Returns | TRN, period, standard-rated supplies, output/input VAT, net payable, filing due date, status |
| Corporate Tax | Return ID, taxable income, tax rate, tax payable, small business relief flag, filing date, status |
| Deferred Tax | DTA and DTL per period, tax rate, recoverability assessment |
| Transfer Pricing | Inter-company transactions — type, amount, arm's-length method, documented flag |
| Free Zone Status | Qualifying vs. non-qualifying income, substance test results, nexus maintenance per period |
| Legal Rules | Reference library of tax regulations per jurisdiction — source, authority, effective dates, confidence rating |
| Document Retention | Document types, required retention periods, destroy-after dates, responsible persons |

## Suppliers and Procurement

The Suppliers section covers the full procure-to-pay cycle. Supplier records live under `{company.suppliers}/{supplier-id}/`.

The nav contains three top-level items — Suppliers (tabbed), Supplier Invoices (vault-wide), Purchase Requisitions (vault-wide), and Purchase Orders (vault-wide):

| View | Scope | Use for |
|------|-------|---------|
| Suppliers → Overview | Active supplier | Dashboard: active suppliers, open POs, invoices awaiting approval, pending requisitions |
| Suppliers → Suppliers tab | Active supplier | Supplier records — name, spend category, contract value, payment terms, status |
| Suppliers → Supplier Invoices | Selected supplier | Inbound invoices from that supplier |
| Suppliers → Purchase Requisitions | Selected supplier | PRs scoped to that supplier |
| Suppliers → Purchase Orders | Selected supplier | POs scoped to that supplier |
| Supplier Invoices (nav) | Vault-wide | AP processing — approve, match, track payment across all vendors |
| Purchase Requisitions (nav) | Vault-wide | Central approval queue — approve, reject, convert to PO |
| Purchase Orders (nav) | Vault-wide | Full PO lifecycle from approved requisition through delivery confirmation |

## Reports

Reports are read-only aggregated views. They query your existing records in real time — no separate report files are created. Report screens appear or disappear based on which modules are active.

| Report | Data source | Key metrics |
|--------|-------------|-------------|
| Productivity | Daily notes and/or TaskNotes (per task mode setting) | Tasks completed per day/week, completion rate, tasks by project |
| Pipeline | `type: deal` notes | Deal count and value by stage, win/loss ratio, average deal size, time-to-close, deals by owner |
| Sales | Closed-won deals and paid invoices | Revenue by period, top clients, deal source breakdown, revenue vs. target |
| Partners | PRM entities | Deals influenced, commissions paid/pending, registration conversion, certifications active vs. expired |
| Activity | `type: activity` notes | Activity by channel, by contact, by deal, inbound vs. outbound split, trend over time |

The Partners report is only visible when the PRM module is enabled.

## AI Workspace

The AI Workspace lets you browse and launch the skills and playbooks installed in your vault without leaving Obsidian.

### Playbooks

Lists all `type: playbook` notes stored in your vault. In a starter vault the playbooks are served by the skills server rather than stored, so ask BOB to list them (see [[16-playbooks-processes|chapter 16]]). Each entry shows name, trigger phrase, estimated duration, total steps, and status. Clicking a playbook opens a detail view with the full trigger, outcome, and step-by-step workflow.

To launch a playbook: copy the trigger phrase and paste it into the Agent Client panel. BOB matches the trigger and begins execution. See [[04-daily-use|chapter 3, Working with BOB Day to Day]] for how to run playbooks.

The status filter defaults to active playbooks only. Set it to *All* to include drafts and archived playbooks.

### Skills

Lists all `type: skill` notes stored in your vault. In a starter vault that means the local skills; the rest are served by the skills server and are found by asking BOB (see [[14-skills-system|chapter 14]]). Each entry shows name, category, version, dev status (`draft / integrated / certified`), pricing tier, value chains, and prerequisites.

To invoke a skill: type its trigger phrase or `/skill-name` in the Agent Client panel. Skills marked `disable-model-invocation: true` are infrastructure tools that run via scripts rather than direct AI invocation.

## Folders and context keys in the workspace

The workspace shows the folders your vault really has. The skills that fill those folders find them through context keys, not folder names, as [[21-reference|chapter 21]] explains. If you rename a top-level folder, the workspace, Obsidian's own settings and the Bases do not follow a context pack automatically: they read folder names literally and are re-rendered from the pack by the `bob-install` step that renders Obsidian paths (see the troubleshooting entry in [[20-troubleshooting|chapter 20]]).

## Base Links

Base Links is a shortcut panel that lists every `.base` file in `{vault.bases}`. Clicking a link opens the Base in Obsidian's native Base viewer, which supports inline field editing. Use Base Links when you want to edit a record's fields in place rather than opening the full note.

## Settings

Settings controls all plugin-level configuration. Changes take effect immediately.

| Setting area | Controls |
|-------------|---------|
| Modules | Toggle Planner, CRM, PRM on/off; disabled modules disappear from nav and reports |
| App | Default tab on open, week start day, daily note folder, task and journal heading names |
| Task mode | Checkbox only / TaskNotes only / Hybrid — determines what Productivity report reads |
| Team person categories | Which `person_category` values appear in the Team view |
| Custom entities | Load or reload `entities.json` for entity type overrides |
| Currency | Display currency for deal values and invoice amounts |
| Reminders | Enable desktop notifications, clear completed reminders |
| TaskNotes folders | Active folder and archive folder paths |

## How the Plugin Reads Your Data

The plugin resolves field names and display settings through four layers. Later layers override earlier ones.

| Layer | Source | Role |
|-------|--------|------|
| 1 — Built-in fallback | Inside `main.js` | Default field names; keeps the plugin functional in an empty vault |
| 2 — Schemas | `{vault.schemas.source}/{entity}.yaml` | Field keys, labels, types, enums, required flags |
| 3 — Bases | `{vault.bases}/{Entity}.base` | Column visibility, filters, sort order, groupBy, named views |
| 4 — Custom entities | `.obsidian/plugins/bob-workspace/entities.json` | Add entity types, override folder paths, add enum values |

Editing schemas and base files is the normal route to changing how the workspace looks. You do not need to touch code. Template files are excluded automatically — any file in a path segment named `Templates` or `templates` is ignored by all entity lists and dashboards.

