# Schemas Clases inform type checking of the input data of each request.
#
# - These are used to inform the type annotations in or python GET and POST reques functions.
# - The type hinting also show up in the API docs
# - This is class we populate with the request information before we send it the ORM.

from pydantic import BaseModel


class Users(BaseModel):
    user_name: str
    first_name: str
    last_name: str

    class Config:
        orm_mode = True
