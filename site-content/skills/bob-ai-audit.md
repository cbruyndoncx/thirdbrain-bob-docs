---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: bob-ai-audit — ThirdBrain BOB skill
  description: 'Productizes the BOB-native "living Operational Audit" system: instead of shipping a one-off PDF of findings, hidden costs, and recommended AI initiatives (the A'
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: bob-ai-audit
catLabel: business
area: strategy
desc: Turns a business operational audit into live, trackable Obsidian entities instead of a frozen PDF — imports a mapped business-baseline process, maps a process to a…
summary: 'Productizes the BOB-native "living Operational Audit" system: instead of shipping a one-off PDF of findings, hidden costs, and recommended AI initiatives (the APG-style audit model), this skill authors those as real Obsidian entities — `audit-finding`, `audit-waste`, `ai-initiative`, `audit-process`, `client-audit-summary` — that render live in Obsidian Bases, update in place as work progresses, and generate a proper BPMN process diagram. Entities are the source of truth; nothing in this skill treats JSON as storage.'
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[CEO / Founder, Operations Manager]'
inputs:
- design-system — Brand design tokens used by the live dashboard output.
- 'source_process — Path to the source `type: process` note produced by business-baseline (e.g. in the company processes folder, `{company.processes}`)'
- out_dir — Audit folder for the converted note — in the process audits folder (`{company.process-audits}`) for a company audit, or the client's folder (`{client.root}`) for a client copy. Never _demo-carebridge.
- audit — Audit engagement id this process belongs to (added to tags)
- process_definition — The process to map — its steps, tools/lanes, and flow between steps, gathered from the audit conversation or discovery notes
- audit_dir — Company-scope audit folder, e.g. under the process audits folder (`{company.process-audits}`), or a client-delivery copy under the client's folder (`{client.root}`)
- card_data — The pain point, hidden cost, or blueprint initiative to record, including its id, severity/category, and any supporting quote/citation
- audit_dir — Same audit folder as map-process
- vault_path — Absolute path to the vault root
- audit_dir — Company-scope audit folder to scan
- client_id — Client identifier — must match a client folder (`client.root`)
- audit_dir — Audit folder containing the initiative note
- initiative_id — id of an ai-initiative note with no client_id set
- kpi_context — The KPI id this initiative should move (must match a KPI note field), a target value (a business judgment call from the audit conversation), and optionally a baseline value and review date
- audit_dir — Audit folder to scan for ai-initiative notes
- audit_dir — Audit folder to scan
- title — Report title, e.g. '<Client Name> — Operational Audit'
- 'brand_theme — Path to a brand-theme note (e.g. {company.assets-brand-guidelines}/example-brand-theme.md). Default: the single *brand-theme.md in the context pack''s company.assets-brand-guidelines folder; none found or several → pdf-report''s generic defaults with a NOTE (non-fatal). --no-brand-theme skips discovery'
- audit_dir — Audit folder to scan for entity notes
- 'vault_name — Obsidian vault name for the obsidian:// links (default: the resolved vault root''s folder name, e.g. my-vault — override only when Obsidian registers the vault under a different name)'
- 'out_dir — Output folder (default: the audit folder). Required for read-only inputs like the _demo fixture — write to the scratch output folder (`output.scratch`) instead.'
- client_share — Also emit a second variant with all obsidian:// links stripped (plain text, no dead links) for sending outside the vault
- vault — Vault root or any path inside it (autodetected by anchoring on .obsidian or the vault.core folder; default .)
- port — 127.0.0.1 port (default 8123 — do NOT use the TaskNotes plugin API port; resolve `apiPort` from the TaskNotes plugin settings as described in `tasknotes` → Resolve the port)
- 'vault_name — Obsidian vault name for the cards'' obsidian:// deep links (default: the resolved vault root''s folder name, e.g. my-vault)'
- emit_embed_note — Audit id — write {audit-id}-live-dashboard.md (iframe + start instructions) next to the audit and exit, without starting the server
outputs:
- The previous audit-process note, moved aside before the fresh one is written; a same-day re-run appends a counter (`_2`, `_3`). Not written with --no-archive or when no note existed.
- audit-dashboard-note (markdown)
- audit-report-pdf (pdf)
- bpmn-diagram (bpmn)
- card-note (markdown)
- embed-note (markdown)
- http://127.0.0.1:{port}/{audit-id} (shell), /api/audits + /api/audit/{audit-id} (JSON, re-scanned per request)
- initiative-note (markdown)
- live-dashboard (http)
- matrix-svg (svg)
- portal-html (html)
- portal-html-client (html)
- process-note (markdown)
- summary-note (markdown)
- workspace-config (json)
- '{audit_dir}/audit-dashboard.md'
- '{audit_dir}/effort-impact-matrix.svg'
- '{audit_dir}/{audit-id}-audit-report.pdf (or caller-chosen path)'
- '{audit_dir}/{card-id}.md'
- '{audit_dir}/{initiative_id}.md (kpi_experiment field updated)'
- '{audit_dir}/{process-id}.bpmn'
- '{audit_dir}/{process-id}.md'
- '{client.root}/{client_id}-audit-summary.md'
- '{company.process-audits}/{audit-id}/{audit-id}-live-dashboard.md (type: reference; only with --emit-embed-note)'
- '{initiative title} ({initiative_id}).md'
- '{initiative title} ({initiative_id}).md` — kpi-experiment-tasknote (markdown)'
- '{out_dir}/_archive/{process-id}_{YYYY-MM-DD}.md'
- '{out_dir}/{audit-id}-portal-client.html (only with --client-share; links stripped)'
- '{out_dir}/{audit-id}-portal.html (owner variant, obsidian:// links)'
- '{out_dir}/{process-id}.bpmn (only with --generate-bpmn)'
- '{out_dir}/{process-id}.md (type: audit-process, status: draft)'
- '{vault}/.obsidian/plugins/bob-workspace/workspace.json'
prompts:
- Import this process into the audit
- Convert this business-baseline process
- Map this process for the audit
---
