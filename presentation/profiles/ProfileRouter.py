from fastapi import APIRouter, Depends
from services.profiles.ProfileService import ProfileService
from schemas.profiles import ProfileCreateSchema, ProfileUpdateSchema
from config.utils.profiles import utils
from ..users.UserRouter import oauth2_scheme

router = APIRouter(prefix="/profile",tags=["Profile"])



@router.post("/create")
async def index(
    profile_in: ProfileCreateSchema = Depends(utils.create_profileForm),
    service: ProfileService = Depends(ProfileService)
):
    return await service.create_profile(profile_in=profile_in)

@router.post("/update")
async def index(
    token: str = Depends(oauth2_scheme),
    profile_in: ProfileUpdateSchema = Depends(utils.update_profileForm),
    service: ProfileService = Depends(ProfileService)
):
    return await service.update_profile(profile_in=profile_in, token=token)
