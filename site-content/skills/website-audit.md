---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: website-audit — ThirdBrain BOB skill
  description: Orchestrates comprehensive website audits by running the SEO, GEO and UX sub-audits one after the other (never concurrently; see `references/crawl_etiquette.md`
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: website-audit
catLabel: marketing-seo
area: marketing
desc: Audits websites across SEO, GEO, and UX in a single scored report.
summary: Orchestrates comprehensive website audits by running the SEO, GEO and UX sub-audits one after the other (never concurrently; see `references/crawl_etiquette.md`), then merging results into a unified report.
difficulty: beginner
inputType: url
outputType: document
requires: '[none]'
roles: '[Head of Marketing]'
inputs:
- client_icp_index — Client ICP profile; the company-scope equivalent is icp.md.
- icp — Ideal customer profile — who the output targets.
- marketing_context — Positioning and messaging context.
- url — Website URL to analyze
- scope — `company`, or a client-id under the clients root (`client.root`) — a string with one reserved value, not a closed set
- persona — Buyer persona lens — path to an ICP/persona note or free-text description. When omitted, resolved via the fallback chain in references/persona_lens.md
- competitors — 1-5 competitor domains/URLs. When provided, adds a Competitive Positioning section (see references/competitive_benchmarking.md). Omit to skip the module entirely.
- competitor_notes — Free-text user knowledge about the named competitors (win/loss reasons, known strengths/weaknesses) — folded into the narrative, never scored.
- url — Website URL to re-audit (must match a prior audit-metadata.yaml entry)
outputs:
- Append-only audit log — one entry per run with scores, persona lens and file pointers; the baseline `re-audit` diffs against.
- Combined SEO/GEO/UX report with persona map, action plan and, when competitors were given, competitive positioning.
- One file per sub-audit — `seo`, `geo`, `ux`, and `competitor` when competitors were given — merged in Phase 3 and read back by `re-audit` as the finding baseline.
- PDF rendering of the report, built by pdf-report from `website-audit-input.json`.
- The distilled Persona Lens block the sub-agents audit through, with the source it was resolved from.
- comparison-report (markdown)
- '{output_base}/audit-metadata.yaml'
- '{output_base}/research/persona-lens.md'
- '{output_base}/research/{kind}-findings.json'
- '{output_base}/website-audit-{domain}-{YYYY-MM-DD}.md'
- '{output_base}/website-audit-{domain}-{YYYY-MM-DD}.pdf'
prompts:
- Run a full website audit covering SEO and GEO
- Audit our website for search visibility and AI citability
- Analyze our site's metadata, technical SEO, and content structure
- Check our website's compatibility with AI answer engines
---
