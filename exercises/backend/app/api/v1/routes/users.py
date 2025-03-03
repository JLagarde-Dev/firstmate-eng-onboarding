from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import create_user, get_user_by_name

router = APIRouter()

@router.post("/", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = get_user_by_name(db, user.first_name, user.last_name)
    if existing_user:
        raise HTTPException(status_code=400, detail="user already registered")
    return create_user(db, user)
