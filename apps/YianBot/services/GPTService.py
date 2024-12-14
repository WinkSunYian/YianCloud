import openai
from configs.CHAT_GPT import CHAT_GPT


class GPTService:
    openai.api_key = CHAT_GPT.API_KEY
    openai.base_url = CHAT_GPT.BASE_URL

    @staticmethod
    async def get_ai_chat(messages: list) -> str:
        """调用 GPT API 获取回复"""
        gpt_response = await GPTService.call_gpt_api(messages)
        return gpt_response.choices[0].message.content

    @staticmethod
    async def call_gpt_api(messages: list) -> str:
        """调用 GPT API 获取回复"""
        response = openai.chat.completions.create(
            model=CHAT_GPT.MODEL, messages=messages
        )
        return response
