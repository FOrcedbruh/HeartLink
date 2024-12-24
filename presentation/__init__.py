from fastapi import APIRouter
from .users.UserRouter import router as AuthRouter

router = APIRouter(prefix="/api/v2")
router.include_router(router=AuthRouter)