"""Unit tests for the student modules (run: python -m unittest -v)."""

import unittest

from pydantic import ValidationError

from students import Student, add_student
from utils.helpers import (average_score, highest_score, letter_grade,
                           lowest_score, median_score)


class StudentTests(unittest.TestCase):
    def setUp(self):
        self.data = [Student(name="A", score=40), Student(name="B", score=80),
                     Student(name="C", score=60)]

    def test_empty_list_is_safe(self):
        self.assertEqual(average_score([]), 0.0)
        self.assertEqual(median_score([]), 0.0)
        self.assertIsNone(highest_score([]))
        self.assertIsNone(lowest_score([]))

    def test_statistics(self):
        self.assertAlmostEqual(average_score(self.data), 60.0)
        self.assertEqual(median_score(self.data), 60)
        self.assertEqual(highest_score(self.data).name, "B")
        self.assertEqual(lowest_score(self.data).name, "A")

    def test_validation_rejects_bad_input(self):
        for name, score in (("", 50), ("X", 101), ("X", -1), ("X", "abc")):
            with self.assertRaises(ValidationError):
                add_student(name, score, data=[])

    def test_name_is_stripped(self):
        self.assertEqual(add_student("  Ada ", 70, data=[]).name, "Ada")

    def test_letter_grade_bands(self):
        self.assertEqual([letter_grade(s) for s in (75, 65, 55, 46, 10)],
                         ["A", "B", "C", "D", "F"])


if __name__ == "__main__":
    unittest.main()
