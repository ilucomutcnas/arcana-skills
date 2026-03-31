---
name: "fixing-metadata"
title: "Fixing Metadata"
description: "Use for auditing and fixing page metadata including titles, descriptions, canonical URLs, Open Graph tags, Twitter cards, favicons, structured data, and locale settings."
risk: "safe"
source: "https://github.com/ilucomutcnas/arcana-skills"
date_added: "30.03.2026"
---

## Package Structure

- Main router: `SKILL.md`
- This reference: `references/skills/fixing-metadata.md`
- Examples: `examples/skills/fixing-metadata.md`

## Linked Package Files

- Adjacent: `references/skills/fixing-accessibility.md` — for accessibility-related metadata (lang, aria)
- Validation: `references/skills/ui-visual-validator.md` — for verifying social card rendering

## Purpose

Identify pages with missing or incorrect metadata and fix them. Covers titles, descriptions, canonical URLs, Open Graph tags, Twitter cards, favicons, app icons, manifest, theme-color, structured data (JSON-LD), locale settings, and alternate language links.

## When to Use

- When adding or changing page titles, descriptions, canonical URLs, robots directives
- When implementing Open Graph or Twitter card metadata
- When setting favicons, app icons, manifest, theme-color
- When building shared SEO components or layout metadata defaults
- When adding structured data (JSON-LD)
- When changing locale, alternate languages, or canonical routing
- When shipping new pages, marketing pages, or shareable links

## Workflow

1. Identify pages with missing or incorrect metadata (titles, descriptions, canonical, OG tags).
2. Audit against priority rules — fix critical issues (duplicates, indexing) first.
3. Ensure title, description, canonical, and og:url all agree with each other.
4. Verify social cards render correctly on a real URL, not localhost.
5. Keep diffs minimal and scoped to metadata only — do not refactor unrelated code.

## Quality Standards

- Every page must have a unique, descriptive title (50-60 characters).
- Every page must have a meta description that matches the content (150-160 characters).
- Canonical URL must resolve to the correct page.
- Open Graph and Twitter card metadata must be consistent with page title and description.
- The lang attribute must be set on the HTML element.
- Structured data must validate against schema.org.

## Technical Rules

- og:url must match canonical URL.
- og:image must be at least 1200x630 pixels for optimal sharing.
- Twitter card type: summary_large_image for pages with hero images, summary otherwise.
- JSON-LD structured data must validate with Google Rich Results Test.
- Do not use identical titles or descriptions across multiple pages.

## Validation

- Verify all required metadata tags are present.
- Check consistency between title, description, canonical, and og:url.
- Validate social cards with Facebook Sharing Debugger and Twitter Card Validator.
- Validate structured data with Google Rich Results Test.

## Restrictions

- Do not refactor unrelated code when fixing metadata.
- Do not test social card rendering on localhost.

## Output Requirements

- Report each missing or incorrect metadata element.
- Provide the corrected metadata tag.
- Keep changes scoped to metadata only.
