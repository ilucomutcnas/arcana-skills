# benchmarks-profiling Example

## Scenario: layout runtime regression (+18%) on mixed-script corpus

After a change to line-break candidate generation, benchmark runs on `mixed-app-text.txt` and Arabic/Japanese samples show a runtime increase from baseline.

## Benchmark Results
| Corpus / Width | Baseline (ms) | Candidate (ms) | Delta |
|---|---:|---:|---:|
| mixed-app-text @ 640 | 84 | 99 | +17.9% |
| ar-al-bukhala @ 640 | 102 | 120 | +17.6% |
| ja-rashomon @ 640 | 76 | 88 | +15.8% |

## CPU Profile Notes
- Hot path moved from `measurement.measureTokenSpan` to repeated `line-break.enumerateCandidates` calls.
- Candidate path executes extra fallback branch per token even when script bucket is unchanged.
- `prepare` cost unchanged; regression is isolated to `layout` candidate loop.

## Allocation + Retained Memory Interpretation
- Allocation churn: +22% short-lived arrays per paragraph from candidate fan-out.
- Retained memory: flat (no leak signature), indicating performance issue is compute/churn, not retention.
- Decision: optimize branch pruning and reuse candidate buffers before considering structural rewrite.

## Remediation Plan
1. Gate fallback branch on script-bucket change.
2. Reuse candidate scratch arrays across line attempts.
3. Re-run targeted benchmark suite and corpus canaries.

## Acceptance Threshold
- Regression budget: **must be <= 3%** vs baseline on mixed-script suite.
- Any remaining >3% requires architecture-review sign-off with explicit tradeoff rationale.
