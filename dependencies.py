from fastapi import Depends
from repositories import UserRepository, ProfileRepository, LikeRepository, HobbyRepository
from services import UserService, ProfileService, HobbyService, LikeService
from config import DatabaseConnection, settings
from sqlalchemy.ext.asyncio import AsyncSession

db = DatabaseConnection(
    db_url=settings.db.url,
    echo_pool=settings.db.echo_pool,
    pool_size=settings.db.pool_size,
    db_echo=settings.db.echo
)


def get_user_repository(session: AsyncSession = Depends(db.sesion_creation)) -> UserRepository:
    return UserRepository(session=session)

def get_profile_repository(session: AsyncSession = Depends(db.sesion_creation)) -> ProfileRepository:
    return ProfileRepository(session=session)

def get_like_repository(session: AsyncSession = Depends(db.sesion_creation)) -> LikeRepository:
    return LikeRepository(session=session)

def get_hobby_repository(session: AsyncSession = Depends(db.sesion_creation)) -> HobbyRepository:
    return HobbyRepository(session=session)

#==================================================================

def get_user_service(repository: UserRepository = Depends(get_user_repository)) -> UserService:
    return UserService(repository=repository)

def get_profile_service(repository: ProfileService = Depends(get_profile_repository), auth_repository: UserRepository = Depends(get_user_repository)) -> ProfileService:
    return ProfileService(repository=repository, auth_repository=auth_repository)

def get_like_service(repository: LikeService = Depends(get_like_repository)) -> LikeService:
    return LikeService(repository=repository)

def get_hobby_service(repository: HobbyService = Depends(get_hobby_repository)) -> HobbyService:
    return HobbyService(repository=repository)