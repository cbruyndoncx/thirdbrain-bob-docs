---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: ai-video-gen — ThirdBrain BOB skill
  description: 'Target Audience: Marketers, content creators, and business owners producing social ads, B-roll, product demos, and narrative shorts across multiple generative-v'
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: ai-video-gen
catLabel: video
area: marketing
desc: Generates AI videos across multiple backends — Higgsfield (Soul, Kling, Seedance, +30 models), inference.sh (Grok, Wan, OmniHuman, Fabric, foley, +40), and Google Veo…
summary: 'Target Audience: Marketers, content creators, and business owners producing social ads, B-roll, product demos, and narrative shorts across multiple generative-video providers without a film crew.'
difficulty: advanced
inputType: conversation
outputType: video-script
requires: '[install]'
roles: '[Head of Marketing, Content Manager]'
inputs:
- request — What to produce
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set
- backend — Force a specific backend instead of letting the router pick; still subject to that backend's auth preflight (veo | higgsfield | inference-sh)
- script — The ad or scene script — beats and dialogue, not shot direction
- 'locked_assets — The reusable elements already generated and approved: character sheet, product sheet, locations, props. A shot list written before assets are locked produces prompts that cannot be reproduced'
- style_prefix — One style sentence prepended to every scene prompt. Omit to have one proposed from the assets.
- request — What was requested
outputs:
- auth-guidance (text)
- company-ai-video-gen (markdown)
- mp4 (video)
- shotlist (markdown)
- video-prompt (markdown)
prompts:
- Generate a marketing video using Veo 3
- Create a text-to-video clip for our social media
- Animate this product image into a video with Seedance
- Generate an AI video using Wan 2.5 for our launch
---
