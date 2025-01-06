from db.models import UserMetadata


class UserMetadataRepository:

    @staticmethod
    async def get_by_user_id_and_key(user_id: int, key: str):
        """
        根据用户ID和元数据键获取用户元数据。

        :param user_id: 用户ID
        :param key: 元数据键
        :return: 用户元数据对象
        """
        user_metadata = await UserMetadata.get_or_none(user_id=user_id, key=key)
        return user_metadata

    @staticmethod
    async def create(user_id: int, key: str, value: dict):
        """
        创建用户元数据。

        :param user_id: 用户ID
        :param key: 元数据键
        :param value: 元数据值
        :return: 创建的用户元数据对象
        """
        user_metadata = UserMetadata(user_id=user_id, key=key, value=value)
        await user_metadata.save()
        return user_metadata

    @staticmethod
    async def delete_by_user_id_and_key(user_id: int, key: str):
        """
        根据用户ID和元数据键删除用户元数据。

        :param user_id: 用户ID
        :param key: 元数据键
        """
        await UserMetadata.filter(user_id=user_id, key=key).delete()
