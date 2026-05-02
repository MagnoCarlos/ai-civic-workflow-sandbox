# Evaluation Plan

This project uses simple deterministic rules first so the workflow can be inspected, tested, and improved before adding model-based reasoning.

## What is being evaluated

The workflow should correctly:

- classify the incoming request
- extract basic structured fields
- identify missing or risky information
- retrieve relevant mock context
- require human review before operational use
- produce a useful suggested next action

## Test cases

| Test case | Input pattern | Expected category | Expected risk behaviour | Pass criteria |
|---|---|---|---|---|
| Clear policy request | Mentions policy, regulation, reporting, compliance, or legal requirements | `policy_research_request` | Requires human review because policy/legal interpretation is risky | Category is correct and risk flag is present |
| Funding request | Mentions grant, funding, donor, proposal, budget, or sponsor | `funding_or_grant_request` | Human review required before routing or response | Category is correct and next action mentions funder/deadline/eligibility |
| Media request | Mentions journalist, press, article, interview, media, or publication | `media_or_publication_request` | Human review required before drafting a response | Category is correct and next action asks for publication/deadline/topic |
| Ambiguous request | Does not contain a known keyword | `general_support_request` | Human review required because routing may be unclear | Category defaults safely and asks clarifying questions |
| Missing region | Region is missing or unknown | Any category | Missing region risk flag should appear | Output flags missing region before final guidance |
| High urgency request | Message includes urgent, ASAP, today, deadline, immediately, or emergency | Any category | High urgency risk flag should appear | Urgency becomes `high` and output warns that review is needed |

## Known limitations

- Keyword rules are easy to inspect but limited.
- The mock retrieval step uses static demo context.
- The system does not verify external sources.
- The system does not make final decisions.
- The system does not send, publish, approve, delete, or trigger destructive actions.

## Next improvements

- Add more test inputs.
- Add automated tests with expected outputs.
- Add a simple command-line flag for saving output to a file.
- Add optional LLM classification after the deterministic baseline is tested.
- Add source verification before any real-world use.
