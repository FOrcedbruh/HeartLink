from fastapi import APIRouter
from .users.UserRouter import router as AuthRouter
from .profiles.ProfileRouter import router as ProfileRouter
from .likes.LikeRouter import router as LikeRouter


router = APIRouter(prefix="/api/v2")
router.include_router(router=AuthRouter)
router.include_router(router=ProfileRouter)
router.include_router(router=LikeRouter)