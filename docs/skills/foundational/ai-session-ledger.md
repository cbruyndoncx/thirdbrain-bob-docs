---
description: Build a continuous daily ledger of AI session activity, attributed to clients via file-write paths in ACP-compliant Agent Client Logfiles. Bridges the gap between AI activity metrics (sessions, tokens, skills) and business KPIs (deal value, client profitability) by creating queryable per-(client, date) entries.
title: ai-session-ledger
---

# ai-session-ledger

Build a continuous daily ledger of AI session activity, attributed to clients via file-write paths in ACP-compliant Agent Client Logfiles. Bridges the gap between AI activity metrics (sessions, tokens, skills) and business KPIs (deal value, client profitability) by creating queryable per-(client, date) entries.

- **Area:** Foundational
- **Category:** utilities
- **Level:** advanced
- **Input:** conversation
- **Output:** document
- **Setup:** install
- **Roles:** 

Builds a daily AI session ledger from ACP-compliant Agent Client Logfiles and writes Dataview-ready notes for client costing.

## How you ask

- “AI cost per client”
- “AI activity attribution”
- “AI-to-revenue KPIs”

## Inputs

- date — Target date (YYYY-MM-DD | today | yesterday). Default yesterday.
- from-date — Start date (YYYY-MM-DD)
- to-date — End date (YYYY-MM-DD, defaults to today)

## Outputs

- ledger-entries (markdown)
- {company.finance.ai-ledger}/
- {company.finance.ai-ledger}/{YYYY-MM-DD}-{client-id}.md

