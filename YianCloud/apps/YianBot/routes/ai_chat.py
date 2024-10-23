from fastapi import APIRouter, Depends
from apps.YianBot.models import User
from apps.YianBot.controllers.gpt import get_ai_chat
from core.security import validate_app_key

router = APIRouter()


@router.put("/qq/{qq}")
async def ai_chat(qq: str, message: str, app_key: str = Depends(validate_app_key)):
    user = await User.get(qq=qq)
    response = await get_ai_chat(user, message)
    return {"message": response}
