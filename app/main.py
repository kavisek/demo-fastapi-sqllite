import logging

import numpy as np
import pandas as pd
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.config import *
from app.database import SessionLocal, engine
from fastapi import Depends, FastAPI

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s",
)

log = logging.getLogger(__name__)

# Start API
app = FastAPI()

# Create SQLlite database
models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return f"Welcome to the test API"


@app.post("/user", response_model=schemas.Users)
def create_user(user: schemas.Users, db: Session = Depends(get_db)):
    """Send a request to create a user.

    Args:
        user (schemas.Users): pydantic user class
        db (Session, optional): sqlalchemy local session. Defaults to Depends(get_db).

    Returns:
        _type_: pydantic user class
    """
    # if not validators.url(url.target_url):
    #     raise_bad_request(message="Your provided URL is not valid")

    db_user = crud.create_db_user(db=db, user=user)
    # db_url.url = db_url.key
    # db_url.admin_url = db_url.secret_key

    return db_user


@app.get("/users")
def get_users(db: Session = Depends(get_db)):

    result = db.query(models.Users)
    users = result.all()

    json_data = {}
    for user in users:
        log.info(vars(user))
        json_data[user.user_name] = {
            "first_name": user.first_name,
            "last_name": user.last_name,
        }
    return json_data
