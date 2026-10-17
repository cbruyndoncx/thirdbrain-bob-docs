---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: bob-marker-sweep — ThirdBrain BOB skill
  description: Collects `@BOB:` markers left inline across the vault and files each one as a TaskNote, so an instruction written into a file nobody reopens does not stay invis
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: bob-marker-sweep
catLabel: obsidian
area: foundational
desc: Finds `@BOB:` instruction markers left inline in vault notes and files each one as a TaskNote linked back to its source file.
summary: Collects `@BOB:` markers left inline across the vault and files each one as a TaskNote, so an instruction written into a file nobody reopens does not stay invisible.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[]'
inputs:
- vault — Vault root; defaults to $CLAUDE_PROJECT_DIR or the current directory
outputs:
- preview-report (text)
- stdout
- '{marker-slug}.md'
- '{marker-slug}.md` — marker-tasks (markdown)'
prompts:
- sweep the BOB markers
- did I leave any @BOB notes anywhere?
- show me what the marker sweep would file, don't write anything yet
---
