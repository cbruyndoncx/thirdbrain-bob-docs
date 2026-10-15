---
description: The daily, weekly, and monthly operating rhythm for each BOB workspace
  area — when to act, what BOB does, and what results
title: BOB User Manual — 17. The Operating Cadence
---

# 17. The Operating Cadence

BOB is not a tool you open when you remember to. It works best when you run it on a predictable rhythm: a daily check-in, a weekly review, a monthly close. Each area of the workspace has its own cadence — its own set of recurring actions and the outputs they produce.

This chapter describes that rhythm. For each area it tells you: when to act, what you do, what BOB does, and what you end up with.

## Overview of the Rhythm

| Frequency | Areas touched |
|-----------|--------------|
| Daily | Planner, CRM, Client Work |
| Weekly | Planner, CRM, PRM, Client Work, Suppliers |
| Monthly | Finance, Reports, PRM, Suppliers |
| Ongoing | AI Workspace (as needed) |

No area requires more than a focused block of time at the right interval. The daily passes take minutes. The monthly close takes longer but follows a defined sequence.

## The Daily Briefing

Every working day starts the same way: open BOB and ask for your daily briefing. In the Agent Client panel, type:

```
Daily briefing
```

BOB reads the state of your vault and returns a structured summary: tasks due today, deals that have gone stale, client comms awaiting a reply, supplier invoices approaching due, and any flags from the previous day's notes. The briefing is generated, not stored — run it again at any point in the day to get a fresh read.

After the briefing, you move through each active area below.

---

## Planner Cadence

The Planner covers your personal operational loop: capturing work, planning today, progressing projects.

### Daily — 5 to 10 minutes

**When:** First thing, after the daily briefing.

**What you do:**

1. Open **Inbox** and clear the overdue and due-today groups. Snooze anything that genuinely cannot move today; mark done anything that has already happened.
2. Open **Today** and review the tasks for the day. Add any tasks that surfaced in the briefing using **+ Quick task**.
3. Write your daily intention in the journal textarea — one or two sentences. It autosaves.

**What BOB does:** Nothing automated here. BOB reads Today's note when you ask it to act on tasks later in the day; keeping the note current gives BOB accurate context.

**Output:** A cleared inbox, a task list for the day, and a journal entry that feeds future context.

### Weekly — 20 minutes

**When:** Monday morning or Friday close — pick one and keep it.

**What you do:**

1. Open **Calendar** and scan the past week's daily notes. Tick off any completed tasks that were not already marked.
2. Open **Projects** and check milestone progress on every active project. Update statuses and milestone tick-boxes. Add new milestones if scope has changed.
3. In the Agent Client panel, ask BOB to generate a weekly planner summary:

```
Summarise my week: tasks completed, projects advanced, anything overdue
```

**What BOB does:** Reads the past week's daily notes, TaskNotes, and project files. Returns a structured summary and flags any milestones that are overdue relative to their deadlines.

**Output:** Up-to-date project cards, a weekly summary note (if you ask BOB to save it), and a clear view of what carries forward into the next week.

---

## CRM Cadence

The CRM cadence keeps the pipeline moving and prevents deals and contacts from going cold.

### Daily — 5 minutes

**When:** After the daily briefing and planner pass.

**What you do:**

1. Open **CRM Dashboard** and read the stale deals list. Any deal older than 14 days without an edit needs an action: a follow-up, a stage change, or a close-lost.
2. Scan **Recent activity** for anything that needs a response.
3. For deals that need follow-up, go to **Pipeline**, click the card, and either drag it to the next stage or add an activity note.

**What BOB does:** On request, BOB can draft follow-up messages for stale deals. In the Agent Client panel:

```
Draft follow-up emails for stale deals in my pipeline
```

BOB reads the deal notes, any linked contact records, and recent activity, then drafts messages. Review before sending.

**Output:** Updated deal stages, new activity records, follow-up drafts in your outbox.

### Weekly — 15 minutes

**When:** Same session as the weekly planner review.

**What you do:**

1. Open **Leads** and review the `new` and `qualified` groups. Move leads that have warmed up to `qualified`; disqualify anything that has gone cold.
2. Open **Campaigns → Overview** and check active campaign status and sequence touch counts.
3. Ask BOB for a pipeline health summary:

```
Pipeline health summary — deals by stage, value at risk, win rate this quarter
```

**What BOB does:** Reads all `type: deal` and `type: activity` notes. Returns a structured pipeline summary with deal count, total value by stage, win/loss ratio, and a flag for any deals at risk of slipping.

**Output:** Updated lead statuses, a pipeline health note (save it to `{company.root}/{division}/REPORTS/` if useful), and a clear picture of the week's revenue position.

---

## Client Work Cadence

Client Work cadence keeps delivery on track: meetings logged, deliverables progressed, comms answered.

### Daily — 5 to 10 minutes

**When:** After the CRM pass.

**What you do:**

1. Open **Client Work**, select the most active client, and go to the **Comms** tab. Look for threads where `awaiting_reply` is true. Open the source note, check the thread, and either reply or log a response activity.
2. Switch to **Deliverables** and check for anything in `review` status — these are blocking the client and should move today.
3. If you had a meeting today, log it: **+ New Meeting**, fill in attendees, context, and set status to `completed`. Then ask BOB to write up the notes:

```
Write meeting notes for today's [client name] meeting
```

**What BOB does:** Reads the meeting record, any linked project and deliverable notes, and recent comms threads. Produces structured meeting notes with a decisions section and action items. The notes are saved to the meeting file.

**Output:** Meeting notes on file, comms threads actioned, deliverables unblocked.

### Weekly — 15 minutes

**When:** End of week.

**What you do:**

1. For each active client, open **Client Work → Overview** and review the summary: open deliverables, pending feedback, upcoming meetings.
2. Check the **Decisions** tab for any decisions logged this week and confirm they are documented clearly.
3. Ask BOB for a client status update:

```
Client status update for [client name] — deliverables, open items, risks
```

**What BOB does:** Reads deliverable notes, meeting notes, decision logs, and comms threads for the selected client. Returns a structured status update formatted as a client-facing summary or an internal briefing — specify which.

**Output:** A status update note saved to the client's project folder, or a draft ready to send.

---

## Finance Cadence

Finance cadence is mostly monthly, with a small daily watch on invoices.

### Daily — 2 minutes

**When:** As part of the morning briefing review.

**What you do:**

Open **Finance → Customer Invoices** and check the *Overdue* Bases view. For any overdue invoice, decide: chase, extend terms, or write off. Log your action as an activity record against the client.

**What BOB does:** On request:

```
Draft a payment reminder for overdue invoice [invoice ID]
```

BOB reads the invoice record and the client file, drafts a polite payment reminder in your brand voice. Review before sending.

**Output:** Payment reminders drafted, overdue invoice actions logged.

### Monthly — 2 to 3 hours

**When:** First week of the new month, covering the previous month.

**What you do, in order:**

1. **Close the accounting period.** Open **Finance Setup → Accounting Periods**, find last month's period, and set status to `soft-closed`. This prevents accidental postings while you reconcile.
2. **Reconcile bank accounts.** Open **General Ledger → Bank Reconciliations**, create a new reconciliation for each bank account. The plugin shows the GL balance; you enter the bank statement balance. The difference must be zero before you proceed.
3. **Review journal entries.** Open **General Ledger → Journal Entries** and post any entries still in `draft` status that belong to the closing period.
4. **Generate the trial balance.** Ask BOB:

```
Generate a trial balance for [month] [year]
```

BOB reads the posted journal entries for the period, aggregates debits and credits per account code, and creates a `type: trial-balance` note. Confirm that total debits equal total credits.

5. **Prepare financial statements.** Ask BOB:

```
Prepare financial statements for [month] [year] from the trial balance
```

BOB creates a `type: financial-statement` note for P&L, Balance Sheet, and Cash Flow, linked to the trial balance.

6. **Check tax deadlines.** Open **Finance → Tax → Overview** and review the upcoming deadline dashboard. If a VAT return is due, ask BOB to prepare a draft:

```
Prepare VAT return for period [start] to [end]
```

7. **Hard-close the period.** Once statements are reviewed and signed off, set the accounting period status to `hard-closed`.

**What BOB does:** Reads journal entries, account codes, and bank reconciliation records. Aggregates and creates the trial balance, financial statement, and tax return notes. All records are saved to `{company.finance}`.

**Output:** Reconciled accounts, posted journal entries, trial balance, financial statements, tax return draft, hard-closed period.

---

## PRM Cadence

Partner relationships need a light weekly watch and a monthly review.

### Weekly — 10 minutes

**When:** End of week, after the CRM review.

**What you do:**

1. Open **PRM → Overview** and check: open registrations approaching expiry, certifications expiring within 90 days, pending commissions.
2. For any registration expiring within 30 days, log a follow-up activity and contact the partner.
3. Review any commissions in `pending` status that should have moved to `paid` this period.

**What BOB does:** On request:

```
Partner follow-up list — registrations expiring, certifications due, pending commissions
```

BOB reads all PRM entity notes and returns a consolidated action list with due dates.

**Output:** A partner action list, activity records logged, commission statuses updated.

### Monthly — 20 minutes

**When:** Mid-month, after the finance close.

**What you do:**

1. Open **PRM → Analytics** and review deals influenced and revenue attributed per partner.
2. Open **PRM → Certifications** and check the expiry-sorted view for renewals due next quarter.
3. Ask BOB for a partner performance summary:

```
Monthly partner performance summary
```

**What BOB does:** Reads partner, deal, commission, and registration notes. Returns a structured summary of each active partner's performance for the period.

**Output:** A partner performance note saved to `{company.partners}`, updated commission records.

---

## Suppliers Cadence

Supplier cadence is primarily weekly for AP processing and monthly for spend review.

### Weekly — 10 minutes

**When:** Start of week.

**What you do:**

1. Open **Supplier Invoices** (vault-wide view) and switch to the *Awaiting approval* Bases view. Review and approve or reject each invoice. For approved invoices, confirm the PO match status (2-way or 3-way match).
2. Open **Purchase Requisitions** (vault-wide view) and clear the approval queue — approve, reject, or return for clarification.
3. For approved requisitions, convert to purchase orders using **+ New Purchase Order** and link the originating PR via `pr_ref`.

**What BOB does:** On request:

```
AP processing summary — invoices to approve, requisitions pending, POs awaiting delivery
```

BOB reads supplier invoice, requisition, and PO notes and returns a consolidated action list.

**Output:** Approved invoices, created POs, cleared requisition queue.

### Monthly — 20 minutes

**When:** End of month, before the finance close.

**What you do:**

1. Open **Suppliers → Suppliers tab** and check for suppliers with contracts renewing in the next 60 days.
2. Ask BOB for a procurement spend summary:

```
Procurement spend summary for [month] by supplier and category
```

**What BOB does:** Reads paid supplier invoices and PO records for the period. Returns a spend summary by supplier and spend category.

**Output:** A spend summary note, a list of contracts due for renewal review.

---

## Reports Cadence

Reports are generated on demand rather than on a fixed schedule. The natural trigger is the end of a period or a business review.

| Report | When to run | Typical use |
|--------|-------------|-------------|
| Pipeline | Weekly, after CRM review | Board update, sales meeting prep |
| Sales | Monthly, after finance close | Revenue recognised, top clients, deal sources |
| Partners | Monthly, after PRM review | Partner performance, commission reconciliation |
| Activity | Weekly or monthly | Outreach volume, contact and deal coverage |
| Productivity | Weekly | Task completion rate, project delivery pace |

To generate a report, open **Reports** in the Workspace and select the relevant screen. Alternatively, ask BOB:

```
Generate a [report name] report for [period]
```

BOB reads the underlying entity notes, aggregates the data, and returns the report as structured output. If you want it saved, specify a path or ask BOB to save it to `{company.root}/{division}/REPORTS/`.

---

## AI Workspace Cadence

The AI Workspace does not have a fixed cadence — you use it when you need a skill or playbook that is not part of your routine.

Two situations where it is worth opening:

1. **Before starting a new type of work.** Open **AI Workspace → Skills**, search for the relevant category, and read the skill's trigger phrase and prerequisites before invoking it in the ACP.
2. **When setting up a new recurring process.** Browse **AI Workspace → Playbooks** for a playbook that matches the workflow. Copy the trigger phrase and paste it into the ACP to run the sequence.

For a full reference to skills and playbooks, see [chapter 14, The Skills System](14-skills-system.md) and [chapter 16, Playbooks & Processes](16-playbooks-processes.md).

---

## Cadence at a Glance

| Area | Daily | Weekly | Monthly |
|------|-------|--------|---------|
| Planner | Clear inbox, plan today | Project review, weekly summary | — |
| CRM | Stale deal follow-up | Pipeline health, lead triage | — |
| Client Work | Comms, deliverables, meeting notes | Status updates | — |
| Finance | Overdue invoice watch | — | Period close, statements, tax |
| PRM | — | Registration and certification watch | Performance summary |
| Suppliers | — | AP processing, requisition approval | Spend summary, contract renewals |
| Reports | — | Pipeline, productivity | Sales, partners, activity |

The cadence is a framework, not a rigid schedule. If a client project is quiet, skip the Client Work daily pass. If the pipeline is thin, the CRM weekly review takes five minutes. Run the passes that are relevant to where the business is right now.

