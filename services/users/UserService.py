from repositories import UserRepository
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from schemas.users import UserRegistrationSchema, UserLoginSchema, UserReadSchema
from config.utils.auth import utils
from .helpers import helpers
from .exceptions.exceptions import IncorrectPasswordException


class UserService:

    def __init__(self, repository: UserRepository):
        self.repository = repository


    async def registration(self, user_in: UserRegistrationSchema) -> helpers.TokenInfo:
        hash_password: bytes = utils.hash_passowrd(password=user_in.password)

        new_user = await self.repository.registration(hash_password, user_in.email, user_in.username)

        access_token: str = helpers.create_access_token(user=new_user)
        refresh_token: str = helpers.create_refresh_token(user=new_user)

        return helpers.TokenInfo(
            access_token=access_token,
            refresh_token=refresh_token
        )
    

    async def login(self, user_in: UserLoginSchema):
        user = await self.repository.login(email=user_in.email)

        is_valid_password: bool = utils.validation_password(
            hashed_password=user.password,
            password=user_in.password
        )

        if not is_valid_password:
            raise IncorrectPasswordException()
        
        access_token: str = helpers.create_access_token(user=user)
        refresh_token: str = helpers.create_refresh_token(user=user)

        return helpers.TokenInfo(
            access_token=access_token,
            refresh_token=refresh_token
        )
    
    async def me(self, token: str) -> UserReadSchema:
        payload: dict = helpers.get_current_token(token=token)
        email: str = await helpers.get_current_auth_user(payload=payload)

        auth_user = await self.repository.get_current_auth_user(email=email)

        return UserReadSchema(
            id=auth_user.id,
            username=auth_user.username,
            email=auth_user.email,
            registered_at=auth_user.registered_at
        )
    
    # Метод, обновляющий access токен доступа
    # Метод принимает refresh токен
    async def refresh(self, token: str):
        payload: dict = helpers.get_current_token(token=token)
        email: str = await helpers.get_current_auth_user_for_refresh(payload=payload)

        auth_user = await self.repository.get_current_auth_user(email=email)

        access_token: str = helpers.create_access_token(user=auth_user)

        return helpers.TokenInfo(
            access_token=access_token,
            refresh_token=None
        )
    
    async def delete_user_with_profile(self, user_id: int) -> dict:
        await self.repository.delete(id=user_id)
    
        return {
            "message": "Пользователь успешно удален"
        }


