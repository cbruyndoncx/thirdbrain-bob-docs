---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: content-scorer — ThirdBrain BOB skill
  description: Score content quality and scrub AI patterns before publishing. Works with any written content — blog posts, landing pages, emails, documentation.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: content-scorer
catLabel: marketing-content
area: marketing
desc: Scores blog posts, landing pages, and AI drafts across humanity, specificity, structure, SEO, and readability.
summary: Score content quality and scrub AI patterns before publishing. Works with any written content — blog posts, landing pages, emails, documentation.
difficulty: advanced
inputType: conversation
outputType: document
requires: '[install]'
roles: '[Head of Marketing, Content Manager]'
inputs:
- request — What to produce
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set
- blog-content — Blog post content (file path, URL, or pasted text)
- 'audit-mode — Rating only (concise) or Full audit (with improvements). Default: full (rating-only | full)'
outputs:
- blog-audit-report (markdown)
- content-scorer (markdown)
- '{scope.marketing}/content/blog-audit-{YYYY-MM-DD}.md'
- '{scope.marketing}/content/content-scorer-{YYYY-MM-DD}.md'
prompts:
- Score this article before I publish it
- Run a content audit on my latest blog post
- Check this draft for AI writing patterns and fix them
- Proofread and score this marketing page copy
- Audit this blog as a business asset
- Give me a rating-only report on this blog
- 'Full audit: strengths, weaknesses, and improvements for this article'
- Score this blog for conversion potential and strategic fit
---
