from pydantic import BaseModel



class HobbyCreateSChema(BaseModel):
    title: str


class HobbySchema(HobbyCreateSChema):
    id: int

