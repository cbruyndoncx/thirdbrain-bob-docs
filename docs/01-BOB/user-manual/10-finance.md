---
description: 'How BOB supports the full record-to-report cycle: bookkeeping, AR, AP,
  period close, and financial reporting'
title: BOB User Manual — 10. Finance & Administration
---

# 10. Finance & Administration

This chapter covers BOB's role in your company's accounting and administration. The underlying workflow is the **record-to-report cycle**: every transaction is captured as a journal entry against a chart of accounts, periods are closed in sequence, and financial statements are produced from a signed-off trial balance. BOB handles the mechanical work at each stage. You handle the approvals, the judgement calls, and the filings.

BOB does not connect to bank accounts or tax authorities directly. It prepares documents and postings; you review them, press send, and sign them off. That division of labour is deliberate — the skills are built around it.

---

## 10.1 The Accounting Backbone

### Chart of accounts and accounting periods

Every finance workflow depends on two foundational records: a **chart of accounts** (COA) and a set of **accounting periods**.

The `coa-account` skill manages COA records. It creates, validates, and updates account codes for your jurisdiction — Belgium (PCMN/MAR scheme), UAE (IFRS-aligned), or others. Run it once when setting up, then again whenever you add a new account class.

Accounting periods live in `{company.finance}/PERIODS/`. Each period record carries a status lifecycle:

| Status | Meaning |
|--------|---------|
| `open` | Transactions can be posted freely |
| `soft-closed` | Period is provisionally closed; only adjustments allowed |
| `hard-closed` | Period is locked; no further postings permitted |

You move a period from `open` to `soft-closed` to `hard-closed` by completing the period close (see section 10.4). Once hard-closed, the period's trial balance is the authoritative record.

### Journal entries

Journal entries are the unit of record. Every invoice raised, every payment received, every accrual posted — all end up as a balanced journal entry in `{company.finance}/JOURNALS/`. The `journal-entry-poster` skill creates these entries from source documents: client invoices, supplier invoices, and payment confirmations.

**Posting discipline:** a journal entry must link back to its source document via the `source_document` field. BOB enforces this when posting through skills. Do not create free-standing entries without a source — the trial balance validator will flag them.

---

## 10.2 Accounts Receivable

### Raising and collecting invoices

| Step | What you do | What BOB does | Output | Saved to |
|------|-------------|---------------|--------|----------|
| 1. Raise an invoice | Confirm the line items and amounts | `invoice-description` converts completed work into billing copy | Invoice draft | `{client.invoices}` |
| 2. Collect supplier invoices | Forward emails or point BOB at Gmail | `invoice-collector` downloads PDFs, renames to accounting convention, uploads to Drive | Invoice files in Drive | Google Drive / `02-INVOICES/` |
| 3. Post the entry | Review the draft JE | `journal-entry-poster` creates the AR revenue entry | Journal entry | `{company.finance}/JOURNALS/` |
| 4. Follow up | Trigger a reminder | `ar-followup` drafts payment reminders from Gmail and invoice aging data | Email draft | Returns draft for review |
| 5. Escalate | Mark invoice overdue | `collections-escalation` generates tiered escalation letters and tracks dispute status | Escalation note + email | `02-INVOICES/` + email draft |

**AR aging** is tracked through the `ar_days_aging` and `ar_overdue_eur` KPIs visible in your finance dashboard. BOB flags accounts in amber or red automatically when you run `financial-reporting`.

The escalation sequence has three tiers: a polite reminder, a firm notice, and a formal demand. `collections-escalation` decides the tier based on days overdue and prior contact history. You review and send each communication — BOB does not send emails autonomously.

---

## 10.3 Accounts Payable — Requisition to Payment

The AP workflow is a three-way flow: purchase requisition → purchase order → supplier invoice match. Each step has a human approval gate.

### Step 1 — Purchase requisition

A team member identifies a need and creates a purchase requisition with `purchase-requisition`. The skill captures the business need, cost estimate, spend category, and approval routing.

| Field | Captured by |
|-------|-------------|
| Business justification | You describe; BOB drafts |
| Spend category | BOB classifies from your COA |
| Estimated amount | You enter |
| Approval status | You set (`pending` → `approved` / `rejected`) |

Requisition records live in `{company.finance}/AP/REQUISITIONS/`.

### Step 2 — Purchase order

Once a requisition is approved, run `purchase-order` to generate the formal PO. BOB pulls the supplier record, applies default payment terms, and produces a PO document ready to send. You review the line items and authorise before it goes out.

PO records live in `{company.finance}/AP/ORDERS/`. Each PO carries an `approval_status` field (`draft` → `approved` → `sent` → `fulfilled` / `cancelled`).

### Step 3 — Supplier invoice and three-way match

When the supplier invoice arrives, `order-to-pay` performs the three-way match: PO terms vs. delivery acceptance vs. invoice amount. Discrepancies surface as exceptions for your review. On approval, `journal-entry-poster` posts the AP expense entry and the subsequent payment entry.

Supplier invoices live in `{company.finance}/AP/INVOICES/`. The `match_status` field shows `matched`, `partial`, or `disputed`.

---

## 10.4 Period Close

Closing a period is the most sequenced workflow in the finance module. The `period-close-orchestrator` skill manages it end to end. You start it once; it creates a close checklist, calls sub-skills in the required order, and gates the hard close until every item is signed off.

### Starting a close

Tell BOB: *"Start the monthly close for [period]."* The orchestrator opens the close record in `{company.finance}/CLOSE/` and begins the sequence.

### Close sub-skills

The orchestrator calls the following skills in sequence. You can also run each one independently if you need to rerun a step.

| Sub-skill | What it does |
|-----------|-------------|
| `bank-reconciliation` | Matches GL cash balances to bank statements; surfaces timing differences and unrecorded items |
| `fixed-asset-register` | Posts monthly depreciation entries under IAS 16; handles disposals and impairments |
| `lease-register` | Posts IFRS 16 interest and right-of-use depreciation entries |
| `gratuity-calculator` | Calculates and posts the monthly gratuity accrual for relevant jurisdictions |
| `fx-revaluation` | Revalues foreign-currency receivables, payables, and cash under IAS 21; posts FX gain/loss entries |
| `ecl-calculator` | Calculates the IFRS 9 expected credit loss provision on trade receivables |
| `revenue-recognition-tracker` | Confirms IFRS 15 performance obligations are correctly recognised for the period |
| `trial-balance-generator` | Aggregates all posted journal entries into the period trial balance |
| `vat-return-preparer` | Compiles output and input VAT from posted invoices; produces the VAT return for your jurisdiction |
| `ct-return-preparer` | Prepares the corporate tax provision and, for year-end periods, the CT return filing |

Each sub-skill produces a reviewable output. You sign off each one before the orchestrator advances. If a step fails review, you correct the underlying postings and re-run that sub-skill alone.

### Soft close vs. hard close

After all checklist items are signed off, the orchestrator moves the period to `soft-closed`. At this point you can still post adjustments. When you confirm the accounts are final, the orchestrator hard-closes the period — the trial balance is locked and financial statements can be generated.

---

## 10.5 Financial Reporting

With a hard-closed, signed-off trial balance, three skills produce the period's financial output.

| Skill | What it produces | Where saved |
|-------|-----------------|-------------|
| `trial-balance-generator` | Period trial balance with opening balances, movements, and closing balances per account | `{company.finance}/REPORTS/` |
| `financial-statement-generator` | The four IFRS statements (P&L, balance sheet, cash flow, equity) assembled from the trial balance | `{company.finance}/REPORTS/` |
| `financial-reporting` | Management report: P&L summary, cash position, AR/AP aging, margin by client or project, month-on-month comparison | `{company.finance}/REPORTS/` |

`financial-statement-generator` requires the trial balance to be in `signed-off` status before it will run. This is intentional: it prevents statements being generated from an incomplete period.

The `fs-notes-generator` skill adds the notes pack — accounting policies, going-concern assessment, and disclosure notes — required for statutory accounts.

---

## 10.6 Good Practices

- **One source document per journal entry.** BOB links entries to source documents automatically through skills. If you post a manual entry, fill in `source_document` yourself.
- **Close periods in order.** Do not hard-close a later period before the previous one is hard-closed. The trial-balance balances roll forward sequentially.
- **Review before filing.** BOB prepares VAT and CT returns; a human must review the figures and submit them. Treat the skill output as a draft, not a filing.
- **Keep supplier records current.** `purchase-order` and `order-to-pay` pull payment terms from the supplier record. Stale records produce wrong payment dates.
- **Use the escalation tiers in sequence.** Skipping from a polite reminder to a formal demand without the interim notice weakens your collections position. Let `collections-escalation` manage the sequence.

