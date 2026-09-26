"""
storage.py
Functional module: Data Persistence.
Handles reading and writing student records to a JSON file on disk,
so records survive between program runs.
"""

import json
import os

DATA_FILE = "students.json"


def load_students():
    """Load the list of student records from the JSON file.
    Returns an empty list if the file doesn't exist or is unreadable.
    """
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        print("Warning: could not read existing data file. Starting with an empty list.\n")
        return []


def save_students(students):
    """Save the list of student records to the JSON file."""
    with open(DATA_FILE, "w") as f:
        json.dump(students, f, indent=4)
