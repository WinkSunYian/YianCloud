from repositories.UserMetadataRepository import UserMetadataRepository


class UserMetadataService:
    """
    UserMetadataService 负责处理与用户元数据相关的业务逻辑。
    它提供了获取元数据、创建元数据和删除元数据的功能。
    """

    def __init__(self, user_metadata_repository: UserMetadataRepository):
        """
        构造函数用于注入依赖的 UserMetadataRepository。

        :param user_metadata_repository: UserMetadataRepository 实例。
        """
        self.user_metadata_repository = user_metadata_repository

    async def get_by_user_id_and_name(self, user_id: int, key: str):
        """
        根据用户 ID 和元数据键获取用户元数据。

        :param user_id: 用户 ID。
        :param key: 元数据键。
        :return: 用户元数据的 "data" 部分，如果没有找到则返回 None。
        """
        metadata = await self.user_metadata_repository.get_by_user_id_and_key(
            user_id, key
        )
        if metadata is None:
            return None
        return metadata.value.get("data")

    async def create(self, user_id: int, key: str, value: dict):
        """
        创建用户元数据。

        :param user_id: 用户 ID。
        :param key: 元数据键。
        :param value: 元数据值。
        :return: 创建的用户元数据对象。
        """
        return await self.user_metadata_repository.create(user_id, key, {"data": value})

    async def delete_by_user_id_and_name(self, user_id: int, key: str):
        """
        根据用户 ID 和元数据键删除用户元数据。

        :param user_id: 用户 ID。
        :param key: 元数据键。
        :return: 删除操作的结果。
        """
        return await self.user_metadata_repository.delete_by_user_id_and_key(
            user_id, key
        )
