---
title: Workflow Video to YouTube
---

# Workflow Video to YouTube

*Narrated MP4 with voiceover + music, thumbnail, YouTube metadata, uploaded to channel*

<div class="video-wrap"><iframe width="100%" height="420" src="https://www.youtube.com/embed/Z8TK7vezjJc?rel=0" title="Workflow Video to YouTube" frameborder="0" allowfullscreen loading="lazy"></iframe></div>

> You built the workflow.
> Now it needs a script, a voice, and a thumbnail.

| | |
|---|---|
| **Area** | Marketing |
| **Time savings** | Typical run: 30-45 min per video, 4-6 hours for full batch |
| **Try it** | "New skill or playbook needs a narrated workflow video published to YouTube" |
| **Compounding** | Each run refines templates and context — 9 automated steps improve with accumulated data |
| **Frequency** | Monthly or per campaign |
| **Published** | 2026-08-01 |

## What BOB does

1. sync_workflows.py → Sync any new playbooks into workflow-videos.json
2. resolve-workflows.sh → Resolve config, stage assets into Remotion build
3. render-all.sh → Render silent MP4 + intro/outro PNGs
4. Review rendered video — check scene flow and visual quality
5. generate_scripts.py → Generate voiceover narration text from workflow data
6. Review voiceover scripts — check tone, accuracy, and pacing
7. generate_voiceovers.py → Generate TTS audio clips
8. merge_voiceover.py → Merge voiceover + music onto rendered MP4
9. youtube_thumbnail.py → Generate thumbnail from intro frame
10. generate_youtube_metadata.py → Create YouTube upload markdown
11. Review YouTube metadata — check title, description, thumbnail
12. upload_youtube.py → Upload to YouTube channel

## Outputs

- 📋 Silent MP4
- 🗣️ Voiceover Clips
- 📋 Narrated MP4
- 📋 Thumbnail.jpg
- 📋 Metadata.md
- 🎬 Published Video

