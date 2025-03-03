from pydantic import BaseModel

class UserBase(BaseModel):
    first_name: str
    last_name: str

class UserCreate(UserBase):
    present: bool

class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True
