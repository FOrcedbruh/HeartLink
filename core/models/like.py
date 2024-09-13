from .base import Base
from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, DateTime
from typing import TYPE_CHECKING
from datetime import datetime, UTC

if TYPE_CHECKING:
    from .profile import Profile

class Like(Base):
    __tablename__ = "likes"
    
    
    profile_id: Mapped[int] = mapped_column(ForeignKey("profiles.id"), nullable=False)
    liked_profile_id: Mapped[int] = mapped_column(ForeignKey("profiles.id"), nullable=False)
    profile: Mapped["Profile"] = relationship("Profile", foreign_keys=[profile_id])
    liked_profile: Mapped["Profile"] = relationship("Profile", foreign_keys=[liked_profile_id], back_populates="likes")
    
    liked_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())