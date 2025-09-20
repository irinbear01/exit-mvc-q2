from datetime import date
from models.subject import Subject
from models.enrollment import Enrollment
from models import db

def calc_age(dob_str):  # "YYYY-MM-DD"
    y,m,d = map(int, dob_str.split("-"))
    today = date.today()
    return today.year - y - ((today.month, today.day) < (m, d))

def can_enroll(student, subject):
    # อายุ
    if calc_age(student.dob) < 15:
        return False, "อายุต้องไม่น้อยกว่า 15 ปี"

    # capacity
    if subject.capacity != -1 and subject.enrolled >= subject.capacity:
        return False, "จำนวนรับเต็มแล้ว"

    # prereq (ต้องมีเกรดในวิชาบังคับก่อน)
    if subject.prereq_id:
        g = Enrollment.query.filter_by(student_id=student.id, subject_id=subject.prereq_id).first()
        if not g or g.grade is None:
            return False, f"ยังไม่มีเกรดในวิชาบังคับก่อน {subject.prereq_id}"

    return True, ""

def do_enroll(student, subject):
    # กันลงซ้ำ
    exists = Enrollment.query.filter_by(student_id=student.id, subject_id=subject.id).first()
    if exists:
        return False, "ลงทะเบียนวิชานี้แล้ว"

    db.session.add(Enrollment(student_id=student.id, subject_id=subject.id, grade=None))
    subject.enrolled += 1
    db.session.commit()
    return True, "ลงทะเบียนสำเร็จ"
