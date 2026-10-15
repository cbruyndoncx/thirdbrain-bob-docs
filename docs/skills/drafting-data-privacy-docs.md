---
description: Drafts data privacy, GDPR, EU AI Act, ePrivacy and information security documents — Privacy Policy, Cookie Policy, Employee Privacy Notice, Acceptable Use Policy, DSAR Procedure, Breach Response Plan, Retention Schedule, Information Security Policy, DPA Article 28 template, and Data Protection Complaints Procedure. Use when asked to draft, write, generate, or amend any of those, or when a client asks "what is your data processing position". Supports greenfield drafting and suggested-edits modes. NOT legal advice — every output is a starting draft for review by a DPO or counsel. Jurisdiction coverage uses a per-country pack system; any country without a pack needs one built first. Always render via scripts/render_template.py rather than copying a template by hand. Per-country packs and their verification status live in references/jurisdictions/.
title: drafting-data-privacy-docs
---

# drafting-data-privacy-docs

Drafts data privacy, GDPR, EU AI Act, ePrivacy and information security documents — Privacy Policy, Cookie Policy, Employee Privacy Notice, Acceptable Use Policy, DSAR Procedure, Breach Response Plan, Retention Schedule, Information Security Policy, DPA Article 28 template, and Data Protection Complaints Procedure. Use when asked to draft, write, generate, or amend any of those, or when a client asks "what is your data processing position". Supports greenfield drafting and suggested-edits modes. NOT legal advice — every output is a starting draft for review by a DPO or counsel. Jurisdiction coverage uses a per-country pack system; any country without a pack needs one built first. Always render via scripts/render_template.py rather than copying a template by hand. Per-country packs and their verification status live in references/jurisdictions/.

| | |
|---|---|
| **Area** | Operations |
| **Category** | qms |
| **Level** | beginner |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [none] |
| **Roles** | [] |

Drafts data privacy, GDPR, EU AI Act, ePrivacy and information security documents — Privacy Policy, Cookie Policy, Employee Privacy Notice, Acceptable Use Policy, DSAR…

## How you ask

- “what is your data processing position”
- “draft a GDPR document”
- “write data privacy documents”
- “help with our data protection paperwork”
- “AI policy”
- “policy for the EU AI Act”
- “is X compliant?”
- “s Privacy Policy and drafting a client”

## Inputs

- document_types — One or several; see the four-pass grouping (privacy-policy | cookie-policy | complaints-procedure | employee-privacy-notice | acceptable-use-policy | dsar-procedure | breach-response-plan | retention-schedule | information-security-policy | dpa-article-28)
- jurisdiction — Must have a pack under references/jurisdictions/ (ie | uk | ae | be | nl | au | difc | adgm)
- organisation_profile — Captured once per session at Step 3; reused across documents
- existing_document — File path or pasted content of the document to amend
- amendment_focus — Which lens to amend through; defaults to a general review if omitted (ai-compliance | gdpr-gap-closing | modernisation)
- jurisdictions — Two or more; applicability of the second must be established, not assumed (ie | uk | ae | be | nl | au | difc | adgm)
- jurisdiction_code — ISO-style lowercase code, e.g. nl
- regime_family — Whether the pack loads with the EU core or stands alone; sets its regime-family marker (eu-overlay | self-contained)
- jurisdiction_code — ISO-style lowercase code of the pack to verify, e.g. ae

## Outputs

- Markdown master, disclaimer and version block attached
- Per-edit: Current state / Illustrative addition / Why this language / Open items
- Reusable legal-rule note so other skills can consume the research (one folder per jurisdiction under resource.legal)
- Updated in place; the pack-status marker set to unverified | partially-verified | source-verified
- document_md (markdown)
- pack_md (markdown)
- references/jurisdictions/{code}.md
- user-confirmed path
- user-confirmed path, YYYY-MM-DD-{Document-Name}.md
- {resource.legal}/{JURISDICTION}/

