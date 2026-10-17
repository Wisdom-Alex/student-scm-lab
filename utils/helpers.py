"""Helper module: small utility functions for student records."""


def highest_score(data):
    """Return the student with the highest score, or None if no data."""
    if not data:
        return None
    return max(data, key=lambda d: d["score"])


def lowest_score(data):
    """Return the student with the lowest score, or None if no data."""
    if not data:
        return None
    return min(data, key=lambda d: d["score"])
