from repositories.DialogueRepository import DialogueRepository


class DialogueService:
    @staticmethod
    async def get_by_user_id(user_id, limit: int):
        return await DialogueRepository.get_by_user_id(user_id, limit)

    @staticmethod
    async def create(user_id: int, role: str, content: str):
        return await DialogueRepository.create(user_id, role, content)
