from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from core import db_conn
from . import crud
from .schemas import LikeCreateSchema, LikeSchema
from api.v1.auth.schemas import UserSchema


router = APIRouter(prefix="/likes", tags=["Like"])



@router.post("/like")
async def like_profile(session: AsyncSession = Depends(db_conn.sesion_creation), like_in: LikeCreateSchema = Depends(crud.LikeForm)):
    return await crud.like_profile(session=session, like_in=like_in)



@router.get("/{profile_id}")
async def my_likes(profile_id: int, session: AsyncSession = Depends(db_conn.sesion_creation)):
    return await crud.my_likes(session=session, profile_id=profile_id)



@router.post("/check_like_profile/{profile_id}")
async def check_profile(profile_id: int, session: AsyncSession = Depends(db_conn.sesion_creation)):
    return await crud.check_like_profile(session=session, profile_id=profile_id)

@router.post("/get_likes_count")
async def get_likes_count(liked_profile: int = Depends(crud.GetCountForm), session: AsyncSession = Depends(db_conn.sesion_creation)):
    return await crud.get_likes_count(session=session, liked_profile=liked_profile)







    