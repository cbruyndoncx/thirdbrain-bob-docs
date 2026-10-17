---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: corporate-pdf — ThirdBrain BOB skill
  description: USE WHEN user says 'corporate pdf', 'prepare pdf', 'branded pdf', 'pdf with logo', 'export proposal', 'professional pdf', 'client deliverable', or wants to crea
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: corporate-pdf
catLabel: obsidian
area: foundational
desc: Prepare Obsidian markdown files for professional PDF export with company and client logos in headers/footers using Better Export PDF plugin.
summary: USE WHEN user says 'corporate pdf', 'prepare pdf', 'branded pdf', 'pdf with logo', 'export proposal', 'professional pdf', 'client deliverable', or wants to create professional PDFs with company/client branding.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[]'
inputs:
- source_note — Markdown note to render
- brand_theme — Brand theme to apply; defaults to the company theme
- source_note — Deliverable note to render
- client_id — Client whose brand theme and folder apply
- source_notes — Notes to render in one pass
- brand_theme — Brand theme applied to every document in the batch
outputs:
- batch-export-ready-md (markdown)
- client-export-ready-md (markdown)
- export-ready-md (markdown)
- '{client.deliverables}/{document}.pdf.md'
prompts:
- Prepare this document for branded PDF export with our logo
- Set up corporate PDF headers and footers with company branding
- Export this Obsidian note as a professional PDF with logos
---
