from fastapi import APIRouter, File, UploadFile, Depends
from core import db_conn
from sqlalchemy.ext.asyncio import AsyncSession
from . import crud, utils
from api.v1.auth.actions import get_current_auth_user
from api.v1.auth.schemas import UserSchema
from .schemas import ProfileSchema


router = APIRouter(prefix="/profile", tags=["Profiles"])


@router.post("/", response_model_exclude_none=True, response_model=ProfileSchema)
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


@router.patch("/update_photos")
async def set_photos(session: AsyncSession = Depends(db_conn.sesion_creation), authUser: UserSchema = Depends(get_current_auth_user), files: list[UploadFile] = File()):
    return await crud.set_photos(session=session, authUser=authUser, files=files)



