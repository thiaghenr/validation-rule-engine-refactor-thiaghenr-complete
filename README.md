### Task Overview
Utkrusht runs a backend service that validates assessment submissions before they are stored or scored. Currently, the validation logic lives in a single function with hardcoded checks that returns flat error strings. As the number of validation rules grows, this approach is becoming hard to maintain and extend. The team wants validation feedback to be more structured and machine-readable so downstream consumers (like a UI) can handle errors and warnings appropriately. Your task is to refactor this validation into a rule-based design that is easier to extend and produces structured output.

### Objectives
- Refactor the monolithic `validate_submission` function into a set of independent, composable validation rules while preserving the existing validation behavior.
- Return validation results as structured, JSON-serializable data that conveys what went wrong, where, and how severe it is.
- Support the ability to selectively enable or disable individual validation rules.
- Update `main.py` and the tests under `tests/` to work with the refactored validation module.

### How to Verify
- Run `python main.py` and confirm the output is a structured JSON report reflecting any validation issues found.
- Test with both a valid and an invalid submission to ensure correct behavior in each case.
- Run `pytest` from the project root and ensure all tests pass.

### Helpful Tips
- Start by reading through the existing `validate_submission` function to understand what checks are already in place.
- Think about how you want to represent a single validation finding and how to make the overall output JSON-friendly.
- Consider how rules can be registered and selected so that callers can control which validations run.
- Keep rule execution order predictable so tests produce consistent results.
