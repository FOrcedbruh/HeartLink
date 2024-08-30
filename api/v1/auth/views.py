from fastapi import APIRouter, Depends, Response, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from core import db_conn
from .schemas import UserRegistrationSchema, UserLoginSchema, UserSchema
from .actions import TokenInfo, create_access_token, create_refresh_token, http_bearer, get_current_auth_user
from sqlalchemy import select
from core.models import User, Profile
from . import utils




router = APIRouter(prefix="/auth", tags=["Auth"], dependencies=[Depends(http_bearer)])



@router.post("/registration")
async def registration(response: Response, session: AsyncSession = Depends(db_conn.sesion_creation), user_in: UserRegistrationSchema = Depends(UserRegistrationSchema)) -> TokenInfo:
    st = await session.execute(select(User).filter(User.email == user_in.email))
    candidate = st.scalars().first()
    if candidate:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The user already exists"
        )
    else:
        hashed_passowrd: bytes = utils.hash_passowrd(user_in.password)
        user_in.password = hashed_passowrd
        
        user = User(**user_in.model_dump())
        session.add(user)
        await session.commit()
        
        access_token = create_access_token(user=user)
        refresh_token = create_refresh_token(user=user)
        
        response.set_cookie(key="access_token", value=access_token)
        response.set_cookie(key="refresh_token", value=refresh_token)
        
        return TokenInfo(
            access_token=access_token,
            refresh_token=refresh_token,
        )


@router.post("/login")
async def login(response: Response, session: AsyncSession = Depends(db_conn.sesion_creation), user_in: UserLoginSchema = Depends(UserLoginSchema)) -> TokenInfo:
    st = await session.execute(select(User).filter(User.email == user_in.email))
    user = st.scalars().first()
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The user doesn't exist"
        )
    else:
        isValid_password: bool = utils.validation_password(user.password, user_in.password)
        if isValid_password == False:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Incorrect password"
            )
        else:
            access_token = create_access_token(user=user)
            refresh_token = create_refresh_token(user=user)
            
            response.set_cookie(key="access_token", value=access_token)
            response.set_cookie(key="refresh_token", value=refresh_token)
            
            return TokenInfo(
                access_token=access_token,
                refresh_token=refresh_token
            )


@router.post("/logout")
async def logout(response: Response) -> dict:
    response.delete_cookie("acess_token")
    response.delete_cookie("refresh_token")
    
    return {
        "message": "Successfull Log out",
        "status": status.HTTP_200_OK
    }
    
@router.get("/me")
def get_profile(
        authUser: UserSchema = Depends(get_current_auth_user)
    ) -> dict:
   
    userData: dict = {
        "username": authUser.username,
        "email": authUser.email,
    }
    
    return userData
    