from . import db

class Subject(db.Model):
    __tablename__ = "subjects"
    id = db.Column(db.String(8), primary_key=True)   # '0550xxxxx' หรือ '9069xxxx'
    name = db.Column(db.String(200), nullable=False)
    credit = db.Column(db.Integer, nullable=False)   # > 0
    lecturer = db.Column(db.String(200), nullable=False)
    prereq_id = db.Column(db.String(8), nullable=True)  # รหัสวิชาบังคับก่อน (ถ้ามี)
    capacity = db.Column(db.Integer, nullable=False, default=-1)  # -1 = ไม่จำกัด
    enrolled = db.Column(db.Integer, nullable=False, default=0)   # ≥ 0
