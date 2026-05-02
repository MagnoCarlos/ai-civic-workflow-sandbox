# Architecture

This project is a small, deterministic prototype for turning unstructured civic or operational requests into structured, reviewable workflow outputs.

It is intentionally simple. The goal is to show the workflow design clearly before adding external APIs, LLM calls, databases, or production integrations.

## High-level flow

1. Incoming request
2. Input loading
3. Classification
4. Field extraction
5. Mock context retrieval
6. Risk assessment
7. Suggested next action
8. Human review boundary
9. Structured JSON output

## Components

### 1. Input loading

The workflow accepts a JSON request.

Example fields:

- `source`
- `message`
- `language`
- `region`
- `urgency`

If no input file is provided, `demo.py` uses a built-in synthetic example.

### 2. Classification

The request is classified using deterministic keyword rules.

Current categories:

- `policy_research_request`
- `funding_or_grant_request`
- `media_or_publication_request`
- `general_support_request`

The deterministic baseline is useful because it is easy to inspect, test, and improve.

### 3. Field extraction

The system extracts basic structured fields from the request:

- source
- language
- region
- urgency
- message length

In a fuller version, this could be replaced or supported by an LLM-based extractor.

### 4. Mock context retrieval

The prototype uses static context notes instead of live retrieval.

This is intentional because the public demo should be:

- safe
- reproducible
- inspectable
- free from private data
- free from external API dependencies

### 5. Risk assessment

The workflow checks for risk signals such as:

- missing region
- policy/legal interpretation
- high urgency
- missing context

The output always requires human review.

### 6. Suggested next action

The system drafts a next action for a human reviewer.

It does not make final decisions.

It does not publish, send, approve, delete, or trigger destructive actions.

### 7. Structured output

The final output is JSON so it can be inspected or connected later to tools such as:

- dashboards
- ticketing systems
- Google Sheets
- Firebase
- n8n workflows
- human review queues

## Current boundaries

This prototype does not:

- call an LLM
- call external APIs
- verify real policy sources
- store user data
- process private or confidential information
- make final decisions

## Future architecture direction

A fuller version could add:

- LLM-assisted classification
- source retrieval
- source verification
- automated test cases
- confidence scoring
- reviewer comments
- dashboard logging
- n8n or Firebase integration
