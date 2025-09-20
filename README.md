# exit-mvc-q2
เลือกทำข้อที่ 2

## รายละเอียดโปรเจกต์
ภาษาและเทคโนโลยีที่ใช้
Python 3 + Flask
SQLite (ฐานข้อมูลจำลอง)
Jinja2 Template (View)
โครงสร้างแบบ MVC
Model: จัดการ Student, Subject, Enrollment
Controller: ควบคุมการ Login, Register, Enroll, Profile
View: หน้า /login, /register, /subjects/<id>, /me

## วิธีรันระบบ
1. สร้าง virtual environment และติดตั้ง dependency
python3 -m venv .venv
source .venv/bin/activate   # macOS/Linux
.venv\Scripts\activate    # Windows

pip install Flask Flask-SQLAlchemy Flask-Login
2. python seed.py
3. python app.py
4. เปิดเว็บเบราว์เซอร์ไปที่ http://127.0.0.1:5000/login

## การใช้งาน
### Login
กรอกรหัสนักเรียน เช่น 69000001 (ข้อมูลมาจาก seed.py)
### Register Page (/register)
แสดงรายวิชาที่ยังไม่ได้ลงทะเบียน
กด ลงทะเบียน เพื่อเข้าสู่ระบบ
### Subject Detail (/subjects/<id>)
แสดงข้อมูลวิชา: ชื่อ, หน่วยกิต, อาจารย์, capacity, prereq
### Enroll & Redirect (/me)
ถ้าลงทะเบียนสำเร็จจะ redirect ไปหน้าโปรไฟล์
แสดงรายวิชาที่ลงแล้ว พร้อมเกรด (ถ้ามี)
