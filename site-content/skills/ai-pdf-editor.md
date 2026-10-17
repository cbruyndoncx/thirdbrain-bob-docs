---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: ai-pdf-editor — ThirdBrain BOB skill
  description: Edit PDF pages as images, then rebuild the PDF with optional OCR text preservation.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: ai-pdf-editor
catLabel: documents
area: foundational
desc: Edits scanned PDF pages and image-based PDF content by replacing text, correcting OCR-visible mistakes, updating logos or branding, and redacting visual elements.
summary: Edit PDF pages as images, then rebuild the PDF with optional OCR text preservation.
difficulty: expert
inputType: conversation
outputType: document
requires: '[api-key, install]'
roles: '[]'
inputs:
- pdf_path — Scanned or image-based PDF to inspect before editing
- pdf_path — PDF to edit
- changes — Edits to apply — text replacement, logo swap, or redaction, one per entry
- pdf_path — PDF with an existing text layer
- changes — Edits to apply without re-running OCR
outputs:
- edited-pdf (pdf)
- edited-pdf-no-ocr (pdf)
- pdf-preview (png)
- prefer a permanent directory)
prompts:
- Fix the text on page 3 of this scanned PDF
- Replace the old logo with our new one in this PDF document
- Correct the OCR mistakes in this PDF invoice
- Redact sensitive information from this PDF report
---
