"""
Student Record Management System
A simple command-line project for managing student records.
Data is stored in a JSON file (students.json) so records persist between runs.
"""

import json
import os

DATA_FILE = "students.json"
students = []


def load_students():
    """Load student records from the JSON file into memory (if the file exists)."""
    global students
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                students = json.load(f)
        except (json.JSONDecodeError, IOError):
            print("Warning: could not read existing data file. Starting with an empty list.\n")
            students = []
    else:
        students = []


def save_students():
    """Save the current list of student records to the JSON file."""
    with open(DATA_FILE, "w") as f:
        json.dump(students, f, indent=4)


def find_student_by_id(student_id):
    """Return the student dictionary with the given ID, or None if not found."""
    for s in students:
        if s["id"] == student_id:
            return s
    return None


def add_student():
    try:
        student_id = int(input("Enter ID: "))
        if find_student_by_id(student_id):
            print("A student with this ID already exists.\n")
            return
        name = input("Enter Name: ").strip()
        age = int(input("Enter Age: "))
        course = input("Enter Course: ").strip()
        marks = float(input("Enter Marks: "))

        student = {
            "id": student_id,
            "name": name,
            "age": age,
            "course": course,
            "marks": marks
        }
        students.append(student)
        save_students()
        print("Student added successfully!\n")
    except ValueError:
        print("Invalid input. ID and Age must be whole numbers, Marks must be a number.\n")


def view_students():
    if not students:
        print("No records found.\n")
        return
    print(f"{'ID':<6}{'Name':<15}{'Age':<5}{'Course':<10}{'Marks':<6}")
    print("-" * 42)
    for s in students:
        print(f"{s['id']:<6}{s['name']:<15}{s['age']:<5}{s['course']:<10}{s['marks']:<6}")
    print()


def update_student():
    try:
        student_id = int(input("Enter ID of student to update: "))
    except ValueError:
        print("Invalid ID.\n")
        return

    student = find_student_by_id(student_id)
    if not student:
        print("No student found with that ID.\n")
        return

    print("Leave a field blank to keep it unchanged.")
    name = input(f"New Name [{student['name']}]: ").strip()
    age = input(f"New Age [{student['age']}]: ").strip()
    course = input(f"New Course [{student['course']}]: ").strip()
    marks = input(f"New Marks [{student['marks']}]: ").strip()

    if name:
        student["name"] = name
    if age:
        try:
            student["age"] = int(age)
        except ValueError:
            print("Age unchanged (invalid number).")
    if course:
        student["course"] = course
    if marks:
        try:
            student["marks"] = float(marks)
        except ValueError:
            print("Marks unchanged (invalid number).")

    save_students()
    print("Student updated successfully!\n")


def delete_student():
    try:
        student_id = int(input("Enter ID of student to delete: "))
    except ValueError:
        print("Invalid ID.\n")
        return

    student = find_student_by_id(student_id)
    if not student:
        print("No student found with that ID.\n")
        return

    confirm = input(f"Delete {student['name']} (ID {student['id']})? (y/n): ").strip().lower()
    if confirm == "y":
        students.remove(student)
        save_students()
        print("Student deleted successfully!\n")
    else:
        print("Deletion cancelled.\n")


def search_student():
    keyword = input("Enter ID or Name to search: ").strip().lower()
    results = [
        s for s in students
        if keyword == str(s["id"]) or keyword in s["name"].lower()
    ]
    if not results:
        print("No matching records found.\n")
        return
    print(f"{'ID':<6}{'Name':<15}{'Age':<5}{'Course':<10}{'Marks':<6}")
    print("-" * 42)
    for s in results:
        print(f"{s['id']:<6}{s['name']:<15}{s['age']:<5}{s['course']:<10}{s['marks']:<6}")
    print()


def main():
    load_students()
    while True:
        print("---- Student Record Management System ----")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Search Student")
        print("6. Exit")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            search_student()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.\n")


if __name__ == "__main__":
    main()
