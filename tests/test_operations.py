"""
test_operations.py
Basic unit tests for the core record operations (add, update, delete, search).
Run with: python -m unittest discover
"""

import sys
import os
import unittest

# Allow importing modules from the project root when running tests directly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from operations import add_student, update_student, delete_student, search_students, find_student_by_id


class TestOperations(unittest.TestCase):

    def setUp(self):
        """Runs before every test: start with a fresh, empty list."""
        self.students = []

    def test_add_student_success(self):
        success, message = add_student(self.students, 101, "Riya", 20, "CS", 85)
        self.assertTrue(success)
        self.assertEqual(len(self.students), 1)

    def test_add_student_duplicate_id(self):
        add_student(self.students, 101, "Riya", 20, "CS", 85)
        success, message = add_student(self.students, 101, "Aman", 19, "ME", 70)
        self.assertFalse(success)
        self.assertEqual(len(self.students), 1)

    def test_add_student_invalid_marks(self):
        success, message = add_student(self.students, 102, "Aman", 19, "ME", 150)
        self.assertFalse(success)
        self.assertEqual(len(self.students), 0)

    def test_update_student(self):
        add_student(self.students, 101, "Riya", 20, "CS", 85)
        success, message = update_student(self.students, 101, name="Riya Sharma")
        self.assertTrue(success)
        self.assertEqual(self.students[0]["name"], "Riya Sharma")

    def test_delete_student(self):
        add_student(self.students, 101, "Riya", 20, "CS", 85)
        success, message = delete_student(self.students, 101)
        self.assertTrue(success)
        self.assertEqual(len(self.students), 0)

    def test_search_by_name(self):
        add_student(self.students, 101, "Riya", 20, "CS", 85)
        add_student(self.students, 102, "Aman", 19, "ME", 70)
        results = search_students(self.students, "riya")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["id"], 101)

    def test_find_student_by_id_not_found(self):
        result = find_student_by_id(self.students, 999)
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
