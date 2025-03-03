from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.user import UserCreate, UserResponse, UserEdit
from app.services.user_service import create_user, get_user_by_name, get_user_by_id, edit_user_data, get_all_users

router = APIRouter()

@router.post("/", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = get_user_by_name(db, user.first_name, user.last_name)
    if existing_user:
        raise HTTPException(status_code=400, detail="user already registered")
    return create_user(db, user)


@router.get("/", response_model=list[UserResponse])
def get_users(present: bool | None = None, db: Session = Depends(get_db)):
    return get_all_users(db, present)

@router.put("/{user_id}", response_model=UserResponse)
def edit_user(id: str, user: UserEdit, db: Session = Depends(get_db)):
    existing_user = get_user_by_id(db, id)
    if not existing_user:
        raise HTTPException(status_code=404, detail="user not found")
    return edit_user_data(db, id, user)
