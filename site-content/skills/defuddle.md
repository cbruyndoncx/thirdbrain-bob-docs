---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: defuddle — ThirdBrain BOB skill
  description: Use this skill when the user wants readable page content from a standard public web page and token efficiency matters more than raw HTML fidelity.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: defuddle
catLabel: obsidian
area: foundational
desc: Extracts clean markdown content from web pages using Defuddle CLI.
summary: Use this skill when the user wants readable page content from a standard public web page and token efficiency matters more than raw HTML fidelity.
difficulty: advanced
inputType: conversation
outputType: document
requires: '[install]'
roles: '[]'
inputs:
- url — Page to extract and print as clean text
- url — Page to extract
- save_path — Vault destination; defaults to resource.web-extracts/{domain}/{page-title}.md, or output.scratch/web-{domain}-{YYYY-MM-DD}.md without vault context
- url — Page whose title, author, and date are wanted without the body
outputs:
- Extracted markdown returned in the response; no file is written.
- The requested metadata property returned inline; no file is created.
- saved-article (markdown)
- web (markdown)
prompts:
- Extract the clean content from this web page URL
- Read this article and save it as clean markdown
- Fetch this documentation page without the navigation clutter
---
