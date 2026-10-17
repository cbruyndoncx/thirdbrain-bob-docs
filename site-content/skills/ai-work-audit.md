---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: ai-work-audit — ThirdBrain BOB skill
  description: Use this skill to audit Claude Code work across a defined period. It supports two main routes
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: ai-work-audit
catLabel: business
area: strategy
desc: Audits AI-assisted work across Claude Code, Codex, Gemini CLI, and vault ACP session logs.
summary: Use this skill to audit Claude Code work across a defined period. It supports two main routes
difficulty: advanced
inputType: conversation
outputType: document
requires: '[install]'
roles: '[]'
inputs:
- week — Target week as concrete dates (e.g. "2026-03-31 to 2026-04-06") or relative ("this week", "last week")
- 'output-format — Output format (default: markdown) (markdown | json | summary)'
- keyword — Client name, project name, or search term to filter sessions
- from-date — Start date (YYYY-MM-DD)
- to-date — End date (YYYY-MM-DD, defaults to today)
- 'output-format — Output format (default: xlsx) (xlsx | json)'
- keyword — Keyword filter (case-insensitive). Use a vault path fragment such as the vault folder name (e.g. "my-vault") to match all in-vault Codex work.
- to-date — End date (YYYY-MM-DD)
- 'output-format — Output format (default: summary stdout) (markdown | json | summary)'
- agent-logs — ACP logfile folder to count; defaults to this vault's agent client logfiles
- client — Client ID to filter (e.g. "acme-industries")
- keyword — Keyword to filter (matches bucket, skill, files, body)
- from-date — Start date (YYYY-MM-DD), defaults to 7 days ago
- to-date — End date (YYYY-MM-DD), defaults to today
- 'scope — Filter: --last N, --today, --since YYYY-MM-DD, or --id PREFIX (default: --last 5)'
- show-cost — Include estimated USD cost per session
- verbose — Show per-turn user prompts and tool calls
- keyword — Keyword filter (case-insensitive). Use a vault path fragment such as the vault folder name (e.g. "my-vault") to match in-vault Gemini work.
- keyword — Optional keyword filter (Codex/Gemini). Default — all sessions in range.
- sessions-or-dir — One or more session .jsonl paths, or --dir {claude-project-dir} to scan all.
- top — Show only the N roughest skills.
- 'min-calls — Ignore skills with fewer than N tool calls (default: 5 — rates are noisy below this).'
outputs:
- agent-client-inventory (text)
- codex-session-report (json)
- combined-totals-report (markdown)
- gemini-session-report (json)
- ledger-audit-report (markdown)
- quick-scan-output (text)
- session-audit-report (xlsx)
- skill-friction-report (markdown)
- stdout
- stdout (optionally saved to {company.reports}/ai_quick_scan_{YYYY-MM-DD}.md)
- stdout (optionally saved via --output)
- weekly-audit-report (markdown)
- '{company.reports}/ai_work_audit_{YYYY-MM-DD}.md'
- '{company.reports}/session_audit_{YYYY-MM-DD}.xlsx'
prompts: []
---
