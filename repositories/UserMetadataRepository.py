from db.models import UserMetadata


class UserMetadataRepository:
    """
    UserMetadataRepository 用于处理与用户元数据（UserMetadata）相关的数据库操作。
    包括获取、创建和删除用户元数据。
    """

    def __init__(self):
        """构造函数用于初始化可能的配置或服务，当前没有额外初始化。"""
        pass

    async def get_by_user_id_and_key(self, user_id: int, key: str):
        """
        根据用户 ID 和元数据键获取用户元数据。

        :param user_id: 用户 ID。
        :param key: 元数据键。
        :return: 返回对应的用户元数据对象，若没有找到则返回 None。
        """
        user_metadata = await UserMetadata.get_or_none(user_id=user_id, key=key)
        return user_metadata

    async def create(self, user_id: int, key: str, value: dict):
        """
        创建新的用户元数据。

        :param user_id: 用户 ID，表示该元数据所关联的用户。
        :param key: 元数据键。
        :param value: 元数据值，通常是字典类型。
        :return: 返回创建成功的用户元数据对象。
        """
        user_metadata = UserMetadata(user_id=user_id, key=key, value=value)
        await user_metadata.save()
        return user_metadata

    async def delete_by_user_id_and_key(self, user_id: int, key: str):
        """
        根据用户 ID 和元数据键删除用户元数据。

        :param user_id: 用户 ID。
        :param key: 元数据键。
        :return: 无返回值，执行删除操作。
        """
        await UserMetadata.filter(user_id=user_id, key=key).delete()
