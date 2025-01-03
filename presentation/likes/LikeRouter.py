from fastapi import APIRouter, Depends
from services.likes.LikeService import LikeService
from schemas.likes import LikeCreateSchema, LikeSchema
from config.utils.likes import utils
from dependencies import get_like_service

router = APIRouter(prefix="/like", tags=["Like"])


@router.post("/", response_model=LikeSchema)
async def index(
    like_in: LikeCreateSchema = Depends(utils.LikeForm),
    service: LikeService = Depends(get_like_service)
) -> LikeSchema:
    return await service.like(like_in=like_in)


@router.get("/{profile_id}", response_model=list[LikeSchema])
async def index(
    profile_id: int,
    service: LikeService = Depends(get_like_service)
) -> list[LikeSchema]:
    return await service.get_likes_by_profile_id(profile_id=profile_id)


@router.get("/likes_count/{profile_id}", response_model=dict)
async def index(
    profile_id: int,
    service: LikeService = Depends(get_like_service)
) -> dict:
    return await service.get_likes_count(profile_id=profile_id)