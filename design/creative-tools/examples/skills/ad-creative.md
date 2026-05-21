# Ad Creative — Examples

## Angle-Based Output with Character Counts

```
## Angle: Pain Point — Manual Reporting

### Headlines (30 char max)
1. "Stop Building Reports by Hand" (29)
2. "Automate Your Weekly Reports" (28)
3. "Reports in 5 Min, Not 5 Hrs" (27)

### Descriptions (90 char max)
1. "Marketing teams save 10+ hours/week with automated reporting. Start free." (73)
2. "Connect your data sources once. Get automated reports forever. No code required." (80)
```

## Iteration Log Template

```
## Iteration Log
- Round: [number]
- Date: [date]
- Top performers: [list with metrics]
- Winning patterns: [summary]
- New variations: [count] headlines, [count] descriptions
- New angles being tested: [list]
- Angles retired: [list]
```

## Bulk CSV Output

```csv
headline,description
"Stop Building Reports",Marketing teams save 10+ hours/week. Start free.
"Automate Weekly Reports",Connect data sources once. Automated reports forever.
```

## Performance Iteration Workflow

```
Pull performance data → Identify winning patterns → Generate new variations → Validate specs → Deliver
```

## Platform Quick Reference

| Platform | Headline Max | Description Max |
|----------|-------------|----------------|
| Google RSA | 30 chars | 90 chars |
| Meta Ads | 40 chars | 125 chars (recommended) |
| LinkedIn | 70 chars | 100 chars |
| TikTok | — | 100 chars (recommended) |
| Twitter/X | — | 280 chars |

For full platform specs, see `ad-creative__references/platform-specs.md`.
For AI+Remotion visual workflows, see `ad-creative__references/generative-tools.md`.

## Stage 3.8 Example: Campaign Revision Loop and Release Evidence

### Campaign Context
- Campaign: Spring analytics launch for SMB ecommerce teams.
- Channels: Google RSA, Meta feed, LinkedIn sponsored content.
- Conversion action: book a demo.

### Variant QA Table
| ID | Platform | Headline | Body/Description | Counts | Claim + Disclaimer Status |
|---|---|---|---|---|---|
| G-01 | Google RSA | Cut Reporting Time 60% | Automate weekly reports in one dashboard. | H 22 / D 47 | Claim cited to case-study-v2, disclaimer N/A |
| G-02 | Google RSA | CPA Down 35% in 14 Days | See paid-social performance fixes fast. | H 22 / D 43 | Rejected: no source for 35% claim |
| M-01 | Meta | Stop Manual Reports | Connect ads + store data, get daily insights. | H 19 / B 46 | Pass with footnote in landing page |
| L-01 | LinkedIn | Revenue Clarity for Ecommerce Teams | Replace spreadsheet reporting with shared dashboards. | H 35 / D 54 | Pass |

### Rejection Reasons
| Variant | Severity | Reason | Owner | Fix |
|---|---|---|---|---|
| G-02 | Blocker | Unsubstantiated percentage claim | Growth copywriter | Replace with cited result from approved case study |
| M-03 | Major | Body exceeded recommended length after legal text | Paid social manager | Split disclaimer to destination page + update CTA |
| L-04 | Minor | Duplicates angle already in L-01 | Creative strategist | Swap to urgency angle with unique hook |

### Approved Final Copy
| Platform | Final Headline | Final Body | Evidence |
|---|---|---|---|
| Google RSA | Cut Reporting Time 60% | Automate weekly reporting and share results in minutes. | Character report + case-study citation |
| Meta | Stop Manual Reports | Connect ad and store data for daily decision-ready insights. | Meta char check + compliance note |
| LinkedIn | Revenue Clarity for Ecommerce Teams | Replace spreadsheet reporting with one stakeholder-ready dashboard. | LinkedIn char check + legal signoff |

### Evidence-Pack Checklist
- [x] Character-limit export for all approved variants.
- [x] Claim substantiation links and legal reviewer initials.
- [x] Rejection log with blocker/major/minor status.
- [x] Final approved variants CSV and upload-ready mapping.
- [x] Performance learning memo for next iteration round.

### Handoff Note
Send approved tables, rejection log, and citations to `creative-qa-gate-automation` for final campaign go/no-go gate before package delivery.
