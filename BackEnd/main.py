# backend/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Cho phép Frontend gọi API mà không bị chặn lỗi CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_methods=["*"],
)

def get_message():
    return "Hello from Backend"

@app.get("/api/message")
def read_message():
    return {"message": get_message()}

# --- PHẦN UNIT TEST (Pytest vẫn chạy bình thường) ---
def test_get_message():
    assert get_message() == "Hello from Backend"