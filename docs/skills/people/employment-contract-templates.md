---
description: Create legally aware draft employment documentation while keeping licensed legal review explicit. Use this skill to structure the document package, surface jurisdiction-sensitive clauses, and prepare a clean handoff for counsel or HR review.
title: employment-contract-templates
---

# employment-contract-templates

Create legally aware draft employment documentation while keeping licensed legal review explicit. Use this skill to structure the document package, surface jurisdiction-sensitive clauses, and prepare a clean handoff for counsel or HR review.

- **Area:** People
- **Category:** human resources
- **Level:** beginner
- **Input:** conversation
- **Output:** document
- **Setup:** none
- **Roles:** HR Manager

Creates employment contracts, offer letters, and HR policy drafts as Markdown and .docx files.

## How you ask

- “Draft an employment contract for a senior developer role”
- “Create an offer letter template for our Dubai office”
- “Build an HR policy document for remote work arrangements”
- “Prepare an employment agreement for contractor conversion”

## Inputs

- region-context — Statutory benefits, notice periods, gratuity, and work-permit constraints used to seed jurisdiction-specific clauses in the baseline draft.
- request — The document package to draft — type, role, and any compensation or classification detail already known.
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set
- profile — Company or client profile — jurisdiction, legal form, and registration details used to seed the baseline structure since no existing template exists.
- existing-template — The contract or offer-letter template to read first, before any change because of jurisdiction, role, or classification is proposed.
- region-context — Statutory rules for the new jurisdiction, used to identify what in the existing template is now stale or non-compliant.
- request — What is changing — the new role, location, or worker classification the template must be adapted for.
- profile — Company or client profile used to confirm which existing template terms stay stable versus which must change.

## Outputs

- Adapted employment document, formatted and ready for HR or candidate-facing distribution.
- Formatted employment document draft ready for HR or candidate-facing distribution.
- Markdown working draft showing what changed from the source template, with review notes for anything that should not change without counsel.
- Markdown working draft with visible placeholders and counsel-review notes.
- {scope.operations}/legal/employment-contract-templates-{YYYY-MM-DD}.docx
- {scope.operations}/legal/employment-contract-templates-{YYYY-MM-DD}.md

