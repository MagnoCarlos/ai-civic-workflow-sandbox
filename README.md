# AI Civic Workflow Sandbox

A sanitised AI workflow automation prototype for turning unstructured requests into structured, reviewable actions.

This public demo uses synthetic data only. It does not include employer, client, private, or confidential information.

## What it demonstrates

This project demonstrates how I think about practical AI engineering:

- classifying incoming requests
- extracting structured fields from messy text
- retrieving relevant context
- drafting a suggested action or response
- keeping a human-in-the-loop review step
- logging decisions for auditability
- defining evaluation criteria before deployment

## Workflow

Incoming request
→ Classification
→ Field extraction
→ Context retrieval
→ Draft response/action
→ Human review
→ Logged decision

## Example input

```json
{
  "source": "email",
  "message": "We need help understanding whether a new policy affects small business reporting requirements in Angola.",
  "language": "English",
  "region": "Angola",
  "urgency": "medium"
}
