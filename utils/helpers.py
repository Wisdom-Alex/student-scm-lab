"""Helper module: statistics and grading for student records."""

from typing import Optional
from statistics import median

from students import Student

# Grade boundaries, highest first: (minimum score, letter).
GRADE_BANDS: tuple[tuple[int, str], ...] = ((70, "A"), (60, "B"), (50, "C"), (45, "D"))


def highest_score(data: list[Student]) -> Optional[Student]:
    """Return the student with the highest score, or None if no data."""
    return max(data, key=lambda s: s.score, default=None)


def lowest_score(data: list[Student]) -> Optional[Student]:
    """Return the student with the lowest score, or None if no data."""
    return min(data, key=lambda s: s.score, default=None)


def average_score(data: list[Student]) -> float:
    """Return the mean score, or 0.0 when the list is empty."""
    if not data:
        return 0.0
    return sum(s.score for s in data) / len(data)


def median_score(data: list[Student]) -> float:
    """Return the median score, or 0.0 when the list is empty."""
    return median(s.score for s in data) if data else 0.0


def letter_grade(score: float) -> str:
    """Map a numeric score to a letter grade using GRADE_BANDS."""
    for cut_off, grade in GRADE_BANDS:
        if score >= cut_off:
            return grade
    return "F"
