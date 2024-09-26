from fastapi import APIRouter
from .users import router as users_router
from .signin import router as signin_router

router = APIRouter()

# 注册子路由
router.include_router(users_router, prefix="/users")
router.include_router(signin_router, prefix="/signin")
