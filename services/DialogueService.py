from repositories.DialogueRepository import DialogueRepository


class DialogueService:
    @staticmethod
    async def get_by_user_id(user_id):
        return await DialogueRepository.get_by_user_id(user_id)

    @staticmethod
    async def create(user_id, message):
        return await DialogueRepository.create(user_id, message)
