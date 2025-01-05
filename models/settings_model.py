from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Enum
from .base import Base
import enum
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from .user import User


class Themes(enum.Enum):
    DARK: str = "dark"
    LIGHT: str = "light"




class SettingsModel(Base):
    __tablename__ = "settings_tables"

    color_theme: Mapped[Themes] = mapped_column(Enum(Themes), nullable=False)
    dynamic_navbar: Mapped[bool] = mapped_column(default=True)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False, unique=True)
    user: Mapped["User"] = relationship(back_populates="settings")