import openai
from apps.YianBot.base.BaseAIService import BaseAIService
from configs.CHAT_GPT import CHAT_GPT


class ChatGPTService(BaseAIService):
    def __init__(
        self,
        api_key: str = CHAT_GPT.API_KEY,
        base_url: str = CHAT_GPT.BASE_URL,
        model: str = CHAT_GPT.MODEL,
    ):
        openai.api_key = api_key
        openai.base_url = base_url
        self.model = model

    async def get_response(
        self, messages: list, temperature: float = 1.3, stream: bool = False
    ) -> str:
        """调用 ChatGPT API 获取回复"""
        response = openai.chat.completions.create(
            model=self.model, messages=messages, temperature=temperature, stream=stream
        )
        return response.choices[0].message.content
