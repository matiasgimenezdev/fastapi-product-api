from typing import Union

from pydantic import BaseModel


class User(BaseModel):
    username: str
    hashed_password: str
    email: Union[str, None] = None
    full_name: Union[str, None] = None
