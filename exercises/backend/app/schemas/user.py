from pydantic import BaseModel, EmailStr
from typing import Optional, Literal
from uuid import UUID

class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str
    type: Literal["Student", "Teacher"]

    class Config:
        from_attributes = True
    

class UserCreate(UserBase):
    grade_level: Optional[str] = None  # Specific to Students
    present: Optional[bool] = None # Specific to Students
    subject: Optional[str] = None  # Specific to Teachers
    

class UserEdit(UserBase):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None

class UserResponse(UserBase):
    id: UUID
    type: str

class StudentEdit(UserEdit):
    grade_level: Optional[str] = None
    present: Optional[str] = None

class StudentResponse(UserResponse):
    grade_level: str


class TeacherEdit(UserEdit):
    subject: Optional[str] = None

class TeacherResponse(UserResponse):
    subject: str

