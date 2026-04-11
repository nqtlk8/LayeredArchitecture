# --- PHẦN CODE LOGIC ---
def get_message():
    return "Hello from Backend"

# --- PHẦN UNIT TEST ---
# Pytest sẽ tự động tìm và chạy các hàm bắt đầu bằng chữ "test_"
def test_get_message():
    assert get_message() == "Hello from Backend"