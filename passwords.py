# passwords.py
"""Password strength checker.

Function:
    password_strength(password: str) -> dict

Return:
    {
        "strength": "weak" | "medium" | "strong",
        "score": int,           # 0..5
        "feedback": [str]       # list of actionable feedback items (may be empty for strong)
    }

Raises:
    TypeError for non-string inputs.
"""
from typing import Dict, List


def _has_upper(s: str) -> bool:
    return any(c.isupper() for c in s)


def _has_lower(s: str) -> bool:
    return any(c.islower() for c in s)


def _has_digit(s: str) -> bool:
    return any(c.isdigit() for c in s)


def _has_special(s: str) -> bool:
    # Special = any character not alphanumeric; supports Unicode punctuation
    return any(not c.isalnum() for c in s)


def password_strength(password: str) -> Dict[str, object]:
    """
    Evaluate the strength of `password`.

    Returns:
        dict with keys:
            - strength: "weak" | "medium" | "strong"
            - score: integer 0..5
            - feedback: list of actionable suggestions (empty when strong)

    Raises:
        TypeError if password is not a string.
    """
    if not isinstance(password, str):
        raise TypeError("password must be a string")

    # normalize - we treat leading/trailing whitespace as part of input (but warn)
    score = 0
    feedback: List[str] = []

    # length scoring (0..2)
    length = len(password)
    if length >= 12:
        score += 2
    elif length >= 8:
        score += 1

    # character variety (uppercase, lowercase, digit, special) each 1 point
    if _has_upper(password):
        score += 1
    else:
        feedback.append("Add an uppercase letter (A–Z).")

    if _has_lower(password):
        score += 1
    else:
        feedback.append("Add a lowercase letter (a–z).")

    if _has_digit(password):
        score += 1
    else:
        feedback.append("Add a digit (0–9).")

    if _has_special(password):
        score += 1
    else:
        feedback.append("Add a special character (e.g., !, ?, ©, §).")

    # If password is empty or only whitespace, give specific feedback and override scoring
    if password.strip() == "":
        score = 0
        feedback = ["Password must not be empty or contain only whitespace.", "Choose a password at least 8 characters long."]

    # Map score to strength
    if score <= 2:
        strength = "weak"
    elif 3 <= score <= 4:
        strength = "medium"
    else:
        strength = "strong"

    # If strong, clear feedback
    if strength == "strong":
        feedback = []

    return {"strength": strength, "score": score, "feedback": feedback}

