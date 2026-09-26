# Design Diagrams

This document contains the system architecture, workflow, and UML diagrams for the Student Record Management System. Diagrams are written in Mermaid syntax and render automatically on GitHub.

## 1. System Architecture Diagram

Shows how the four main modules relate to each other and to the data file.

```mermaid
graph TD
    User([User]) -->|Menu input| CLI[cli.py<br/>CLI Module]
    CLI -->|calls| OPS[operations.py<br/>Record Management Module]
    CLI -->|calls| STORE[storage.py<br/>Data Persistence Module]
    OPS -->|uses| MODEL[student.py<br/>Data Model Module]
    STORE -->|reads/writes| FILE[(students.json)]
    OPS -->|operates on| DATA[In-memory student list]
    STORE -->|loads into / saves from| DATA
```

## 2. Process Flow / Workflow Diagram

Shows the overall flow when the program runs.

```mermaid
flowchart TD
    Start([Start Program]) --> Load[Load students from students.json]
    Load --> Menu{Display Menu}
    Menu -->|1| Add[Add Student]
    Menu -->|2| View[View All Students]
    Menu -->|3| Update[Update Student]
    Menu -->|4| Delete[Delete Student]
    Menu -->|5| Search[Search Student]
    Menu -->|6| Exit([Exit Program])
    Add --> Save[Save to students.json]
    Update --> Save
    Delete --> Save
    Save --> Menu
    View --> Menu
    Search --> Menu
```

## 3. Use Case Diagram

Shows the interactions available to the single user role of this system.

```mermaid
graph LR
    User([User])
    User --> UC1[Add Student]
    User --> UC2[View Students]
    User --> UC3[Update Student]
    User --> UC4[Delete Student]
    User --> UC5[Search Student]
```

## 4. Class / Component Diagram

Since this project uses functions and dictionaries rather than classes, this diagram represents the modules as components and shows their key functions and dependencies.

```mermaid
classDiagram
    class student_py {
        +create_student(id, name, age, course, marks) dict
        +validate_age(age) bool
        +validate_marks(marks) bool
        +format_student_row(s) str
        +format_table_header() str
    }

    class storage_py {
        +load_students() list
        +save_students(students) void
    }

    class operations_py {
        +find_student_by_id(students, id) dict
        +add_student(students, ...) tuple
        +update_student(students, id, ...) tuple
        +delete_student(students, id) tuple
        +search_students(students, term) list
    }

    class cli_py {
        +handle_add() void
        +handle_view() void
        +handle_update() void
        +handle_delete() void
        +handle_search() void
        +run() void
    }

    cli_py --> operations_py : calls
    cli_py --> storage_py : calls
    cli_py --> student_py : calls (formatting)
    operations_py --> student_py : uses (create/validate)
```

## 5. Sequence Diagram — "Add Student" flow

Shows the sequence of calls when a user adds a new student record.

```mermaid
sequenceDiagram
    actor User
    participant CLI as cli.py
    participant OPS as operations.py
    participant MODEL as student.py
    participant STORE as storage.py
    participant FILE as students.json

    User->>CLI: Selects "1. Add Student"
    CLI->>User: Prompts for ID, Name, Age, Course, Marks
    User->>CLI: Provides input
    CLI->>OPS: add_student(students, id, name, age, course, marks)
    OPS->>MODEL: validate_age(age), validate_marks(marks)
    MODEL-->>OPS: True / False
    OPS->>MODEL: create_student(...)
    MODEL-->>OPS: student dict
    OPS-->>CLI: (success, message)
    CLI->>STORE: save_students(students)
    STORE->>FILE: write JSON
    CLI->>User: Display result message
```
