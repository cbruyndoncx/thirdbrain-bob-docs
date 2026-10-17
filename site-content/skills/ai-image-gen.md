---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: ai-image-gen — ThirdBrain BOB skill
  description: 'Target Audience: Marketers, content creators, and designers who need AI-generated visuals — social graphics, persona portraits, framework diagrams, ad creatives'
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: ai-image-gen
catLabel: images
area: marketing
desc: Generates images across Google Gemini, Google Imagen and OpenAI gpt-image, picking the model that fits the job and the key that is set.
summary: 'Target Audience: Marketers, content creators, and designers who need AI-generated visuals — social graphics, persona portraits, framework diagrams, ad creatives, or product mockups — without leaving the CLI.'
difficulty: advanced
inputType: conversation
outputType: document
requires: '[api-key]'
roles: '[]'
inputs:
- request — Visual direction, subject, and mood to explore for a first pass; requirements can stay loose at this stage.
- request — The specific change to apply to the existing render — what to keep and what to adjust, one or two variables at a time.
- request — Photorealistic subject or scene to render — product shot, portrait, or physical detail where realism matters most.
- aspect-ratio — Output shape locked before rendering (e.g. 1:1, 16:9, 4:5) — Imagen is single-shot, so this is fixed upfront rather than iterated.
- resolution — Resolution tier (1K, 2K, 4K) — applies only to OpenAI gpt-image size selection; Imagen and Gemini ignore it and render at the model's default size.
- request — Subject to merge with the loaded or extracted style before rendering.
- style-id — ID of a saved style from `assets/style-library/STYLE-GUIDE.md` to load and merge with the subject.
- reference-image — Inspiration image to extract a reusable style from via `extract_style`, used when no saved style ID fits.
outputs:
- Draft PNG showing an initial visual direction for the requested subject.
- PNG rendered by merging the loaded or extracted style with the current subject, ready to promote to the style library once confirmed.
- Photorealistic PNG rendered via an Imagen model at the locked aspect ratio.
- Updated PNG produced by continuing the multi-turn session with the requested change applied.
- prefer a permanent directory)
prompts:
- Generate a product hero image using Gemini
- Create a social media graphic with Nano Banana
- Build a style library from these reference images
- Iterate on this AI-generated image — make the background warmer
---
