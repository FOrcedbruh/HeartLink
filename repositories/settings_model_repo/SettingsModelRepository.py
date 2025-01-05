from ..base.base_repository import BaseRepository
from .exceptions.exceptions import SettingsNotFoundException
from models import SettingsModel
from sqlalchemy.ext.asyncio import AsyncSession



class SettingsModelRepository(BaseRepository[SettingsModel]):
    model = SettingsModel
    exception = SettingsNotFoundException = SettingsNotFoundException()

    def __init__(self, session: AsyncSession):
        super().__init__(session=session, model=self.model, exception=self.exception)

    async def update(self, data: dict, id: int) -> SettingsModel:
        settings_model = await self.session.get(self.model, id)

        if not settings_model:
            raise self.exception
        
        for name, val in data.items():
            setattr(settings_model, name, val)
        
        await self.session.commit()
        await self.session.refresh(settings_model)

        return settings_model
    