from datetime import datetime
from typing import List
from db.models import Tag


class TagRepository:
    """
    TagRepository 用于处理与标签（Tag）相关的数据库操作。
    包括通过用户 ID 获取标签、创建标签、检查标签是否存在，以及清除过期标签。
    """

    def __init__(self):
        """构造函数用于初始化可能的配置或服务，当前没有额外初始化。"""
        pass

    async def get_by_user_id(self, user_id: int) -> List[Tag]:
        """
        通过用户 ID 获取所有的标签。

        :param user_id: 用户 ID。
        :return: 返回与用户 ID 相关联的所有标签对象列表。
        """
        return await Tag.filter(user_id=user_id).all()

    async def create(self, user_id: int, name: str, expiry_date: datetime) -> Tag:
        """
        创建新的标签。

        :param user_id: 用户 ID，表示该标签所关联的用户。
        :param name: 标签名称。
        :param expiry_date: 标签过期时间。
        :return: 创建成功的标签对象。
        """
        return await Tag.create(user_id=user_id, name=name, expiry_date=expiry_date)

    async def check_exist(self, user_id: int, name: str) -> bool:
        """
        检查用户是否已经有指定名称的标签。

        :param user_id: 用户 ID。
        :param name: 标签名称。
        :return: 如果标签已存在，返回 True，否则返回 False。
        """
        return await Tag.filter(user_id=user_id, name=name).exists()

    async def clear_expired(self, user_id: int):
        """
        清除过期标签。

        :param user_id: 用户 ID。
        :return: 无返回值。执行删除过期标签的操作。
        """
        await Tag.filter(user_id=user_id, expiry_date__lt=datetime.now()).delete()
