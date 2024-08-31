from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship





class Hobby(Base):
    __tablename__ = "hobbies"
    
    title: Mapped[str] = mapped_column(nullable=False)
    