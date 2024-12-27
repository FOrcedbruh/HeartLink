from fastapi import APIRouter, Depends
from services.hobbies.HobbyService import HobbyService
from schemas.hobbies import HobbySchema

router = APIRouter(prefix="/hobbies", tags=["Hobbies"])

@router.get("/", response_model=list[HobbySchema])
async def index(
    service: HobbyService = Depends(HobbyService)
) -> list[HobbySchema]:
    return await service.get_hobbies()