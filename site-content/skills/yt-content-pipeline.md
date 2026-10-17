---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: yt-content-pipeline — ThirdBrain BOB skill
  description: 5-role NotebookLM workflow for content creation. Turns a notebook of competitor/reference sources into topics, title+thumbnail options, a video script, and visu
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: yt-content-pipeline
catLabel: video
area: marketing
desc: YouTube content creation pipeline using NotebookLM.
summary: 5-role NotebookLM workflow for content creation. Turns a notebook of competitor/reference sources into topics, title+thumbnail options, a video script, and visual prompts.
difficulty: advanced
inputType: conversation
outputType: video-script
requires: '[install]'
roles: '[Head of Marketing, Content Manager]'
inputs:
- request — What to produce
outputs:
- yt-content-pipeline (markdown)
- '{company.marketing}/content-pipeline/YYYY-MM-DD-{slug}.md'
prompts:
- Run the full YouTube content pipeline with these competitor URLs as sources
- Find topic ideas for my channel using the existing NotebookLM notebook
- Write a video script for the topic 'How I Grew 10K Subscribers in 90 Days'
- Generate thumbnail title options for my chosen topic
- Create AI image prompts for the visual scenes in my next video
---
