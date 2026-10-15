---
description: Systematic video idea brainstorming and scoring. The idea is 80% of a video's success -- a great idea with mediocre execution outperforms a mediocre idea with great execution every time. This skill makes ideation data-informed and ruthlessly filtered instead of random.
title: yt-idea-generation
---

# yt-idea-generation

Systematic video idea brainstorming and scoring. The idea is 80% of a video's success -- a great idea with mediocre execution outperforms a mediocre idea with great execution every time. This skill makes ideation data-informed and ruthlessly filtered instead of random.

- **Area:** Marketing
- **Category:** content
- **Level:** beginner
- **Input:** conversation
- **Output:** document
- **Setup:** none
- **Roles:** Content Manager

Brainstorm and score YouTube video ideas.

## How you ask

- “Give me video ideas”
- “Brainstorm topics”
- “What should I make a video about”

## Inputs

- session_goal — What the user wants from this session — batch brainstorm, score existing ideas, fill a pillar gap, or respond to a trend
- pillars — Which content pillars to target — defaults to all pillars from youtube_context.md
- recent_performers — Top 3 recent videos by views or retention — tells us what the audience actually wants
- trending_topics — Current trends, news, or events to leverage
- idea_count — How many raw ideas to generate — defaults to 15
- kb_entry — Path to today's research-kb snapshot (`resource.root`, `research/kb/ai-news-daily/ai-news-daily_kb_YYYY-MM-DD.md`); `ai-news-daily_kb_latest.md` holds the latest completed cycle
- channel_context — youtube_context.md (`company.marketing`) — used to tailor angles to the channel voice

## Outputs

- Scored and prioritized video idea list with top-idea detail cards
- angles (markdown)
- {company.marketing}/video/ideas/video_ideas_{YYYY-MM-DD}.md
- {resource.research-kb}/ai-news-daily/{YYYY-MM-DD}-angles.md

