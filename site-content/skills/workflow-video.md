---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: workflow-video — ThirdBrain BOB skill
  description: Generate animated MP4 videos that visualize how a vault skill or playbook works — inputs flying in, processing steps on screen, outputs landing, and a contextua
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: workflow-video
catLabel: documents
area: foundational
desc: Generate animated workflow videos showing skill inputs, processing steps, and outputs using Remotion.
summary: Generate animated MP4 videos that visualize how a vault skill or playbook works — inputs flying in, processing steps on screen, outputs landing, and a contextual info footer.
difficulty: advanced
inputType: conversation
outputType: document
requires: '[install]'
roles: '[Head of Marketing, Content Manager]'
inputs:
- playbooks — Playbook source for auto-generated workflow entries.
- request — What to produce
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set
outputs:
- Final-frame still, rendered in a separate `remotion still` pass.
- MP4 with TTS voiceover and music merged by merge_voiceover.py (narration step only).
- Rendered MP4 per workflow (landscape; `-portrait`/`-square` variants with --format). The bundled example config renders under {output.scratch}/workflow-video/renders/ instead.
- Upload note per workflow from generate_youtube_metadata.py (publishing step only, human-gated).
- '{scope.marketing.youtube}/{workflow}.md'
- '{scope.marketing}/video/workflow-video/narrated/{workflow}-narrated.mp4'
- '{scope.marketing}/video/workflow-video/renders/{workflow}-final.png'
- '{scope.marketing}/video/workflow-video/renders/{workflow}.mp4'
prompts:
- Render workflow videos for all skills in the company config
- Preview the marketing-report workflow in Remotion Studio
- Render portrait and square versions of the sales pipeline video for social media
- Sync playbook entries into workflow-videos.json and render the new ones
- Add a new workflow video config for the prospect-audit skill
---
