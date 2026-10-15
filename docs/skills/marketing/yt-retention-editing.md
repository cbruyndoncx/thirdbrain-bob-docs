---
description: Build editing plans and review existing videos through the lens of viewer retention. Editing is not about making videos look nice -- it is about keeping viewers watching. Every cut, text overlay, zoom, and B-roll insert is a retention decision. A well-edited video can double average view duration without changing any content.
title: yt-retention-editing
---

# yt-retention-editing

Build editing plans and review existing videos through the lens of viewer retention. Editing is not about making videos look nice -- it is about keeping viewers watching. Every cut, text overlay, zoom, and B-roll insert is a retention decision. A well-edited video can double average view duration without changing any content.

- **Area:** Marketing
- **Category:** content
- **Level:** beginner
- **Input:** conversation
- **Output:** document
- **Setup:** none
- **Roles:** Content Manager

Create retention-focused editing plans and review existing videos for pacing, pattern interrupts, and re-hook placement.

## How you ask

- “Editing plan”
- “Edit for retention”
- “Pattern interrupts”

## Inputs

- youtube_context — Channel niche, audience, positioning and format. Optional — the route collects minimum context from the user when absent.
- script_or_outline — Existing script from yt-script-structure (preferred) or rough outline
- video_title — Video title for context and hook alignment
- format — Talking head, screen share, hybrid, B-roll heavy (talking-head | screen-share | hybrid | b-roll-heavy)
- target_length — Target video length (default 8-12 min)
- editor_context — self-edit or external-editor (changes detail level) (self-edit | external-editor)
- video_url_or_file — YouTube URL, local video file path, or transcript/description of the video
- retention_data — Retention curve description or analytics data (front-loaded drop, steady decline, mid-video cliff, etc.)
- current_editing_style — Current editing approach (jump cuts, smooth transitions, minimal, heavy effects)

## Outputs

- Retention diagnosis with specific timestamp recommendations and priority fixes
- Timestamp-based edit list with pacing, pattern interrupts, music direction, text overlays, and B-roll needs
- {company.marketing}/video/editing/{video-slug}_editing_plan_{YYYY-MM-DD}.md
- {company.marketing}/video/editing/{video-slug}_editing_review_{YYYY-MM-DD}.md

