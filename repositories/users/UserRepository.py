from ..base.base_repository import BaseRepository
from models import User
from sqlalchemy.ext.asyncio import AsyncSession
from .exceptions.exceptions import UserNotFoundException, UserNotExistsException, UserExistsException
from sqlalchemy import select

class UserRepository(BaseRepository[User]):
    model: User = User
    exception: UserNotFoundException = UserNotFoundException()

    def __init__(self, session: AsyncSession):
        super().__init__(session=session, model=self.model, exception=self.exception)

    async def registration(self, hash_password: bytes, email: str, username: str) -> User:
        query = select(self.model).where(self.model.email == email)
        stmt = await self.session.execute(query)
        candidate = stmt.scalars().first()

        if candidate:
            raise UserExistsException()
        
        new_user_dict = {
            "username": username,
            "email": email,
            "password": hash_password
        }
        new_user = User(**new_user_dict)
        self.session.add(new_user)
        await self.session.commit()

        return new_user
    


    async def login(self, email: str) -> User:
        query = select(self.model).where(self.model.email == email)
        stmt = await self.session.execute(query)
        res = stmt.scalars().first()

        if not res:
            raise UserNotExistsException()

        return res
    
    async def get_current_auth_user(self, email: str) -> User:
        query = select(self.model).where(self.model.email == email)
        stmt = await self.session.execute(query)
        res = stmt.scalars().first()

        if not res:
            raise UserNotExistsException()

        return res


        
