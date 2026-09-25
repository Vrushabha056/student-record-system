# Student Record Management System

A simple command-line application for managing student records (add, view, update, delete, search), built as a Python Essentials course project. Data is stored locally in a JSON file so records persist between runs.

## Features
- Add a new student record
- View all student records
- Update an existing record
- Delete a record
- Search by ID or name
- Data automatically saved to `students.json`

## Requirements
- Python 3.7 or higher (no external libraries needed — uses only the standard library)

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/<your-repo-name>.git
   cd <your-repo-name>
   ```

2. **(Optional) Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate      # On Windows: venv\Scripts\activate
   ```

3. **No dependencies to install** — this project only uses Python's built-in `json` and `os` modules.

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

Enter the number corresponding to the action you want to perform, and follow the prompts.

## Data Storage

All records are saved in `students.json` in the same folder as `main.py`. This file is created automatically the first time you add a student, and updated automatically after every add/update/delete operation. Deleting `students.json` will reset the records.

## Project Structure

```
.
├── main.py          # Main program (CLI menu + all logic)
├── students.json     # Auto-generated data file (created after first run)
└── README.md         # This file
```
