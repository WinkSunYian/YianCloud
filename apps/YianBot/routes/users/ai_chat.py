# from fastapi import APIRouter, Depends
# from db.models import User
# from apps.YianBot.controllers.gpt import get_ai_chat
# from common.resp import respSuccessJson, respErrorJson
# from pydantic import BaseModel


# class AIChatRequest(BaseModel):
#     message: str


# router = APIRouter()


# @router.post("/ai-chat")
# async def ai_chat(user_id: str, request: AIChatRequest):
#     user = await User.get(qq=user_id)
#     reply = await get_ai_chat(user, request.message)
#     return respSuccessJson(data=reply)
