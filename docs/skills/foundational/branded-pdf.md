---
description: 'Render print-ready, vault-themed deliverables from Obsidian content through one of five render routes — preceded, for documentation authored one wiki note per chapter, by a config-driven assembly route that builds the print source — so branded marketing assets come out consistent every time instead of being hand-built in HTML/CSS. Every route loads brand tokens from the same company/client theme files and uses the engine that fits the job and the machine: WeasyPrint for multi-page text docs with running footers, Chrome for the same paginated document where WeasyPrint is unavailable or emoji are involved and for themed page images, Edge + Twemoji for emoji-safe visual one-pagers, and an Edge screenshot for table images.'
title: branded-pdf
---

# branded-pdf

Render print-ready, vault-themed deliverables from Obsidian content through one of five render routes — preceded, for documentation authored one wiki note per chapter, by a config-driven assembly route that builds the print source — so branded marketing assets come out consistent every time instead of being hand-built in HTML/CSS. Every route loads brand tokens from the same company/client theme files and uses the engine that fits the job and the machine: WeasyPrint for multi-page text docs with running footers, Chrome for the same paginated document where WeasyPrint is unavailable or emoji are involved and for themed page images, Edge + Twemoji for emoji-safe visual one-pagers, and an Edge screenshot for table images.

- **Area:** Foundational
- **Category:** documents
- **Level:** advanced
- **Input:** conversation
- **Output:** document
- **Setup:** install
- **Roles:** Head of Marketing, Content Manager

Assembles chaptered print sources from canonical wiki chapters, then renders vault-themed deliverables five ways: multi-page PDFs with optional mascot cover + running…

## How you ask

- “Render the branded PDF”
- “Build the lead-magnet PDF”
- “Make an emoji cheatsheet PDF”

## Inputs

- config — Path to the assembly manifest (YAML/JSON) declaring chapters_dir and the documents to build.
- set-version — Repeatable ID=VERSION pair bumping a document's doc_version, e.g. manual=2.2.
- check — Dry run: report which targets are stale and exit 1 if any are, without writing.
- source (Cover PDF (WeasyPrint)) — Path to the guided markdown doc carrying title/doc_id/doc_version/modified frontmatter.
- output — Output PDF path (default: {source}.pdf beside the source).
- source (Document PDF (Chrome, running footer)) — Path to the markdown source. Frontmatter is stripped; the first H1 becomes the cover title. Optional brand_theme/client_id frontmatter selects a theme.
- source (HTML pages → branded PNGs / PDF (Chrome)) — Path to themed HTML containing one or more `.page` elements (theme placeholders filled from the brand theme).
- output — Output PNG path; the stem is reused as {stem}-1.png, {stem}-2.png … when there is more than one page.
- source (Emoji-safe visual PDF (Edge + Twemoji)) — Path to the HTML doc (brand CSS applied; emoji as plain text). Start from assets/emoji-pdf-template.html.
- output — Output PDF path (default: {source-stem}.pdf).
- source (Table → branded PNG (Edge screenshot)) — Path to a .md file (first table used) or a styled .html table.
- output — Output PNG path.

## Outputs

- beside the source (e.g. a marketing-content PDF under {company.marketing}/...)
- beside the source (or the named output)
- beside the source HTML (or the named output)
- branded-pdf (pdf)
- doc-pdf (pdf)
- each `documents[].target` declared in the manifest
- emoji-pdf (pdf)
- page-images (png)
- page-pdf (pdf)
- print-source (markdown)
- table-image (png)
- the named output PNG (e.g. under {company.marketing}/...)
- the named output PNG, or {out-stem}-N.png per page
- {out-stem}.pdf when --pdf is passed

