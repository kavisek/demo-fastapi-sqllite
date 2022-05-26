# SQL LITE CRUD Operations.

# The following function perform CRUD operations on the database.
from sqlalchemy.orm import Session

from . import models, schemas


def create_db_user(db: Session, user: schemas.Users):
    """Add a database user to the database."""
    db_user = models.Users(
        user_name=user.user_name, first_name=user.first_name, last_name=user.last_name
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
