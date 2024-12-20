from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from core.db_connection import db_conn
from . import crud, utils
from schemas import MatchCreateSchema

router = APIRouter(prefix="/matches", tags=["Matches"])



@router.post("/create")
async def index(
    session: AsyncSession = Depends(db_conn.sesion_creation),
    match_in: MatchCreateSchema = Depends(utils.CreateMatchForm)
) -> dict:
    return await crud.create_match(session=session, match_in=match_in)