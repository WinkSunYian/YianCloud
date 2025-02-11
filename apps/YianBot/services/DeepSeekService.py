from openai import OpenAI
from apps.YianBot.base.BaseAIService import BaseAIService
from configs.DEEPSEEK import DEEPSEEK


class DeepSeekService(BaseAIService):
    def __init__(
        self,
        api_key: str = DEEPSEEK.API_KEY,
        base_url: str = DEEPSEEK.BASE_URL,
        model: str = DEEPSEEK.MODEL,
    ):
        self.client = OpenAI(api_key=api_key, base_url=base_url)
        self.model = model

    def get_response(
        self, messages: list, temperature: float = 1.3, stream: bool = False
    ) -> str:
        """获取 DeepSeek 回复"""
        response = self.client.chat.completions.create(
            model=self.model, messages=messages, temperature=temperature, stream=stream
        )
        return response.choices[0].message.content


if __name__ == "__main__":
    deepseek_service = DeepSeekService()
    messages = [
        {
            "role": "system",
            "content": "请你扮演一位名叫逸安/小逸安的女性，你将参与多人聊天，你只需要回答@你的消息，你的语气要简短冷漠带一点文艺",
        },
        {"role": "user", "content": "天奇03：你好"},
        {"role": "user", "content": "木：你好呀"},
        {"role": "user", "content": "七月：@小逸安傻子"},
    ]
    response = deepseek_service.get_response(messages)
    print(response)
