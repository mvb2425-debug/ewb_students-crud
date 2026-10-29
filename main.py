from fastapi import FastAPI, Depends, HTTPException, Response
from sqlalchemy.orm import Session

from database import Base, engine, get_db
from models import Student
from schemas import StudentCreate, StudentUpdate, StudentResponse

Base.metadata.create_all(bind=engine)

app = FastAPI(title="EWB Students CRUD API")

@app.get("/")
def home():
    return {"message": "Welcome to EWB Students CRUD API"}

@app.post("/students", response_model=StudentResponse, status_code=201)
def create_student(student_data: StudentCreate, db: Session = Depends(get_db)):
    if student_data.email:
        existing = db.query(Student).filter(
            Student.email == student_data.email
        ).first()

        if existing:
            raise HTTPException(status_code=409, detail="Email already exists")

    student = Student(**student_data.model_dump())
    db.add(student)
    db.commit()
    db.refresh(student)
    return student

@app.get("/students", response_model=list[StudentResponse])
def get_students(db: Session = Depends(get_db)):
    return db.query(Student).order_by(Student.student_id).all()

@app.get("/students/{student_id}", response_model=StudentResponse)
def get_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(
        Student.student_id == student_id
    ).first()

    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    return student

@app.patch("/students/{student_id}", response_model=StudentResponse)
def update_student(
    student_id: int,
    student_data: StudentUpdate,
    db: Session = Depends(get_db)
):
    student = db.query(Student).filter(
        Student.student_id == student_id
    ).first()

    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    changes = student_data.model_dump(exclude_unset=True)

    if changes.get("email"):
        duplicate = db.query(Student).filter(
            Student.email == changes["email"],
            Student.student_id != student_id
        ).first()

        if duplicate:
            raise HTTPException(status_code=409, detail="Email already exists")

    for field, value in changes.items():
        setattr(student, field, value)

    db.commit()
    db.refresh(student)
    return student

@app.delete("/students/{student_id}", status_code=204)
def delete_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(
        Student.student_id == student_id
    ).first()

    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    db.delete(student)
    db.commit()
    return Response(status_code=204)