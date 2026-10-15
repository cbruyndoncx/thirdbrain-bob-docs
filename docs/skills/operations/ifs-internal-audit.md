---
description: Analyseer bestaande bedrijfsprocedures tegen IFS Food 8 eisen, score naleving per domein, identificeer KO/Major/Minor afwijkingen, en genereer actieplannen met deadlines — inclusief PDF rapport.
title: ifs-internal-audit
---

# ifs-internal-audit

Analyseer bestaande bedrijfsprocedures tegen IFS Food 8 eisen, score naleving per domein, identificeer KO/Major/Minor afwijkingen, en genereer actieplannen met deadlines — inclusief PDF rapport.

- **Area:** Operations
- **Category:** compliance
- **Level:** beginner
- **Input:** conversation
- **Output:** document
- **Setup:** none
- **Roles:** Operations Manager

Performs internal audits against IFS Food 8 requirements and produces gap analyses with KO/Major/Minor classification.

## How you ask

- “Voer een interne IFS-audit uit op onze procedures”
- “Check onze HACCP-documentatie tegen IFS hoofdstuk 2”
- “Gap-analyse: welke IFS-eisen dekken onze SOP's niet?”
- “Status update van de corrigerende maatregelen uit de vorige audit”
- “Bereid ons voor op de externe IFS-audit volgende maand”

## Inputs

- site — Site or facility under audit
- audit_date — Date of the audit
- profile — Company or client profile — sector and operating context.
- site — Site under audit
- domain — IFS clause area to audit
- audit_ref — Prior audit whose findings are being followed up
- finding_ids — Specific findings to check; defaults to all open

## Outputs

- audit-pdf (pdf)
- audit-report (markdown)
- corrective-action-report (markdown)
- corrective-actions (markdown)
- domain-audit-pdf (pdf)
- domain-audit-report (markdown)
- gap-matrix (markdown)
- {client.deliverables}/ifs-audit/ifs-audit-{YYYY-MM-DD}.md
- {client.deliverables}/ifs-audit/ifs-audit-{YYYY-MM-DD}.pdf
- {client.deliverables}/ifs-audit/ifs-corrective-actions-{YYYY-MM-DD}.md
- {client.deliverables}/ifs-audit/ifs-gap-matrix-{YYYY-MM-DD}.md

