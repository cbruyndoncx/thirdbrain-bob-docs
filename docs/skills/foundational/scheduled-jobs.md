---
description: 'Target Audience: vault operators who want a single, version-controlled inventory of every recurring background job — and a safe way to push that inventory into the system scheduler.'
title: scheduled-jobs
---

# scheduled-jobs

Target Audience: vault operators who want a single, version-controlled inventory of every recurring background job — and a safe way to push that inventory into the system scheduler.

- **Area:** Foundational
- **Category:** utilities
- **Level:** advanced
- **Input:** conversation
- **Output:** document
- **Setup:** install
- **Roles:** 

Manages recurring background jobs across Linux, WSL, and Mac with the canonical `{me.profile-root}/scheduled-jobs.yaml` manifest.

## How you ask

- “List every managed scheduled job and show which ones are enabled.”
- “Preview the crontab diff from {me.profile-root}/scheduled-jobs.yaml without writing it.”
- “Add this recurring job to the manifest, validate it, and show me the sync diff.”
- “Sync the approved manifest block while preserving unmanaged crontab entries.”

## Inputs

- jobs_yaml — Canonical scheduled-jobs manifest at {me.profile-root}/scheduled-jobs.yaml

## Outputs

- backup (text)
- crontab-diff (diff)
- job-table (text)
- managed-crontab-block (cron)
- stdout
- updated-manifest (yaml)
- user crontab (between markers)
- {company.schedule-runs}/crontab-backups/crontab_backup_<ts>.txt
- {me.profile-root}/scheduled-jobs.yaml

