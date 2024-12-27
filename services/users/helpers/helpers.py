from config.utils.auth import utils
from schemas.users import UserSchema
from config import settings, DatabaseConnection
from pydantic import BaseModel
from jwt import InvalidTokenError
from ..exceptions.exceptions import TokenTypeException, InvalidTokenException


TOKEN_TYPE_FIELD = "type"
ACCESS_TYPE = "access"
REFRESH_TYPE = "refresh"



# Метод создает JWT
def create_token(
        data: dict,
        token_type: str,
        expires_minutes: int,
    ) -> str:
    payload = {TOKEN_TYPE_FIELD: token_type}
    payload.update(data)
    return utils.encode_token(payload=payload, expires_minutes=expires_minutes)

# Метод создает токен доступа
def create_access_token(
    user: UserSchema
) -> str:
    data = {
        "sub": user.email,
        "id": user.id,
        "username": user.username
    }
    return create_token(data=data, token_type=ACCESS_TYPE, expires_minutes=settings.jwt.access_token_expires_minutes)


# Метод создает токен обновления
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

# Метод получает текущий токен авторизованного пользователя
# Метод возвращает декодированный payload токена
def get_current_token(
        token: str
    ) -> dict:
    try:
        payload = utils.decode_jwt(token=token)
        
    except InvalidTokenError as e:
        raise InvalidTokenException(error_messsage=e)
        
    return payload

# Метод возращает почту текущего авторизованного пользователя
async def get_current_auth_user(payload: dict) -> str:
    email: str | None = payload.get('sub')
    token_type: str = payload.get(TOKEN_TYPE_FIELD)
    if token_type != ACCESS_TYPE:
       raise TokenTypeException(token_type=ACCESS_TYPE)
    
    return email
    
# Метод возвращает почту пользователя для обновления токена доступа
async def get_current_auth_user_for_refresh(payload: dict) -> str:
    email: str | None = payload.get('sub')
    token_type: str = payload.get(TOKEN_TYPE_FIELD)
    if token_type != REFRESH_TYPE:
        raise TokenTypeException(token_type=REFRESH_TYPE)
    
    return email
    

db = DatabaseConnection(
    db_url=settings.db.url,
    echo_pool=settings.db.echo_pool,
    pool_size=settings.db.pool_size,
    db_echo=settings.db.echo
)