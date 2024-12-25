from fastapi import APIRouter
from .users.UserRouter import router as AuthRouter
from .profiles.ProfileRouter import router as ProfileRouter


router = APIRouter(prefix="/api/v2")
router.include_router(router=AuthRouter)
router.include_router(router=ProfileRouter)