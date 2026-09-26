"""
operations.py
Functional module: Student Record Management.
Contains the core logic for adding, viewing, updating, deleting,
and searching student records. Works on an in-memory list that the
caller (cli.py) loads from and saves to storage.py.
"""

from student import create_student, validate_age, validate_marks


def find_student_by_id(students, student_id):
    """Return the student dict with the given ID, or None if not found."""
    for s in students:
        if s["id"] == student_id:
            return s
    return None


def add_student(students, student_id, name, age, course, marks):
    """Add a new student record. Returns (success, message)."""
    if find_student_by_id(students, student_id):
        return False, "A student with this ID already exists."
    if not validate_age(age):
        return False, "Age must be between 5 and 100."
    if not validate_marks(marks):
        return False, "Marks must be between 0 and 100."

    students.append(create_student(student_id, name, age, course, marks))
    return True, "New record saved."


def update_student(students, student_id, name=None, age=None, course=None, marks=None):
    """Update fields of an existing student. Only provided fields are changed."""
    student = find_student_by_id(students, student_id)
    if not student:
        return False, "No student found with that ID."

    if name:
        student["name"] = name
    if age is not None:
        if not validate_age(age):
            return False, "Age must be between 5 and 100. Other fields were not saved."
        student["age"] = age
    if course:
        student["course"] = course
    if marks is not None:
        if not validate_marks(marks):
            return False, "Marks must be between 0 and 100. Other fields were not saved."
        student["marks"] = marks

    return True, "Student updated successfully."


def delete_student(students, student_id):
    """Remove a student record by ID. Returns (success, message)."""
    student = find_student_by_id(students, student_id)
    if not student:
        return False, "No student found with that ID."
    students.remove(student)
    return True, "Student deleted successfully."


def search_students(students, search_term):
    """Search by ID (exact) or name (partial, case-insensitive match)."""
    term = search_term.strip().lower()
    return [
        s for s in students
        if term == str(s["id"]) or term in s["name"].lower()
    ]
