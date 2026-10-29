from sqlalchemy import Column, Integer, String, Date
from database import Base

class Student(Base):
    __tablename__ = "students"

    student_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    email = Column(String(255), unique=True, index=True)
    phone = Column(String(30))
    course = Column(String(100))
    address = Column(String(255))
    enrollment_date = Column(Date)