from fastapi import APIRouter
from apps.YianBot.models import User
from apps.YianBot.controllers.gpt import get_ai_chat

router = APIRouter()


@router.put("/qq/{qq}")
async def ai_chat(qq: str, message: str):
    user = await User.get(qq=qq)
    return await get_ai_chat(user, message)
