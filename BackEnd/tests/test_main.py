from fastapi.testclient import TestClient
# Import app từ file main.py nằm ở thư mục cha
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import app

client = TestClient(app)

def test_read_message():
    # Giả lập một request GET đến API
    response = client.get("/api/message")
    
    # Kiểm tra mã trạng thái (200 OK) và dữ liệu trả về
    assert response.status_code == 200
    assert response.json() == {"message": "Hello from FastAPI Backend!"}