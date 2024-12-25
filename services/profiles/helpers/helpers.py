from models import User
from ...users.helpers import helpers
from repositories.users.UserRepository import UserRepository
from config import S3Client, settings

async def get_auth_user_for_profile(token: str, repository: UserRepository) -> User:
    payload: dict = helpers.get_current_token(token=token)
    email: str = await helpers.get_current_auth_user(payload=payload)


    return await repository.get_current_auth_user(email=email)

async def delete_images_from_s3(object_names: list[str], s3: S3Client) -> None:
    files_to_erase: list[str] = [filename[len(settings.s3.get_url) + 1:] for filename in object_names]
    await s3.delete_files(filenames=files_to_erase)