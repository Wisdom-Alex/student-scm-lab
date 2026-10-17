"""Main script: runs the demo application."""

from pydantic import ValidationError

from students import students, add_student, average_score
from utils.helpers import highest_score, lowest_score


def main() -> None:
    print("Current Students:", students)
    add_student("Amina", 67)
    add_student("Chukwu", 91)
    print("Highest:", highest_score(students))
    print("Lowest:", lowest_score(students))
    print("Average:", average_score(students))
    print("Empty average:", average_score([]))

    try:
        add_student("Bad Data", 250)
    except ValidationError as exc:
        print("Rejected invalid student:", exc.errors()[0]["msg"])


if __name__ == "__main__":
    main()
