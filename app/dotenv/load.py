from os.path import join

from dotenv import load_dotenv
from loguru import logger

from app.core.constant import BASE_DIR, _env


def load_environments(load_type=None):

    dotenv_path: str = join(BASE_DIR, "/dotenv")

    if load_type is None:
        raise EnvironmentError("No Environment Loaded")

    if load_type == _env.LOCAL:
        dotenv_path = join(dotenv_path, "local", ".env")
    elif load_type == _env.DEV:
        dotenv_path = join(dotenv_path, "dev", ".env")
    elif load_type == _env.DETA:
        dotenv_path = join(dotenv_path, "beta", ".env")
    elif load_type == _env.LIVE:
        dotenv_path = join(dotenv_path, "live", ".env")

    logger.debug(f"Loaded environment {dotenv_path}")

    load_dotenv(dotenv_path=dotenv_path, verbose=True)
