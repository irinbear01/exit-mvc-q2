from . import db

class Enrollment(db.Model):
    __tablename__ = "enrollments"
    student_id = db.Column(db.String(8), primary_key=True)
    subject_id = db.Column(db.String(8), primary_key=True)
    grade = db.Column(db.String(2), nullable=True)  # A,B+,B,C+,C,D+,D,F หรือ None
