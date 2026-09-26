# Problem Statement

## Problem

Educational institutions and individual students often need a simple way to keep track of student records — names, ages, courses, and marks — without relying on spreadsheets that are easy to accidentally overwrite, or full database systems that are overkill for small-scale use. This project addresses that gap with a lightweight, dependency-free command-line tool.

## Scope

This project is a command-line Student Record Management System that allows a user to add, view, update, delete, and search student records. Data is persisted locally in a JSON file, so records are retained between sessions without requiring a database server or internet connection.

The scope is intentionally focused: single-user, local storage, and a text-based interface, in line with the tools and concepts covered in a Python Essentials course (functions, data structures, file handling, exception handling, and modular program design).

## Target Users

- Individual students or small course instructors who need to track a small set of student records without setting up a database.
- Learners studying Python who want a reference example of a modular, testable CLI application.

## High-Level Features

- **Add** a new student record (ID, Name, Age, Course, Marks), with validation on ID uniqueness, age range, and marks range.
- **View** all student records in a formatted table.
- **Update** an existing record, changing only the fields provided.
- **Delete** a record, with confirmation before removal.
- **Search** for a record by ID or partial name match.
- **Persistent storage**: all changes are automatically saved to a local JSON file.
- **Modular design**: the project is split into a data model, a persistence layer, a business-logic layer, and a CLI layer, each independently testable.
- **Automated tests**: core record operations are covered by unit tests.
