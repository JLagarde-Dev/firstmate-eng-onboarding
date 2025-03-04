from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.services.auth_service import login
from app.schemas.auth import Token
from app.db.session import get_db

router = APIRouter()

@router.post("/login", response_model=Token)
def login_for_access_token(email: str, password: str, db: Session = Depends(get_db)):
    return login(db, email, password)
