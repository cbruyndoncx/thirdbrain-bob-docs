---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: ux-browser-audit — ThirdBrain BOB skill
  description: For product managers, UX designers, and development teams who need automated usability testing of web application user flows.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: ux-browser-audit
catLabel: development
area: foundational
desc: Automated browser-based UX audit that walks through an application as a real user — navigating flows, detecting friction points, measuring load times, and producing a…
summary: For product managers, UX designers, and development teams who need automated usability testing of web application user flows.
difficulty: advanced
inputType: conversation
outputType: document
requires: '[install]'
roles: '[Product Manager]'
inputs:
- url — Application URL to audit
- flow — Specific flow to test (e.g., 'signup to dashboard', 'checkout', 'onboarding'). If omitted, audits the primary user journey from landing page.
- persona — User persona perspective (e.g., 'new user', 'returning customer', 'admin')
- credentials — Login credentials if the flow requires authentication
- url — Page URL to audit
- url_before — Original version URL or previous audit report
- url_after — Updated version URL
- flow — User flow to compare
outputs:
- prefer a permanent directory)
- report (markdown)
- screenshots (png)
- '{vault.attachments}/ux-audit-page-{slug}/'
- '{vault.attachments}/ux-audit-{app-name}/'
prompts:
- UX audit
- Walk through my app
- Test the user flow
---
