---
type: knowledge-base
title: "BOB User Manual — 11. Operations & Projects"
description: "Project management lifecycle, meeting intelligence, process improvement, supplier management, and order fulfilment in BOB"
status: draft
created: 2026-08-07
modified: 2026-08-07
tags: [bob, user-manual, wiki]
---

# 11. Operations & Projects

This chapter covers the work between a signed contract and a delivered result. Projects, processes, meetings, suppliers, and fulfilment all live here. The common thread is **status and checkpoints**: every workflow in this module has a defined lifecycle, and BOB surfaces blockers before they become problems.

---

## 11.1 Project Structure

A project in BOB belongs to a client or to a company division. It lives at `{client.projects}` for client work, or `{company.root}/{division}/YYYY-MM-{name}/` for internal initiatives.

Every project has a `project_id`, a `project` title, and a `status` field. The status lifecycle is:

| Status | Meaning |
|--------|---------|
| `planning` | Charter approved; schedule and WBS in progress |
| `active` | Delivery underway |
| `on-hold` | Paused; reason documented in the project note |
| `completed` | All deliverables accepted; closure report filed |
| `archived` | Closed project retained for reference |

PM artifacts (charter, WBS, schedule, risk register, RACI, status reports, closure report) all carry their parent `project_id`, which lets BOB pull the full project picture at any time.

---

## 11.2 Project Management Skills by Phase

BOB's PM skills follow the standard project lifecycle. The recommended entry point for any new project is `project-context`, which establishes the delivery approach and tailoring decisions and then chains into `project-charter` automatically.

### Initiate

| Skill | When to use | Output |
|-------|-------------|--------|
| `project-context` | First step on any new project — sets up PMBOK 7 tailoring and delivery approach | Context record + charter hand-off |
| `project-charter` | Formalise scope, objectives, stakeholders, milestones, and budget | Charter document |

Run `project-context` before anything else. It prevents you from applying a heavyweight sequential approach to a two-week internal job, and vice versa.

### Plan

| Skill | When to use | Output |
|-------|-------------|--------|
| `project-wbs` | Decompose scope into work packages with effort estimates | WBS document + optional canvas |
| `project-schedule` | Build a CPM schedule with PERT estimates | SVG Gantt chart + JSON schedule |
| `project-risk` | Identify and quantify risks with Monte Carlo simulation | Risk register + probability chart |
| `project-raci` | Assign responsibilities across tasks and team roles | RACI matrix (activity-based and role-based views) |
| `project-stakeholder` | Build the formal stakeholder register and power-interest grid | Stakeholder register + SVG grid |

These skills read each other's outputs. `project-schedule` will reference the WBS work packages; `project-raci` will reference the schedule tasks. Run them in the order shown.

### Execute

During delivery, the primary tool is `project-status`. Run it weekly or before any steering committee meeting.

**What you do:** tell BOB to generate a status report for the project.

**What BOB does:** reads the project's PM artifacts, milestones, risk register, and any recent meeting notes; derives a RAG (red/amber/green) health rating; flags overdue items and budget variances.

**Output:** an executive status report saved to the project folder.

The `project-evm` skill adds earned value metrics — CPI, SPI, cost variance — as an SVG trend chart if you have actual cost and progress data recorded.

For scope changes, `project-change-control` maintains a change log and routes approvals. Do not adjust the WBS or schedule directly without logging a change request first.

### Close

| Skill | When to use | Output |
|-------|-------------|--------|
| `project-closure` | All deliverables accepted | Closure report: deliverable acceptance, lessons learned, performance summary, outstanding handoffs |

The closure report must be filed before a project moves to `completed` status. You cannot close a project with draft deliverables outstanding — the vault validator will block it.

---

## 11.3 Meeting Intelligence

Meetings generate decisions and actions. Without a system, both disappear into inboxes.

`meeting-intelligence` analyses meeting transcripts, notes, or recording-derived text and extracts:

- Decisions taken (with owner and date)
- Action items (owner, due date, status)
- Blockers and open questions
- Sentiment and execution-risk signals
- A follow-up email draft for the attendees

### Workflow

| Step | What you do | What BOB does | Output |
|------|-------------|---------------|--------|
| 1. Provide notes | Paste or link the meeting notes or transcript | Reads and structures the content | — |
| 2. Review extractions | Check decisions and actions for accuracy | Flags ambiguous ownership or missing due dates | Structured extraction |
| 3. Save | Confirm the output | Saves to the meeting note in the relevant `20-MEETINGS/` folder | Meeting note with decisions and action items |
| 4. Send summary | Approve the email draft | Returns draft for review | Email draft |

Decisions extracted by `meeting-intelligence` can be promoted to the decision log at `{company.decisions}`. Action items become tasks in `{output.tasks}`. BOB will suggest both; you decide which to keep.

**Good practice:** run `meeting-intelligence` within 24 hours of the meeting, while context is fresh and ownership is still clear.

---

## 11.4 Processes and Improvement

### Process definitions and runs

A process definition describes how repeating work flows through your business — inputs, activities, responsible skills, and completion conditions. Definitions live in `{company.processes}/definitions/`. Each time a process runs, it creates a process run record in `{company.runs}` with its own `case_id` and event log.

Process definitions connect to value chains. When you ask BOB to run a process, it follows the definition: calls the skills in sequence, applies any policies, and halts at approval gates for your sign-off.

### Continuous improvement

`process-kaizen` runs an AI-powered Kaizen analysis on a process that has already been mapped. It reads the existing process note, identifies waste (muda), produces a 5S checklist, and sets up a PDCA cycle. This skill is a downstream consumer — it does not re-map the process from scratch. You need a process note in place before invoking it.

`root-cause-analysis` uses a 5-Whys framework and fishbone diagrams to diagnose recurring failures or customer issues. Use it when the same problem appears more than twice, or when a single incident has significant business impact.

| Skill | Input required | Output |
|-------|---------------|--------|
| `process-kaizen` | Existing `type: process` note | Waste audit, PDCA cycle, improvement suggestions |
| `root-cause-analysis` | Problem description or issue record | Root cause tree, contributing factors, corrective actions |

---

## 11.5 Suppliers and Procurement

### Supplier records

Suppliers live in `{company.suppliers}`. Each supplier record carries `supplier_id`, `supplier_name`, spend category, default payment terms, and annual contract value. Keeping these current is important — the AP skills pull payment terms directly from the supplier record.

For how supplier records connect to purchase orders and invoices, see [[10-finance|chapter 10, Finance & Administration]].

### Sourcing

`strategic-sourcing` handles new supplier selection: spend analysis, Kraljic matrix positioning, RFI/RFP/RFQ templates, total cost of ownership calculations, and BATNA negotiation preparation. Use it when you are evaluating a new vendor category or renegotiating a significant contract.

### Supplier performance

`supplier-feedback` tracks ongoing supplier performance and review history. It is the longitudinal partner to `strategic-sourcing`: after you have selected a supplier, `supplier-feedback` captures delivery scores, quality ratings, and corrective action history over time.

A typical quarterly cycle:

1. Run `supplier-feedback` — review performance against agreed KPIs
2. If scores are below threshold, run `root-cause-analysis` on the failure pattern
3. If the contract is up for renewal, return to `strategic-sourcing` for the renegotiation

### Procurement within projects

For project-specific procurement — make-or-buy decisions, vendor evaluation, contract type selection — use `project-procurement`. It produces a procurement management plan tied to the project and its WBS.

---

## 11.6 Order Fulfilment and Delivery

For product businesses, BOB supports the order-to-confirmation chain.

| Skill | Stage | What it does |
|-------|-------|-------------|
| `order-management` | Order received | Tracks the order lifecycle from receipt to fulfilment; surfaces fulfilment bottlenecks and backlog prioritisation |
| `logistics-shipping` | Dispatch | Analyses shipment performance, carrier options, and delivery routes |
| `delivery-confirmation` | Confirm | Generates proof-of-delivery documents and manages customer sign-off |

These skills work from data you provide — ERP exports, CSV files, or direct ERP queries if an integration is configured. They produce reports and documents; physical logistics remain your responsibility.

The `order-to-fulfill` playbook chains all three skills into a single repeatable flow. Trigger it when an order is confirmed and work your way through the checkpoints.

---

## 11.7 Good Practices

- **Start every project with `project-context`.** The tailoring step prevents over-engineering small jobs and under-planning complex ones.
- **Run `project-status` before steering meetings, not after.** Preparing the report forces a look at the data; findings in the room are already late.
- **Log change requests before editing plans.** A change request creates a decision trail. Direct edits to the schedule or WBS create version confusion.
- **Run `meeting-intelligence` on every significant meeting.** Undocumented decisions are the most common source of rework and missed handoffs.
- **Keep supplier records current.** Stale payment terms and contact details create AP delays and missed escalation windows.
- **Use `process-kaizen` after at least one full process run.** Without run data, the waste analysis is speculative. Let the process run, then improve it.

