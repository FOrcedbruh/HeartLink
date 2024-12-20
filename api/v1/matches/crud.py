from sqlalchemy.ext.asyncio import AsyncSession
from api.v1.auth.schemas import UserSchema
from core.models import Match
from .schemas import MatchCreateSchema
from fastapi import status, HTTPException
from . import utils


# создание нового мэтча (совпадения по лайкам) пользователей
async def create_match(session: AsyncSession, authUser: UserSchema, match_in: MatchCreateSchema) -> dict:
    if not authUser:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Вы не авторизованы"
        )
    
    new_match = Match(**match_in.model_dump())

    session.add(new_match)

    await session.commit()

    return {
        "status": status.HTTP_201_CREATED,
        "congratulation": utils.MATCH_SUCCESS_MESSAGE
    }


