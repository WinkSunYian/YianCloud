from services.UserService import UserService
from apps.YianBot.services.GPTService import GPTService
from configs.CHAT_GPT import CHAT_GPT


class ChatService:

    @staticmethod
    async def get_gpt_response(param: str, user_message: str):
        """根据 qq 或 account 获取用户对话记录并向 GPT API 请求回复"""
        # 1. 根据 qq 或 account 获取用户信息
        user = await UserService.get_user(param)
        if not user:
            return {"error": "User not found."}

        # 2. 获取用户的对话记录并构建消息上下文
        messages = await ChatService.prepare_messages(user, user_message)

        # 3. 获取 GPT 回复
        gpt_response = await GPTService.get_ai_chat(messages)

        # 4. 保存用户与 GPT 的对话记录
        await ChatService.save_dialogues(user, user_message, gpt_response)

        # 5. 返回 GPT 回复
        return gpt_response

    @staticmethod
    async def prepare_messages(user: dict, user_message: str):
        """构建 GPT 请求消息上下文"""
        # 初始化 system 消息
        messages = [{"role": "system", "content": CHAT_GPT.CUE_WORD}]

        # 获取用户对话记录
        dialogues = await UserService.get_user_dialogues(user, limit=5)
        for dialogue in dialogues:
            messages.append({"role": "user", "content": dialogue["content"]})
            messages.append({"role": "assistant", "content": dialogue["content"]})

        # 添加当前用户消息
        messages.append({"role": "user", "content": user_message})

        return messages

    @staticmethod
    async def save_dialogues(user: dict, user_message: str, gpt_response: str):
        """保存用户与 GPT 的对话记录"""
        await UserService.add_user_dialogue(user, role="user", content=user_message)
        await UserService.add_user_dialogue(
            user, role="assistant", content=gpt_response
        )
