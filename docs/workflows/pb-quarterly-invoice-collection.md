---
title: Quarterly Invoice Collection
---

# Quarterly Invoice Collection

*Every expected supplier invoice for the quarter is either filed on Google Drive under the naming convention with its date recorded in the tracking sheet, or listed as an explicit exception with the reason*

> Quarter's closed. Half the supplier invoices are still in someone's inbox.

| | |
|---|---|
| **Area** | Finance |
| **Time savings** | Typical run: 45-90 minutes across two sittings (agent pass, then portal downloads) |
| **Try it** | "End of quarter, or 'collect the invoices for Q<n>' — supplier invoices for the period must be gathered, named, and filed before the books close" |
| **Compounding** | Each run refines templates and context — 5 automated steps improve with accumulated data |
| **Frequency** | Per trigger event |

## Inputs

- 📅 Quarter and explicit date boundaries (e.g. Q3 2026 → 2026/07/01 to 2026/10/01)
- 👤 Destination Drive folder name for the period
- 📁 Path to the subscriptions sheet
- 📋 Card statement screenshots or exports for the quarter
- 📝 Any supplier exclusions for this run

## What BOB does

1. xlsx-tools → Read the subscriptions sheet and the card statements; build the expected-invoice checklist for the quarter: one row per supplier charge with date, amount, and an empty invoice-received column
2. Confirm the checklist — flag any charge that is private rather than business, and any supplier known to be portal-only before the search runs
3. invoice-collector → Search Gmail for the quarter's date boundaries, download PDF attachments, rename to `yyyymmdd_supplier_invoiceid.pdf`, upload to the period's Drive folder
4. xlsx-tools → Reconcile collected PDFs against the checklist: fill the invoice date and filename per matched row, and report the unmatched rows as the portal list — the invoices that must be fetched by hand
5. Log into each portal on the list and download the invoices to the local Downloads folder. No renaming — the agent handles that
6. invoice-collector → Classify everything in Downloads: identify supplier, invoice date, and invoice number from each PDF, rename to the convention, upload to the same Drive folder, and update the checklist rows
7. Final reconciliation report — filed count, Drive folder, and the remaining exceptions split into private / still missing / ambiguous, each with the reason it was not filed

