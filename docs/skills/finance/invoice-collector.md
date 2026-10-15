---
description: Search Gmail for business invoices, download PDF attachments, rename following accounting conventions, and upload to a Google Drive folder.
title: invoice-collector
---

# invoice-collector

Search Gmail for business invoices, download PDF attachments, rename following accounting conventions, and upload to a Google Drive folder.

- **Area:** Finance
- **Category:** finance
- **Level:** advanced
- **Input:** data
- **Output:** spreadsheet
- **Setup:** api-key
- **Roles:** Finance Manager

Collects supplier invoices from Gmail or a local Downloads folder, renames the PDFs to accounting conventions, uploads them to Google Drive, and reconciles them against…

## How you ask

- “Collect all invoices from Gmail for January 2026”
- “Download and rename invoice PDFs from my inbox for accounting”
- “Gather business invoices from the last quarter and upload to Drive”
- “Here's my subscriptions sheet and the Visa statement — which Q3 invoices am I still missing?”
- “Everything is in my downloads, classify them and put them on the Drive”

## Inputs

- request — What to produce
- checklist — Expected-invoice checklist (spreadsheet or markdown table) listing the supplier charges that must have an invoice for the period
- source-folder — Folder holding the downloaded PDFs; defaults to the user's Downloads folder
- drive-folder — Destination Drive folder name or ID for the period
- checklist — Expected-invoice checklist to update with the newly filed invoices

## Outputs

- Draft `supplier-invoice` note created per collected invoice (Step 8).
- Filed/missing table plus exceptions, including the portal list when a checklist was supplied
- Google Drive/{folder-name}/yyyymmdd_supplier_invoiceid.pdf
- Per-file classification result, checklist rows closed, and unclassifiable files left in place
- invoice-pdfs (pdf)
- prefer a permanent directory)
- supplier-aliases (markdown)
- {scope.finance.accounting}/supplier_aliases.md
- {scope.finance.ap-invoices}/SI-{YYYY}-{NNN}.md

