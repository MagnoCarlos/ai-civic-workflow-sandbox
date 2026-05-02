"""
AI Civic Workflow Sandbox

A deterministic demo that turns an unstructured civic/support request into a
structured, reviewable workflow output.

No API keys.
No external services.
No employer, client, private, or confidential data.
Synthetic/demo logic only.
"""

import json
import sys
from datetime import datetime, timezone
from pathlib import Path


DEFAULT_REQUEST = {
    "source": "email",
    "message": "We need help understanding whether a new policy affects small business reporting requirements in Angola.",
    "language": "English",
    "region": "Angola",
    "urgency": "medium"
}


POLICY_KEYWORDS = [
    "policy", "law", "regulation", "compliance", "reporting",
    "requirements", "public sector", "government", "legal"
]

FUNDING_KEYWORDS = [
    "grant", "funding", "donor", "proposal", "budget", "sponsor"
]

MEDIA_KEYWORDS = [
    "journalist", "press", "article", "interview", "media", "publication"
]

URGENT_KEYWORDS = [
    "urgent", "asap", "today", "deadline", "immediately", "emergency"
]


def load_request() -> dict:
    """
    Load request data from a JSON file if provided.
    If no file is provided, use a safe built-in synthetic example.
    """
    if len(sys.argv) < 2:
        return DEFAULT_REQUEST

    input_path = Path(sys.argv[1])

    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    with input_path.open("r", encoding="utf-8") as file:
        return json.load(file)


def normalise_text(value: str) -> str:
    return value.lower().strip()


def classify_request(message: str) -> str:
    """
    Classify the request using simple deterministic keyword rules.

    This is intentionally not an LLM call. The goal is to show the workflow
    structure first before adding model-based reasoning later.
    """
    text = normalise_text(message)

    if any(keyword in text for keyword in POLICY_KEYWORDS):
        return "policy_research_request"

    if any(keyword in text for keyword in FUNDING_KEYWORDS):
        return "funding_or_grant_request"

    if any(keyword in text for keyword in MEDIA_KEYWORDS):
        return "media_or_publication_request"

    return "general_support_request"


def detect_urgency(message: str, provided_urgency: str | None) -> str:
    text = normalise_text(message)

    if any(keyword in text for keyword in URGENT_KEYWORDS):
        return "high"

    if provided_urgency:
        return normalise_text(provided_urgency)

    return "unknown"


def extract_fields(request: dict) -> dict:
    """
    Extract structured fields from the incoming request.
    In a fuller system, this could be replaced with an LLM or extraction model.
    """
    message = request.get("message", "")

    return {
        "source": request.get("source", "unknown"),
        "language": request.get("language", "unknown"),
        "region": request.get("region", "unknown"),
        "urgency": detect_urgency(message, request.get("urgency")),
        "message_length": len(message),
    }


def retrieve_context(category: str, region: str) -> list[dict]:
    """
    Mock context retrieval.

    This deliberately uses static demo context instead of live web retrieval.
    That keeps the public demo safe, reproducible, and easy to inspect.
    """
    context_library = {
        "policy_research_request": [
            {
                "title": "Policy research workflow note",
                "summary": "Check official sources, identify obligations, and separate verified facts from interpretation."
            },
            {
                "title": "Responsible AI review rule",
                "summary": "Do not provide legal advice. Prepare a briefing note for qualified human review."
            }
        ],
        "funding_or_grant_request": [
            {
                "title": "Grant triage workflow note",
                "summary": "Extract funder, deadline, eligibility, documents required, and next action owner."
            }
        ],
        "media_or_publication_request": [
            {
                "title": "Media request workflow note",
                "summary": "Identify publication, deadline, topic, spokesperson need, and approval requirements."
            }
        ],
        "general_support_request": [
            {
                "title": "General triage workflow note",
                "summary": "Clarify request type, missing information, urgency, and routing destination."
            }
        ]
    }

    results = context_library.get(category, context_library["general_support_request"])

    if region == "unknown":
        results.append({
            "title": "Missing region warning",
            "summary": "Ask the requester to confirm the country or region before producing final guidance."
        })

    return results


def assess_risk(category: str, fields: dict, context: list[dict]) -> dict:
    """
    Identify risk flags that require human review.
    """
    risk_flags = []

    if fields["region"] == "unknown":
        risk_flags.append("Missing region may cause incorrect routing or advice.")

    if category == "policy_research_request":
        risk_flags.append("Policy/legal interpretation requires qualified human review.")

    if fields["urgency"] == "high":
        risk_flags.append("High urgency request should be reviewed before action is taken.")

    if not context:
        risk_flags.append("No relevant context found.")

    return {
        "risk_level": "medium" if risk_flags else "low",
        "risk_flags": risk_flags,
        "human_review_required": True
    }


def draft_next_action(category: str, fields: dict, risk: dict) -> str:
    """
    Create a suggested next action for a human reviewer.
    """
    region = fields["region"]

    if category == "policy_research_request":
        return (
            f"Retrieve relevant official policy sources for {region}, summarise possible obligations, "
            "flag uncertainty, and prepare a briefing note for human review."
        )

    if category == "funding_or_grant_request":
        return (
            "Extract funder, deadline, eligibility criteria, required documents, and route the request "
            "to the appropriate project or partnerships lead."
        )

    if category == "media_or_publication_request":
        return (
            "Confirm publication, deadline, topic, and approval requirements before drafting a response."
        )

    return (
        "Ask clarifying questions, identify the correct owner, and log the request for follow-up."
    )


def build_workflow_output(request: dict) -> dict:
    message = request.get("message", "")

    category = classify_request(message)
    fields = extract_fields(request)
    context = retrieve_context(category, fields["region"])
    risk = assess_risk(category, fields, context)
    next_action = draft_next_action(category, fields, risk)

    return {
        "workflow_name": "ai_civic_workflow_sandbox",
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "input_summary": {
            "source": fields["source"],
            "language": fields["language"],
            "region": fields["region"],
            "urgency": fields["urgency"]
        },
        "classification": {
            "category": category
        },
        "extracted_fields": fields,
        "retrieved_context": context,
        "risk_assessment": risk,
        "suggested_next_action": next_action,
        "decision_boundary": (
            "This demo suggests a next action only. A human reviewer must approve, edit, "
            "or reject the output before operational use."
        )
    }


def main() -> None:
    request = load_request()
    output = build_workflow_output(request)

    print(json.dumps(output, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
