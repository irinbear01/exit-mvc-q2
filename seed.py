from app import app, db
from models.student import Student
from models.subject import Subject
from models.enrollment import Enrollment

with app.app_context():
    db.drop_all(); db.create_all()

    # 10 นักเรียน + 1 แอดมิน (ID ต้องขึ้นต้น 69 และยาว 8)
    students = [
        Student(id="69000001", prefix="Mr.", first_name="Anan", last_name="Sorn",
                dob="2008-01-12", current_school="Satit A", email="anan@example.com"),
        Student(id="69000002", prefix="Ms.", first_name="Burin", last_name="Thong",
                dob="2007-05-02", current_school="Satit B", email="burin@example.com"),
        Student(id="69000003", prefix="Mr.", first_name="Chai", last_name="Korn",
                dob="2008-11-03", current_school="Satit C", email="chai@example.com"),
        Student(id="69000004", prefix="Ms.", first_name="Dao", last_name="Mek",
                dob="2009-06-21", current_school="Satit D", email="dao@example.com"),
        Student(id="69000005", prefix="Mr.", first_name="Ek", last_name="Art",
                dob="2007-12-27", current_school="Satit E", email="ek@example.com"),
        Student(id="69000006", prefix="Ms.", first_name="Fah", last_name="Nam",
                dob="2008-03-09", current_school="Satit F", email="fah@example.com"),
        Student(id="69000007", prefix="Mr.", first_name="Gun", last_name="Yod",
                dob="2007-09-18", current_school="Satit G", email="gun@example.com"),
        Student(id="69000008", prefix="Ms.", first_name="Hana", last_name="Mori",
                dob="2008-08-30", current_school="Satit H", email="hana@example.com"),
        Student(id="69000009", prefix="Mr.", first_name="Itt", last_name="Chai",
                dob="2007-02-10", current_school="Satit I", email="itt@example.com"),
        Student(id="69000010", prefix="Ms.", first_name="June", last_name="Ray",
                dob="2008-04-14", current_school="Satit J", email="june@example.com"),
        Student(id="69009999", prefix="Mr.", first_name="Admin", last_name="One",
                dob="1990-01-01", current_school="STAFF", email="admin@example.com", role="admin"),
    ]
    db.session.add_all(students)

    # 10 วิชา (มี prereq อย่างน้อย 1) — 0550xxxxx = วิชาคณะ, 9069xxxx = ศึกษาทั่วไป
    subjects = [
        Subject(id="05501001", name="Programming I",  credit=3, lecturer="Dr.A", prereq_id=None, capacity=30, enrolled=0),
        Subject(id="05501002", name="Programming II", credit=3, lecturer="Dr.A", prereq_id="05501001", capacity=30, enrolled=0),
        Subject(id="05501003", name="Discrete Math",  credit=3, lecturer="Dr.B", prereq_id=None, capacity=-1, enrolled=0),
        Subject(id="05501004", name="Data Structures",credit=3, lecturer="Dr.C", prereq_id="05501001", capacity=35, enrolled=0),
        Subject(id="05501005", name="Computer Systems",credit=3,lecturer="Dr.D",prereq_id=None, capacity=25, enrolled=0),
        Subject(id="90690001", name="Academic Writing",credit=2, lecturer="Dr.E", prereq_id=None, capacity=40, enrolled=0),
        Subject(id="90690002", name="Public Speaking", credit=2, lecturer="Dr.F", prereq_id=None, capacity=40, enrolled=0),
        Subject(id="90690003", name="Critical Thinking",credit=2,lecturer="Dr.G", prereq_id=None, capacity=-1, enrolled=0),
        Subject(id="05501006", name="Database Systems",credit=3,lecturer="Dr.H", prereq_id=None, capacity=30, enrolled=0),
        Subject(id="05501007", name="Web Development", credit=3,lecturer="Dr.I", prereq_id=None, capacity=30, enrolled=0),
    ]
    db.session.add_all(subjects)

    # ให้บางคน มีเกรด ใน Prog I เพื่อจะลง Prog II ได้
    db.session.add_all([
        Enrollment(student_id="69000001", subject_id="05501001", grade="B"),
        Enrollment(student_id="69000002", subject_id="05501001", grade="C+"),
        Enrollment(student_id="69000003", subject_id="05501001", grade="A"),
    ])
    # อัปเดต enrolled เริ่มต้น
    s = {sub.id: sub for sub in subjects}
    s["05501001"].enrolled = 3

    db.session.commit()
    print("Seed data inserted.")
