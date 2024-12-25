from fastapi import APIRouter, Depends
from services.users.UserService import UserService
from schemas.users import UserRegistrationSchema, UserLoginSchema, UserReadSchema
from config.utils.auth import utils
from fastapi.security import HTTPBearer, OAuth2PasswordBearer



http_bearer = HTTPBearer(auto_error=False)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login/")

router = APIRouter(prefix="/auth", tags=["Auth"], dependencies=[Depends(http_bearer)])


@router.post("/registration")
async def index(
    user_in: UserRegistrationSchema = Depends(utils.registrationForm),
    service: UserService = Depends(UserService)
):
    return await service.registration(user_in=user_in)


@router.post("/login")
async def index(
    user_in: UserLoginSchema = Depends(utils.loginForm),
    service: UserService = Depends(UserService)
):
    return await service.login(user_in=user_in)

@router.get("/users/me", response_model=UserReadSchema)
async def index(
    token: str = Depends(oauth2_scheme),
    service: UserService = Depends(UserService)
) -> UserReadSchema:
    return await service.me(token=token)


@router.post("/refresh")
async def index(
    token: str = Depends(oauth2_scheme),
    service: UserService = Depends(UserService)
): 
    return await service.refresh(token=token)