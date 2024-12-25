from models import User
from ...users.helpers import helpers
from repositories.users.UserRepository import UserRepository


async def get_auth_user_for_profile(token: str, repository: UserRepository) -> User:
    payload: dict = helpers.get_current_token(token=token)
    email: str = await helpers.get_current_auth_user(payload=payload)


    return await repository.get_current_auth_user(email=email)