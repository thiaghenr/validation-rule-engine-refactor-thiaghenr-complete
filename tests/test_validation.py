from typing import Any, Dict

from validation import validate_submission


def _make_valid_submission() -> Dict[str, Any]:
    return {
        "candidate_id": "cand_123",
        "score": 90,
        "completed": True,
        "tags": ["python", "backend"],
    }


def test_valid_submission_has_no_errors() -> None:
    submission = _make_valid_submission()
    result = validate_submission(submission)
    assert isinstance(result, dict)
    assert "errors" in result
    assert result["errors"] == []


def test_invalid_submission_collects_errors() -> None:
    submission = _make_valid_submission()
    submission["candidate_id"] = ""  # invalid: empty string
    submission["score"] = -5  # invalid: out of range

    result = validate_submission(submission)

    assert isinstance(result, dict)
    assert isinstance(result.get("errors"), list)
    messages = " ".join(result["errors"])
    assert "candidate_id is required" in messages
    assert "score must be an integer between 0 and 100" in messages
