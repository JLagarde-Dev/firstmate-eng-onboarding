import uuid
from sqlalchemy import Column, String, TIMESTAMP, func
from sqlalchemy.dialects.postgresql import UUID
from app.db.session import Base

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)  # ✅ Use PostgreSQL UUID
    first_name = Column(String, index=True, nullable=False)
    last_name = Column(String, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    type = Column(String, nullable=False)

    created_at = Column(TIMESTAMP, server_default=func.now())  # ✅ Use TIMESTAMP instead of Integer
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())  # ✅ Fix onupdate

    __mapper_args__ = {
        "polymorphic_identity": "user",
        "polymorphic_on": type,
    }
