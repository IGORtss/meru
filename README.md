# Meru

Meru is an AI-native Linux environment for developers.

The V0 is deliberately narrow:

`User → Orchestrator → Task → Developer Agent → Policy Engine → Tool → Sandbox → Validation → Action Log`

Its first real acceptance scenario is: **analyze an authorized workspace and fix a failing test without escaping that workspace**.

## V0 stack

- Arch Linux + Hyprland
- Python 3.12+
- uv
- SQLite
- Pydantic
- Typer + Rich
- Ollama-compatible local LLM provider
- Bubblewrap sandbox
- pytest + Ruff

Read `AGENTS.md` and `docs/PROJECT_SPECIFICATION.md` before architectural changes.
