---
description: USE WHEN user says 'corporate pdf', 'prepare pdf', 'branded pdf', 'pdf with logo', 'export proposal', 'professional pdf', 'client deliverable', or wants to create professional PDFs with company/client branding.
title: corporate-pdf
---

# corporate-pdf

USE WHEN user says 'corporate pdf', 'prepare pdf', 'branded pdf', 'pdf with logo', 'export proposal', 'professional pdf', 'client deliverable', or wants to create professional PDFs with company/client branding.

| | |
|---|---|
| **Area** | Foundational |
| **Category** | obsidian |
| **Level** | beginner |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [none] |
| **Roles** | [] |

Prepare Obsidian markdown files for professional PDF export with company and client logos in headers/footers using Better Export PDF plugin.

## How you ask

- “Prepare this document for branded PDF export with our logo”
- “Set up corporate PDF headers and footers with company branding”
- “Export this Obsidian note as a professional PDF with logos”

## Inputs

- source_note — Markdown note to render
- brand_theme — Brand theme to apply; defaults to the company theme
- source_note — Deliverable note to render
- client_id — Client whose brand theme and folder apply
- source_notes — Notes to render in one pass
- brand_theme — Brand theme applied to every document in the batch

## Outputs

- batch-export-ready-md (markdown)
- client-export-ready-md (markdown)
- export-ready-md (markdown)
- {client.deliverables}/{document}.pdf.md

