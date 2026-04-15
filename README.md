# Student Management System

## Mô tả
Đây là ứng dụng nhỏ dùng để tra cứu thông tin sinh viên theo ID. Hệ thống hiển thị thông tin sinh viên, danh sách môn học và các sinh viên cùng lớp. Dự án sử dụng kiến trúc Layered Architecture (controller, service, repository) với Python (FastAPI), SQLite và HTML/JavaScript.

## Cài đặt và chạy
Clone project:
git clone <repo-url>
cd LayeredArchitecture

Tạo và kích hoạt môi trường:
python -m venv venv
venv\Scripts\activate

Cài thư viện:
pip install -r backend/requirements.txt

Khởi tạo database:
python -m backend.database.init_db

Chạy backend:
uvicorn backend.main:app --reload

Mở frontend bằng Live Server và truy cập trình duyệt.

## Cách sử dụng
Nhập ID sinh viên (ví dụ: 1), nhấn "Tìm" để xem thông tin, môn học và danh sách cùng lớp.

## Test
python -m unittest backend/tests/test_main.py

## Thành viên
Nguyễn Quốc Thắng
Võ Thị Bình
Lê Thị Mai Trang

## Tham khảo
FastAPI, Python unittest

## License
Dùng cho mục đích học tập.
