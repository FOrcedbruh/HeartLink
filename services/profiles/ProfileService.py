from repositories.profiles.ProfileRepository import ProfileRepository
from repositories.users.UserRepository import UserRepository
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from config import DatabaseConnection, settings
from schemas.profiles import ProfileCreateSchema, ProfileUpdateSchema
from models import Profile
from .helpers import helpers
from .exceptions.exceptions import UnAuthUserException

db = DatabaseConnection(
    db_url=settings.db.url,
    echo_pool=settings.db.echo_pool,
    pool_size=settings.db.pool_size,
    db_echo=settings.db.echo
)

class ProfileService:
    
    def __init__(self, session: AsyncSession = Depends(db.sesion_creation)):
        self.repository = ProfileRepository(session=session)
        self.auth_repository = UserRepository(session=session)

    async def create_profile(self, profile_in: ProfileCreateSchema):
        profile_in_dict = profile_in.model_dump(exclude_none=True)
        profile_in_dict["currentStage"] = 1
        profile_to_create = Profile(**profile_in_dict)
        return await self.repository.create(data=profile_to_create)
    
    async def update_profile(self, profile_in: ProfileUpdateSchema, token: str) -> Profile:
        auth_user = await helpers.get_auth_user_for_profile(token=token, repository=self.auth_repository)

        if not auth_user:
            raise UnAuthUserException()

        return await self.repository.update(profile_in.model_dump(exclude_none=True), id=auth_user.id)
    
