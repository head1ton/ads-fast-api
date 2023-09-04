from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
    async_sessionmaker,
)

from app.core.config import settings

DB_URL = "mysql+aiomysql://{}:{}@{}:{}/{}".format(
    settings.MYSQL_USER,
    settings.MYSQL_PASSWORD,
    settings.MYSQL_HOST,
    settings.MYSQL_PORT,
    settings.MYSQL_DB,
)

async_engine = create_async_engine(DB_URL, echo=True, pool_pre_ping=True)
SessionFactory = async_sessionmaker(async_engine, expire_on_commit=False)


async def get_async_db() -> AsyncSession:
    async with SessionFactory() as session:
        try:
            yield session
        except SQLAlchemyError as e:
            await session.rollback()
            raise e
        finally:
            await session.close()


_db = get_async_db()
