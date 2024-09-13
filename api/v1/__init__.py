from fastapi import APIRouter
from .auth.views import router as authRouter
from .profiles.views import router as profilesRouter
from .like.views import router as likeRouter

router = APIRouter(prefix="/api/v1")
router.include_router(router=authRouter)
router.include_router(router=profilesRouter)
router.include_router(router=likeRouter)