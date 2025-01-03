from repositories.profiles.ProfileRepository import ProfileRepository
from repositories.users.UserRepository import UserRepository
from config import settings, S3Client
from schemas.profiles import ProfileCreateSchema, ProfileUpdateSchema, ProfileSchema
from models import Profile
from .helpers import helpers
from .exceptions.exceptions import UnAuthUserException



s3 = S3Client()

class ProfileService:
    
    def __init__(self, repository: ProfileRepository, auth_repository: UserRepository):
        self.repository = repository
        self.auth_repository = auth_repository


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
    

    async def add_photos_to_profile(self, profile_id: int, files, token: str) -> dict:
        auth_user = await helpers.get_auth_user_for_profile(token=token, repository=self.auth_repository)

        if not auth_user:
            raise UnAuthUserException()
        
        urls: list[str] = []
        for file in files:
            urls.append(settings.s3.get_url + "/" + file.filename)
        
        await s3.upload_files(files=files)

        await self.repository.update_images(data=urls, id=profile_id)

        return {
            "message": f"Фото успешно добавлены ({len(urls)})"
        }
    

    async def delete_photos_from_profile(self, object_names: list[str], profile_id: int, token: str) -> dict:
        auth_user = await helpers.get_auth_user_for_profile(token=token, repository=self.auth_repository)
        if not auth_user:
            raise UnAuthUserException()
        
        await self.repository.erase_images(data=object_names, id=profile_id)
        await helpers.delete_images_from_s3(object_names=object_names, s3=s3)

        return {
            "message": f"Фото удалены ({len(object_names)})"
        }
    

    async def feed(self, gender_in: str, limit: int, offset: int) -> list[ProfileSchema]:
        return await self.repository.list_for_feed(data=gender_in, offset=offset, limit=limit)
    

    async def get_profile_for_auth(self, token: str) -> ProfileSchema:
        auth_user = await helpers.get_auth_user_for_profile(token=token, repository=self.auth_repository)

        if not auth_user:
            raise UnAuthUserException()
        
        return await self.repository.get_profile_by_user_id(id=auth_user.id)
    
    async def get_profile(self, token: str, profile_id: int) -> ProfileSchema:
        auth_user = await helpers.get_auth_user_for_profile(token=token, repository=self.auth_repository)

        if not auth_user:
            raise UnAuthUserException()
        
        return await self.repository.get_one(id=profile_id)
    
    async def get_profile_stage(self, profile_id: int) -> dict:
        stage: int = await self.repository.get_stage(id=profile_id)

        return {
            "stage": stage
        }