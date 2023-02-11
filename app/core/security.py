import hashlib
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(hashed_pw: str, pw: str) -> bool:
    return pwd_context.verify(secret=pw, hash=hashed_pw)


def hash_token(token: str) -> str:
    return hashlib.sha256(token.encode()).hexdigest()
