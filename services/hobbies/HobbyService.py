from repositories.hobbies.HobbyRepository import HobbyRepository
from schemas.hobbies import HobbySchema

class HobbyService:

    def __init__(self, repository: HobbyRepository):
        self.repository = repository

    async def get_hobbies(self) -> list[HobbySchema]:
        return await self.repository.list()