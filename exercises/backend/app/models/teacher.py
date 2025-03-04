from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.session import Base
from app.models.user import User

class Teacher(User):
    __tablename__ = "teachers"

    id = Column(String, ForeignKey("users.id"), primary_key=True)
    subject = Column(String)

    __mapper_args__ = {"polymorphic_identity": "Teacher"}