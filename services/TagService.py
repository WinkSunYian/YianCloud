from repositories.TagRepository import TagRepository


class TagService:
    @staticmethod
    async def get_by_user_id(user_id: int):
        return await TagRepository.get_by_user_id(user_id)

    @staticmethod
    async def create(user_id: int, name: str):
        return await TagRepository.create(user_id, name)

    @staticmethod
    async def check_exist(tag_id: int):
        return await TagRepository.check_exist(tag_id)

    @staticmethod
    async def clear_expired(tag_id: int, name: str):
        return await TagRepository.clear_expired(tag_id, name)
