from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import Depends, status, UploadFile, HTTPException
from api.v1.auth.schemas import UserSchema
from core.models import Profile
from core import s3_client, settings
from botocore.exceptions import InvalidConfigError
from .schemas import ProfileSchema

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
    profile.currentStage = profile_in.get("currentStage")
    
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
    profile.currentStage = profile_in.get("currentStage")
    
    await session.commit()
    
    return {
        "status": status.HTTP_200_OK,
        "detail": "Updated"
    }
    


async def set_photos(session: AsyncSession, files: list[UploadFile], authUser: UserSchema):
    st = await session.execute(select(Profile).filter(Profile.user_id == authUser.id))
    profile = st.scalars().first()
    photosUrls: list[str] = []
    if not files:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Files not found"
        )
    for file in files:
        photosUrls.append( settings.s3.get_url + "/" + file.filename)

    try:
        await s3_client.upload_files(files=files)
        
    except InvalidConfigError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Data sending error: {e}"
        )
    
    profile.profileImages = photosUrls
    
    await session.commit()
    
    return {
        "status": status.HTTP_200_OK,
        "detail": "Updated"
    }
    
    


async def get_profile(session: AsyncSession, authUser: UserSchema):
    st = await session.execute(select(Profile).filter(Profile.user_id == authUser.id))
    profile = st.scalars().first()
    
    if not profile:
        return ""
    
    return ProfileSchema(
        user_id=profile.user_id,
        age=profile.age,
        firstname=profile.firstname,
        surname=profile.surname,
        hobbies=profile.hobbies,
        profileImage=profile.profileImages,
        bio=profile.bio,
        gender=profile.gender,
        currentStage=profile.currentStage
    )
    



async def delete_profileImages(authUser: UserSchema, filenames: list[str]):
    user = authUser
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not Found"
        )
    try:
        await s3_client.delete_files(filenames=filenames)
    except InvalidConfigError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error: {str(e)}"
        )
    
    return {
        "status": status.HTTP_200_OK,
        "message": "Deleted"
    }
    
    
    
async def feed(session: AsyncSession, gender_in: str) -> dict:
    st = await session.execute(select(Profile).filter(Profile.gender == gender_in))
    profiles = st.scalars().all()
    
    
    return {
        "status": status.HTTP_200_OK,
        "profiles": list(profiles)
    }

async def get_profile_stage(session: AsyncSession, authUser: UserSchema) -> int:
    st = await session.execute(select(Profile).filter(Profile.user_id == authUser.id))
    profile = st.scalars().first()

    return profile.currentStage
