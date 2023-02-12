from os import getenv


def get_bool(key: str, default: bool) -> bool:
    return getenv(key, str(default)).lower() == "true"


def get_optional(key: str, default: str | bool | None) -> str | bool | None:
    res = getenv(key, str(default)).lower()
    if res == "none":
        return None
    elif res in ("true", "false"):
        return res == "true"
    else:
        return res


LOG_LEVEL: str = getenv("LOG_LEVEL", "INFO").lower()
VERSION: str = getenv("VERSION", "0.0.0")
SHOW_COMMIT: bool = get_bool("SHOW_COMMIT", True)

APP_TOS: str | None = get_optional("APP_TOS", None)
APP_CONTACT: dict[str, str] | None = {
    "Contact": str(get_optional("APP_CONTACT", None))
} if get_optional("APP_CONTACT", None) is not None else None
APP_HOST: str = getenv("APP_HOST", "0.0.0.0")
APP_PORT: int = int(getenv("APP_PORT", 8000))
APP_NAME: str = getenv("APP_NAME", "FastAPI")
APP_RELOAD: bool = get_bool("APP_RELOAD", False)
APP_DEBUG: bool = get_bool("APP_DEBUG", False)
APP_DOCS_URL: str | None = get_optional("APP_DOCS_URL", "/docs")
APP_REDOC_URL: str | None = get_optional("APP_REDOC_URL", "/redocs")
APP_ALLOW_REGISTRATION: bool = get_bool("APP_ALLOW_REGISTRATION", False)
SECRET_KEY: str = getenv("SECRET_KEY", None)
ALGORITHM: str = getenv("ALGORITHM", "HS256")

APP_ADMIN_USERNAME: str = getenv("APP_ADMIN_USERNAME", "admin")
APP_ADMIN_PASSWORD: str = getenv("APP_ADMIN_PASSWORD", "password")

DB_DRIVER: str = getenv("DB_DRIVER", "postgresql+asyncpg")
POSTGRES_HOST: str = getenv("POSTGRES_HOST", "main_db")
POSTGRES_PORT: int = int(getenv("POSTGRES_PORT", 5432))
POSTGRES_USER: str = getenv("POSTGRES_USER", "admin")
POSTGRES_PASSWORD: str = getenv("POSTGRES_PASSWORD", "password")
POSTGRES_DB: str = getenv("POSTGRES_DB", "db")

REDIS_HOST: str = getenv("REDIS_HOST", "redis")
REDIS_PORT: int = int(getenv("REDIS_PORT", 6379))
REDIS_CACHE_TTL: int = int(getenv("REDIS_CACHE_TTL", 300))
