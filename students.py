"""Data module: Pydantic-validated student records (Python 3.12+)."""

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


def add_student(name: str, score: float) -> Student:
    """Validate and append a student. Raises pydantic.ValidationError."""
    student = Student(name=name, score=score)
    students.append(student)
    return student
