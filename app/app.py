from fastapi import FastAPI

from core.environment import APP_CONTACT, APP_DEBUG, APP_DOCS_URL, APP_NAME, APP_REDOC_URL, APP_TOS
from core.version import get_version
from database import db, db_context
from models.users import User


app = FastAPI(
    title=APP_NAME,
    debug=APP_DEBUG,
    docs_url=APP_DOCS_URL,
    redoc_url=APP_REDOC_URL,
    version=get_version(),
    contact=APP_CONTACT,
    terms_of_service=APP_TOS
)


@app.on_event("startup")
async def on_startup() -> None:
    await db.create_tables()

    async with db_context():
        await User.init_admin()
