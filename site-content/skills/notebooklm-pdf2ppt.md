---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: notebooklm-pdf2ppt — ThirdBrain BOB skill
  description: Single-file `uv run` script that converts PDF slides to PPTX using a PDF → SVG → EMF → PPTX pipeline. No rasterization — vector graphics are preserved at any zo
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: notebooklm-pdf2ppt
catLabel: documents
area: foundational
desc: Converts PDF slide exports to PowerPoint (.pptx) using a vector-preserving pipeline.
summary: Single-file `uv run` script that converts PDF slides to PPTX using a PDF → SVG → EMF → PPTX pipeline. No rasterization — vector graphics are preserved at any zoom level.
difficulty: advanced
inputType: conversation
outputType: document
requires: '[install]'
roles: '[]'
inputs:
- source-pdf — NotebookLM PDF slide export to convert; the full document is converted page-for-page.
- output-path — Destination PPTX path; when omitted the file is written next to the input PDF, or to the vault fallback location.
- source-pdf — NotebookLM PDF slide export to convert; only the requested page range is included in the output.
- pages — Page range or list to convert (e.g. `1-5,7`), passed to `--pages`.
- source-pdf — NotebookLM PDF slide export whose NotebookLM branding/watermark should be removed during conversion.
- request — Whether to report dependency status only, or to also print the install commands for whatever is missing. The route reads no PDF.
outputs:
- Converted PPTX containing only the requested page range, vector graphics preserved.
- Converted PPTX with every page from the source PDF, vector graphics preserved.
- Converted PPTX with the NotebookLM watermark removed via `--remove-watermark`, vector graphics preserved.
- JSON dependency status (`ok`, `pdf2svg`, `inkscape`) confirming whether the environment is ready for conversion.
- prefer a permanent directory)
prompts:
- Convert this NotebookLM PDF export to PowerPoint
- Transform my NotebookLM slides into a .pptx file
- Convert this PDF slide deck to PPTX with high quality
---
