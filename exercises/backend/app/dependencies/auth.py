from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.core.security import decode_access_token
from app.models.user import User
from app.db.session import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    token_data = decode_access_token(token)
    if not token_data:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

    user = db.query(User).filter(User.email == token_data.email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
    
    return user

def require_teacher_role(token: str = Depends(oauth2_scheme)):
    try:
        token_data = decode_access_token(token)
        if token_data.role != "Teacher":
            raise HTTPException(status_code=403, detail="Forbidden: Teacher role required")
    except HTTPException as e:
        if e.status_code != 401:
            raise
        raise HTTPException(status_code=403, detail=e.detail)
