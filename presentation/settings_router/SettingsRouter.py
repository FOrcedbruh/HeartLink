from fastapi import APIRouter, Body, Depends
from schemas.settings_schema import SettingsModelReadSchema, SettingsModelUpdateSchema, SetttingsModelCreateSchema
from services import SettingsModelService
from dependencies import get_settings_service


router = APIRouter(prefix="/user_settings", tags=["UserSettings"])


@router.post("/create")
async def index(
    settings_in: SetttingsModelCreateSchema = Body(),
    service: SettingsModelService = Depends(get_settings_service)
) -> SettingsModelReadSchema:
    return await service.create_settings(settings_in=settings_in)

@router.get("/{settings_id}")
async def index(
    settings_id: int,
    service: SettingsModelService = Depends(get_settings_service)
) -> SettingsModelReadSchema:
    return await service.get_settings(settings_id=settings_id)

@router.patch("/update/{settings_id}")
async def index(
    settings_id: int,
    settings_in: SettingsModelUpdateSchema = Body(),
    service: SettingsModelService = Depends(get_settings_service)
) -> SettingsModelReadSchema:
    return await service.update_settings(settings_in=settings_in, settings_id=settings_id)

