# Content Creator — Examples

## Brand Voice Setup

```bash
# Analyze existing content for voice baseline
python content-creator__scripts/brand_voice_analyzer.py content.txt

# Output includes: voice profile, readability score, sentence analysis, recommendations
```

## SEO Blog Post Optimization

```bash
# Optimize article for SEO
python content-creator__scripts/seo_optimizer.py article.md "main keyword"

# Output includes: SEO score (0-100), keyword density, structure assessment, meta suggestions
```

## Content Calendar Quick Start

```bash
# Copy the template for this month
cp content-creator__assets/content_calendar_template.md this_month.md
```

## Content Pillar Ratio

Follow the 40/25/25/10 distribution:
- 40% — educational content
- 25% — engagement content
- 25% — promotional content
- 10% — community content

## Reference Guide Routing

| Need | Reference File |
|------|---------------|
| Brand voice setup | `content-creator__references/brand_guidelines.md` |
| Blog/article templates | `content-creator__references/content_frameworks.md` |
| Platform-specific rules | `content-creator__references/social_media_optimization.md` |

## Content Creation Process

1. Start with audience need/pain point
2. Research keywords
3. Create outline using templates
4. Write first draft without editing
5. Optimize for SEO
6. Edit for brand voice
7. Proofread and fact-check
8. Optimize for platform
9. Schedule strategically

## Stage 3.8 Example: Editorial Launch Package

### Deliverables
| Asset | Channel | Owner | Status | Publish dependency |
|---|---|---|---|---|
| 1,800-word blog post | Website | Content lead | Approved | Must publish first for canonical URL |
| Thought-leadership post | LinkedIn | Social editor | Approved | Uses blog URL + hero takeaway |
| 7-post thread | X/Twitter | Social editor | Approved with edits | Needs shortened claim language |
| Newsletter teaser | Email | Lifecycle marketer | Approved | Must reference final blog headline |

### Brand Voice and Tone Checklist
- [x] Authoritative but practical (no hype claims).
- [x] Uses customer-first framing before feature details.
- [x] Maintains consistent terminology across all channels.
- [x] CTA tone aligned with brand guidelines.

### SEO / Factual / Source Validation
| Check | Result | Evidence |
|---|---|---|
| Primary keyword placement | Pass | H1, intro paragraph, conclusion |
| SEO score | Pass (82/100) | `seo_optimizer.py` report export |
| External data citations | Pass | 3 source links in blog references |
| Product claims | Pass | PM-reviewed fact sheet v4 |
| Internal links | Pass | 5 links to product docs and case study |

### Revision Log
| Round | Change | Reason | Owner | Outcome |
|---|---|---|---|---|
| R1 | Removed “guaranteed growth” language | Compliance risk | Content lead | Approved |
| R2 | Tightened X thread post 4 | Character overflow | Social editor | Approved |
| R3 | Updated newsletter teaser CTA | Mismatch with final blog title | Lifecycle marketer | Approved |

### Stakeholder Signoff Matrix
| Role | Decision | Date | Notes |
|---|---|---|---|
| Content lead | Approve | 2026-05-20 | Final editorial quality confirmed |
| Product marketing | Approve | 2026-05-20 | Messaging aligned to launch brief |
| Legal/compliance | Approve | 2026-05-20 | Claims and disclaimers cleared |
| Social channel owner | Approve | 2026-05-21 | Platform variants validated |

### Publishing Calendar Dependency Note
Schedule lock order: blog publication -> LinkedIn post (T+1h) -> X thread (T+3h) -> newsletter teaser (next morning). If the blog URL or headline changes, reopen QA and refresh all downstream copy links before release.
