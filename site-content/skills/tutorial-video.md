---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: tutorial-video — ThirdBrain BOB skill
  description: Generate professional narrated tutorial videos from markdown scripts. Converts scene-based scripts into Remotion (React) compositions with corporate motion grap
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: tutorial-video
catLabel: video
area: marketing
desc: Generate narrated animated tutorial videos from markdown scripts using Remotion and Edge TTS.
summary: Generate professional narrated tutorial videos from markdown scripts. Converts scene-based scripts into Remotion (React) compositions with corporate motion graphics, generates voiceover via Edge TTS, and renders to MP4.
difficulty: advanced
inputType: conversation
outputType: video-script
requires: '[install]'
roles: '[Content Manager]'
inputs:
- script-path — Path to markdown video script with scene definitions
- output-dir — Output directory (defaults to scratch, `output.scratch`, subfolder tutorial-video-{date})
- script-path — Path to markdown video script
- 'voice — Edge TTS voice ID (default: en-US-AndrewNeural)'
- project-dir — Path to existing Remotion project directory
- angles_path — Path to angles markdown under the resource root (`resource.root`, subfolder research/kb/ai-news-daily/YYYY-MM-DD-angles.md) or raw research-kb entry
- 'date — Date label for output naming (default: today YYYY-MM-DD)'
- 'voice — Edge TTS voice (default: en-US-GuyNeural — news-like style)'
outputs:
- audio-files (markdown)
- prefer a permanent directory)
- remotion-project (markdown)
- script (markdown)
- video (mp4)
- '{output-dir}/'
- '{output-dir}/out/{name}.mp4'
- '{output-dir}/public/voiceover/'
- '{project-dir}/out/{name}.mp4'
prompts:
- Create a tutorial video from this script
- Generate a narrated training video for the team
- Build an animated explainer video with voiceover
- Re-render the tutorial video with updated narration
---
