---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: notebooklm — ThirdBrain BOB skill
  description: Operate Google NotebookLM entirely via the `nlm` CLI (Python package `notebooklm-mcp-cli`). No MCP server needed — all operations run as shell commands.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: notebooklm
catLabel: research
area: research
desc: Operate Google NotebookLM via the `nlm` CLI (v0.5+).
summary: Operate Google NotebookLM entirely via the `nlm` CLI (Python package `notebooklm-mcp-cli`). No MCP server needed — all operations run as shell commands.
difficulty: advanced
inputType: conversation
outputType: document
requires: '[api-key]'
roles: '[]'
inputs:
- request — What to do — create notebook, add sources, query, etc.
- notebook_id — Notebook ID or alias
- artifact_type — audio, video, slides, report, quiz, flashcards, mindmap, infographic, data-table (audio | video | slides | report | quiz | flashcards | mindmap | infographic | data-table)
- options — Type-specific options (format, style, focus prompt, etc.)
- artifact_type — audio, video, slide-deck, report, quiz, flashcards, mind-map, infographic, data-table (audio | video | slides | report | quiz | flashcards | mindmap | infographic | data-table)
- output_path — Local file path for download
- query — Research query
- notebook_id — Target notebook
- mode — fast (~30s) or deep (~5min) (fast | deep)
- notebook — Notebook alias or ID
- notebook_slug — Kebab-case folder name (derived from notebook title if omitted)
- dashboard_title — Dashboard title (derived from notebook title if omitted)
- question — Question to ask
- title — Short title for the Q&A note
- concept — What the deck is about — topic, narrative, catalog, pitch, etc.
- 'slide_count — Number of slides (default: 10, range 5-20)'
- visual_style — Art direction — e.g. 'IKEA catalog', 'Kurzgesagt flat vector', 'editorial magazine'. Auto-suggested if omitted.
- concept — What the deck is about
- 'slide_count — Number of slides (default: 10)'
- visual_style — Art direction
outputs:
- Command output or structured answer
- Discovered and imported sources
- Generated NotebookLM studio artifact
- NotebookLM studio artifact
- User-specified or default filename
- dashboard (markdown)
- file (varies)
- prefer a permanent directory)
- qa-note (markdown)
- script (markdown)
- slides (slide_deck)
- source-notes (markdown)
- user-specified output path for artifact
- user-specified output path for result
- user-specified output path for sources
- '{resource.research}/notebooklm/{notebook-slug}/QA/{date} {title}.md'
- '{resource.research}/notebooklm/{notebook-slug}/Sources/*.md'
- '{resource.research}/notebooklm/{notebook-slug}/{dashboard-title}.md'
prompts:
- Notebooklm
- Notebook lm
- Podcast generation
---
