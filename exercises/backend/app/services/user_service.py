from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate

def create_user(db: Session, user: UserCreate):
    db_user = User(first_name=user.first_name, last_name=user.last_name, present=user.present)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_name(db: Session, first_name: str, last_name: str):
    return db.query(User).filter(User.first_name == first_name, User.last_name == last_name).first()
