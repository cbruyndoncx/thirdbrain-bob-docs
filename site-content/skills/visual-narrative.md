---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: visual-narrative — ThirdBrain BOB skill
  description: 'Turn a business narrative into a style-locked illustrated video: an ordered sequence of beats, one generated visual per beat, narration, brand treatment, and se'
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: visual-narrative
catLabel: content
area: marketing
desc: Scripted visual narrative pipeline for business — turns a beat script into a style-locked illustrated sequence with narration and multiple rendered cuts.
summary: 'Turn a business narrative into a style-locked illustrated video: an ordered sequence of beats, one generated visual per beat, narration, brand treatment, and several cuts from one script.'
difficulty: advanced
inputType: conversation
outputType: document
requires: '[install]'
roles: '[]'
inputs:
- subject — What the narrative is about
- format — what-if | process-explainer | compliance-scenario | case-study | vision-film
- beats — Beat count including cover (default 10, range 6-15)
- treatment — Visual treatment name (suggested if omitted)
- 'variants — Cuts to produce (default: full + social)'
- subject — Subject used to fit check, style canon, and beat script — no generation, no render. Use when the script needs approval or the generator quota is spent
- format — Format used to fit check, style canon, and beat script — no generation, no render. Use when the script needs approval or the generator quota is spent
- subject — Subject used to recommend treatments suited to the subject, with full paragraphs and fit rationale
outputs:
- 2-3 treatment paragraphs with fit rationale
- book_config (json)
- conversation
- prefer a permanent directory)
- script (markdown)
- video_full (mp4)
- video_social (mp4)
prompts:
- What-if video
- Explainer narrative
- Case study video
---
