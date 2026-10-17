---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: scheduled-jobs — ThirdBrain BOB skill
  description: 'Target Audience: vault operators who want a single, version-controlled inventory of every recurring background job — and a safe way to push that inventory into '
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: scheduled-jobs
catLabel: utilities
area: foundational
desc: Manages recurring background jobs across Linux, WSL, and Mac with the canonical `{me.profile-root}/scheduled-jobs.yaml` manifest.
summary: 'Target Audience: vault operators who want a single, version-controlled inventory of every recurring background job — and a safe way to push that inventory into the system scheduler.'
difficulty: advanced
inputType: conversation
outputType: document
requires: '[install]'
roles: '[]'
inputs:
- jobs_yaml — Canonical scheduled-jobs manifest at {me.profile-root}/scheduled-jobs.yaml
outputs:
- backup (text)
- crontab-diff (diff)
- job-table (text)
- managed-crontab-block (cron)
- stdout
- updated-manifest (yaml)
- user crontab (between markers)
- '{company.schedule-runs}/crontab-backups/crontab_backup_<ts>.txt'
- '{me.profile-root}/scheduled-jobs.yaml'
prompts:
- List every managed scheduled job and show which ones are enabled.
- Preview the crontab diff from {me.profile-root}/scheduled-jobs.yaml without writing it.
- Add this recurring job to the manifest, validate it, and show me the sync diff.
- Sync the approved manifest block while preserving unmanaged crontab entries.
---
