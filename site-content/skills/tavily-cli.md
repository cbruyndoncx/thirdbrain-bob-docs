---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: tavily-cli — ThirdBrain BOB skill
  description: Web search, content extraction, site crawling, URL discovery, and deep research through the `tvly` command-line tool. Returns JSON optimized for LLM consumption
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: tavily-cli
catLabel: utilities
area: foundational
desc: Search the web, extract page content, crawl sites, discover URLs, and run deep research via the Tavily CLI (`tvly`).
summary: Web search, content extraction, site crawling, URL discovery, and deep research through the `tvly` command-line tool. Returns JSON optimized for LLM consumption.
difficulty: expert
inputType: conversation
outputType: document
requires: '[install, api-key]'
roles: '[]'
inputs:
- query — Search query (keep under 400 characters)
- urls — One or more URLs to extract
- url — Root URL to map
- url — Root URL to crawl
- query — Research topic or question
outputs:
- --output-dir <dir> (or -o <file>)
- content (markdown-or-json)
- docs.md
- extracted-document (markdown)
- pages (markdown-files-or-json)
- report (markdown-or-json)
- results (json)
- stdout (or -o <file>)
- urls (json)
prompts:
- Search the web for the latest official documentation on this API.
- Extract clean markdown from these three known URLs.
- Map this documentation site before choosing which section to crawl.
- Run a cited deep-research report on this question.
---
