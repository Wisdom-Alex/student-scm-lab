"""Main script: runs the demo application."""

from students import students, add_student, average_score
from utils.helpers import highest_score, lowest_score


def main():
    add_student("Amina", 67)
    add_student("Chukwu", 91)
    print("Highest:", highest_score(students))
    print("Lowest:", lowest_score(students))
    print("Average:", average_score(students))


if __name__ == "__main__":
    main()
