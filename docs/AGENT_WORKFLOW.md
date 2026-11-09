# Development workflow
Adapted from Cuebooker's agent workflow.

1. Discovery: inspect AGENTS.md, HANDOFF, live tree, current branch and exact requirements.
2. Product scope and visual acceptance criteria recorded before major work.
3. Impact/architecture analysis; ADR for a structural deviation.
4. Small reviewable change on feature branch with tests.
5. Validation: npm ci, typecheck, tests, generate; browser/mobile/keyboard screenshots before visual acceptance.
6. Handoff: update docs/HANDOFF.md with proven status and limitations.
7. Draft PR reviewed before merge; production/DNS must never change without separate approval.

No invented completed tasks, no unverified deployment claims, no unauthorized production changes. Use the simplest technical boundary needed. Keep design reference and implementation distinct.
