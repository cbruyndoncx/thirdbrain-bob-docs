---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: social-publisher — ThirdBrain BOB skill
  description: Publish content to social media platforms. YouTube and Instagram use PEP 723 API scripts runnable with `uv run`. LinkedIn and Substack use Playwright browser au
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: social-publisher
catLabel: marketing-seo
area: marketing
desc: Publishes content to YouTube, LinkedIn, Substack, and Instagram (own Business account via the Graph API).
summary: Publish content to social media platforms. YouTube and Instagram use PEP 723 API scripts runnable with `uv run`. LinkedIn and Substack use Playwright browser automation (no API registration needed).
difficulty: expert
inputType: url
outputType: document
requires: '[config, api-key, mcp]'
roles: '[Head of Marketing, Content Manager]'
inputs:
- operator-profile — Operator profile — personal-scope publishing identity.
- profile — Company or client profile — entity and relationship context.
- video-file — Video file to upload
- channel — YouTube channel handle (e.g. @thirdbrain-bob)
- image — Source image for thumbnail
- text — Overlay text for the thumbnail
- video-id — ID of the existing video
- channel — YouTube channel handle with the @ prefix; selects the cached per-channel OAuth token
- privacy — Target privacyStatus; always passed explicitly because the script defaults to public (public | unlisted | private)
- content — Markdown file with post content and optional frontmatter (title, image, visibility)
- content — Markdown file with schedule datetime in frontmatter
- caption — Post caption/hook text (accompanies the carousel)
- carousel-pdf — Flattened/rasterized PDF deck, plain ASCII filename (render slides to PNG then reassemble into an image-only PDF — do not upload a vector-text print-to-PDF export)
- article — Markdown file with frontmatter (title, subtitle, tags, audience, status)
- content — Plain text or short markdown content for the note
- request — List posts request
- draft-title — Title of the draft to delete
- account — Instagram handle with the @ prefix; selects the stored Graph API credentials
- images — One image (--image) or 2 to 20 images (--carousel)
- caption — Caption text, or a caption file (--caption-file)
- video_path — Path to rendered MP4
- title — Video title
- description_path — Path to description .md file (from yt-description-seo)
- tags — YouTube tags
- thumbnail_path — Thumbnail PNG path
- 'quartz_vault_path — Root path of the Quartz content directory (default: read from `thirdbrain_config.json` under the resources root, `resource.root`)'
- topic_tags — Topic tags for the local video registry
outputs:
- Graph API media ID of the published post
- JPEG saved beside the source image by default; use --output to place it with the video's project assets when the source image is elsewhere.
- Published YouTube video URL
- Quartz note with the YouTube embed, dated by the video publish date. The scratch path is the fallback when no Quartz content directory is configured.
- The video's privacyStatus as returned by the API after the change
- article (markdown)
- confirmation (markdown)
- conversation
- note (markdown)
- post-list (markdown)
- prefer a permanent directory)
- registry-entry (json)
- video (video)
- '{quartz_content_path}/ai-news/{YYYY-MM-DD}.md'
- '{resource.root}/thirdbrain_videos.json'
- '{source-image-dir}/{source-image-stem}-thumbnail.jpg'
prompts:
- Set a custom thumbnail on my YouTube video
- Post this to LinkedIn
- Schedule LinkedIn post for Monday
- Publish this article to Substack
- List my Substack drafts
- Post these three images to my Instagram as a carousel
---
