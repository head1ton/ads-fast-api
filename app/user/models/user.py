from typing import Optional

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from common.mixins.timestamp_mixin import TimestampMixin
from core.db import Base
from utils.datetime import get_current_linux_timestamp


class User(Base, TimestampMixin):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        primary_key=True, autoincrement=True, name="user_id"
    )
    email: Mapped[str] = mapped_column(String(200), comment="이메일")
    password: Mapped[str] = mapped_column(String(200), comment="비밀번호")
    name: Mapped[Optional[str]] = mapped_column(String(30), comment="이름")
    nickname: Mapped[Optional[str]] = mapped_column(String(30), comment="별명")
    photo_url: Mapped[Optional[str]] = mapped_column(
        String(200), comment="사진 ex) /users/1/images/profile.jpg"
    )
    phone: Mapped[Optional[str]] = mapped_column(String(30), comment="전화번호")
    reg_type: Mapped[Optional[int]] = mapped_column(
        default=2, comment="등록 타입(0: 가입고객/신규, 1: 가입고객/N15, 2: DB고객, 3: DB고객)"
    )
    corp: Mapped[Optional[str]] = mapped_column(String(100), comment="회사명")
    team: Mapped[Optional[str]] = mapped_column(String(100), comment="부서명")
    position: Mapped[Optional[int]] = mapped_column(String(20), comment="직급")
    brand_name: Mapped[Optional[str]] = mapped_column(String(200), comment="브랜드 이름")
    agree_terms: Mapped[Optional[bool]] = mapped_column(default=False, comment="약관동의")
    agree_private: Mapped[Optional[bool]] = mapped_column(
        default=False, comment="개인 정보보호 동의"
    )
    agree_email: Mapped[Optional[bool]] = mapped_column(
        default=False, comment="이메일 수신 동의"
    )
    agreed_at: Mapped[Optional[str]] = mapped_column(
        default=get_current_linux_timestamp(), comment="동의 날짜"
    )
    status: Mapped[Optional[int]] = mapped_column(
        default=3, comment="계정 상태 - 1:활성, 2:비활성, 3:임시"
    )
    user_grp_id: Mapped[Optional[int]] = mapped_column(default=2, comment="유저그룹 차후 수정")
    is_auth: Mapped[Optional[bool]] = mapped_column(default=False, comment="인증여부")
    is_admin: Mapped[Optional[bool]] = mapped_column(default=False, comment="관리자여부")
    # comp_id: Mapped[int] = mapped_column(ForeignKey("comp.id"))
    # comp: Mapped["Comp"] = relationship(back_populates="user")

    def __repr__(self) -> str:
        return f"User(user_id={self.id!r}, nickname={self.nickname!r}, email={self.email!r}"
