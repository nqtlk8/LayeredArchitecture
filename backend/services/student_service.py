from backend.repositories.impl.student_repository_impl import StudentRepositoryImpl

class StudentService:

    def __init__(self):
        self.repo = StudentRepositoryImpl()

    def get_student_info(self, student_id):
        student = self.repo.get_student_by_id(student_id)
        if not student:
            return None

        subjects = self.repo.get_subjects_by_student(student_id)
        clazz = self.repo.get_class_by_student(student_id)

        # 🔥 thêm classmates
        classmates = self.repo.get_students_by_class(student.class_id)

        return {
            "student": {
                "id": student.id,
                "name": student.name,
                "class": clazz.name if clazz else None
            },
            "subjects": [
                {"id": s.id, "name": s.name} for s in subjects
            ],
            "classmates": [
                {
                    "id": s.id,
                    "name": s.name,
                    "class": clazz.name if clazz else None
                }
                for s in classmates
            ]
        }