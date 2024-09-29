from fastapi import APIRouter, Body, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from core.db_connection import db_conn
from sqlalchemy import select
from core.models import Hobby
from .schemas import HobbySchema, HobbyCreateSChema
# from . import utils


router = APIRouter(prefix="/hobbies", tags=["Hobbies"])



# @router.post("/create")
# async def create_hobbie(hobby_in: HobbyCreateSChema = Depends(utils.hobbyForm), session: AsyncSession = Depends(db_conn.sesion_creation)):
#     hobby = Hobby(**hobby_in.model_dump())
#     session.add(hobby)
    
#     await session.commit()
    
#     return {
#         "message": hobby.title
#     }


@router.get("/")
async def get_hobbies(session: AsyncSession = Depends(db_conn.sesion_creation)) -> list[HobbySchema]:
    st = await session.execute(select(Hobby))
    hobbies = st.scalars().all()
    
    
    return list(hobbies)