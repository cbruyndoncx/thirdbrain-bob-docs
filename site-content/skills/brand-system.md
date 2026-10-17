---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: brand-system — ThirdBrain BOB skill
  description: Authors a complete, agent-readable brand design system. Two routes — `discover-assets` (find and verify real brand assets from official sources) and `write-spec
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: brand-system
catLabel: documents
area: foundational
desc: Authors a brand design system as a Google DESIGN.md spec with companion UI and media standards and HTML preview showcases.
summary: Authors a complete, agent-readable brand design system. Two routes — `discover-assets` (find and verify real brand assets from official sources) and `write-spec` (generate a Google DESIGN.md file with tokens + rationale). Run them in sequence for a new brand; run `write-spec` alone when assets are already documented.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[Head of Marketing]'
inputs:
- design-system — Brand design system — colors, type, tokens. `company.brand`, file DESIGN.md.
- 'product-design-system — Product-level design system, when scoped to a product: `DESIGN.md` in the product''s brand folder (`product.brand`).'
- client-design-system — Client design system, when scoped to a client. `client.brand`, file `DESIGN.md`.
- brand_name — Brand, product, or client identifier (e.g., "DJI Pocket 4", "company-name", "client-id")
- scope — Routes output location (company → `company.brand`, product → `product.brand`, client → `client.brand`) (company | product | client)
- known_assets — Anything the user already has (logo files, color list, brand PDF, website URL)
- design_md — Path to the brand's DESIGN.md
- brand_assets_md — Path to the brand's brand-assets.md (Gaps Flagged section becomes the Open Questions panel)
- output_html — Where to write the HTML showcase
- brand_name — Brand name used to authors the companion UI-STANDARDS.md with page templates, interaction states, application patterns (modal/toast/tooltip), stack/plugin discipline, performance budget, and SEO/analytics rules. Sibling to DESIGN.md but updated more frequently. Use when site is being redesigned or new lead pages/forms are being added
- scope — Scope used to authors the companion UI-STANDARDS.md with page templates, interaction states, application patterns (modal/toast/tooltip), stack/plugin discipline, performance budget, and SEO/analytics rules. Sibling to DESIGN.md but updated more frequently. Use when site is being redesigned or new lead pages/forms are being added (company | product | client)
- design_md_ref — Path to brand's DESIGN.md (UI-STANDARDS depends on it for tokens)
- stack_choices — Pre-decided stack (CMS, page builder, plugins) if known
- ui_standards_md — Ui standards md used to generates a companion HTML showcase rendering interaction states, application patterns, and the stack-discipline checklist from UI-STANDARDS.md. Sibling to the brand-showcase preview (Route C)
- design_md — Brand DESIGN.md for token resolution (colors, fonts)
- output_html — Output html used to generates a companion HTML showcase rendering interaction states, application patterns, and the stack-discipline checklist from UI-STANDARDS.md. Sibling to the brand-showcase preview (Route C)
- brand_name — Brand name used to authors MEDIA-STANDARDS.md covering video templates (title card, lower-third, end card), slide deck patterns, motion timing for video, audio/voiceover rules, platform-specific specs, and media-specific anti-patterns. Sibling to DESIGN.md and UI-STANDARDS.md. Use when video, slide, or animation deliverables are being produced and need brand-consistent application rules
- scope — Scope used to authors MEDIA-STANDARDS.md covering video templates (title card, lower-third, end card), slide deck patterns, motion timing for video, audio/voiceover rules, platform-specific specs, and media-specific anti-patterns. Sibling to DESIGN.md and UI-STANDARDS.md. Use when video, slide, or animation deliverables are being produced and need brand-consistent application rules (company | product | client)
- design_md_ref — Path to brand's DESIGN.md (MEDIA-STANDARDS depends on it for tokens)
- media_standards_md — Media standards md used to generates an HTML showcase rendering video frame mockups (title card / lower-third / end card), aspect-ratio examples, slide templates, motion timing scale, platform spec table, and media anti-patterns themed with brand tokens. Sibling to brand-showcase (Route C) and ui-standards-showcase (Route E)
- design_md — Design md used to generates an HTML showcase rendering video frame mockups (title card / lower-third / end card), aspect-ratio examples, slide templates, motion timing scale, platform spec table, and media anti-patterns themed with brand tokens. Sibling to brand-showcase (Route C) and ui-standards-showcase (Route E)
- output_html — Output html used to generates an HTML showcase rendering video frame mockups (title card / lower-third / end card), aspect-ratio examples, slide templates, motion timing scale, platform spec table, and media anti-patterns themed with brand tokens. Sibling to brand-showcase (Route C) and ui-standards-showcase (Route E)
- brand_name — Brand, product, or client identifier
- scope — Scope used to generate a Google DESIGN.md format file with YAML token frontmatter and prose rationale — colors, typography, layout, elevation, shapes, components, do's/don'ts (company | product | client)
- brand_assets_ref — Path to brand-assets.md from discover-assets (recommended)
- aesthetic_direction — User-stated direction (editorial, premium, technical, warm, etc.)
outputs:
- Companion to DESIGN.md covering web UI patterns, states, application components, stack discipline, performance budget
- Google DESIGN.md spec with YAML token frontmatter and 8 prose sections (Overview, Colors, Typography, Layout, Elevation, Shapes, Components, Do's/Don'ts)
- Self-contained HTML brand showcase with rendered palette, typography, components, Do's/Don'ts, open questions, and sign-off block. Opens in any browser; print-friendly.
- Self-contained HTML rendering all interaction states and application patterns, with tooling discipline checklist
- Self-contained HTML rendering video templates, slide patterns, motion timing, platform specs, anti-patterns
- Sibling to DESIGN.md + UI-STANDARDS — video templates, slide patterns, motion timing for video, platform specs, media anti-patterns
- Verified asset locations, source URLs, color extraction methodology, authenticity flags (verified human-created vs flagged for review)
- '{scope.brand}/DESIGN.md'
- '{scope.brand}/MEDIA-STANDARDS.md'
- '{scope.brand}/UI-STANDARDS.md'
- '{scope.brand}/brand-assets.md'
- '{scope.deliverables}/{date}-brand-review/brand-showcase.html'
- '{scope.deliverables}/{date}-brand-review/media-standards-showcase.html'
- '{scope.deliverables}/{date}-brand-review/ui-standards-showcase.html'
prompts:
- Set up brand for [X]
- Create design system
- Write DESIGN.md
---
