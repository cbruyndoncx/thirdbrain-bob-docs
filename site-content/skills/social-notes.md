---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: social-notes — ThirdBrain BOB skill
  description: Transform social media videos into structured Obsidian knowledge-base notes enriched with engagement stats, chapter structure, and community insights.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: social-notes
catLabel: marketing-content
area: marketing
desc: Create structured Obsidian knowledge-base notes from social media videos and posts.
summary: Transform social media videos into structured Obsidian knowledge-base notes enriched with engagement stats, chapter structure, and community insights.
difficulty: intermediate
inputType: conversation
outputType: document
requires: '[config]'
roles: '[Content Manager]'
inputs:
- source-url — URL of the social media video or post to extract; determines platform-specific auth, subtitle, and stats handling.
- video-transcript — Downloaded transcript read and corrected before note synthesis; produced by the `download-transcript-and-metadata` route.
- video-metadata — Downloaded metadata read for chapters, stats, and comments used in the corroboration pass; produced by the `download-transcript-and-metadata` route.
- video-transcript — Corrected transcript synthesized into the note's sections rather than reflowed verbatim.
- video-metadata — Platform, stats, chapters, and comments merged into the note's header, tags, and Community Insights section.
- operator-profile — Read for `### Platform Entitlements` before any audio or video download — gates the `--whisper` and audio `--word-timestamps` fallback to entitled platforms, and, when screenshots are requested, decides whether frame capture uses local extraction (yt-dlp + ffmpeg) or Playwright.
- profile — Company or client profile used only when the note adds a Comparison to Our Setup or Bridge to ThirdBrain Vault section mapping the video to vault capabilities.
- knowledge-base-note — Path of the created note to open; produced by the `create-the-note` route.
outputs:
- ASR corrections made against corroborating sources, prompt-injection flags, and chapter-based screenshot timestamp suggestions carried into note creation; no file is written by this route.
- Clean transcript with 5-minute timestamp markers, from platform subtitles or Whisper audio transcription.
- Confirmation that the created note was opened in Obsidian via the advanced-uri handler; writes no new file.
- Platform, stats, chapters, tags, description, and top comments/creator replies for the video.
- Structured knowledge-base note synthesizing the transcript and metadata, with TL;DR, key takeaways, resources, and community insights; body guidance saves the final note under the resources root (`resource.root`) with a snake_case filename derived from the title.
- Word-level start/end timestamps; produced only when --word-timestamps is passed. Consumed by content-repurposer's long-to-shorts route.
- prefer a permanent directory)
- '{resource.root}/{title_snake_case}.md'
prompts:
- Create notes from this YouTube video
- Summarize this TikTok and save it to my vault
- Transcribe this Instagram Reel and extract key points
- Make knowledge base notes from this LinkedIn video
- Create notes from this video and map ideas to our vault capabilities
---
