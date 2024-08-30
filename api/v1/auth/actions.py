from . import utils
from .schemas import UserSchema
from core import settings, db_conn
from pydantic import BaseModel
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, OAuth2PasswordBearer
from jwt import InvalidTokenError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from core.models import User



TOKEN_TYPE_FIELD = "type"
ACCESS_TYPE = "access"
REFRESH_TYPE = "refresh"

http_bearer = HTTPBearer(auto_error=False)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login/")

def create_token(
        data: dict,
        token_type: str,
        expires_minutes: int,
    ) -> str:
    payload = {TOKEN_TYPE_FIELD: token_type}
    payload.update(data)
    return utils.encode_token(payload=payload, expires_minutes=expires_minutes)


def create_access_token(
    user: UserSchema
) -> str:
    data = {
        "sub": user.email,
        "id": user.id,
        "username": user.username
    }
    return create_token(data=data, token_type=ACCESS_TYPE, expires_minutes=settings.jwt.access_token_expires_minutes)



def create_refresh_token(
    user: UserSchema
) -> str:
    data = {
        "sub": user.email,
    }
    return create_token(data=data, token_type=REFRESH_TYPE, expires_minutes=settings.jwt.refresh_token_expires_minutes)


class TokenInfo(BaseModel):
    access_token: str
    refresh_token: str | None
    token_type: str = "Bearer"


def get_current_token(
        token: str = Depends(oauth2_scheme)
    ) -> dict:
    try:
        payload = utils.decode_jwt(token)
        
    except InvalidTokenError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Invalid token error: {e}"
        )
        
    return payload


async def get_current_auth_user(payload: dict = Depends(get_current_token), session: AsyncSession = Depends(db_conn.sesion_creation)):
    email: str | None = payload.get('sub')
    token_type: str = payload.get(TOKEN_TYPE_FIELD)
    if token_type != ACCESS_TYPE:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Expected {ACCESS_TYPE} token type"
        )
    else:
        st = await session.execute(select(User).filter(User.email == email))
        user = st.scalars().first()
        
        if user == None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token"
            )
            
        return user