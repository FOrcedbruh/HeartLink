from sqlalchemy.ext.asyncio import AsyncSession
from ..base.base_repository import BaseRepository
from models import Hobby
from .exceptions.exceptions import HobbyNotFoundException


class HobbyRepository(BaseRepository[Hobby]):
    model = Hobby
    exception: HobbyNotFoundException = HobbyNotFoundException()

    def __init__(self, session: AsyncSession):
        super().__init__(session=session, model=self.model, exception=self.exception)