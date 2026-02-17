from fastapi import FastAPI, HTTPException
from sqlmodel import Field, Session, SQLModel, create_engine, select
from datetime import datetime
from typing import Optional
import os

# connect to db
postgres_url = os.environ["DATABASE_URL"]

# build app
app = FastAPI()


# health checks
@app.get("/")
def read_root():
    return {"status": "Backend is Online", "framework": "FastAPI"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


# sqlmodel class setups


class student(SQLModel, table=True):
    def __init__(self):
        id: Optional[int] = Field(default=None, primary_key=True)
        first_name: str
        last_name: str
        email: str = Field(unique=True, index=True)
        date_added: datetime
        age: Optional[int] = None
        bio: Optional[str] = None
        subjects: Optional[list]
