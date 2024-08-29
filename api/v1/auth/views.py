from fastapi import APIRouter, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession
from core import db_conn
from .schemas import UserRegistrationSchema, UserLoginSchema
from .actions import TokenInfo


router = APIRouter(prefix="/auth", tags=["Auth"])



@router.post("/registration")
async def registration(session: AsyncSession = Depends(db_conn.sesion_creation), User_in: UserRegistrationSchema = Depends(UserRegistrationSchema)) -> TokenInfo:
    pass



@router.post("/login")
async def login(session: AsyncSession = Depends(db_conn.sesion_creation), User_in: UserLoginSchema = Depends(UserLoginSchema)) -> TokenInfo:
    pass