from pydantic import BaseModel



class LikeCreateSchema(BaseModel):
    profile_id: int
    liked_profile_id: int


class LikeSchema(LikeCreateSchema):
    id: int
