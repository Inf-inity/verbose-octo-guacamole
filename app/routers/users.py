from fastapi import APIRouter, Form, Request

from core.environment import APP_ALLOW_REGISTRATION
from core.exceptions import InvalidCredentials, InvalidPassword, NameDuplicated
from core.security import create_access_token, get_token, hash_token, user_auth, verify_password
from models.users import User


router = APIRouter(tags=["users"])


@router.post("/token")
async def login(username: str = Form(min_length=2, max_length=32), password: str = Form(min_length=8, max_length=128)):
    if not (user := await User.get_user_by(name=username)) or not verify_password(password, user.password):
        raise InvalidCredentials
    token = create_access_token({"sub": username})
    user.token = hash_token(token)
    return {"access_token": token, "token_type": "bearer"}


@router.get("/users/me", dependencies=[user_auth])
async def get_me(request: Request):
    return (await User.get_user_by(token=get_token(request))).serialize


if APP_ALLOW_REGISTRATION:
    @router.post("/users/new")
    async def sign_in(
            username: str = Form(min_length=2, max_length=32),
            password: str = Form(min_length=8, max_length=128),
            second_time_password: str = Form(min_length=8, max_length=128)
    ):
        if password != second_time_password:
            raise InvalidPassword
        if await User.get_user_by(name=username):
            raise NameDuplicated
        user = await User.create(name=username, password=password)
        token = create_access_token({"sub": username})
        user.token = hash_token(token)
        return {"access_token": token, "token_type": "bearer"}
