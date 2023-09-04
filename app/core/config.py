from distutils.util import strtobool
from functools import lru_cache
from os import getenv

from pydantic_settings import BaseSettings

from app.core.constant import _env
from app.dotenv.load import load_environments


class Settings(BaseSettings):

    # FastAPI Settings
    FASTAPI_HOST: str = getenv("FASTAPI_HOST", "0.0.0.0")
    FASTAPI_PORT: str = getenv("FASTAPI_PORT", "8888")
    FASTAPI_LOG_LEVEL: str = getenv("FASTAPI_LOG_LEVEL", "error")
    FASTAPI_RELOAD: bool = strtobool(getenv("FASTAPI_RELOAD", "True"))
    FASTAPI_DEBUG: bool = strtobool(getenv("FASTAPI_DEBUG", "True"))
    FASTAPI_CORS_ORIGINS: str = getenv("FASTAPI_CORS_ORIGINS", "['*']")

    # DB Settings
    MYSQL_HOST: str = getenv("MYSQL_HOST", "localhost")
    MYSQL_PORT: str = getenv("MYSQL_PORT", "3306")
    MYSQL_USER: str = getenv("MYSQL_USER", "testadmin")
    MYSQL_PASSWORD: str = getenv("MYSQL_PASSWORD", "MYSQL_PASSWORD")
    MYSQL_DB: str = getenv("MYSQL_DB", "MYSQL_DB")
    MYSQL_CHARSET: str = getenv("MYSQL_CHARSET", "utf-8")
    MYSQL_DEBUG: str = getenv("MYSQL_DEBUG", "False")
    MYSQL_ENABLE_SSL: str = getenv("MYSQL_ENABLE_SSL", "False")

    # JWT Setting
    ALGORITHM: str = "HS256"
    SECRET_KEY: str = getenv("SECRET_KEY", "SECRET_KEY")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7 * 4  # 28 days
    EMAIL_RESET_TOKEN_EXPIRE_MILLISECOND: int = 60 * 24 * 7 * 4 * 3

    class Config:
        case_sensitive = True
        env_file_encoding = "utf-8"


@lru_cache
def load_settings():
    deploy_type = _env.LOCAL  # 개발 환경 설정

    load_environments(load_type=deploy_type)

    settings = Settings()

    return settings


settings = load_settings()
