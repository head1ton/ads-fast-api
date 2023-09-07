from typing import Optional, List

import bcrypt
from sqlalchemy import select

from app.user.models import User
from app.user.repository.user import UserRepository
from common.exceptions import (
    PasswordDoesNotMatchException,
    DuplicateEmailOrNicknameException,
)
from core.db import session


class UserService:
    encoding: str = "UTF-8"

    def __init__(self):
        ...

    async def get_user_list(
        self,
        limit: int = 12,
        prev: Optional[int] = None,
    ) -> List[User]:
        query = select(User)

        if prev:
            query = query.where(User.id < prev)

        if limit > 12:
            limit = 12

        query = query.limit(limit)
        result = await session.execute(query)
        return result.scalars().all()

    async def create_user(
        self,
        email: str,
        password1: str,
        password2: str,
        nickname: str,
    ) -> None:
        # logger.debug(f"email : {email}, password1 : {password1}, nickname : {nickname}")
        if password1 != password2:
            raise PasswordDoesNotMatchException

        user = await UserRepository().get_find_nick_email(
            email=email, nickname=nickname
        )

        if user:
            raise DuplicateEmailOrNicknameException

        hashed_password: str = self.hash_password(plain_password=password1)

        user: User = User(email=email, password=hashed_password, nickname=nickname)

        await UserRepository().save_user(user=user)

    def hash_password(self, plain_password: str) -> str:
        hashed_password: bytes = bcrypt.hashpw(
            plain_password.encode(self.encoding), salt=bcrypt.gensalt()
        )

        return hashed_password.decode(self.encoding)
