"""Helper module: small utility functions for student records."""


def highest_score(data):
    return max(data, key=lambda d: d["score"])


def lowest_score(data):
    return min(data, key=lambda d: d["score"])
