---
description: Automation inventory audited, credentials and integrations verified, safe patches applied, and external side effects gated before close
title: Ops Automation Health Check
---

# Ops Automation Health Check

*Automation inventory audited, credentials and integrations verified, safe patches applied, and external side effects gated before close*

> Monthly ops review, before patching scheduled jobs/integrations, or when an automation silently fails

**Outcome:** Automation inventory audited, credentials and integrations verified, safe patches applied, and external side effects gated before close

| | |
|---|---|
| **Area** | Operations |
| **Time savings** | Typical run: 60-90 minutes, single session |
| **Try it** | Monthly ops review, before patching scheduled jobs/integrations, or when an automation silently fails |
| **Frequency** | 60-90 minutes, single session |

## Inputs

- 📋 Current scheduled jobs manifest: `10-ME/00-PROFILE/scheduled-jobs.yaml
- 📋 Scheduled-run TaskNotes under `00-CORE/TaskNotes/Tasks/`
- 📋 Recent scheduled-run logs under `99-TMP/OUTPUT/scheduled-runs/`
- 📋 Relevant skill configs and `.env` files for integrations being checked
- 📋 Known external systems: Google Workspace, YouTube, Gmail, Google Drive

## What BOB does

1. scheduled-jobs → list managed jobs and compare against the live scheduler without writing changes
2. tasknotes → inventory scheduled-run TaskNotes: identify enabled recurring tasks, `run_command`, `verify_path`, `max_turns`, model, lock settings, and last output
3. Credential and integration check: verify required tokens/configs exist and identify expired, revoked, missing, wrong-account, or over-scoped credentials
4. API health check: run non-mutating health probes for each integration and inspect recent logs for repeated failures, retries, or silent no-ops
5. Side-effect gate review: classify every automation as read-only, local-write, vault-write, or external-write; confirm outbound actions are disabled, dry-run capable, or explicitly approved before patching
6. Patch stale scripts/configs: apply the smallest safe changes, one automation family at a time, with backups where the tool supports them
7. Verification and audit close: rerun health checks, verify expected outputs, capture decisions, unresolved risks, and next scheduled review

## Outputs

- 📄 Ops health audit note with checked systems, findings, fixes, and resid
- 📄 Updated scheduled-jobs manifest or TaskNotes only where changes were n
- 📄 Patch summary with files changed and verification evidence
- 📄 Escalation list for credentials, provider outages, or owner decisions

