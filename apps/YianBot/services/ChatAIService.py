from configs.CHAT_GPT import CHAT_GPT


class ChatAIService:
    def __init__(self, user_metadata_service, ai_service):
        """通过构造函数注入依赖"""
        self.user_metadata_service = user_metadata_service
        self.ai_service = ai_service

    async def get_gpt_response(self, identifier: str, messages: list) -> str:
        """获取 AI 的回复"""
        # 获取用户的面具
        user_cue_word = await self.user_metadata_service.get_by_user_id_and_name(
            user_id=identifier, key="面具"
        )
        gpt_cue_word = CHAT_GPT.CUE_WORD if not user_cue_word else user_cue_word

        # 将面具信息拼接到 messages
        messages.insert(0, {"role": "system", "content": gpt_cue_word})

        # 调用 AI 服务获取回复
        gpt_response = await self.ai_service.get_response(messages)
        return gpt_response
