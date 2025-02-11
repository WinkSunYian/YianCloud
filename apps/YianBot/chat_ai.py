from fastapi import Depends
from pydantic import BaseModel
from utils.ServiceRouter import ServiceRouter
from apps.YianBot.services.ChatAIService import ChatAIService
from core.Container import Container
from core.security import get_appkey


class ChatRequest(BaseModel):
    messages: list


class ChatAiRouter(ServiceRouter):
    def __init__(self):
        self.container = Container()
        self.chat_ai_service = self.container.get_chat_ai_service()
        self.set_path("/users/{user_id}/chat-ai")
        self.set_desc(
            "post", "获取ChatGpt的回复", "user_id: 用户ID\nmessage: 输入的消息"
        )
        self.setup_routes()

    async def post(
        self,
        user_id: str,
        chat_request: ChatRequest,
        app_key: str = Depends(get_appkey),
    ):
        print(user_id, chat_request.messages)
        response = await self.chat_ai_service.get_gpt_response(
            user_id, chat_request.messages
        )
        print(response)
        return self.res(data={"response": response})
