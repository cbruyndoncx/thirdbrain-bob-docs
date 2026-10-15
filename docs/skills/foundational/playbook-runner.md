---
description: 'Create new Playbooks or execute existing ones. Three modes: build interviews the user about a process and generates an SOP, a Playbook, or both; create builds a new playbook recipe file with sequence diagram; run loads a playbook, creates a tracking TaskNote, and executes steps in sequence.'
title: playbook-runner
---

# playbook-runner

Create new Playbooks or execute existing ones. Three modes: build interviews the user about a process and generates an SOP, a Playbook, or both; create builds a new playbook recipe file with sequence diagram; run loads a playbook, creates a tracking TaskNote, and executes steps in sequence.

- **Area:** Foundational
- **Category:** utilities
- **Level:** beginner
- **Input:** conversation
- **Output:** document
- **Setup:** none
- **Roles:** Operations Manager

Create and execute vault Playbooks.

## How you ask

- “I have a client onboarding process I want to document — help me build a playbook from it”
- “Create a playbook that chains prospect-audit, then sales-pipeline-report, then proposal generation”
- “Run the quarterly-review playbook for client Bobbolt”
- “Resume the marketing-launch playbook — I think it was waiting on my approval at step 4”

## Inputs

- source (Build Playbook) — Process name or description to document
- source (Create Playbook) — Playbook specification or process steps
- source (Run Playbook) — Playbook name or path to execute

## Outputs

- playbook (markdown)
- playbook-deliverables (markdown)
- tracking-tasknote (markdown)
- {client.deliverables}/{playbook-name}.md
- {company.processes.playbooks}/{playbook-name}.md
- {output.tasks}/{playbook-name}-{YYYY-MM-DD}.md

