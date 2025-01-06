from repositories.UserMetadataRepository import UserMetadataRepository


class UserMetadataService:
    @staticmethod
    async def get_by_user_id_and_name(user_id: int, key: str):
        metadata = await UserMetadataRepository.get_by_user_id_and_key(user_id, key)
        if metadata is None:
            return None
        return metadata.value.get("data")

    @staticmethod
    async def create(user_id: int, key: str, value: dict):
        return await UserMetadataRepository.create(user_id, key, {"data": value})

    @staticmethod
    async def delete_by_user_id_and_name(user_id: int, key: str):
        return await UserMetadataRepository.delete_by_user_id_and_key(user_id, key)
