# models.py file will describe the content of your database.
# 
# # Models container the general schema structure of the
# underlying sqllite database.

# - This inform the response after a success POST or GET request.
# - SQLlite will generate a table for every class and use the "__tablename__" attribute
# for the tablename.

import datetime as dt

from sqlalchemy import Boolean, Column, DateTime, Integer, String

from .database import Base


class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    user_name = Column(String, unique=True)
    first_name = Column(
        String,
    )
    last_name = Column(
        String,
    )
    last_modified = Column(DateTime, default=dt.datetime.now())
    is_active = Column(Boolean, default=True)
