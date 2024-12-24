from pydantic import BaseModel
from datetime import datetime

class MatchCreateSchema(BaseModel):
    first_id: int
    second_id: int


class MatchReadSchema(MatchCreateSchema):
    id: int
    created_at: datetime