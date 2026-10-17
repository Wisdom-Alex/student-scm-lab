"""Data module: holds the student records used by the demo application."""

students = [
    {"name": "James", "score": 45},
    {"name": "Deborah", "score": 82},
]


def average_score(data):
    """Return the mean score, or 0 when the list is empty."""
    if len(data) == 0:
        return 0  # avoid division by zero
    return sum(d["score"] for d in data) / len(data)


def add_student(name, score):
    """Append a student after validating the input.

    Raises ValueError for a blank name or an out-of-range score and
    TypeError when the score is not a number.
    """
    if not isinstance(name, str) or not name.strip():
        raise ValueError("name must be a non-empty string")
    if isinstance(score, bool) or not isinstance(score, (int, float)):
        raise TypeError("score must be a number")
    if not 0 <= score <= 100:
        raise ValueError("score must be between 0 and 100")
    students.append({"name": name.strip(), "score": score})
