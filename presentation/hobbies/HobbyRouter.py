from fastapi import APIRouter, Depends
from services import HobbyService
from dependencies import get_hobby_service
from schemas.hobbies import HobbySchema

router = APIRouter(prefix="/hobbies", tags=["Hobbies"])

@router.get("/", response_model=list[HobbySchema])
async def index(
    service: HobbyService = Depends(get_hobby_service)
) -> list[HobbySchema]:
    return await service.get_hobbies()