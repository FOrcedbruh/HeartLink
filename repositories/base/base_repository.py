from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from typing import TypeVar, Generic
from models import Base
from .exceptions.exceptions import BaseException


ModelType = TypeVar(name="ModelType", bound=Base)
ExceptionType = TypeVar(name="ExceptionType", bound=BaseException)



# Базовый репозиторий, который является родтельским для остальных
# Предоставляет основные методы CRUD
class BaseRepository(Generic[ModelType]):

    def __init__(self, session: AsyncSession, model: ModelType, exception: ExceptionType):
        self.session = session
        self.model = model
        self.exception = exception


    async def list(self) -> list[ModelType]:
        query = select(self.model)
        stmt = await self.session.execute(query)
        res = stmt.scalars().all()

        if not res:
            raise self.exception

        return res
    
    async def get_one(self, id: int) -> ModelType:
        res = await self.session.get(self.model, id)

        if not res:
            raise  self.exception
        
        return res
        
    async def create(self, data: ModelType) -> ModelType:
        self.session.add(data)
        await self.session.commit()
        await self.session.refresh(data)

        return data
    
    async def delete(self, id: int) -> None:
        res = await self.session.get(self.model, id)
        if not res:
            raise self.exception
        
        await self.session.delete(res)
        await self.session.commit()

        

        



        