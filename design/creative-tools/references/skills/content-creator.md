---
name: "content-creator"
title: "Content Creator"
description: "Use for creating brand-consistent content with voice analysis, SEO-optimized blog posts, platform-specific social media content, and content calendar planning."
risk: "safe"
source: "https://github.com/ilucomutcnas/arcana-skills"
date_added: "30.03.2026"
---

## Package Structure

- Main router: `SKILL.md`
- This reference: `references/skills/content-creator.md`
- Examples: `examples/skills/content-creator.md`
- Brand guidelines: `content-creator__references/brand_guidelines.md`
- Content frameworks: `content-creator__references/content_frameworks.md`
- Social media optimization: `content-creator__references/social_media_optimization.md`
- Calendar template: `content-creator__assets/content_calendar_template.md`
- Scripts: `content-creator__scripts/brand_voice_analyzer.py`, `content-creator__scripts/seo_optimizer.py`

## Linked Package Files

- Adjacent: `references/skills/ad-creative.md` — for promotion copy of content pieces
- Adjacent: `references/skills/pdf-processing.md` — for branded PDF deliverables
- Validation: `content-creator__scripts/seo_optimizer.py` — for SEO scoring

## Purpose

Professional-grade brand voice analysis, SEO optimization, and platform-specific content creation. Covers establishing brand voice, writing SEO-optimized blog posts, creating social media content per platform, and planning content calendars.

## When to Use

- When writing blog posts or articles with SEO optimization
- When creating social media content for specific platforms
- When establishing or maintaining brand voice consistency
- When planning content calendars with pillar ratios
- When analyzing existing content for voice characteristics

## Workflow

### Brand Voice Setup (First Time)
1. Run `content-creator__scripts/brand_voice_analyzer.py` on existing content to establish baseline.
2. Review `content-creator__references/brand_guidelines.md` to select voice attributes and archetypes.
3. Define primary and secondary personality archetypes, choose 3-5 tone attributes.
4. Write 3 sample pieces, test consistency with the analyzer, refine.

### SEO Blog Posts
1. Research keywords: primary (500-5000 monthly searches), 3-5 secondary, 10-15 LSI.
2. Choose template from `content-creator__references/content_frameworks.md`.
3. Write 1,500-2,500 words following template structure.
4. Run `content-creator__scripts/seo_optimizer.py blog_post.md "primary keyword"`.
5. Adjust keyword density to 1-3%, ensure heading structure, add links, optimize meta description.

### Social Media Content
1. Identify platforms based on audience. Review `content-creator__references/social_media_optimization.md`.
2. Use repurposing matrix from `content-creator__references/content_frameworks.md`.
3. Adapt content per platform: length, hashtags, image dimensions, engagement elements.
4. Schedule using `content-creator__assets/content_calendar_template.md`.

### Content Calendar
1. Copy calendar template. Set monthly goals and KPIs.
2. Follow 40/25/25/10 content pillar ratio.
3. Balance platforms throughout the week aligned with optimal posting times.
4. Batch create all weekly content in one session.

## Quality Standards

- SEO score above 75/100.
- Readability appropriate for target audience.
- Consistent brand voice throughout.
- Clear value proposition and actionable takeaways.
- Platform-optimized formatting.

## Technical Rules

- Brand voice analyzer: `python content-creator__scripts/brand_voice_analyzer.py <file> [json|text]`
- SEO optimizer: `python content-creator__scripts/seo_optimizer.py <file> [primary_keyword] [secondary_keywords]`
- Content frameworks reference covers: blog post templates, social templates, repurposing matrix, email templates.
- Social media reference covers: platform specs, hashtag strategy, algorithm factors, analytics.

## Validation

- SEO optimizer score above 75.
- Brand voice consistency confirmed.
- Platform-specific requirements met.
- CTAs present and clear.

## Restrictions

- Do not write before researching keywords.
- Do not ignore platform-specific requirements.
- Do not over-optimize for SEO (keyword stuffing).
- Do not publish without proofreading.

## Output Requirements

- Content pieces optimized for target platform.
- SEO score and recommendations when applicable.
- Brand voice consistency assessment.
