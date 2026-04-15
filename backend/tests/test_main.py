import unittest
from backend.repositories.impl.student_repository_impl import StudentRepositoryImpl
from backend.services.student_service import StudentService
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)


class TestBackend(unittest.TestCase):

    def setUp(self):
        self.repo = StudentRepositoryImpl()
        self.service = StudentService()

    # =====================
    # REPOSITORY TEST
    # =====================
    def test_repo_get_student(self):
        student = self.repo.get_student_by_id(1)
        self.assertIsNotNone(student)
        self.assertEqual(student.name, "Trang")

    def test_repo_get_subjects(self):
        subjects = self.repo.get_subjects_by_student(1)
        self.assertTrue(len(subjects) > 0)

    def test_repo_get_class(self):
        clazz = self.repo.get_class_by_student(1)
        self.assertIsNotNone(clazz)

    # =====================
    # SERVICE TEST
    # =====================
    def test_service_get_student(self):
        result = self.service.get_student_info(1)

        self.assertIsNotNone(result)
        self.assertIn("student", result)
        self.assertIn("subjects", result)

    def test_service_not_found(self):
        result = self.service.get_student_info(999)
        self.assertIsNone(result)

    # =====================
    # CONTROLLER TEST
    # =====================
    def test_api_success(self):
        response = client.get("/student/1")

        self.assertEqual(response.status_code, 200)
        data = response.json()

        self.assertIn("student", data)
        self.assertIn("subjects", data)
        self.assertIn("classmates", data)

    def test_api_not_found(self):
        response = client.get("/student/999")
        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()