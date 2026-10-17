"""Helper module: small utility functions for student records."""

from students import Student


def highest_score(data: list[Student]) -> Student | None:
    """Return the student with the highest score, or None if no data."""
    return max(data, key=lambda s: s.score, default=None)


def lowest_score(data: list[Student]) -> Student | None:
    """Return the student with the lowest score, or None if no data."""
    return min(data, key=lambda s: s.score, default=None)
