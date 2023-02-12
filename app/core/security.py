import hashlib

from enum import Enum, auto
from jose import jwt
from passlib.context import CryptContext

from fastapi import Depends, Request
from fastapi.security.base import SecurityBase

from .environment import ALGORITHM, SECRET_KEY
from .exceptions import InvalidTokenError, PermissionDeniedError


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class PermissionLevel(Enum):
    USER = auto()
    ADMIN = auto()


class UserAuth(SecurityBase):
    def __init__(self, min_level: PermissionLevel) -> None:
        self.model = SecurityBase()
        self.scheme_name = self.__class__.__name__
        self.min_level: PermissionLevel = min_level

    async def __call__(self, request: Request) -> bool:
        from models.users import User
        token = get_token(request)
        user = await User.get_user_by(token=token)
        if not token or not user:
            raise InvalidTokenError

        if self.min_level == PermissionLevel.ADMIN and not user.admin:
            raise PermissionDeniedError

        return True


user_auth = Depends(UserAuth(PermissionLevel.USER))
admin_auth = Depends(UserAuth(PermissionLevel.ADMIN))


def hash_password(password: str) -> str:
    return pwd_context.hash(secret=password)


def verify_password(pw: str, hashed_pw: str) -> bool:
    return pwd_context.verify(secret=pw, hash=hashed_pw)


def hash_token(token: str) -> str:
    return hashlib.sha256(token.encode()).hexdigest()


def create_access_token(data: dict):
    to_encode = data.copy()
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


def get_token(request: Request) -> str:
    authorization: str = request.headers.get("Authorization", "")
    return authorization.removeprefix("Bearer ")
