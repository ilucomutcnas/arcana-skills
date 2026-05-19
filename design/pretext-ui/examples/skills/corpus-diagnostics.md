# corpus-diagnostics Example

## Scenario: multilingual editorial corpus sweep at 480/640/768

A maintainer validates a new inline-flow adjustment by sweeping representative corpora across three widths before release signoff.

## Corpus Matrix
| Corpus | Script profile | 480px result | 640px result | 768px result |
|---|---|---|---|---|
| `corpora/ar-al-bukhala.txt` | Arabic RTL, punctuation-heavy | 2 high-severity wrap drifts | 1 medium drift | stable |
| `corpora/ja-rashomon.txt` | Japanese CJK dense lines | stable | 1 low spacing drift | stable |
| `corpora/en-gatsby-opening.txt` | English prose | stable | stable | stable |
| `corpora/mixed-app-text.txt` | Mixed RTL/LTR + UI tokens | 1 high bidi boundary drift | 1 medium wrap drift | stable |

## Mismatch Taxonomy
| Category | Symptom | Likely layer | Severity | Action |
|---|---|---|---|---|
| Wrap threshold drift | Break moves one token earlier/later | measurement + line-break boundary | High | Block until fixed and re-swept |
| Bidi boundary inversion | Inline English token appears in wrong visual run | bidi/inline-flow metadata | High | Escalate to architecture review |
| CJK spacing wobble | Minor spacing variance with same breakpoints | measurement rounding | Low | Track; accept with note if non-regressive |
| Punctuation carryover | Closing punctuation orphaned to next line | line-break candidate ranking | Medium | Fix ranking, rerun canaries |

## Canary Decision Table
| Decision | When used | Current call |
|---|---|---|
| Keep | Canary still detects meaningful regressions and has stable baseline | `en-gatsby-opening` |
| Replace | Corpus no longer reflects active script/layout risks | none |
| Split | Single canary hides two distinct failure modes | `mixed-app-text` split into bidi-focused and wrap-focused subsets |
| Remove | Corpus is redundant/noise after newer representative additions | none |

## Follow-up Actions
- **Layout maintainer**: fix punctuation carryover in line-break ranking; rationale: medium severity appears at two widths.
- **Browser accuracy owner**: cross-check Arabic + mixed corpora in Chromium/Firefox/WebKit to confirm drift scope.
- **Roadmap owner**: schedule split of `mixed-app-text` canary into two tracked probes for clearer regression ownership.

## Acceptance Criteria
- Canary decision is explicit and justified (not implied).
- Script-sensitive mismatches remain separated by taxonomy; no “one generic mismatch” flattening.
- Browser sweep artifacts and corpus sweep artifacts are cross-linked in the review notes.
