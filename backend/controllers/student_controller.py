from fastapi import APIRouter, HTTPException
from backend.services.student_service import StudentService

router = APIRouter()
service = StudentService()

@router.get("/student/{student_id}")
def get_student(student_id: int):
    if student_id <= 0:
        raise HTTPException(status_code=400, detail="Invalid student ID")

    try:
        result = service.get_student_info(student_id)

        if result is None:
            raise HTTPException(status_code=404, detail="Student not found")

        return result

    except HTTPException:
        raise 

    except Exception as e:
        print("Error:", e)
        raise HTTPException(status_code=500, detail="Internal Server Error")