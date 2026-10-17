---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: yt-end-screen-cta — ThirdBrain BOB skill
  description: Write end screen CTA scripts that convert the last 20-30 seconds of a YouTube video into subscriber growth, next-video clicks, and playlist engagement. The last
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: yt-end-screen-cta
catLabel: content
area: marketing
desc: Write end screen CTA scripts with verbal and visual directions for YouTube videos.
summary: Write end screen CTA scripts that convert the last 20-30 seconds of a YouTube video into subscriber growth, next-video clicks, and playlist engagement. The last 30 seconds are the highest-intent moment -- the viewer watched the entire video and is primed to act. Design end-of-video experiences where verbal CTAs and visual end screen elements work together.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[Content Manager]'
inputs:
- youtube_context — Channel niche, audience, positioning and format. Optional — the route collects minimum context from the user when absent.
- video_title — The video title (CTA must feel like a natural extension of the video's promise)
- primary_goal — subscriber-growth, next-video, lead-magnet, or playlist-series (subscriber-growth | next-video | lead-magnet | playlist-series)
- next_content — The specific video, playlist, or resource to link from the end screen
- key_takeaway — What the viewer just learned (used to bridge into the CTA naturally)
outputs:
- Complete end screen CTA with verbal script, visual layout, element selection, and companion CTAs
- '{company.marketing}/video/end-screens/{video-slug}_end_screen_{YYYY-MM-DD}.md'
prompts:
- End screen
- End card
- CTA strategy
---
