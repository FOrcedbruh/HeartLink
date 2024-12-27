from sqlalchemy.ext.asyncio import AsyncSession
from schemas.likes import LikeSchema, LikeCreateSchema
from repositories.likes.LikeRepository import LikeRepository
from fastapi import Depends
from models import Like
from .helpers import helpers


class LikeService:
    

    def __init__(self, session: AsyncSession = Depends(helpers.db.sesion_creation)):
        self.repository = LikeRepository(session=session)

    async def like(self, like_in: LikeCreateSchema) -> LikeSchema:
        like_to_create = Like(**like_in.model_dump(exclude_none=True))
        return await self.repository.create(data=like_to_create)
    
    async def get_likes_by_profile_id(self, profile_id: int) -> list[LikeSchema]:
        return await self.repository.list_by_profile_id(id=profile_id)
    
    async def get_likes_count(self, profile_id: int) -> dict:
        count = await self.repository.get_count(id=profile_id)
        return {
            "count": count
        }