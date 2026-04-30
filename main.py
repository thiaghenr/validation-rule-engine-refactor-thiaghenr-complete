import json
from typing import Any, Dict

from validation import validate_submission


def main() -> None:
    sample_submission: Dict[str, Any] = {
        "candidate_id": "cand_123",
        "score": 85,
        "completed": True,
        "tags": ["python", "backend"],
    }

    result = validate_submission(sample_submission)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
