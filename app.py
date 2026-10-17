"""Main script: runs the demo application."""

from pydantic import ValidationError

from students import students, add_student, format_report
from utils.helpers import highest_score, lowest_score


def main() -> None:
    add_student("Amina", 67)
    add_student("Chukwu", 91)
    print(format_report(students))
    print()
    print("Highest:", highest_score(students))
    print("Lowest:", lowest_score(students))

    try:
        add_student("Bad Data", 250)
    except ValidationError as exc:
        print("Rejected invalid student:", exc.errors()[0]["msg"])


if __name__ == "__main__":
    main()
