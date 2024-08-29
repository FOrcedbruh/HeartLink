# from .base import Base, profiles_hobbies
# from sqlalchemy.orm import Mapped, mapped_column, relationship
# from typing import TYPE_CHECKING

# if TYPE_CHECKING:
#     from .profile import Profile


# class Hobby(Base):
#     __tablename__ = "hobbies"
    
#     title: Mapped[str] = mapped_column(nullable=False)
#     profiles: Mapped[list["Profile"]] = relationship(secondary=profiles_hobbies, back_populates="hobbies")
    