from uvicorn import run

from core.environment import APP_HOST, APP_PORT, APP_RELOAD, LOG_LEVEL


if __name__ == "__main__":
    run("app:app", host=APP_HOST, port=APP_PORT, reload=APP_RELOAD, log_level=LOG_LEVEL)
