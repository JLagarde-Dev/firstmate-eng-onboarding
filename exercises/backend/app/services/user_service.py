from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate, UserEdit

def create_user(db: Session, user: UserCreate):
    db_user = User(first_name=user.first_name, last_name=user.last_name, present=user.present)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_name(db: Session, first_name: str, last_name: str):
    return db.query(User).filter(User.first_name == first_name, User.last_name == last_name).first()

def get_user_by_id(db: Session, id: str):
    return db.query(User).filter(User.id == id).first()

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

def delete_user_by_id(db: Session, user_id: int):
    db_user = db.query(User).filter(User.id == user_id).first()
    db.delete(db_user)
    db.commit()


