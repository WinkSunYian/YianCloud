from fastapi import APIRouter
from .server_status import router as server_status_router
from .users import router as users_router
from .signin import router as signin_router
from .websockets import router as websockets_router

router = APIRouter()

# 注册子路由
router.include_router(server_status_router, prefix="/server_status")
router.include_router(websockets_router, prefix="/ws")
router.include_router(users_router, prefix="/users")
router.include_router(signin_router, prefix="/signin")
