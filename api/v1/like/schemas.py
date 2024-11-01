from pydantic import BaseModel
from datetime import datetime


class LikeCreateSchema(BaseModel):
    profile_id: int
    liked_profile_id: int


class LikeSchema(LikeCreateSchema):
    id: int
    like_at: datetime
