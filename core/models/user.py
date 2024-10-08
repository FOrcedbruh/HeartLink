from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, DateTime
from .base import Base
from typing import TYPE_CHECKING
from datetime import datetime

if TYPE_CHECKING:
    from .profile import Profile


class User(Base):
    __tablename__ = "users"
    
    username: Mapped[str] = mapped_column(String(12), nullable=False, unique=True)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    password: Mapped[bytes] = mapped_column(nullable=False)
    
    profile: Mapped["Profile"] = relationship(back_populates="user", cascade="all, delete-orphan", uselist=False)
    registered_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())