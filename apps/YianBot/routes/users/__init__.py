from fastapi import APIRouter
from .users import router as users_router
from .tags import router as tags_router
from .ai_chat import router as ai_chat_router

# router = APIRouter()
# router.include_router(users_router, prefix="/users/{user_id}")
# router.include_router(tags_router, prefix="/users/{user_id}")
# router.include_router(ai_chat_router, prefix="/users/{user_id}")
