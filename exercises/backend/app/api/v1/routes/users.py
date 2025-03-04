from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.user import UserCreate, UserResponse, UserEdit
from app.dependencies.auth import get_current_user, require_teacher_role
from app.services.user_service import create_user, get_user_by_email, get_user_by_id, edit_user_data, get_all_users, delete_user_by_id
from uuid import UUID

router = APIRouter()

@router.get("/me", response_model=UserResponse)
def read_users_me(current_user: UserResponse = Depends(get_current_user)):
    return current_user

@router.post("/", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = get_user_by_email(db, user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="email already registered")
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

@router.delete("/{user_id}", response_model=None)
def delete_user(
    user_id: UUID,
    db: Session = Depends(get_db), 
    current_user: str = Depends(get_current_user),  # Require authentication
    _: None = Depends(require_teacher_role),  # Require Teacher role
                ):
    existing_user = get_user_by_id(db, user_id)
    if not existing_user:
        raise HTTPException(status_code=404, detail="user not found")
    delete_user_by_id(db, user_id)
    return {"detail": "user deleted successfully"}

