# AI Civic Workflow Sandbox

A sanitised AI workflow automation prototype for turning unstructured civic or operational requests into structured, reviewable actions.

This public demo uses synthetic data only. It does not include employer, client, private, or confidential information.

## What it demonstrates

This project demonstrates practical AI workflow engineering:

- classifying incoming requests
- extracting structured fields from messy text
- retrieving relevant mock context
- assessing risk and uncertainty
- drafting a suggested next action
- keeping a human-in-the-loop review step
- producing structured JSON output
- defining evaluation criteria before deployment

## Quick start

Run the demo with the sample input:

```bash
python demo.py sample_input.json
```

Or run it without an input file to use the built-in synthetic example:

```bash
python demo.py
```

The script prints a structured JSON workflow output.

## Project files

| File | Purpose |
|---|---|
| `demo.py` | Deterministic workflow demo |
| `sample_input.json` | Example incoming request |
| `sample_output.json` | Example structured output |
| `architecture.md` | System design and component notes |
| `evals.md` | Evaluation plan and test cases |
| `responsible-ai.md` | Responsible AI boundaries and failure cases |

## Workflow

1. Incoming request
2. Classification
3. Field extraction
4. Mock context retrieval
5. Risk assessment
6. Suggested next action
7. Human review boundary
8. Structured JSON output

## Example input

```json
{
  "source": "email",
  "message": "We need help understanding whether a new policy affects small business reporting requirements in Angola.",
  "language": "English",
  "region": "Angola",
  "urgency": "medium"
}
```

## Example output

```json
{
  "workflow_name": "ai_civic_workflow_sandbox",
  "timestamp_utc": "example-runtime-timestamp",
  "input_summary": {
    "source": "email",
    "language": "English",
    "region": "Angola",
    "urgency": "medium"
  },
  "classification": {
    "category": "policy_research_request"
  },
  "extracted_fields": {
    "source": "email",
    "language": "English",
    "region": "Angola",
    "urgency": "medium",
    "message_length": 104
  },
  "retrieved_context": [
    {
      "title": "Policy research workflow note",
      "summary": "Check official sources, identify obligations, and separate verified facts from interpretation."
    },
    {
      "title": "Responsible AI review rule",
      "summary": "Do not provide legal advice. Prepare a briefing note for qualified human review."
    }
  ],
  "risk_assessment": {
    "risk_level": "medium",
    "risk_flags": [
      "Policy/legal interpretation requires qualified human review."
    ],
    "human_review_required": true
  },
  "suggested_next_action": "Retrieve relevant official policy sources for Angola, summarise possible obligations, flag uncertainty, and prepare a briefing note for human review.",
  "decision_boundary": "This demo suggests a next action only. A human reviewer must approve, edit, or reject the output before operational use."
}
```

## Responsible AI boundaries

This prototype is designed around human review.

It does not automatically:

- publish content
- send messages
- delete records
- approve decisions
- provide legal advice
- make final operational decisions

The aim is to support civic, research, media, nonprofit, and operational teams by reducing manual triage work while keeping accountability with humans.

## Current limitations

This prototype does not:

- call an LLM
- call external APIs
- verify live policy sources
- store user data
- process private or confidential information
- make final decisions

The current version is intentionally deterministic so the workflow can be inspected, tested, and improved before adding model-based reasoning.

## Why I built this

I am interested in building practical AI systems that are useful in real operational environments, especially for African and public-interest contexts.

My background combines product engineering, software prototyping, embedded systems, validation, testing, technical communication, and Portuguese/English fluency.
