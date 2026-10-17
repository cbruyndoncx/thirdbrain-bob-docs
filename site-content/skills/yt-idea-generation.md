---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: yt-idea-generation — ThirdBrain BOB skill
  description: Systematic video idea brainstorming and scoring. The idea is 80% of a video's success -- a great idea with mediocre execution outperforms a mediocre idea with g
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: yt-idea-generation
catLabel: content
area: marketing
desc: Brainstorm and score YouTube video ideas.
summary: Systematic video idea brainstorming and scoring. The idea is 80% of a video's success -- a great idea with mediocre execution outperforms a mediocre idea with great execution every time. This skill makes ideation data-informed and ruthlessly filtered instead of random.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[Content Manager]'
inputs:
- session_goal — What the user wants from this session — batch brainstorm, score existing ideas, fill a pillar gap, or respond to a trend
- pillars — Which content pillars to target — defaults to all pillars from youtube_context.md
- recent_performers — Top 3 recent videos by views or retention — tells us what the audience actually wants
- trending_topics — Current trends, news, or events to leverage
- idea_count — How many raw ideas to generate — defaults to 15
- kb_entry — Path to today's research-kb snapshot (`resource.root`, `research/kb/ai-news-daily/ai-news-daily_kb_YYYY-MM-DD.md`); `ai-news-daily_kb_latest.md` holds the latest completed cycle
- channel_context — youtube_context.md (`company.marketing`) — used to tailor angles to the channel voice
outputs:
- Scored and prioritized video idea list with top-idea detail cards
- angles (markdown)
- '{company.marketing}/video/ideas/video_ideas_{YYYY-MM-DD}.md'
- '{resource.research-kb}/ai-news-daily/{YYYY-MM-DD}-angles.md'
prompts:
- Give me video ideas
- Brainstorm topics
- What should I make a video about
---
