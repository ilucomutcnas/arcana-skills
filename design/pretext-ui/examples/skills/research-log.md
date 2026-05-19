# research-log Example

## Scenario: revisit shaping-heavy experiment

Historic experiment proposed aggressive glyph-cluster caching for Arabic and Thai shaping. Current maintainer must decide whether to revive or keep rejected after new evidence.

## Old Hypothesis vs Current Evidence
- **Old hypothesis:** persistent cluster cache would cut runtime by 20% with no layout drift.
- **Current evidence:** modest speedups in narrow cases, but repeated cache invalidation bugs under width sweeps and mixed fallback fonts.

## Rejected Path (Why it failed)
- Cache keys omitted fallback font chain, causing stale width reuse.
- Bidi boundary transitions invalidated cluster assumptions.
- Maintenance overhead exceeded measured benefit after fixing correctness bugs.

## Durable Conclusion
Pretext should prefer deterministic per-layout shaping with bounded local memoization, not broad persistent caches spanning heterogeneous script contexts.

## Decision Table
| Option | Evidence quality | Risk | Recommendation |
|---|---|---|---|
| Revive persistent cache | Medium (stale, partial) | High correctness risk | Reject |
| Local memoization only | High (current tests/corpora) | Low | Accept |
| Hybrid with feature flag | Low (untested rollout plan) | Medium | Hold |

## Recommendation
Keep the prior rejection for persistent cache architecture. Adopt targeted local memoization in layout hot paths and cite this decision in any future proposal touching script-sensitive shaping.
