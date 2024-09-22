from .schemas import LikeCreateSchema, LikeSchema
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, Body, HTTPException, status
from core.models import Like
from api.v1.auth.actions import get_current_auth_user
from api.v1.auth.schemas import UserSchema
from sqlalchemy import select
from core.models import Profile


def LikeForm(liked_profile_id: int = Body(), profile_id: int = Body(), authUser: UserSchema = Depends(get_current_auth_user)) -> LikeCreateSchema:
    if not authUser:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauth user"
        )
    return LikeCreateSchema(
        liked_profile_id=liked_profile_id,
        profile_id=profile_id
    )




async def like_profile(session: AsyncSession, like_in: LikeCreateSchema) -> dict:
    if not like_in:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User not found"
        )
    
    like = Like(**like_in.model_dump())
    session.add(like)
    
    await session.commit()
    
    return {
        "Created like": LikeSchema(
                liked_profile_id=like.liked_profile_id,
                profile_id=like.profile_id,
                id=like.id
            ),
        "status": status.HTTP_201_CREATED
    }



async def my_likes(profile_id: int, session: AsyncSession) -> list[LikeSchema]:
    st = await session.execute(select(Like).filter(Like.liked_profile_id == profile_id))
    likes = st.scalars().all()
    
    return list(likes)



    
    

async def check_like_profile(session: AsyncSession, profile_id: int) -> dict:
    st = await session.execute(select(Profile).filter(Profile.id == profile_id))
    profile = st.scalars().first()
    
    
    
    return {
        "status": status.HTTP_200_OK,
        "profile": profile
    }