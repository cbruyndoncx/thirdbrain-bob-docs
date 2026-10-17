---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: demo-video — ThirdBrain BOB skill
  description: Record and post-produce screen demos. Capture → trim → brand → narrate → music → final MP4.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: demo-video
catLabel: documents
area: foundational
desc: Records and post-produces screen demos with ffmpeg and Remotion.
summary: Record and post-produce screen demos. Capture → trim → brand → narrate → music → final MP4.
difficulty: advanced
inputType: conversation
outputType: document
requires: '[install]'
roles: '[]'
inputs:
- name — Demo identifier in kebab-case (e.g. fix-my-marketing)
- name — Demo identifier in kebab-case
- prompt — The prompt or skill to execute while recording
- recording — Recording used to remove idle segments from a raw recording using frame-diff analysis
- 'fade — Crossfade duration between segments (default: 0.5s)'
- recording — Raw or trimmed recording containing confidential content
- spec — List of regions - x, y, w, h in source pixels, plus optional start/end seconds and strength
- config — demo-videos.json with branding and per-demo messaging
- demo — Demo ID from config (e.g. audit-before-after)
- narration — Full narration text or @file.txt path
- 'voice — TTS voice (Edge TTS default: en-US-JennyNeural; with --tts openai the default is echo)'
- proof-artifact — Screenshot to display as proof overlay (5s before outro)
- source (Teaser (Hyperframes)) — Finished demo recording (e.g. the company marketing folder's `demo-recordings/public/*.mp4`, under `company.marketing`)
- scenes — 4 (start_seconds, duration_seconds) tuples for the 4 overlay-card scenes
- brand — brncx | gbl
- narration — Narration text following template in references/teaser-settings.md
- name — Short identifier in kebab-case (e.g. thirdbrain-dashboard-tour)
- 'script — Interaction script (.ps1, .py, or .js/.ts). Annotate with # CAPTION: "text" to auto-generate captions.'
- avatar_video — Talking-head MP4 from avatar-video skill (512×512 MuseTalk output or larger). Avatar audio is the sole audio track.
- 'brand — a key of shorts-config.json `_assets.branding`: default (neutral, the default) | brncx | gbl'
- capture_mode — monitor (default, full-screen via record_demo.ps1) | playwright (browser session via playwright-cli)
- captions — Pre-existing captions JSON to override auto-generation (for re-renders after tweaking)
outputs:
- Per-brand palette, fonts, intro/outro copy and template key — created only when adding a new brand, then passed to the renderer as `--brand`.
- Per-demo scene, narration and outro-headline config — created only when adding a new demo, then passed to the renderer as `--demo` on every later run.
- blurred (mp4)
- captions_json (json)
- final (mp4)
- prefer a permanent directory)
- recording (mp4)
- teaser (mp4)
- timeline (json)
- trimmed (mp4)
- '{output-dir}/final/{name}-narrated.mp4'
- '{output-dir}/transcripts/{name}-timeline.json'
- '{output-dir}/trimmed/{name}.mp4'
- '{output-dir}/{name}-blurred.mp4'
- '{projects-sibling-dir}/hyperframes-engine/renders/{demo-id}-{brand}.mp4'
- '{scope.marketing}/demo-teaser/brand.yaml'
- '{scope.marketing}/demo-teaser/{demo-id}.yaml'
prompts:
- Record a demo of fix my marketing
- Capture me running the prospect audit
- Start recording a demo called daily-briefing
- Record the board of advisors session
---
