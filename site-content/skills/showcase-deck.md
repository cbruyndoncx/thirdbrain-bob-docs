---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: showcase-deck — ThirdBrain BOB skill
  description: Build print-ready, on-brand 16:9 slide decks as a single self-contained HTML file (with browser navigation) plus a one-slide-per-page PDF, from a brand config (
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: showcase-deck
catLabel: documents
area: foundational
desc: Builds self-contained, branded 16:9 HTML slide decks + their PDFs from a brand config and a slide-content spec, and re-skins an existing deck to a new brand.
summary: 'Build print-ready, on-brand 16:9 slide decks as a single self-contained HTML file (with browser navigation) plus a one-slide-per-page PDF, from a brand config (tokens + fonts + logo) and a slide-content spec — so a showcase deck comes out consistent and re-brandable every time instead of being hand-built in HTML/CSS. The same engine re-skins an existing deck to a new brand: swap the color tokens, fonts, and embedded logo/mascot, and optionally white-label it for a partner.'
difficulty: advanced
inputType: conversation
outputType: document
requires: '[install]'
roles: '[CEO / Founder, Head of Marketing, Head of Sales, Content Manager]'
inputs:
- brand — Brand config JSON (colors, fonts, scale, logo, mascot, footer). See references/brand-config-schema.md.
- content — Slide-content JSON ({title, slides:[{class, foot, html}]}). Author html with the component classes in references/deck-structure.md.
- out — Output HTML path for the assembled deck (PDF rendered alongside via the render route).
- source (Re-brand an existing deck) — Source deck HTML to re-brand.
- from — Brand config the source deck currently uses (reskin maps by value, not variable name).
- to — Target brand config to re-skin into (optionally with a scrub block for white-labelling).
- out — Output HTML path for the re-branded deck.
- in — Input deck HTML file.
- out — Output PDF path.
outputs:
- beside the HTML (one slide per page, via render_deck_pdf.py)
- deck-html (html)
- deck-pdf (pdf)
- reskinned-html (html)
- the named output HTML (re-render the PDF via the render route)
- the named output HTML (self-contained; open in a browser or feed to the render route)
- the named output PDF (13.333in x 7.5in pages)
prompts:
- Build a showcase deck
- Make a branded slide deck
- Turn these slides into a deck PDF
---
