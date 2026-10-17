---
type: knowledge-base
title: "BOB User Manual — 8. Sales & CRM"
description: "The lead-to-cash module: lead lifecycle, deal stages, qualification and proposal workflows, pipeline reporting, and invoicing handoff"
status: draft
created: 2026-08-07
modified: 2026-08-31
tags: [bob, user-manual, wiki]
---

# 8. Sales & CRM

The Sales & CRM module is BOB's implementation of the **lead-to-cash value chain** — the full journey from a name on a list to a paid invoice. Every skill, record type, and workflow in this module exists to move deals forward and keep the pipeline honest.

You are the decision-maker at every gate. BOB handles the research, the drafting, and the reporting.

## 8.1 The lead-to-cash backbone

The chain runs in seven stages. Skills and playbooks are mapped to each one.

| Stage | What happens | BOB's role |
|-------|-------------|------------|
| Prospect | Identify and reach potential buyers | Drafts outreach, scouts trigger events, builds target lists |
| Qualify | Assess fit, authority, need, timeline | Scores the lead, surfaces gaps, prepares discovery questions |
| Propose | Scope the work, price it, present it | Drafts proposals and quotes, models pricing |
| Close | Negotiate terms and sign | Prepares objection responses, tracks open items |
| Deliver | Do the work | Hands off to the delivery team (see [[11-operations-projects|chapter 11]]) |
| Invoice | Bill for completed work | Generates invoice descriptions, confirms amounts |
| Collect | Chase and confirm payment | Drafts reminders, escalates overdue accounts |

This chapter covers Prospect through Invoice. Collection is handled by the Finance module — see [[10-finance|chapter 10]].

## 8.2 Lead records and the lead lifecycle

Every lead lives as a note in the vault under `{lead.root}`. The note holds contact details, qualification data, activity history, and the current stage tag.

### Lifecycle stages

A lead moves through a defined set of states. You control the transitions; BOB updates the record when you confirm.

| Stage tag | Meaning |
|-----------|---------|
| `new` | Captured but not yet assessed |
| `qualified` | Meets your ICP; worth pursuing |
| `nurture` | Interesting but not ready — keep warm |
| `disqualified` | Poor fit or timing; archived with a reason |
| `client` | Deal won; promoted to a client record |

When a deal closes, BOB promotes the lead note to `{client.root}` and creates the project folder structure. The original lead note is linked from the client record as provenance.

### What "qualified" means

BOB qualifies against the criteria you configured during setup — typically industry, company size, role of the contact, budget signal, and timeline. The `lead-qualifier` skill produces a scorecard; you review it and confirm or override the outcome. Your override is logged.

## 8.3 Deal stages

Active deals carry a deal-stage tag distinct from the lead lifecycle. The deal stage tracks sales progress; the lead lifecycle tracks the prospect relationship.

| Deal stage | Typical exit criteria |
|------------|-----------------------|
| `lead` | ICP confirmed, contact identified |
| `qualified` | Pain confirmed, decision-maker engaged |
| `proposal` | Proposal sent, no objections pending |
| `negotiation` | Commercial terms under discussion |
| `won` | Contract signed or PO received |
| `lost` | Prospect chose another path — reason recorded |

BOB never changes a deal stage automatically. You record the change; BOB updates the `sales-pipeline-report` on the next run.

## 8.4 Workflows

### Capturing a lead

When a new prospect appears — from an inbound inquiry, a referral, a conference, or an outbound list — you create a lead note. You can do this manually or ask BOB:

1. Tell BOB: "Add a new lead — Acme Corp, contact Jana Hofer, CFO, referred by our accountant."
2. BOB creates the note in `{lead.root}` with the stage tag `new` and today's date.
3. BOB prompts you for any missing qualification fields.
4. You review and save.

**Output:** a lead note at `{company.leads}/acme-corp/acme-corp.md`.

### Qualifying a lead

Run this after a first conversation or when enough information exists to score the lead properly.

1. Open the lead note or name the prospect to BOB.
2. Invoke `lead-qualifier`. BOB reads the lead note and your ICP configuration.
3. BOB returns a qualification scorecard: strengths, red flags, missing information, and a recommended stage.
4. If gaps remain, BOB can run `prospect-audit` to pull public information about the company and add it to the note.
5. You confirm the stage (`qualified`, `nurture`, or `disqualified`) and optionally add a note explaining your decision.

**Output:** updated lead note with qualification scorecard appended and stage tag set.

### Scoping and proposal

Once a lead is qualified, the work shifts to defining the engagement and presenting a price.

1. Run `proposal-writer`. BOB interviews you about the deal: problem, scope, deliverables, timeline, investment.
2. BOB drafts the proposal document and saves a working draft to `{client.sales}`.
3. Run `quotation-generator` if the proposal requires a priced line-item quote. BOB reads your service catalog (configured in `{company.root}`) and builds the quote.
4. If pricing needs justification or competitive framing, run `pricing-strategy`. BOB models the options and notes the rationale.
5. Review all three documents together. Revise in Obsidian or send BOB targeted corrections.
6. When satisfied, mark the draft `status: approved` in the frontmatter. BOB does not send anything — distribution is your action.

**Output:** proposal note and optional quote note in `{client.sales}`, rendered PDF via `branded-pdf` if requested.

### Outreach and sequences

For cold or semi-warm outreach, use the channel-appropriate skill.

| Skill | Channel | What you provide |
|-------|---------|-----------------|
| `cold-email` | Email | Target profile, your offer, any known context |
| `linkedin-outreach` | LinkedIn | Target profile, connection angle, tone preference |
| `outbound-sequence` | Multi-step email | Sequence length, goals, escalation logic |

BOB drafts in your brand voice (as captured by `brand-voice-generator` — see [[09-marketing|chapter 9]]). Each draft lands in `{company.marketing}/{channel}/` as a file you review before sending. BOB does not send messages.

For account-based or multi-channel campaigns, use the [[ABM multi-channel sequence]] playbook, which chains these skills with tracking checkpoints.

### Pipeline reporting

Run `sales-pipeline-report` before any pipeline review meeting or at your cadence (weekly is typical).

1. Invoke the skill. BOB reads all active lead and deal notes.
2. BOB aggregates: deal count by stage, total pipeline value, average days in stage, deals past expected close date, win rate over the trailing 90 days.
3. The report is saved to `{company.reports}` and returned in the panel.
4. Stale deals (past expected close with no recent activity) are flagged. BOB surfaces them; you decide what to do.

**Output:** a dated pipeline report note. Key KPIs tracked: `qualified_pipeline_eur`, `win_rate_90d`, `stale_pipeline_pct`.

## 8.5 Skills in this module

| Skill | Primary use |
|-------|-------------|
| `lead-qualifier` | ICP scoring and stage recommendation |
| `prospect-audit` | Public research on a company or contact |
| `crm-pipeline` | Lead and deal record management |
| `proposal-writer` | Full proposal drafting |
| `quotation-generator` | Priced line-item quotes from your catalog |
| `pricing-strategy` | Pricing options and justification |
| `cold-email` | Cold outreach email drafts |
| `linkedin-outreach` | LinkedIn message drafts |
| `outbound-sequence` | Multi-step email sequences |
| `sales-pipeline-report` | Pipeline health and deal aggregation |
| `objection-playbook` | Objection response library |
| `negotiation` | Negotiation prep and tactics |
| `sales-enablement` | Battle cards, talk tracks, competitive positioning |

## 8.6 Where records live

| Record type | Vault path |
|-------------|------------|
| Active leads | `{lead.root}` |
| Promoted clients | `{client.root}` |
| Proposals and quotes | `{client.sales}` |
| Outreach drafts | `{company.marketing}/{channel}/` |
| Pipeline reports | `{company.reports}` |
| Service catalog | `{company.offerings}` |

## 8.7 Handoff to Finance

When a deal moves to `won` and delivery is underway or complete, the invoicing step begins. The trigger is yours — BOB does not auto-invoice.

1. Open the client project note and tell BOB: "Generate the invoice description for this engagement."
2. BOB runs `invoice-description`, reads the scope and agreed amounts from the proposal and quote, and drafts the invoice line items and payment terms.
3. You or your finance admin transfers the line items to your accounting system. BOB does not write directly to any external accounting platform.
4. The invoice record is saved to `{client.invoices}` and linked from the project note.

For collection follow-up after an invoice is overdue, see [[10-finance|chapter 10, Finance]].

## 8.8 Playbooks for this module

| Playbook | When to use |
|----------|-------------|
| [[Lead-to-Cash E2E]] | Run the full chain end to end for a new deal |
| [[Sales Call Prep]] | Prepare for a discovery or proposal call |
| [[MEDDPICC Qualification]] | Rigorous enterprise qualification |
| [[SPICED Discovery]] | Structured discovery for consultative sales |
| [[Gap Selling Discovery]] | Surface the prospect's current-state pain |
| [[Challenger Sale]] | Teach, tailor, take-control selling approach |
| [[Proposal from meeting]] | Fast proposal from a meeting transcript |
| [[Mutual Action Plan]] | Shared close plan with the prospect |
| [[Procurement to Signature]] | Navigate procurement and legal cycles |
| [[Win-Loss Review]] | Structured debrief on deals closed or lost |
| [[Sales conversion improvement]] | Diagnose and fix a dropping win rate |

## 8.9 Good practices

- **Keep lead notes current.** BOB's pipeline report is only as accurate as the data in the vault. A note that hasn't been updated in three weeks will produce a stale report.
- **Record disqualification reasons.** "Not now — budget frozen until Q1" is more useful than `disqualified`. BOB uses these notes when you ask it to identify re-engagement timing.
- **Don't skip the qualification scorecard.** Running `lead-qualifier` takes two minutes and forces you to test your assumptions before spending time on a proposal.
- **Mark drafts `status: approved` before distributing.** This creates a clear audit trail of what was sent and when.
- **Run a win-loss review after every closed deal.** The [[Win-Loss Review]] playbook takes under 20 minutes and builds the pattern library BOB uses to improve future proposals.

