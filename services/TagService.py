from datetime import datetime
from repositories.TagRepository import TagRepository


class TagService:
    """
    TagService 负责处理与标签相关的业务逻辑。
    它提供了获取标签、创建标签、检查标签是否存在以及清除过期标签等功能。
    """

    def __init__(self, tag_repository: TagRepository):
        """
        构造函数用于注入依赖的 TagRepository。

        :param tag_repository: TagRepository 实例。
        """
        self.tag_repository = tag_repository

    async def get_by_user_id(self, user_id: int):
        """
        根据用户 ID 获取该用户的所有标签。

        :param user_id: 用户 ID。
        :return: 该用户的所有标签。
        """
        return await self.tag_repository.get_by_user_id(user_id)

    async def create(self, user_id: int, name: str, expiry_date: datetime):
        """
        创建一个新标签。

        :param user_id: 用户 ID。
        :param name: 标签名称。
        :param expiry_date: 标签过期时间。
        :return: 创建的标签。
        """
        return await self.tag_repository.create(user_id, name, expiry_date)

    async def check_exist(self, user_id: int, name: str) -> bool:
        """
        检查用户的指定标签是否存在。

        :param user_id: 用户 ID。
        :param name: 标签名称。
        :return: 标签是否存在。
        """
        return await self.tag_repository.check_exist(user_id, name)

    async def clear_expired(self, user_id: int):
        """
        清除用户所有过期的标签。

        :param user_id: 用户 ID。
        :return: 删除的标签数量。
        """
        return await self.tag_repository.clear_expired(user_id)
