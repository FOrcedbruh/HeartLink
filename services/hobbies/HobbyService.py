from repositories.hobbies.HobbyRepository import HobbyRepository
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from .helpers import helpers
from schemas.hobbies import HobbySchema

class HobbyService:

    def __init__(self, session: AsyncSession = Depends(helpers.db.sesion_creation)):
        self.repository = HobbyRepository(session=session)

    async def get_hobbies(self) -> list[HobbySchema]:
        return await self.repository.list()