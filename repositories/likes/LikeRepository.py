from sqlalchemy.ext.asyncio import AsyncSession
from ..base.base_repository import BaseRepository
from models import Like
from .exceptions.exceptions import LikeNotFoundException
from sqlalchemy import select


# Репозиторий, работающий с таблицей лайков
class LikeRepository(BaseRepository[Like]):
    model = Like
    exception: LikeNotFoundException = LikeNotFoundException()


    def __init__(self, session: AsyncSession):
        super().__init__(session=session, model=self.model, exception=self.exception)
        self.session = session

    async def list_by_profile_id(self, id: int) -> list[Like]:
        query = select(self.model).where(self.model.liked_profile_id == id)
        stmt = await self.session.execute(query)
        res = stmt.scalars().all()

        if not res:
            raise self.exception

        return list(res)
    
    async def get_count(self, id: int) -> int:
        query = select(self.model).filter(self.model.liked_profile_id == id)
        stmt = await self.session.execute(query)

        res = stmt.scalars().all()

        if not res:
            raise self.exception

        return len(list(res))
    
