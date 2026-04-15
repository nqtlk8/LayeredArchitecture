from backend.database.db import get_connection

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    # XÓA DATA CŨ (tránh duplicate)
    cursor.execute("DROP TABLE IF EXISTS StudentSubject")
    cursor.execute("DROP TABLE IF EXISTS Student")
    cursor.execute("DROP TABLE IF EXISTS Subject")
    cursor.execute("DROP TABLE IF EXISTS Class")

    # CREATE TABLE
    cursor.execute("""
    CREATE TABLE Class (
        id INTEGER PRIMARY KEY,
        name TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE Student (
        id INTEGER PRIMARY KEY,
        name TEXT,
        class_id INTEGER,
        FOREIGN KEY (class_id) REFERENCES Class(id)
    )
    """)

    cursor.execute("""
    CREATE TABLE Subject (
        id INTEGER PRIMARY KEY,
        name TEXT,
        class_id INTEGER,
        FOREIGN KEY (class_id) REFERENCES Class(id)
    )
    """)

    cursor.execute("""
    CREATE TABLE StudentSubject (
        student_id INTEGER,
        subject_id INTEGER,
        PRIMARY KEY (student_id, subject_id)
    )
    """)

    # INSERT CLASS
    classes = [
        (1, "SE2023"),
        (2, "SE2024")
    ]
    cursor.executemany("INSERT INTO Class VALUES (?, ?)", classes)

    # INSERT STUDENT
    students = [
        (1, "Trang", 1),
        (2, "An", 1),
        (3, "Binh", 1),
        (4, "Linh", 2),
        (5, "Huy", 2)
    ]
    cursor.executemany("INSERT INTO Student VALUES (?, ?, ?)", students)

    # INSERT SUBJECT
    subjects = [
        (1, "Math", 1),
        (2, "English", 1),
        (3, "Programming", 1),
        (4, "Database", 2),
        (5, "AI", 2)
    ]
    cursor.executemany("INSERT INTO Subject VALUES (?, ?, ?)", subjects)

    # INSERT STUDENT - SUBJECT
    student_subjects = [
        (1, 1), (1, 2), (1, 3),
        (2, 1), (2, 2),
        (3, 2), (3, 3),
        (4, 4), (4, 5),
        (5, 4)
    ]
    cursor.executemany("INSERT INTO StudentSubject VALUES (?, ?)", student_subjects)

    conn.commit()
    conn.close()

    print("Database initialized with sample data!")

if __name__ == "__main__":
    init_db()