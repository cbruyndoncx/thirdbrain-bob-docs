---
description: Edit PDF pages as images, then rebuild the PDF with optional OCR text preservation.
title: ai-pdf-editor
---

# ai-pdf-editor

Edit PDF pages as images, then rebuild the PDF with optional OCR text preservation.

| | |
|---|---|
| **Area** | Foundational |
| **Category** | documents |
| **Level** | expert |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [api-key, install] |
| **Roles** | [] |

Edits scanned PDF pages and image-based PDF content by replacing text, correcting OCR-visible mistakes, updating logos or branding, and redacting visual elements.

## How you ask

- “Fix the text on page 3 of this scanned PDF”
- “Replace the old logo with our new one in this PDF document”
- “Correct the OCR mistakes in this PDF invoice”
- “Redact sensitive information from this PDF report”

## Inputs

- pdf_path — Scanned or image-based PDF to inspect before editing
- pdf_path — PDF to edit
- changes — Edits to apply — text replacement, logo swap, or redaction, one per entry
- pdf_path — PDF with an existing text layer
- changes — Edits to apply without re-running OCR

## Outputs

- edited-pdf (pdf)
- edited-pdf-no-ocr (pdf)
- pdf-preview (png)
- prefer a permanent directory)

