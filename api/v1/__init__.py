from fastapi import APIRouter
from .auth.views import router as authRouter
from .profiles.views import router as profilesRouter
from .like.views import router as likeRouter
from .hobbies.views import router as hobbiesRouter

router = APIRouter(prefix="/api/v1")
router.include_router(router=authRouter)
router.include_router(router=profilesRouter)
router.include_router(router=likeRouter)
router.include_router(router=hobbiesRouter)