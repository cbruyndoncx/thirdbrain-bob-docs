---
layout: workflow-detail.njk
bodyClasses: workflow-detail
seo:
  title: Workflow Video To Youtube — BOB Workflow
  description: Workflow Video to YouTube
  socialImage: https://img.youtube.com/vi/Z8TK7vezjJc/maxresdefault.jpg
skillName: pb-workflow-video-to-youtube
youtubeId: Z8TK7vezjJc
published: '2026-08-01'
privacy: public
title: Workflow Video to YouTube
thumbnail: https://img.youtube.com/vi/Z8TK7vezjJc/maxresdefault.jpg
subtitle: Narrated MP4 with voiceover + music, thumbnail, YouTube metadata, uploaded to channel
inputs: []
outputs:
- label: Silent MP4
  icon: 📋
- label: Voiceover Clips
  icon: 🗣️
- label: Narrated MP4
  icon: 📋
- label: Thumbnail.jpg
  icon: 📋
- label: Metadata.md
  icon: 📋
- label: Published Video
  icon: 🎬
steps:
- label: sync_workflows.py → Sync any new playbooks into workflow-videos.json
  actor: agent
- label: resolve-workflows.sh → Resolve config, stage assets into Remotion build
  actor: agent
- label: render-all.sh → Render silent MP4 + intro/outro PNGs
  actor: agent
- label: Review rendered video — check scene flow and visual quality
  actor: human
- label: generate_scripts.py → Generate voiceover narration text from workflow data
  actor: agent
- label: Review voiceover scripts — check tone, accuracy, and pacing
  actor: human
- label: generate_voiceovers.py → Generate TTS audio clips
  actor: agent
- label: merge_voiceover.py → Merge voiceover + music onto rendered MP4
  actor: agent
- label: youtube_thumbnail.py → Generate thumbnail from intro frame
  actor: agent
- label: generate_youtube_metadata.py → Create YouTube upload markdown
  actor: agent
- label: Review YouTube metadata — check title, description, thumbnail
  actor: human
- label: upload_youtube.py → Upload to YouTube channel
  actor: agent
trigger: '"New skill or playbook needs a narrated workflow video published to YouTube"'
timeSavings: 'Typical run: 30-45 min per video, 4-6 hours for full batch'
compounding: Each run refines templates and context — 9 automated steps improve with accumulated data
frequency: Monthly or per campaign
hook: 'You built the workflow.

  Now it needs a script, a voice, and a thumbnail.'
outcome: ''
benefits: []
cta: ''
category: ''
filterGroup: strategy
area: marketing
---

Narrated MP4 with voiceover + music, thumbnail, YouTube metadata, uploaded to channel


This is an automated business workflow inside ThirdBrain BOB — the Business Operating Brain.
