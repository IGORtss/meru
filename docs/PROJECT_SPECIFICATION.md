# Meru — V0 Project Specification

## Purpose
Meru is an AI-native Linux environment aimed primarily at developers. AI agents are native system components, but their authority is constrained by deterministic policy, scoped capabilities, sandboxing and audit logs.

## Base
Arch Linux and Hyprland.

## V0 vertical slice
User → Orchestrator → Task → Developer Agent → Policy Engine → Tool Registry → Bubblewrap Sandbox → workspace → validation → Action Log.

## V0 acceptance scenario
Given an explicitly authorized project containing a reproducible failing test, Meru creates a persistent Task, delegates it to the Developer Agent, reproduces the failure, reads only allowed resources, proposes and performs a permitted edit, reruns validation, records significant actions, and completes only after the test passes.

## Required V0 components
- Task domain model and state machine
- SQLite Task Store
- deterministic Policy Engine
- scoped capabilities
- Tool Registry
- read_file, write_file and run_tests tools
- Bubblewrap sandbox
- Action Log
- LLMProvider interface
- Ollama provider
- Developer Agent
- minimal Orchestrator
- CLI
- tests

## Task states
CREATED, PLANNING, READY, RUNNING, WAITING_AUTH, WAITING_DEPENDENCY, VALIDATING, RETRYING, BLOCKED, COMPLETED, FAILED, CANCELLED.

## Risk
LOW: automatic when scoped capability exists.
MEDIUM: automatic only when an applicable grant/rule exists; otherwise approval.
HIGH: explicit contextual approval or denial.

## Security
The LLM never receives root, never bypasses Policy Engine and never calls host tools directly. Tool execution must be mediated by capabilities and logged. Access outside the Task workspace must be denied unless separately authorized.

## Validation
Tool success alone is not Task success. A code repair is complete only when its defined validation succeeds.

## Out of V0
Voice, radial UI, full AI Center, System/File/Research/Desktop Agents, advanced memory, cloud sync and broad desktop automation.
