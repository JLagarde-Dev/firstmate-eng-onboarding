from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.routes import users
from app.db.session import engine, Base

Base.metadata.create_all(bind=engine)  # Ensure tables exist

app = FastAPI(title="FastAPI PostgreSQL REST API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to a list of origins you want to allow
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router, prefix="/users", tags=["users"])
