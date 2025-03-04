from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from app.db.session import Base
from app.models.user import User

class Student(User):
    __tablename__ = "students"

    id = Column(String, ForeignKey("users.id"), primary_key=True)
    grade_level = Column(String)
    present = Column(Boolean)

    __mapper_args__ = {"polymorphic_identity": "Student"}