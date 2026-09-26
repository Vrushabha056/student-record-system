"""
cli.py
Functional module: Command-Line Interface.
Displays the menu, collects user input, and calls into operations.py
for the actual record logic. Handles all print/input so the other
modules stay reusable and testable on their own.
"""

from storage import load_students, save_students
from student import format_student_row, format_table_header
from operations import (
    add_student,
    update_student,
    delete_student,
    search_students,
    find_student_by_id,
)

students = []


def handle_add():
    try:
        student_id = int(input("Enter ID: "))
        name = input("Enter Name: ").strip()
        age = int(input("Enter Age: "))
        course = input("Enter Course: ").strip()
        marks = float(input("Enter Marks: "))
    except ValueError:
        print("Invalid input. ID and Age must be whole numbers, Marks must be a number.\n")
        return

    success, message = add_student(students, student_id, name, age, course, marks)
    print(message + "\n")
    if success:
        save_students(students)


def handle_view():
    if not students:
        print("No records found.\n")
        return
    print(f"Total students: {len(students)}")
    print(format_table_header())
    for s in students:
        print(format_student_row(s))
    print()


def handle_update():
    try:
        student_id = int(input("Enter ID of student to update: "))
    except ValueError:
        print("Invalid ID.\n")
        return

    student = find_student_by_id(students, student_id)
    if not student:
        print("No student found with that ID.\n")
        return

    print("Leave a field blank to keep it unchanged.")
    name = input(f"New Name [{student['name']}]: ").strip()
    age_input = input(f"New Age [{student['age']}]: ").strip()
    course = input(f"New Course [{student['course']}]: ").strip()
    marks_input = input(f"New Marks [{student['marks']}]: ").strip()

    age = int(age_input) if age_input else None
    marks = float(marks_input) if marks_input else None

    success, message = update_student(students, student_id, name or None, age, course or None, marks)
    print(message + "\n")
    if success:
        save_students(students)


def handle_delete():
    try:
        student_id = int(input("Enter ID of student to delete: "))
    except ValueError:
        print("Invalid ID.\n")
        return

    student = find_student_by_id(students, student_id)
    if not student:
        print("No student found with that ID.\n")
        return

    confirm = input(f"Delete {student['name']} (ID {student['id']})? (y/n): ").strip().lower()
    if confirm == "y":
        success, message = delete_student(students, student_id)
        print(message + "\n")
        if success:
            save_students(students)
    else:
        print("Deletion cancelled.\n")


def handle_search():
    term = input("Enter ID or Name to search: ").strip()
    results = search_students(students, term)
    if not results:
        print("No matching records found.\n")
        return
    print(format_table_header())
    for s in results:
        print(format_student_row(s))
    print()


def run():
    global students
    students = load_students()

    menu_actions = {
        "1": handle_add,
        "2": handle_view,
        "3": handle_update,
        "4": handle_delete,
        "5": handle_search,
    }

    while True:
        print("---- Student Record Management System ----")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Search Student")
        print("6. Exit")
        choice = input("Enter choice: ").strip()

        if choice == "6":
            print("Goodbye!")
            break
        action = menu_actions.get(choice)
        if action:
            action()
        else:
            print("Invalid choice, try again.\n")
