from pydantic import BaseModel

class UserBase(BaseModel):
    first_name: str
    last_name: str

class UserCreate(UserBase):
    present: bool


class UserEdit(UserBase):
    first_name: str | None = None
    last_name: str | None = None
    present: bool | None = None

class UserResponse(UserBase):
    id: int
    present: bool
    class Config:
        from_attributes = True
