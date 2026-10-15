---
description: Collects `@BOB:` markers left inline across the vault and files each one as a TaskNote, so an instruction written into a file nobody reopens does not stay invisible.
title: bob-marker-sweep
---

# bob-marker-sweep

Collects `@BOB:` markers left inline across the vault and files each one as a TaskNote, so an instruction written into a file nobody reopens does not stay invisible.

| | |
|---|---|
| **Area** | Foundational |
| **Category** | obsidian |
| **Level** | beginner |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [none] |
| **Roles** | [] |

Finds `@BOB:` instruction markers left inline in vault notes and files each one as a TaskNote linked back to its source file.

## How you ask

- “sweep the BOB markers”
- “did I leave any @BOB notes anywhere?”
- “show me what the marker sweep would file, don't write anything yet”

## Inputs

- vault — Vault root; defaults to $CLAUDE_PROJECT_DIR or the current directory

## Outputs

- preview-report (text)
- stdout
- {marker-slug}.md
- {marker-slug}.md` — marker-tasks (markdown)

