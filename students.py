"""Data module: Pydantic-validated student records (Python 3.12+)."""

from statistics import median

from pydantic import BaseModel, Field, field_validator


class Student(BaseModel):
    """A single student record validated on creation."""

    name: str = Field(min_length=1)
    score: float = Field(ge=0, le=100)

    @field_validator("name")
    @classmethod
    def strip_name(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("name must not be blank")
        return value


students: list[Student] = [
    Student(name="James", score=45),
    Student(name="Deborah", score=82),
]


def average_score(data: list[Student]) -> float:
    """Return the mean score, or 0.0 when the list is empty."""
    if not data:
        return 0.0
    return sum(s.score for s in data) / len(data)


def median_score(data: list[Student]) -> float:
    """Return the median score, or 0.0 when the list is empty."""
    return median(s.score for s in data) if data else 0.0


def letter_grade(score: float) -> str:
    """Map a numeric score to a letter grade."""
    for cut_off, grade in ((70, "A"), (60, "B"), (50, "C"), (45, "D")):
        if score >= cut_off:
            return grade
    return "F"


def add_student(name: str, score: float) -> Student:
    """Validate and append a student. Raises pydantic.ValidationError."""
    student = Student(name=name, score=score)
    students.append(student)
    return student


def format_report(data: list[Student]) -> str:
    """Return a console-friendly table with summary statistics."""
    lines = [f"{'Name':<12}{'Score':>7}  Grade"]
    for s in sorted(data, key=lambda x: x.score, reverse=True):
        lines.append(f"{s.name:<12}{s.score:>7.1f}  {letter_grade(s.score)}")
    lines.append("")
    lines.append(f"{'Average':<12}{average_score(data):>7.2f}")
    lines.append(f"{'Median':<12}{median_score(data):>7.2f}")
    return "\n".join(lines)
