from fastapi import FastAPI

from core.environment import APP_CONTACT, APP_DEBUG, APP_DOCS_URL, APP_NAME, APP_REDOC_URL, APP_TOS
from core.version import get_version


app = FastAPI(
    title=APP_NAME,
    debug=APP_DEBUG,
    docs_url=APP_DOCS_URL,
    redoc_url=APP_REDOC_URL,
    version=get_version(),
    contact=APP_CONTACT,
    terms_of_service=APP_TOS
)
