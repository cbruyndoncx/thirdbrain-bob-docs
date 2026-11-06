---
title: Playbooks — Reusable Job Recipes for the Vault
type: knowledge-base
status: final
created: 2026-03-14
modified: 2026-03-15
tags:
  - playbooks
  - vault-architecture
  - tasknotes
  - automation
---

# Playbooks

> **Background**: Playbooks are inspired by [[what_is_jtbd|Jobs To Be Done]] thinking — defining the complete job a chain of skills is hired to accomplish. Read that note first if you're unfamiliar with the concept.

## The Problem Playbooks Solve

This vault has a skill for each narrow job. Each knows how to do one thing well — write copy, run an SEO audit, generate a report. But real work is never one skill. Publishing a YouTube video involves content strategy, copywriting, editing, image generation, social posting, and quality scoring — in a specific order, with human decisions at key moments.

Without playbooks, the human is the orchestrator: remembering which skills to call, in what order, loading context files manually, and tracking progress mentally. That's the job the vault should be doing.

---

## Two Distinct Things

### 1. Playbook (the recipe)

A static, reusable recipe that describes a complete job. It lives in the **playbook library** and defines:

- What triggers the job
- What the desired outcome looks like
- Which skills to invoke and in what order
- Which context files the agent needs
- Where the human must weigh in
- What quality standard the output must meet

A playbook doesn't change per execution, only per revision.

### 2. Running Instance (TaskNote)

When someone says *"start playbook: X"*, the vault creates a TaskNote linked to the playbook. This is the **live execution** — it tracks which step you're on, what the agent is waiting for, and how close you are to done.

---

## How a Playbook Looks

Playbooks use standard Obsidian markdown with frontmatter:

```yaml
---
type: playbook
title: "Publish YouTube content piece"
trigger: "When I have a video topic ready to produce"
outcome: "All assets ready — script, thumbnails, description, LinkedIn post"
total-steps: 8
estimated-duration: "2-3 hours active, 1-2 sessions"
status: active
tags: [content-ops, youtube]
---
```

The body contains four sections:

### Required Context

Every file the agent needs, pre-linked. No searching, no guessing:

```markdown
## Required Context
- [[brand_voice_guide]]
- [[icp_profile]]
- [[product-marketing-context]]
- [[youtube_description_template]]
```

### Steps

Each step uses **dual numbering** — `step (remaining)`. The first number is execution order, the parenthetical is how many steps remain. Each step names the skill and marks whether it's a human or agent step:

```markdown
## Steps
1 (8). content-strategy → select angle (HUMAN)
2 (7). copywriting → PSP script draft (AGENT)
3 (6). copy-editing → 7-sweeps (AGENT)
4 (5). Review script (HUMAN)
5 (4). ai-image-gen → thumbnails (AGENT)
6 (3). Select thumbnail (HUMAN)
7 (2). social-content → LinkedIn post (AGENT)
8 (1). content-scorer → must score 75+ (AGENT)
```

**Why dual numbering?** Step order reads naturally (1 is first). The parenthetical maps to `remaining-steps` in the running TaskNote — it counts down from `total-steps` to 1. Tasks closest to completion surface first in kanban views.

### Inputs Per Run

What changes each time the playbook is executed:

```markdown
## Inputs per run
- Topic/idea or source URL
- Target publish date
- Reference thumbnails (if any)
```

### Quality Gate

The definition of "done" — not just "steps completed" but "output meets standard":

```markdown
## Quality gate
- content-scorer must return 75+
- All HUMAN steps must be completed (no skip)
```

---

## Where Playbooks Live

The playbook library is hierarchical — generic templates that can be customized per scope:

| Location | Purpose | Example |
|----------|---------|---------|
| `{company.playbooks}` | Generic library playbooks | "Publish content piece" |
| `{company.processes}/Playbooks/` | Company-specific jobs | "Client onboarding" |
| `{me.playbooks}` | Personal recurring jobs | "Weekly review" |
| `{client.root}/Playbooks/` | Client-scoped overrides | "Acme approval process" |

A client-scoped playbook can override a library playbook — different context files, adjusted steps, client-specific quality gates. The `playbook` field in the running TaskNote points to whichever version applies.

---

## How a Running Instance Works

When a playbook is started, the vault creates a TaskNote with extra fields:

```yaml
---
type: task
title: "Publish: Claude Code Content OS video"
status: awaiting-input
playbook: "[[Publish YouTube content piece]]"
remaining-steps: 5
awaiting: "Review script — pick from 3 drafts below"
priority: high
assignee: [Agent]
---
```

### New Frontmatter Fields

| Field | Type | Purpose |
|-------|------|---------|
| `playbook` | wikilink | Links back to the playbook being executed |
| `remaining-steps` | number | Counts down from `total-steps` to 0 |
| `awaiting` | text | What the agent needs from the human right now |

### Status Lifecycle

The standard TaskNote lifecycle gets one new status:

```
open → in-progress ↔ awaiting-input → done
```

- **`awaiting-input`** — The agent has hit a HUMAN step and needs a decision. The `awaiting` field describes exactly what's needed.
- When the human responds, the agent resumes, sets status back to `in-progress`, and decrements `remaining-steps`.
- At `remaining-steps: 0` + quality gate passed → `done`.

---

## The Execution Flow

```
1. Human: "start playbook: Publish YouTube content piece"
              │
2. Agent reads playbook
   Loads all Required Context files
   Creates TaskNote with remaining-steps: 8
              │
3. Step 1 (HUMAN): content-strategy → select angle
   → Agent presents options
   → Sets status: awaiting-input
   → Sets awaiting: "Pick content angle from options below"
              │
4. Human responds with choice
              │
5. Step 2 (AGENT): copywriting → PSP script draft
   → Agent runs skill autonomously
   → remaining-steps: 6
              │
         ... continues ...
              │
6. Step 8 (AGENT): content-scorer → quality check
   → Score ≥ 75 → status: done
   → Score < 75 → loops back for revision
```

---

## Viewing Playbooks in Flight

A dedicated Bases view (`playbooks-in-flight.base`) shows all active playbook-linked tasks:

- Filtered to tasks where `playbook` is not empty and `status` is not `done`
- Sorted by `remaining-steps` ascending — closest to completion first
- Columns: title, status, remaining-steps, awaiting, playbook, assignee

This gives a dashboard of everything in motion: what's running, what's blocked on you, and what's almost done.

---

## Relationship to Existing Vault Concepts

| Concept | Role | Analogy |
|---------|------|---------|
| **Skill** | Knows *how* to do one thing | A tool in the toolbox |
| **Playbook** | Defines *what needs to happen* end-to-end | The assembly instructions |
| **TaskNote** | Tracks *where you are* in the job | The progress checklist |
| **Context files** | Provide the *information* the agent needs | The materials list |

Skills are verbs. Playbooks are sentences. The vault connects them.

### Where Do Outputs Go?

Each skill saves outputs to its own standard location — the playbook doesn't override this. There is no separate "playbook output folder." The TaskNote itself serves as the run log, tracking which steps completed and what was decided at human checkpoints.

---

## What This Changes for Users

**Before playbooks**: You trigger skills one at a time, remember the sequence, load context manually, and track progress in your head.

**After playbooks**: You say "start playbook: X." The agent knows what to do, loads what it needs, runs what it can, and asks you only when it needs a human decision. You see the progress in a kanban column. When the quality gate passes, it's done.

The human role shifts from **orchestrator** to **decision-maker** — you weigh in on the judgment calls, not the logistics.
