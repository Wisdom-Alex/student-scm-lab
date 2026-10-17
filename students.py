"""Data module: holds the student records used by the demo application."""

students = [
    {"name": "James", "score": 45},
    {"name": "Deborah", "score": 82},
]


def average_score(data):
    if len(data) == 0:
        return 0  # Preventive maintenance: avoid division by zero
    total = 0
    for d in data:
        total += d["score"]
    return total / len(data)


def add_student(name, score):
    students.append({"name": name, "score": score})


print("Current Students:", students)
print("Average Score:", average_score(students))
