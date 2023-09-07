from sqlalchemy import select

from app.user.models import User
from core.db import Transactional, session


class UserRepository:
    @Transactional()
    async def save_user(self, user: User) -> None:
        session.add(user)

    async def get_find_nick_email(self, nickname: str, email: str) -> User | None:
        query = select(User).where(User.email == email, User.nickname == nickname)

        result = await session.execute(query)
        return result.scalar()
