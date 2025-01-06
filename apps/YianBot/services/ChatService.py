from services.DialogueService import DialogueService
from services.UserService import UserService
from services.UserMetadataService import UserMetadataService
from apps.YianBot.services.GPTService import GPTService
from configs.CHAT_GPT import CHAT_GPT
from common.exceptions.http_exceptions import UserNotFoundException


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
        # 使用默认提示词
        gpt_cue_word = await UserMetadataService.get_by_user_id_and_name(
            user_id=user_id, key="面具"
        )
        gpt_cue_word = CHAT_GPT.CUE_WORD if not gpt_cue_word else gpt_cue_word
        messages = [{"role": "system", "content": gpt_cue_word}]

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
