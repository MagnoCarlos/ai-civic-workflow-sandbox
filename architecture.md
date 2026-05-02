# Architecture

This project is a small, deterministic prototype for turning unstructured civic or operational requests into structured, reviewable workflow outputs.

It is intentionally simple. The goal is to show the workflow design clearly before adding external APIs, LLM calls, databases, or production integrations.

## High-level flow

```text
Incoming request
    ↓
Input loading
    ↓
Classification
    ↓
Field extraction
    ↓
Mock context retrieval
    ↓
Risk assessment
    ↓
Suggested next action
    ↓
Human review boundary
    ↓
Structured JSON output
