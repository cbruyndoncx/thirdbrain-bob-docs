---
description: 'Target audience: marketing operators and content publishers who own one or more WordPress sites and ship markdown from a vault or static-site source.'
title: wordpress-publisher
---

# wordpress-publisher

Target audience: marketing operators and content publishers who own one or more WordPress sites and ship markdown from a vault or static-site source.

- **Area:** Marketing
- **Category:** marketing seo
- **Level:** intermediate
- **Input:** url
- **Output:** document
- **Setup:** config
- **Roles:** Head of Marketing, Content Manager

Publishes WordPress posts and pages from markdown.

## How you ask

- “Publish to WordPress”
- “Push to WP”
- “Promote to prod”

## Inputs

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

## Outputs

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

