from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import Boolean
from sqlalchemy import Integer
from sqlalchemy import TEXT
import datetime

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    id: Mapped[str] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(255))
    full_name: Mapped[str] = mapped_column(String(100))
    user_name: Mapped[str] = mapped_column(String(50), unique=True)
    delete_id: Mapped[str] = mapped_column(String(255))
    created_at: Mapped[int]
    links: Mapped[List["Link"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )
    def __repr__(self) -> str:
        return f"Question(id={self.id!r}, email={self.email!r}, full_name={self.full_name!r}, user_name={self.user_name!r}, created_at={self.created_at})"

class Link(Base):
    __tablename__ = "links"
    id: Mapped[str] = mapped_column(primary_key=True)
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id", ondelete='CASCADE'))
    website: Mapped[str] = mapped_column(String(100))
    link: Mapped[str]
    created_at: Mapped[int]
    user: Mapped["User"] = relationship(back_populates="links")
    def __repr__(self) -> str:
        return f"Choice(id={self.id!r}, user_id={self.user_id!r}, website={self.website!r}, link={self.link!r}, created_at={self.created_at!r})"


class Post(Base):
    __tablename__ = "posts"
    id: Mapped[str] = mapped_column(primary_key=True)
    author: Mapped[str] = mapped_column(String(255))
    title: Mapped[str] = mapped_column(String(255))
    delete_id: Mapped[str] = mapped_column(String(255))
    active: Mapped[bool] = mapped_column(Boolean, default=False)
    content: Mapped[str] = mapped_column(TEXT)

    created_at: Mapped[int] = mapped_column(Integer)
    updated_at: Mapped[int] = mapped_column(Integer)
    def __repr__(self) -> str:
        return f"Question(id={self.id!r}, author={self.author!r}, title={self.title!r}, content={self.content!r}, created_at={self.created_at})"