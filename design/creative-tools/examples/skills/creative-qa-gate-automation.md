# Creative QA Gate Automation — Example

## Scenario
Cross-channel spring campaign includes ad copy, social posts, product images, icon SVG set, partner PDF one-pager, and final handoff package.

## Deliverable Matrix
| Deliverable | Owner | Auto checks | Manual checks | Gate |
|---|---|---|---|---|
| Ad variants | Growth | character limits, naming | claims, legal disclaimer | Pass |
| Blog + LinkedIn + X thread + teaser | Content | SEO score, link checks | tone/factual review | Pass |
| Product images | Design | dimensions, size, metadata | visual realism/crop safety | Pass after loop |
| SVG icons | Design systems | viewBox/stroke/name checks | accessibility labels | Pass |
| PDF one-pager/form | Ops | page/fields/bounding-box scripts | disclaimer/readability | Pass |
| Handoff package | Creative ops | manifest/path lint | owner/status audit | Pass |

## Severity Table
- Blocker: Missing legal disclaimer on paid claim variant.
- Major: One marketplace image exceeded max file size.
- Minor: CTA punctuation inconsistency in one social teaser.

## Revision Loop Log
1. Blocker assigned to ad-creative owner; disclaimer added; legal re-approved.
2. Major assigned to raster owner; recompressed export and revalidated.
3. Minor assigned to content owner; copy standardized.

## Stakeholder Signoff Matrix
| Role | Status | Evidence |
|---|---|---|
| Creative lead | Approved | QA summary v3 |
| Channel owners | Approved | Channel gate sheets |
| Legal/compliance | Approved | Claim substantiation + disclaimer check |
| Release ops | Approved | Final evidence pack + manifest |

## Release Decision
Go: all blockers closed, majors resolved, signoff complete.

## Final Evidence Pack Summary
Attached: validation matrix, issue log, revision history, signoff sheet, release manifest, rollback note.
