from pydantic import BaseModel
import datetime

# схемы для валидации данных при работе с matches

class MatchCreateSchema(BaseModel):
    first_id: int
    second_id: int


class MatchReadSchema(MatchCreateSchema):
    id: int
    created_at: datetime