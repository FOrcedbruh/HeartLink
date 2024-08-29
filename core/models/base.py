from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Table, ForeignKey


class Base(DeclarativeBase):
    __abstract__ = True
    
    id: Mapped[int] = mapped_column(primary_key=True)
    
# profiles_hobbies = Table(
#     "profiles_hobbies", Base.metadata,
#     profile_id = mapped_column(ForeignKey("profiles.id"), primary_key=True),
#     hobby_id = mapped_column(ForeignKey("hobbies.id"), primary_key=True)
# )