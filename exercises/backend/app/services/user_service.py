from sqlalchemy.orm import Session
from app.models.user import User
from app.models.teacher import Teacher
from app.models.student import Student
from app.schemas.user import UserCreate, UserEdit
from fastapi import HTTPException
from app.core.security import hash_password
from uuid import UUID


def create_user(db: Session, user: UserCreate):
    hashed_pwd = hash_password(user.password)

    if user.type == "Student":
        new_user = Student(first_name=user.first_name, last_name=user.last_name, email=user.email, password=hashed_pwd, type="Student", present=user.present, grade_level=user.grade_level)
    elif user.type == "Teacher":
        new_user = Teacher(first_name=user.first_name, last_name=user.last_name, email=user.email, password=hashed_pwd, type="Teacher", subject=user.subject)
    else:
        new_user = User(username=user.username, email=user.email, password=hashed_pwd, type="Admin")

    print(new_user)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

def get_user_by_name(db: Session, first_name: str, last_name: str):
    return db.query(User).filter(User.first_name == first_name, User.last_name == last_name).first()

def get_user_by_id(db: Session, id: UUID):
    return db.query(User).filter(User.id == id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def edit_user_data(db: Session, user_id: int, user: UserEdit):
    db_user = db.query(User).filter(User.id == user_id).first()
    if user.first_name is not None:
        db_user.first_name = user.first_name
    if user.last_name is not None:
        db_user.last_name = user.last_name
    if user.present is not None:
        db_user.present = user.present
    db.commit()
    db.refresh(db_user)
    return db_user

def get_all_users(db: Session, present: bool | None):
    db_user = db.query(User).filter(User.present == present if present is not None else True).all()
    return db_user

def delete_user_by_id(db: Session, user_id: UUID):
    db_user = db.query(User).filter(User.id == user_id).first()
    db.delete(db_user)
    db.commit()


