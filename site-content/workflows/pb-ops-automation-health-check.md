---
layout: workflow-detail.njk
bodyClasses: workflow-detail
seo:
  title: Ops Automation Health Check — BOB Workflow
  description: Ops Automation Health Check
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: pb-ops-automation-health-check
youtubeId: ''
published: ''
privacy: unlisted
title: Ops Automation Health Check
thumbnail: ''
subtitle: Automation inventory audited, credentials and integrations verified, safe patches applied, and external side effects gated before close
inputs:
- label: 'Current scheduled jobs manifest: `10-ME/00-PROFILE/scheduled-jobs.yaml'
  icon: 📋
- label: Scheduled-run TaskNotes under `00-CORE/TaskNotes/Tasks/`
  icon: 📋
- label: Recent scheduled-run logs under `99-TMP/OUTPUT/scheduled-runs/`
  icon: 📋
- label: Relevant skill configs and `.env` files for integrations being checked
  icon: 📋
- label: 'Known external systems: Google Workspace, YouTube, Gmail, Google Drive'
  icon: 📋
outputs:
- label: Ops health audit note with checked systems, findings, fixes, and resid
  icon: 📄
- label: Updated scheduled-jobs manifest or TaskNotes only where changes were n
  icon: 📄
- label: Patch summary with files changed and verification evidence
  icon: 📄
- label: Escalation list for credentials, provider outages, or owner decisions
  icon: 📄
steps:
- label: scheduled-jobs → list managed jobs and compare against the live scheduler without writing changes
  actor: agent
- label: 'tasknotes → inventory scheduled-run TaskNotes: identify enabled recurring tasks, `run_command`, `verify_path`, `max_turns`, model, lock settings, and last output'
  actor: agent
- label: 'Credential and integration check: verify required tokens/configs exist and identify expired, revoked, missing, wrong-account, or over-scoped credentials'
  actor: agent
- label: 'API health check: run non-mutating health probes for each integration and inspect recent logs for repeated failures, retries, or silent no-ops'
  actor: agent
- label: 'Side-effect gate review: classify every automation as read-only, local-write, vault-write, or external-write; confirm outbound actions are disabled, dry-run capable, or explicitly approved before
    patching'
  actor: human
- label: 'Patch stale scripts/configs: apply the smallest safe changes, one automation family at a time, with backups where the tool supports them'
  actor: agent
- label: 'Verification and audit close: rerun health checks, verify expected outputs, capture decisions, unresolved risks, and next scheduled review'
  actor: agent
trigger: Monthly ops review, before patching scheduled jobs/integrations, or when an automation silently fails
timeSavings: 'Typical run: 60-90 minutes, single session'
compounding: ''
frequency: 60-90 minutes, single session
hook: Monthly ops review, before patching scheduled jobs/integrations, or when an automation silently fails
outcome: Automation inventory audited, credentials and integrations verified, safe patches applied, and external side effects gated before close
benefits: []
cta: ''
category: ''
filterGroup: strategy
area: operations
---


