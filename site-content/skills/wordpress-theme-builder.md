---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: wordpress-theme-builder — ThirdBrain BOB skill
  description: 'Target audience: brand designers, web developers, and agency leads building WordPress theme deliverables for clients — from one-off bespoke themes to white-labe'
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: wordpress-theme-builder
catLabel: marketing-seo
area: marketing
desc: Scaffolds WordPress block themes for client websites.
summary: 'Target audience: brand designers, web developers, and agency leads building WordPress theme deliverables for clients — from one-off bespoke themes to white-label child-theme programs.'
difficulty: advanced
inputType: url
outputType: document
requires: '[install]'
roles: '[Head of Marketing, Content Manager]'
inputs:
- spec — Path to YAML theme spec (theme name, slug, author, base palette, license)
- output_dir — Output directory passed as --output-dir; use the client's theme folder (`{client.themes}/{slug}/`) for client work, else the scratch output area (`{output.scratch}/themes/{slug}/`)
- tokens — Path to design-tokens YAML
- theme_dir — Path to existing theme folder
- theme_dir — Theme root
- name — Pattern slug (kebab-case)
- title — Pattern title shown in inserter
- html — Path to HTML or markdown file containing block markup
- categories — Comma-separated pattern categories; default "featured
- parent_slug — Parent theme folder name (must match exactly)
- child_spec — Path to YAML child-theme spec (name, slug, client overrides)
- output_dir — Target child theme folder passed as --output-dir; normally the client's theme folder (`{client.themes}/{child-slug}/`)
- theme_dir — Theme root to validate
- output_zip — Output zip path; default {theme_dir}/../{slug}-{version}.zip
outputs:
- Written only when the tokens come from a `brand-system` spec — palette, type scale and spacing extracted by hand into the tokens YAML shape, then passed back in as `tokens`. See workflows/from_design_tokens.md.
- child-theme (wordpress-child-theme)
- pass/fail per check, exit code 0 on full pass
- pass/fail per check, exit code 0 on full pass` — validation-report (text)
- pattern-file (php)
- theme-folder (wordpress-block-theme)
- theme-json (json)
- theme-zip (zip)
- '{client.themes}/tokens.yaml'
- '{client.themes}/{child-slug}/'
- '{client.themes}/{slug}/ or {output.scratch}/themes/{slug}/'
- '{theme_dir}/../{slug}-{version}.zip'
- '{theme_dir}/patterns/{name}.php'
- '{theme_dir}/theme.json'
prompts:
- Build a new WordPress block theme for ACME Corp from this design tokens YAML
- Update the colors in the ACME theme — designer just sent revised tokens
- Add a hero-cta block pattern to the agency base theme
- Scaffold a child theme for ACME on top of our base agency theme
- Validate and package the ACME theme for delivery
---
