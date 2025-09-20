from flask import Flask, render_template, request, redirect, session, url_for
from models import db
from models.student import Student
from models.subject import Subject
from models.enrollment import Enrollment
from services.registration_service import can_enroll, do_enroll

app = Flask(__name__)
app.config["SECRET_KEY"] = "exam-secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

# --------- Auth ----------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        sid = request.form.get("student_id", "").strip()
        u = Student.query.filter_by(id=sid).first()
        if not u:
            return "Invalid student ID", 400
        session["user"] = {"id": u.id, "role": u.role}
        return redirect("/register")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

def current_user():
    u = session.get("user")
    return Student.query.filter_by(id=u["id"]).first() if u else None

# --------- Views ----------
@app.route("/register")
def register_page():
    u = current_user()
    if not u: return redirect("/login")
    # รายวิชาที่ยังไม่ได้ลง
    enrolled_ids = [e.subject_id for e in Enrollment.query.filter_by(student_id=u.id).all()]
    subjects = Subject.query.filter(~Subject.id.in_(enrolled_ids)).order_by(Subject.id).all()
    return render_template("register.html", user=u, subjects=subjects)

@app.route("/subjects/<sid>")
def subject_detail(sid):
    u = current_user()
    if not u: return redirect("/login")
    subj = Subject.query.get_or_404(sid)
    return render_template("subject_detail.html", user=u, subj=subj)

@app.route("/enroll/<sid>", methods=["POST"])
def enroll(sid):
    u = current_user()
    if not u: return redirect("/login")
    subj = Subject.query.get_or_404(sid)

    ok, msg = can_enroll(u, subj)
    if not ok:
        return f"ลงทะเบียนไม่สำเร็จ: {msg}", 400

    ok, msg = do_enroll(u, subj)
    if not ok:
        return f"ลงทะเบียนไม่สำเร็จ: {msg}", 400

    # ตาม Business Rules ลงสำเร็จต้องกลับหน้าโปรไฟล์นักเรียน
    return redirect("/me")

# --------- หน้าโปรไฟล์ ----------
@app.route("/me")
def me():
    u = current_user()
    if not u: return redirect("/login")
    rows = (
        db.session.query(Subject, Enrollment.grade)
        .join(Enrollment, Enrollment.subject_id == Subject.id)
        .filter(Enrollment.student_id == u.id)
        .order_by(Subject.id)
        .all()
    )
    return render_template("me.html", user=u, rows=rows)

# --------- Bootstrap DB ครั้งแรก ----------
@app.cli.command("init-db")
def init_db():
    db.drop_all(); db.create_all()
    print("DB ready. Run: python seed.py to insert sample data")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
