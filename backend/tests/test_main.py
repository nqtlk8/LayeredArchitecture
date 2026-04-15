import pytest
import sys
import os
from fastapi.testclient import TestClient

# Giúp Python tìm thấy module 'backend' từ thư mục gốc
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from backend.repositories.impl.student_repository_impl import StudentRepositoryImpl
from backend.services.student_service import StudentService
from backend.main import app

client = TestClient(app)

# Sử dụng fixture để khởi tạo đối tượng (thay cho setUp trong Unittest)
@pytest.fixture
def student_resources():
    repo = StudentRepositoryImpl()
    service = StudentService()
    return repo, service

# =====================
# REPOSITORY TEST
# =====================
def test_repo_get_student(student_resources):
    repo, _ = student_resources
    student = repo.get_student_by_id(1)
    assert student is not None
    assert student.name == "Trang"

def test_repo_get_subjects(student_resources):
    repo, _ = student_resources
    subjects = repo.get_subjects_by_student(1)
    assert len(subjects) > 0

def test_repo_get_class(student_resources):
    repo, _ = student_resources
    clazz = repo.get_class_by_student(1)
    assert clazz is not None

# =====================
# SERVICE TEST
# =====================
def test_service_get_student(student_resources):
    _, service = student_resources
    result = service.get_student_info(1)
    assert result is not None
    assert "student" in result
    assert "subjects" in result

def test_service_not_found(student_resources):
    _, service = student_resources
    result = service.get_student_info(999)
    assert result is None

# =====================
# CONTROLLER TEST
# =====================
def test_api_success():
    response = client.get("/student/1")
    assert response.status_code == 200
    data = response.json()
    assert "student" in data
    assert "subjects" in data
    assert "classmates" in data

def test_api_not_found():
    response = client.get("/student/999")
    assert response.status_code == 404
