from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict, EmailStr, Field

class StudentCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    date_of_birth: date
    email: Optional[EmailStr] = None
    phone: Optional[str] = Field(default=None, max_length=30)
    course: Optional[str] = Field(default=None, max_length=100)
    address: Optional[str] = Field(default=None, max_length=255)
    enrollment_date: Optional[date] = None

class StudentUpdate(BaseModel):
    name: Optional[str] = Field(default=None, min_length=1, max_length=100)
    date_of_birth: Optional[date] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = Field(default=None, max_length=30)
    course: Optional[str] = Field(default=None, max_length=100)
    address: Optional[str] = Field(default=None, max_length=255)
    enrollment_date: Optional[date] = None

class StudentResponse(StudentCreate):
    student_id: int

    model_config = ConfigDict(from_attributes=True)