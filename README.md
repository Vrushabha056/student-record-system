# Student Record Management System

A command-line application for managing student records (add, view, update, delete, search), built as an evaluated course project. The project is organized into separate modules for data modeling, persistence, business logic, and the CLI, with a small suite of unit tests.

## Overview

This project lets a user manage a list of student records — each with an ID, Name, Age, Course, and Marks — entirely from the terminal. Records are saved to a local JSON file so they persist between runs.

## Features

- Add a new student record (with validation on ID uniqueness, age, and marks)
- View all student records in a formatted table
- Update an existing record (leave a field blank to keep it unchanged)
- Delete a record (with confirmation)
- Search by ID or partial name match
- Automatic persistence to `students.json`
- Unit-tested core logic (7 tests covering add/update/delete/search)

## Technologies / Tools Used

- Python 3 (standard library only — `json`, `os`)
- `unittest` for testing
- Git & GitHub for version control

## Project Structure

```
.
├── main.py                  # Entry point — run this to start the program
├── student.py               # Data model: student record structure + validation
├── storage.py                # Data Persistence module: load/save JSON file
├── operations.py             # Record Management module: add/update/delete/search logic
├── cli.py                     # CLI module: menu, input/output, user interaction
├── tests/
│   └── test_operations.py     # Unit tests for the operations module
├── students.json               # Auto-generated data file (created on first run)
├── statement.md                 # Problem statement, scope, and target users
└── README.md                     # This file
```

### Why this structure?
The project is split into three functional modules so each part has a single responsibility and can be tested independently:
1. **Data Persistence** (`storage.py`) — reading/writing the JSON file
2. **Record Management** (`operations.py`) — the actual add/update/delete/search logic, independent of any user interface
3. **CLI** (`cli.py`) — handles all user-facing input/output and calls into the other two modules

## Requirements

- Python 3.7 or higher
- No external libraries needed

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/Vrushabha056/student-record-system.git
   cd student-record-system
   ```

2. **(Optional) Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate      # On Windows: venv\Scripts\activate
   ```

3. **No dependencies to install** — the project only uses Python's standard library.

## How to Run

```bash
python main.py
```

You'll see a menu like this:

```
---- Student Record Management System ----
1. Add Student
2. View All Students
3. Update Student
4. Delete Student
5. Search Student
6. Exit
Enter choice:
```

Enter the number corresponding to the action you want, and follow the prompts.

## How to Run Tests

From the project root:

```bash
python -m unittest discover -s tests
```

This runs all unit tests in `tests/test_operations.py` and reports pass/fail for each.

## Data Storage

All records are saved in `students.json` in the project root. This file is created automatically the first time you add a student and updated after every add/update/delete. Deleting `students.json` resets the records.
