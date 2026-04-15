from backend.repositories.interfaces.student_repository import IStudentRepository
from backend.repositories.entities.student import Student
from backend.repositories.entities.subject import Subject
from backend.repositories.entities.class_model import ClassModel
from backend.database.db import get_connection


class StudentRepositoryImpl(IStudentRepository):

    def get_student_by_id(self, student_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT id, name, class_id FROM Student WHERE id = ?",
            (student_id,)
        )
        row = cursor.fetchone()
        conn.close()

        if row:
            return Student(*row)
        return None


    def get_subjects_by_student(self, student_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT s.id, s.name, s.class_id
            FROM Subject s
            JOIN StudentSubject ss ON s.id = ss.subject_id
            WHERE ss.student_id = ?
        """, (student_id,))

        rows = cursor.fetchall()
        conn.close()

        return [Subject(*row) for row in rows]


    def get_class_by_student(self, student_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT c.id, c.name
            FROM Class c
            JOIN Student s ON c.id = s.class_id
            WHERE s.id = ?
        """, (student_id,))

        row = cursor.fetchone()
        conn.close()

        if row:
            return ClassModel(*row)
        return None
    
    def get_students_by_class(self, class_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT id, name, class_id FROM Student WHERE class_id = ?", (class_id,))
        rows = cursor.fetchall()

        conn.close()

        return [Student(id=row[0], name=row[1], class_id=row[2]) for row in rows]