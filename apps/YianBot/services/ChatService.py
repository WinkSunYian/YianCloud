from services.DialogueService import DialogueService
from services.UserService import UserService
from apps.YianBot.services.GPTService import GPTService
from configs.CHAT_GPT import CHAT_GPT


class ChatService:

    @staticmethod
    async def get_gpt_response(identifier: str, user_message: str):
        user = await UserService.get_user(identifier)
        messages = await ChatService.prepare_messages(user.id, user_message)
        gpt_response = await GPTService.get_ai_chat(messages)
        await ChatService.save_dialogues(user.id, user_message, gpt_response)
        return gpt_response

    @staticmethod
    async def prepare_messages(user_id: int, user_message: str):
        messages = [{"role": "system", "content": CHAT_GPT.CUE_WORD}]

        dialogues = await DialogueService.get_by_user_id(user_id=user_id, limit=10)
        for dialogue in dialogues:
            messages.append({"role": dialogue.role, "content": dialogue.content})

        messages.append({"role": "user", "content": user_message})
        return messages

    @staticmethod
    async def save_dialogues(user_id: int, user_message: str, gpt_response: str):
        await DialogueService.create(user_id=user_id, role="user", content=user_message)
        await DialogueService.create(
            user_id=user_id, role="assistant", content=gpt_response
        )
