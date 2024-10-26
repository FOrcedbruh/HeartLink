from fastapi import APIRouter, File, UploadFile, Depends, Body
from core import db_conn
from sqlalchemy.ext.asyncio import AsyncSession
from . import crud, utils
from api.v1.auth.actions import get_current_auth_user
from api.v1.auth.schemas import UserSchema
from .schemas import ProfileUpdateSchema


router = APIRouter(prefix="/profile", tags=["Profiles"])


@router.get("/", response_model_exclude_none=True)
async def get_profile(session: AsyncSession = Depends(db_conn.sesion_creation), authUser: UserSchema = Depends(get_current_auth_user)):
    return await crud.get_profile(session=session, authUser=authUser)

@router.post("/create")
async def createProfile(session: AsyncSession = Depends(db_conn.sesion_creation), profile_in: dict = Depends(utils.create_profileForm), authUser: UserSchema = Depends(get_current_auth_user)):
    return await crud.create_profile(session=session, profile_in=profile_in, authUser=authUser)



@router.patch("/update_gender_age")
async def updateGenderAndAge(session: AsyncSession = Depends(db_conn.sesion_creation), profile_in: dict = Depends(utils.update_gender_and_ageForm), authUser: UserSchema = Depends(get_current_auth_user)):
    return await crud.update_gender_and_age(session=session, profile_in=profile_in, authUser=authUser)



@router.patch("/update_bio_hobbies")
async def updateBioAndHobbies(session: AsyncSession = Depends(db_conn.sesion_creation), profile_in: dict = Depends(utils.update_bio_and_hobbiesForm), authUser: UserSchema = Depends(get_current_auth_user)):
    return await crud.update_hobbies_and_boi(session=session, profile_in=profile_in, authUser=authUser)


@router.patch("/update/images")
async def update_photos(session: AsyncSession = Depends(db_conn.sesion_creation), authUser: UserSchema = Depends(get_current_auth_user), files: list[UploadFile] = File()):
    return await crud.update_photos(session=session, authUser=authUser, files=files)


@router.post("/delete/images")
async def delete_images(authUser: UserSchema = Depends(get_current_auth_user), filenames: list[str] = Body(), session: AsyncSession = Depends(db_conn.sesion_creation)):
    return await crud.delete_profileImages(authUser=authUser, filenames=filenames, session=session)



@router.post("/feed")
async def feed(session: AsyncSession = Depends(db_conn.sesion_creation), gender_in: str =  Body()):
    return await crud.feed(session=session, gender_in=gender_in)

@router.post("/get_profile_stage")
async def get_profile_stage(session: AsyncSession = Depends(db_conn.sesion_creation), authUser: UserSchema = Depends(get_current_auth_user)) -> int:
    return await crud.get_profile_stage(session=session, authUser=authUser)

@router.patch("/update")
async def update_profile(session: AsyncSession = Depends(db_conn.sesion_creation), authUser: UserSchema = Depends(get_current_auth_user), profile_for_update: ProfileUpdateSchema = Body()):
    return await crud.update_profile(session=session, authUser=authUser, profile_for_update=profile_for_update)