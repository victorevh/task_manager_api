import time
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError


DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)


def wait_for_db():
    while True:
        try:
            with engine.connect() as connection:
                print("db connected!")
                break
        except OperationalError:
            print("waiting db...")
            time.sleep(2)