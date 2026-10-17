---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: playbook-runner — ThirdBrain BOB skill
  description: 'Create new Playbooks or execute existing ones. Three modes: build interviews the user about a process and generates an SOP, a Playbook, or both; create builds a'
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: playbook-runner
catLabel: utilities
area: foundational
desc: Create and execute vault Playbooks.
summary: 'Create new Playbooks or execute existing ones. Three modes: build interviews the user about a process and generates an SOP, a Playbook, or both; create builds a new playbook recipe file with sequence diagram; run loads a playbook, creates a tracking TaskNote, and executes steps in sequence.'
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[Operations Manager]'
inputs:
- source (Build Playbook) — Process name or description to document
- source (Create Playbook) — Playbook specification or process steps
- source (Run Playbook) — Playbook name or path to execute
outputs:
- playbook (markdown)
- playbook-deliverables (markdown)
- tracking-tasknote (markdown)
- '{client.deliverables}/{playbook-name}.md'
- '{company.processes.playbooks}/{playbook-name}.md'
- '{output.tasks}/{playbook-name}-{YYYY-MM-DD}.md'
prompts:
- I have a client onboarding process I want to document — help me build a playbook from it
- Create a playbook that chains prospect-audit, then sales-pipeline-report, then proposal generation
- Run the quarterly-review playbook for client Bobbolt
- Resume the marketing-launch playbook — I think it was waiting on my approval at step 4
---
