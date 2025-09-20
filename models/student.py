from . import db

class Student(db.Model):
    __tablename__ = "students"
    id = db.Column(db.String(8), primary_key=True)  # ต้องขึ้นต้นด้วย '69'
    prefix = db.Column(db.String(20), nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    dob = db.Column(db.String(10), nullable=False)  # YYYY-MM-DD
    current_school = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), default="student")  # 'student' 'admin'
