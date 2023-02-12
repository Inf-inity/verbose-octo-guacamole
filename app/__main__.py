from uvicorn import run

from core.environment import APP_HOST, APP_PORT, APP_RELOAD, LOG_LEVEL, SECRET_KEY


if __name__ == "__main__":
    if not SECRET_KEY:
        raise ValueError("Missing environment var 'SECRET_KEY'")
    run("app:app", host=APP_HOST, port=APP_PORT, reload=APP_RELOAD, log_level=LOG_LEVEL)
