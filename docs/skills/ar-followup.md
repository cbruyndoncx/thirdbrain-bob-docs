---
description: Obsidian-native accounts receivable management. Track invoices from creation through collection, send payment reminders, and never lose sight of outstanding money.
title: ar-followup
---

# ar-followup

Obsidian-native accounts receivable management. Track invoices from creation through collection, send payment reminders, and never lose sight of outstanding money.

| | |
|---|---|
| **Area** | Finance |
| **Category** | finance |
| **Level** | beginner |
| **Input** | data |
| **Output** | spreadsheet |
| **Setup** | [none] |
| **Roles** | [Finance Manager] |

Drafts AR follow-ups from Gmail and invoice records, tracks outstanding invoices, and prepares payment reminders.

## How you ask

- “Log a new invoice for client Acme Corp — $5,000 due in 30 days”
- “Send payment reminders for all overdue invoices”
- “Run an AR aging report for this quarter”
- “Check which invoices are still outstanding”

## Inputs

- invoice-template — Template the new invoice note is built from — supplies the frontmatter field set the route must populate.
- profile — Supplies the legal client name, payment terms, and currency the invoice is issued under.
- invoices — Existing invoice notes, scanned to find the highest `INV-{YYYY}-{NNN}` so the new ID is unique vault-wide.
- request — The invoice to raise — client, amount, and any deal or billing summary it is drawn from.
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set
- invoices — The invoice note being settled — its current `payment_status` and `amount` decide whether the payment closes it.
- profile — Confirms the currency and banking relationship the receipt is booked against.
- request — Which invoice was paid, the amount received, the date, and the bank account it landed in.
- invoices — Invoice being chased — `due_date` and `reminder_count` select which escalation template applies.
- profile — Billing contact and agreed payment terms the reminder addresses and cites.
- request — Which invoice or invoices to chase, and any tone or deadline the sender wants imposed.
- invoices — The full invoice set across all clients — the population the aging buckets are computed from.
- profile — Reporting currency and client naming used to label the per-client breakdown.
- books-root — Bookkeeping root the report is written under; defaults to the company finance root (`company.finance`). One run, one root.
- request — Reporting cut asked for — as-at date, client filter, and whether overdue statuses should be auto-updated.
- invoices — Invoice set filtered to the reporting month, supplying invoiced, collected, and outstanding totals.
- month — Accounting month to summarise, written `YYYY-MM`; it scopes the figures and names the output file.
- books-root — Bookkeeping root the summary is written under; defaults to the company finance root (`company.finance`). One run, one root.
- profile — Reporting currency and entity name the summary is presented under.

## Outputs

- Aging buckets, per-client outstanding balances, payment velocity, collection rate, and 60-day-plus alerts.
- Invoice updated with `last_reminder_date`, incremented `reminder_count`, `next_reminder_date`, and an appended Activity Log entry.
- Invoice updated with `paid_date`, `amount_paid`, `payment_method`, the `je_ref` wikilink, and an appended Activity Log entry.
- New invoice note with populated frontmatter, `payment_status`, and an initialised Activity Log.
- Reminder email shown for send/edit/cancel approval before anything leaves the vault.
- Total invoiced, total collected, total outstanding, outstanding-invoice count, and collection rate for the month.
- {client.invoices}/{invoice_id}.md
- {scope.finance}/AR/ar_aging_{YYYY-MM}.md
- {scope.finance}/AR/ar_summary_{YYYY-MM}.md

