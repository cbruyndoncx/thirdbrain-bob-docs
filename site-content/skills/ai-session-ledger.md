---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: ai-session-ledger — ThirdBrain BOB skill
  description: Build a continuous daily ledger of AI session activity, attributed to clients via file-write paths in ACP-compliant Agent Client Logfiles. Bridges the gap betwe
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: ai-session-ledger
catLabel: utilities
area: foundational
desc: Builds a daily AI session ledger from ACP-compliant Agent Client Logfiles and writes Dataview-ready notes for client costing.
summary: Build a continuous daily ledger of AI session activity, attributed to clients via file-write paths in ACP-compliant Agent Client Logfiles. Bridges the gap between AI activity metrics (sessions, tokens, skills) and business KPIs (deal value, client profitability) by creating queryable per-(client, date) entries.
difficulty: advanced
inputType: conversation
outputType: document
requires: '[install]'
roles: '[]'
inputs:
- date — Target date (YYYY-MM-DD | today | yesterday). Default yesterday.
- from-date — Start date (YYYY-MM-DD)
- to-date — End date (YYYY-MM-DD, defaults to today)
outputs:
- ledger-entries (markdown)
- '{company.finance.ai-ledger}/'
- '{company.finance.ai-ledger}/{YYYY-MM-DD}-{client-id}.md'
prompts:
- AI cost per client
- AI activity attribution
- AI-to-revenue KPIs
---
