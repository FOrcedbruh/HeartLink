from ..base.base_repository import BaseRepository
from sqlalchemy.ext.asyncio import AsyncSession
from models import Profile
from .exceptions.exceptions import ProfileNotFoundException
from sqlalchemy import select


class ProfileRepository(BaseRepository[Profile]):
    model = Profile
    exception: ProfileNotFoundException = ProfileNotFoundException()

    def __init__(self, session: AsyncSession):
        super().__init__(session=session, model=self.model, exception=self.exception)
    
    async def update(self, data: dict, id: int) -> Profile:
        query = select(self.model).where(self.model.user_id == id)
        stmt = await self.session.execute(query)
        profile = stmt.scalars().first()

        if not profile:
            raise self.exception
        
        for name, val in data.items():
            setattr(profile, name, val)

        await self.session.commit()
        await self.session.refresh(profile)

        return profile
    
    async def update_images(self, data: list[str], id: int) -> Profile:
        profile = await self.session.get(self.model, id)

        if not profile:
            raise ProfileNotFoundException()
        
        if not profile.profileImages:
            profile.profileImages = data
        else:
            profile.profileImages.extend(data)

        await self.session.commit()
        await self.session.refresh(profile)

        return profile
    
    async def erase_images(self, data: list[str], id: int) -> Profile:
        profile = await self.session.get(self.model, id)

        if not profile:
            raise ProfileNotFoundException()
        
        for el in data:
            profile.profileImages.remove(el)

        await self.session.commit()
        await self.session.refresh(profile)

        return profile

        