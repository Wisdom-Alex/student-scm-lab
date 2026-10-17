"""Main script: runs the demo application."""

from students import students, add_student, average_score
from utils.helpers import highest_score, lowest_score


def main():
    print("Current Students:", students)
    add_student("Amina", 67)
    add_student("Chukwu", 91)
    print("Highest:", highest_score(students))
    print("Lowest:", lowest_score(students))
    print("Average:", average_score(students))

    # Corrective checks: empty list and invalid input no longer crash the app.
    print("Empty average:", average_score([]))
    print("Empty highest:", highest_score([]))
    try:
        add_student("Bad Data", 250)
    except ValueError as exc:
        print("Rejected invalid student:", exc)


if __name__ == "__main__":
    main()
