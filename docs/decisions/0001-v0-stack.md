# ADR-0001: V0 implementation stack

Status: accepted.

Use Python 3.12+ and uv for the first vertical slice, SQLite for persistence, Pydantic for domain contracts, Typer/Rich for the temporary CLI, Bubblewrap for process/filesystem isolation, an Ollama-compatible provider for local inference, pytest for tests and Ruff/Pyright for static quality checks.

This is a V0 implementation decision, not a requirement that every future Meru component remain Python.
