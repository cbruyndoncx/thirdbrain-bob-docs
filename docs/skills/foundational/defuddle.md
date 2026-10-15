---
description: Use this skill when the user wants readable page content from a standard public web page and token efficiency matters more than raw HTML fidelity.
title: defuddle
---

# defuddle

Use this skill when the user wants readable page content from a standard public web page and token efficiency matters more than raw HTML fidelity.

- **Area:** Foundational
- **Category:** obsidian
- **Level:** advanced
- **Input:** conversation
- **Output:** document
- **Setup:** install
- **Roles:** 

Extracts clean markdown content from web pages using Defuddle CLI.

## How you ask

- “Extract the clean content from this web page URL”
- “Read this article and save it as clean markdown”
- “Fetch this documentation page without the navigation clutter”

## Inputs

- url — Page to extract and print as clean text
- url — Page to extract
- save_path — Vault destination; defaults to resource.web-extracts/{domain}/{page-title}.md, or output.scratch/web-{domain}-{YYYY-MM-DD}.md without vault context
- url — Page whose title, author, and date are wanted without the body

## Outputs

- Extracted markdown returned in the response; no file is written.
- The requested metadata property returned inline; no file is created.
- saved-article (markdown)
- web (markdown)

