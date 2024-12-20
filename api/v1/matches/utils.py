from .schemas import MatchCreateSchema
from fastapi import Body


def CreateMatchForm(
    first_id: int = Body(),
    second_id: int = Body()
) -> MatchCreateSchema:
    return MatchCreateSchema(
        first_id,
        second_id
    )


MATCH_SUCCESS_MESSAGE: str = "Поздравляем, у вас мэтч! Скорей начните общаться"