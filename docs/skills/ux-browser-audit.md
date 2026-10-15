---
description: For product managers, UX designers, and development teams who need automated usability testing of web application user flows.
title: ux-browser-audit
---

# ux-browser-audit

For product managers, UX designers, and development teams who need automated usability testing of web application user flows.

| | |
|---|---|
| **Area** | Foundational |
| **Category** | development |
| **Level** | advanced |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [install] |
| **Roles** | [Product Manager] |

Automated browser-based UX audit that walks through an application as a real user — navigating flows, detecting friction points, measuring load times, and producing a…

## How you ask

- “UX audit”
- “Walk through my app”
- “Test the user flow”

## Inputs

- url — Application URL to audit
- flow — Specific flow to test (e.g., 'signup to dashboard', 'checkout', 'onboarding'). If omitted, audits the primary user journey from landing page.
- persona — User persona perspective (e.g., 'new user', 'returning customer', 'admin')
- credentials — Login credentials if the flow requires authentication
- url — Page URL to audit
- url_before — Original version URL or previous audit report
- url_after — Updated version URL
- flow — User flow to compare

## Outputs

- prefer a permanent directory)
- report (markdown)
- screenshots (png)
- {vault.attachments}/ux-audit-page-{slug}/
- {vault.attachments}/ux-audit-{app-name}/

