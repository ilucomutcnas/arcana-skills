## Purpose

These instructions exist to solve a recurring failure pattern in large skill ecosystems.

When skills are stored as isolated, flat, or weakly connected files, agents tend to fail in predictable ways: they load too much irrelevant material, miss adjacent knowledge that should have been used, rely on broken or stale links, produce inconsistent outputs across related files, and treat real-world tasks as if each capability exists in isolation.

This system was designed to fix those problems.

Domain packages, routers, mini-skills, references, examples, manifests, and linked support files exist to make large skill ecosystems usable, scalable, and reliable. The goal is not to store knowledge as a monolith, and not to split everything into disconnected fragments. The goal is to create a routed domain system: one that stays lightweight at the entry point, loads only what is relevant for the current task, preserves cross-skill connectivity, and remains structurally coherent as the ecosystem grows.

These instructions define how to build, maintain, validate, and improve that system.

The operating objective is to preserve five things at the same time:
- routing efficiency,
- structural integrity,
- cross-file consistency,
- selective loading,
- real-world task usefulness.

In short: this system exists because real work does not happen in a vacuum, and large skill ecosystems fail when structure, linkage, and domain relationships are not maintained deliberately.
