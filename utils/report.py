"""Report module: console formatting for student data."""

from students import Student
from utils.helpers import average_score, letter_grade, median_score


def format_report(data: list[Student]) -> str:
    """Return a console-friendly table with summary statistics."""
    lines = [f"{'Name':<12}{'Score':>7}  Grade"]
    for s in sorted(data, key=lambda x: x.score, reverse=True):
        lines.append(f"{s.name:<12}{s.score:>7.1f}  {letter_grade(s.score)}")
    lines += [
        "",
        f"{'Average':<12}{average_score(data):>7.2f}",
        f"{'Median':<12}{median_score(data):>7.2f}",
    ]
    return "\n".join(lines)
