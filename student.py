"""
student.py
Defines what a student record looks like and provides helper functions
to build and validate one. This is the data model layer of the project.
"""


def create_student(student_id, name, age, course, marks):
    """Build a student record (a dictionary) from individual fields."""
    return {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course,
        "marks": marks
    }


def validate_marks(marks):
    """Marks must be a number between 0 and 100."""
    return 0 <= marks <= 100


def validate_age(age):
    """Age must be a realistic student age."""
    return 5 <= age <= 100


def format_student_row(s):
    """Return a single formatted line representing a student, for display."""
    return f"{s['id']:<6}{s['name']:<15}{s['age']:<5}{s['course']:<10}{s['marks']:<6}"


def format_table_header():
    """Return the header line used above a list of student rows."""
    return f"{'ID':<6}{'Name':<15}{'Age':<5}{'Course':<10}{'Marks':<6}\n" + "-" * 42
