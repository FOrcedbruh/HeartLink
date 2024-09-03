from .base import Base
from sqlalchemy import String, ForeignKey, Enum, ARRAY
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING
import enum
from sqlalchemy.ext.mutable import MutableList

if TYPE_CHECKING:
    from .user import User


class Genders(enum.Enum):
    MALE: str = "male"
    FEMALE: str = "female"
    BOY: str = "boy"
    GIRL: str = "girl"


class Profile(Base):
    __tablename__ = "profiles"
    
    firstname: Mapped[str] = mapped_column(nullable=False)
    surname: Mapped[str] = mapped_column(nullable=False)
    gender: Mapped[Genders] = mapped_column(Enum(Genders), nullable=True)
    age: Mapped[int] = mapped_column(nullable=True)
    profileImages: Mapped[list[str]] = mapped_column(MutableList.as_mutable(ARRAY(String)), nullable=True)
    hobbies: Mapped[list[str]] = mapped_column(MutableList.as_mutable(ARRAY(String)), nullable=True)
    bio: Mapped[str] = mapped_column(nullable=True)
    
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False, unique=True)
    user: Mapped["User"] = relationship(back_populates="profile")