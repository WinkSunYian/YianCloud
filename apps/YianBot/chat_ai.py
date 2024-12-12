from fastapi import Depends
from utils.ServiceRouter import ServiceRouter
from common.error_code import ERROR_USER_NOT_FOUND
from services.UserService import UserService
from apps.YianBot.services.ChatService import ChatService
from core.security import get_appkey
from pydantic import BaseModel
class ChatRequest(BaseModel):
    message: str  # 通过请求体提交的消息字段
    
class chat_ai(ServiceRouter):
    def __init__(self):
        self.set_path("/users/{user_id}/chat-ai")
        self.set_desc(
            "post", "获取ChatGpt的回复", "user_id: 用户ID\nmessage: 输入的消息"
        )
        self.setup_routes()

    async def post(
        self, user_id: str, chat_request: ChatRequest, app_key: str = Depends(get_appkey)
    ):
        chat = await ChatService.get_gpt_response(user_id, chat_request.message)
        return self.res(data={"chat": chat})
