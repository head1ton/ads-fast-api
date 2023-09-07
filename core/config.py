import os

from pydantic_settings import BaseSettings


class Config(BaseSettings):
    ENV: str = "development"
    DEBUG: bool = True
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000
    DB_URL: str = f"mysql+aiomysql://testadmin:Devmysql1234!@localhost:3306/testdb"
    JWT_SECRET_KEY: str = "adsapi0123456789AbCdEfGhIjLmNoPqRsTuVwXyZ"
    JWT_ALGORITHM: str = "HS256"
    SENTRY_SDN: str = "None"
    CELERY_BROKER_URL: str = "amqp://user:bitnami@localhost:5672/"
    CELERY_BACKEND_URL: str = "redis://:password@localhost6379/0"
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379


class DevelopmentConfig(Config):
    DB_URL: str = f"mysql+aiomysql://testadmin:Devmysql1234!@localhost:3306/testdb"
    REDIS_HOST: str = "redis"
    REDIS_PORT: int = 6379


class LocalConfig(Config):
    DB_URL: str = f"mysql+aiomysql://testadmin:Devmysql1234!@localhost:3306/testdb"


class ProductionConfig(Config):
    DEBUG: str = "False"
    DB_URL: str = f"mysql+aiomysql://testadmin:Devmysql1234!@localhost:3306/testdb"


def get_config():
    env = os.getenv("ENV", "local")
    config_type = {
        "local": LocalConfig(),
        "dev": DevelopmentConfig(),
        "prod": ProductionConfig(),
    }
    return config_type[env]


config: Config = get_config()
