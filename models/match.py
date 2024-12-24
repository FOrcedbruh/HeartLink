# from sqlalchemy.orm import Mapped, mapped_column, relationship
# from .base import Base
# from typing import TYPE_CHECKING
# from sqlalchemy import ForeignKey


# if TYPE_CHECKING:
#     from .profile import Profile


# class Match(Base):
#     __tablename__ = "matches"

#     first_id: Mapped[int] = mapped_column(ForeignKey("profiles.id"), nullable=False)
#     second_id: Mapped[int] = mapped_column(ForeignKey("profiles.id"), nullable=False)

#     first_profile: Mapped["Profile"] = relationship(back_populates="matches")
#     second_profile: Mapped["Profile"] = relationship(back_populates="matches")

