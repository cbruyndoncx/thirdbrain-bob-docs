---
description: Take one piece of content and transform it into structured outputs for different formats and channels.
title: content-repurposer
---

# content-repurposer

Take one piece of content and transform it into structured outputs for different formats and channels.

- **Area:** Marketing
- **Category:** marketing content
- **Level:** beginner
- **Input:** conversation
- **Output:** document
- **Setup:** none
- **Roles:** Head of Marketing, Content Manager

Reformat existing content into new assets — case studies, FAQs, podcast show notes, testimonial variants, quote cards, subject lines, MP4 video cuts, and repurposing…

## How you ask

- “Turn this client interview transcript into a case study”
- “Generate an FAQ from this product documentation”
- “Create show notes for this podcast episode transcript”
- “Format these customer testimonials into short and social variants”
- “Pull the best quotes from this article for quote cards”
- “Give me subject line ideas for this newsletter”
- “Cut this webinar recording into 30-60 second shorts”
- “What else can I make from this blog post? Give me a repurposing matrix”

## Inputs

- source-content — Project summary, client testimonial, or results data the case study is built from.
- tone-of-voice — Brand voice preserved across repurposed formats; stamped into the output as `brand_voice_source`.
- profile — Company or client profile — entity and relationship context.
- output-breadth — Whether this is the only deliverable from the source or one of several. `multi-format` triggers the format-priority ordering step before transforming; `single-format` skips it. (single-format | multi-format)
- request — What to produce, including any angle, length, or audience already fixed by the caller.
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set
- source-content — Product docs, support logs, or service pages the questions are mined from.
- source-content — Episode transcript or recording notes, ideally with timings, for the episode being written up.
- source-content — Raw feedback, survey responses, or emails containing the praise being formatted.
- source-content — Long-form content — article, transcript, or report — the quotes are pulled from.
- source-content — Email body or campaign brief the subject lines must accurately represent.
- source-content — The source asset being planned around — the article, talk, or report that will feed several channels.
- target-channels — Channels the plan must cover. Absent, the route proposes the channel set and says why each earned a slot.
- video_path — Path to source MP4/MOV on local filesystem
- words_json — Word-level timestamps from social_transcript.py --word-timestamps (improves caption sync)
- count — Number of clips to generate
- min_secs — Shortest clip the segment selection may produce, in seconds.
- max_secs — Longest clip the segment selection may produce, in seconds.
- banner_png — Brand banner PNG overlaid at top of vertical frame

## Outputs

- Case study in challenge / solution / results / takeaway structure, with every figure traceable to the source.
- Clip index with timestamps, durations, titles, and next steps; publishing copy comes from yt-title-craft and yt-description-seo.
- Episode summary, timestamped sections, verbatim quotes, and the linked resources mentioned in the episode.
- Full, short, one-line, and social variants of each testimonial with the original speaker attribution preserved exactly.
- Grouped questions with concise answers, each answer grounded in the source rather than inferred.
- Prioritised multi-format plan naming each derived asset, its channel, its effort, and why it ranks where it does.
- Ranked pull quotes, each verbatim, with the context line that makes it readable out of its source.
- Rendered vertical shorts, one per selected segment, with word-by-word captions burned in.
- Subject line options grouped by category, each with preview text and none overstating the email body.
- prefer a permanent directory)
- {scope.marketing}/content/case_study_{client-or-topic}.md
- {scope.marketing}/content/faq_{topic}.md
- {scope.marketing}/content/quotes_{source}.md
- {scope.marketing}/content/repurposing_matrix_{source}.md
- {scope.marketing}/content/show_notes_{episode}.md
- {scope.marketing}/content/subject_lines_{campaign}.md
- {scope.marketing}/content/testimonials_{client}.md

## Seen in these workflows

- [One great piece of content.](../../workflows/marketing/content-repurposer.md)

