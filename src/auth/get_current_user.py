from typing import Annotated

from fastapi import Depends
from models.user import User
from fastapi.security import OAuth2PasswordBearer
from data.users import users


# ? https://fastapi.tiangolo.com/tutorial/security/
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/user/token")


def get_user(username: str):
    if username in users:
        user = users[username]
        return user
    return None


def decode_token(token):
    user = get_user(token)
    return user


def fake_hash_password(password: str):
    return "fakehashed" + password


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = decode_token(token)
    return user
