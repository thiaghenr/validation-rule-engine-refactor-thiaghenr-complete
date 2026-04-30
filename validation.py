from typing import Any, Dict, List


def validate_submission(submission: Dict[str, Any]) -> Dict[str, List[str]]:
    """Validate a single assessment submission.

    The current implementation returns a dictionary with a single key
    "errors" that maps to a list of human-readable error messages.
    If the list is empty, the submission is considered valid.
    """
    errors: List[str] = []

    # candidate_id: required, non-empty string
    if (
        "candidate_id" not in submission
        or not isinstance(submission["candidate_id"], str)
        or not submission["candidate_id"].strip()
    ):
        errors.append("candidate_id is required and must be a non-empty string")

    # score: required, integer between 0 and 100
    if "score" in submission:
        score = submission["score"]
        if not isinstance(score, int) or not (0 <= score <= 100):
            errors.append("score must be an integer between 0 and 100")
    else:
        errors.append("score is required")

    # completed: optional, but if present must be a boolean
    if "completed" in submission and not isinstance(submission["completed"], bool):
        errors.append("completed must be a boolean if provided")

    # tags: optional list of strings, at most 5 items
    if "tags" in submission:
        tags = submission["tags"]
        if not isinstance(tags, list):
            errors.append("tags must be a list of strings")
        else:
            for tag in tags:
                if not isinstance(tag, str):
                    errors.append("tags must be a list of strings")
                    break
            if len(tags) > 5:
                errors.append("no more than 5 tags are allowed")

    return {"errors": errors}
