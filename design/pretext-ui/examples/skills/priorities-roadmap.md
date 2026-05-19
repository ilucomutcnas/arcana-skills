# priorities-roadmap Example

## Scenario: triage competing maintenance tasks

Incoming work queue:
1. Browser wrap mismatch on Arabic canary.
2. Optional API cleanup for layout metadata naming.
3. Performance regression alert from mixed-script benchmark.
4. New demo polish request.

## Priority Matrix
| Task | User impact | Regression risk | Dependency weight | Priority |
|---|---|---|---|---|
| Arabic browser mismatch | High | High | Blocks release confidence | P0 |
| Mixed-script perf regression | High | High | Affects canary trust | P0 |
| API naming cleanup | Medium | Medium | Requires migration notes | P1 |
| Demo polish | Low | Low | No release gate impact | P3 |

## Not-Now Decisions
- Defer demo polish until mismatch/perf gates are green.
- Defer API cleanup until current release candidate closes; keep note linked to migration plan.

## Selected Roadmap Order
1. Fix Arabic browser mismatch with corpus + browser evidence.
2. Remove perf regression to <=3% threshold.
3. Schedule API cleanup behind architecture-review with migration analysis.
4. Revisit demo polish after release branch stabilization.

## Communication Note
Post roadmap update in contributor channel with rationale: “Release quality gates (accuracy + performance) take precedence over aesthetic/demo improvements; API cleanup remains planned with migration-safe window.”
