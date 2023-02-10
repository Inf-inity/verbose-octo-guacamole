from __future__ import annotations

from datetime import datetime
from typing import Any

from sqlalchemy import BigInteger, Boolean, Column, DateTime, String
from sqlalchemy.orm import Mapped

from core.environment import APP_ADMIN_USERNAME, APP_ADMIN_PASSWORD
from database import Base, db, select


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = Column(BigInteger, primary_key=True, unique=True, autoincrement=True)
    name: Mapped[str] = Column(String(32), unique=True)
    password: Mapped[str] = Column(String(256))
    registration: Mapped[datetime] = Column(DateTime)
    enabled: Mapped[bool] = Column(Boolean, default=True)
    admin: Mapped[bool] = Column(Boolean, default=False)
    token: Mapped[str] | str | None = Column(String(256), default=None, nullable=True, unique=True)

    @staticmethod
    async def create(name: str, password: str | None = None, enabled: bool = True, admin: bool = False) -> User:
        user = User(
            name=name, password=password, registration=datetime.utcnow(), enabled=enabled, admin=admin
        )
        await db.add(user)
        return user

    @staticmethod
    async def init_admin() -> User | None:
        if await db.exists(select(User)):
            return

        user = await User.create(name=APP_ADMIN_USERNAME, password=APP_ADMIN_PASSWORD, enabled=True, admin=True)
        return user

    async def remove(self):
        await db.delete(self)

    @property
    def serialize(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "registration": self.registration.timestamp(),
            "enabled": self.enabled,
            "admin": self.admin,
        }
