from fastapi import FastAPI
from app.core.database import engine, wait_for_db
from app.models.base import Base

from app.models import user, project, task

app = FastAPI()

wait_for_db()

Base.metadata.create_all(bind=engine)
@app.get("/")
def health_check():
    return {"status": "ok"}