from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from . import utils
from .schemas import ProfileSchema


async def create_profile(session: AsyncSession, profile_in = Depends(utils.create_profileForm)):
    pass