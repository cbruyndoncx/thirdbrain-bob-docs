---
description: Transform meeting transcripts into professional, context-rich proposals that reflect accumulated client intelligence.
title: proposal-writer
---

# proposal-writer

Transform meeting transcripts into professional, context-rich proposals that reflect accumulated client intelligence.

- **Area:** Sales & Clients
- **Category:** sales
- **Level:** beginner
- **Input:** conversation
- **Output:** document
- **Setup:** none
- **Roles:** Head of Sales

Generates context-rich proposal documents from meeting transcripts by loading full client intelligence — meeting history, ICP data, deal context, and relationship…

## How you ask

- “Draft a proposal from this meeting transcript”
- “Create a professional proposal for the consulting engagement”
- “Generate a scope of work from these call notes”
- “Write a proposal matching our company's style guide”
- “Generate the proposal with our company template and include the BOB process-flow diagrams”

## Inputs

- transcript — Meeting transcript or call notes
- client-id — Client folder identifier
- template — docx template for formatting. Default (`--template auto`): `proposal_template.docx` in `{company.sales}/templates/`, else the `*_proposal_template.docx` there (shortest name when several)
- process-flow — Companion mermaid process-flow .md. Default (`--process-flow auto`): `process_flow_template.md` in `{company.sales}/templates/`, else the `*_process_flow_template.md` there. Diagrams are rendered via mmdc and inserted at {{PROCESS_FLOW_*}} placeholders in the template.
- icp — loaded from your vault context
- marketing-context — loaded from your vault context
- offerings — loaded from your vault context
- profile — loaded from your vault context
- tone-of-voice — loaded from your vault context
- all — loaded from your vault context
- proposalall — loaded from your vault context
- contact-details — loaded from your vault context
- decision-maker-mapall — loaded from your vault context
- lead-qualificationall — loaded from your vault context
- prospect-analysisall — loaded from your vault context
- proposal-markdown — The already-drafted proposal body. Passed to generate_proposal.py as its positional content argument; nothing from Phases 0-2 is re-run
- client-name — Client name written into the document header and the default filename
- output-path — Destination .docx. Absent, the script names it {Client}_Proposal_{YYYYMMDD}.docx in the working directory
- template — Branded .docx template used as the base document. Absent, the script formats from scratch with brand colours
- process-flow — Companion mermaid process-flow .md. Its 5 blocks are rendered via mmdc and inserted at the {{PROCESS_FLOW_*}} placeholders; skipped with a warning when mmdc is unavailable
- proposal-date — Date printed on the proposal. Absent, today is used

## Outputs

- Formatted proposal document with template styling and, when supplied, the inserted process-flow diagrams. Pass `--output` resolved under `client.sales` (see references/proposal_structure_and_output.md); without it the script writes `{Client}_Proposal_{YYYYMMDD}.docx` in the working directory
- comparison-report (markdown)
- context-depth-report (markdown)
- context-proposal (docx)
- generic-proposal (docx)
- proposal (docx)
- {client.sales}/proposals/context_comparison_report.md
- {client.sales}/proposals/context_depth_report.md
- {client.sales}/proposals/{client-name}_Proposal_Context_{YYYY-MM-DD}.docx
- {client.sales}/proposals/{client-name}_Proposal_Generic_{YYYY-MM-DD}.docx
- {client.sales}/proposals/{client-name}_Proposal_{YYYY-MM-DD}.docx

## Seen in these workflows

- [The meeting went well.](../../workflows/sales/proposal-writer.md)

