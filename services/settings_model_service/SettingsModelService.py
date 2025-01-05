from repositories import SettingsModelRepository
from schemas.settings_schema import SettingsModelReadSchema, SetttingsModelCreateSchema, SettingsModelUpdateSchema
from models import SettingsModel


class SettingsModelService:

    def __init__(self, repository: SettingsModelRepository):
        self.repository = repository


    async def create_settings(
        self,
        settings_in: SetttingsModelCreateSchema
    ) -> SettingsModelReadSchema:
        settings_to_create = SettingsModel(**settings_in.model_dump(exclude_none=True))
        return await self.repository.create(data=settings_to_create)

    async def get_settings(self, settings_id: int) -> SettingsModelReadSchema:
        return await self.repository.get_one(id=settings_id)
    
    async def update_settings(
        self, 
        settings_in: SettingsModelUpdateSchema,
        settings_id: int
    ) -> SettingsModelReadSchema:
        settings_to_update = settings_in.model_dump(exclude_none=True)

        return await self.repository.update(data=settings_to_update, id=settings_id)

    


        
