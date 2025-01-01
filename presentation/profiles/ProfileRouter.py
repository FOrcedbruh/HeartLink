from fastapi import APIRouter, Depends, UploadFile, File, Body
from services.profiles.ProfileService import ProfileService
from schemas.profiles import ProfileCreateSchema, ProfileUpdateSchema, ProfileSchema
from config.utils.profiles import utils
from ..users.UserRouter import oauth2_scheme
from dependencies import get_profile_service

router = APIRouter(prefix="/profile",tags=["Profile"])



@router.post("/create")
async def index(
    profile_in: ProfileCreateSchema = Depends(utils.create_profileForm),
    service: ProfileService = Depends(get_profile_service)
):
    return await service.create_profile(profile_in=profile_in)

@router.get("/", response_model=ProfileSchema)
async def index(
    token: str = Depends(oauth2_scheme),
    service: ProfileService = Depends(get_profile_service)
) -> ProfileSchema:
    return await service.get_profile_for_auth(token=token)


@router.patch("/update")
async def index(
    token: str = Depends(oauth2_scheme),
    profile_in: ProfileUpdateSchema = Depends(utils.update_profileForm),
    service: ProfileService = Depends(get_profile_service)
):
    return await service.update_profile(profile_in=profile_in, token=token)

@router.patch("/add_images/{profile_id}", response_model=dict)
async def index(
    profile_id: int,
    token: str = Depends(oauth2_scheme),
    service: ProfileService = Depends(get_profile_service),
    files: list[UploadFile] = File()
) -> dict:
    return await service.add_photos_to_profile(profile_id=profile_id, token=token, files=files)

@router.patch("/erase_images/{profile_id}")
async def index(
    profile_id: int,
    token: str = Depends(oauth2_scheme),
    service: ProfileService = Depends(get_profile_service),
    object_names: list[str] = Body()
) -> dict:
    return await service.delete_photos_from_profile(object_names=object_names, token=token, profile_id=profile_id)

@router.post("/feed/{offset}/{limit}")
async def index(
    offset: int,
    limit: int,
    gender_in: str = Body(),
    service: ProfileService = Depends(get_profile_service)
) -> list[ProfileSchema]:
    return await service.feed(gender_in=gender_in, limit=limit, offset=offset)

@router.get("/get_profile_stage/{profile_id}", response_model=dict)
async def index(
    profile_id: int,
    service: ProfileService = Depends(get_profile_service)
) -> dict:
    return await service.get_profile_stage(profile_id=profile_id)


@router.get("/{profile_id}", response_model=ProfileSchema)
async def index(
    profile_id: int,
    token: str = Depends(oauth2_scheme),
    service: ProfileService = Depends(get_profile_service)
) -> ProfileSchema:
    return await service.get_profile(profile_id=profile_id, token=token)
