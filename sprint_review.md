# Sprint 2 Review — Password Strength Module

## Sprint goal
Implement a robust password strength checker using TDD, including actionable feedback for weak passwords, robust error handling, and comprehensive unit tests.

## Completed
- Implemented `password_strength(password: str)` that returns a dict: strength, score, feedback.
- Wrote comprehensive unit tests covering basic use, feedback, error handling (non-string), empty/whitespace, Unicode, and special characters.
- Refactored helper functions to improve readability (`_has_upper`, `_has_lower`, etc.).
- Documented daily standups, review, and retrospective.

## Not completed
- No outstanding tasks for this sprint. (All items in backlog for Sprint 2 as agreed were implemented.)

## Demo notes
- Function signature: `password_strength(password: str) -> dict`
- Example:
  ```py
  from passwords import password_strength
  password_strength("Abc123!@#")  # -> {"strength":"medium","score":3,"feedback":[...]}

