---
layout: workflow-detail.njk
bodyClasses: workflow-detail
seo:
  title: Quarterly Invoice Collection — BOB Workflow
  description: Quarterly Invoice Collection
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: pb-quarterly-invoice-collection
youtubeId: ''
published: ''
privacy: unlisted
title: Quarterly Invoice Collection
thumbnail: ''
subtitle: Every expected supplier invoice for the quarter is either filed on Google Drive under the naming convention with its date recorded in the tracking sheet, or listed as an explicit exception with
  the reason
inputs:
- label: Quarter and explicit date boundaries (e.g. Q3 2026 → 2026/07/01 to 2026/10/01)
  icon: 📅
- label: Destination Drive folder name for the period
  icon: 👤
- label: Path to the subscriptions sheet
  icon: 📁
- label: Card statement screenshots or exports for the quarter
  icon: 📋
- label: Any supplier exclusions for this run
  icon: 📝
outputs: []
steps:
- label: 'xlsx-tools → Read the subscriptions sheet and the card statements; build the expected-invoice checklist for the quarter: one row per supplier charge with date, amount, and an empty invoice-received
    column'
  actor: agent
- label: Confirm the checklist — flag any charge that is private rather than business, and any supplier known to be portal-only before the search runs
  actor: human
- label: invoice-collector → Search Gmail for the quarter's date boundaries, download PDF attachments, rename to `yyyymmdd_supplier_invoiceid.pdf`, upload to the period's Drive folder
  actor: agent
- label: 'xlsx-tools → Reconcile collected PDFs against the checklist: fill the invoice date and filename per matched row, and report the unmatched rows as the portal list — the invoices that must be fetched
    by hand'
  actor: agent
- label: Log into each portal on the list and download the invoices to the local Downloads folder. No renaming — the agent handles that
  actor: human
- label: 'invoice-collector → Classify everything in Downloads: identify supplier, invoice date, and invoice number from each PDF, rename to the convention, upload to the same Drive folder, and update the
    checklist rows'
  actor: agent
- label: Final reconciliation report — filed count, Drive folder, and the remaining exceptions split into private / still missing / ambiguous, each with the reason it was not filed
  actor: agent
trigger: '"End of quarter, or ''collect the invoices for Q<n>'' — supplier invoices for the period must be gathered, named, and filed before the books close"'
timeSavings: 'Typical run: 45-90 minutes across two sittings (agent pass, then portal downloads)'
compounding: Each run refines templates and context — 5 automated steps improve with accumulated data
frequency: Per trigger event
hook: Quarter's closed. Half the supplier invoices are still in someone's inbox.
outcome: ''
benefits: []
cta: ''
category: ''
filterGroup: strategy
area: finance
---


