"""Data module.

Holds the Student model (validated with Pydantic) and the in-memory
student list. Statistics and formatting live in ``utils`` so that this
module has a single responsibility: the data.
"""

from typing import Optional
from pydantic import BaseModel, Field, field_validator


class Student(BaseModel):
    """A single student record, validated when it is created."""

    name: str = Field(min_length=1)
    score: float = Field(ge=0, le=100)

    @field_validator("name")
    @classmethod
    def strip_name(cls, value: str) -> str:
        """Remove surrounding whitespace and reject blank names."""
        value = value.strip()
        if not value:
            raise ValueError("name must not be blank")
        return value


students: list[Student] = [
    Student(name="James", score=45),
    Student(name="Deborah", score=82),
]


def add_student(name: str, score: float, data: Optional[list[Student]] = None) -> Student:
    """Validate a new student and append it to ``data``.

    Args:
        name: Student name (whitespace is stripped).
        score: Score between 0 and 100 inclusive.
        data: Target list. Defaults to the module level ``students`` list.

    Returns:
        The validated Student that was added.

    Raises:
        pydantic.ValidationError: If the name or score is invalid.
    """
    target = students if data is None else data
    student = Student(name=name, score=score)
    target.append(student)
    return student
