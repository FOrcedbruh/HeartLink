from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import Depends, status
from api.v1.auth.schemas import UserSchema
from core.models import Profile



async def create_profile(session: AsyncSession, profile_in: dict, authUser: UserSchema) -> dict:
    profile_in["user_id"] = authUser.id
    profile = Profile(**profile_in)
    session.add(profile)
    
    await session.commit()
    
    return {
        "status": status.HTTP_201_CREATED,
        "detail": "Successfully created"
    }
    

async def update_gender_and_age(session: AsyncSession, profile_in: dict, authUser: UserSchema) -> dict:
    st = await session.execute(select(Profile).filter(Profile.user_id == authUser.id))
    profile = st.scalars().first()
    
    profile.gender = profile_in.get("gender")
    profile.age = profile_in.get("age")
    
    await session.commit()
    
    
    return {
        "status": status.HTTP_200_OK,
        "detail": "Updated"
    }
    
async def update_hobbies_and_boi(session: AsyncSession, profile_in: dict, authUser: UserSchema) -> dict:
    st = await session.execute(select(Profile).filter(Profile.user_id == authUser.id))
    profile = st.scalars().first()
    
    profile.bio = profile_in.get("bio")
    profile.hobbies = profile_in.get("hobbies")
    
    await session.commit()
    
    return {
        "status": status.HTTP_200_OK,
        "detail": "Updated"
    }


