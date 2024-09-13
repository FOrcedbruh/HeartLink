from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from core import db_conn
from . import crud
from .schemas import LikeCreateSchema


router = APIRouter(prefix="/likes", tags=["Like"])



@router.post("/like")
async def like_profile(session: AsyncSession = Depends(db_conn.sesion_creation), like_in: LikeCreateSchema = Depends(crud.LikeForm)):
    return await crud.like_profile(session=session, like_in=like_in)