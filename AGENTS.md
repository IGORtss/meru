# Meru Development Rules

## Source of truth
Read the relevant documentation under `docs/` before implementation. Do not invent architectural behavior.

## Non-negotiable principles
1. AI is a citizen of the system, not its owner.
2. Persistent does not mean continuously inferencing.
3. Prefer structured APIs over visual automation.
4. Security is enforced outside the LLM.
5. Use least privilege and scoped capabilities.
6. Significant actions are auditable.
7. Mutating actions should be reversible when practical.
8. The core must not require a paid cloud provider.
9. Never bypass the Policy Engine.
10. Agents never receive unrestricted host access.
11. Never silently expand Task scope.
12. Every implementation requires tests.

## V0 boundaries
Implement only the vertical slice required for a Developer Agent to repair a failing project inside an authorized workspace.

## Coding rules
- Typed Python.
- Pydantic for domain schemas.
- Business logic independent from CLI/UI.
- LLMs behind a provider interface.
- Policy decisions deterministic.
- Tools declare capabilities and risk.
- Unit tests do not require internet.
