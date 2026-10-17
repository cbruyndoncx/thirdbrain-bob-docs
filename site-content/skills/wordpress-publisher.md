---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: wordpress-publisher — ThirdBrain BOB skill
  description: 'Target audience: marketing operators and content publishers who own one or more WordPress sites and ship markdown from a vault or static-site source.'
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: wordpress-publisher
catLabel: marketing-seo
area: marketing
desc: Publishes WordPress posts and pages from markdown.
summary: 'Target audience: marketing operators and content publishers who own one or more WordPress sites and ship markdown from a vault or static-site source.'
difficulty: intermediate
inputType: url
outputType: document
requires: '[config]'
roles: '[Head of Marketing, Content Manager]'
inputs:
- file_path — Path to markdown file with YAML frontmatter
- env — Target environment (dev|staging|prod), default dev
- phrase — Safety confirmation phrase; required when env=prod (must be APPROVED)
- file_path — Path to markdown file already published in source env
- from_env — Source environment (dev|staging)
- to_env — Target environment (staging|prod)
- phrase — Safety confirmation phrase; required when to_env=prod (must be APPROVED)
- post_id — WordPress post ID to fetch
- site — Site domain matching a _site-config.md entry
- env — Environment (dev|staging|prod), explicitly passed as --env; no default
- folder — Path to folder containing markdown files
- file_path — Path to markdown file with wp_post_id in frontmatter
- mode — trash (recoverable) or delete (permanent), default trash
- config_path — Path to _site-config.md (or any file inside the site folder)
- env — Environment name, default dev
outputs:
- Determined by site content folder structure
- OK/FAILED message
- OK/FAILED message` — register-meta-result (text)
- deleted-post (yaml)
- environments.{env}.wp_post_id, wp_url, wp_status, last_published, external_id
- environments.{env}.wp_status (trash|deleted), sync_state (deleted)
- environments.{to_env}.wp_post_id, wp_url, wp_status
- promoted-post (yaml)
- published-post (yaml)
- pulled-post (markdown)
- succeeded/failed/skipped counts per file
- succeeded/failed/skipped counts per file` — tree-report (text)
prompts:
- Publish to WordPress
- Push to WP
- Promote to prod
---
