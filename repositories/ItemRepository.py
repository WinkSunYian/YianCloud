from tortoise.exceptions import DoesNotExist
from typing import List, Optional
from db.models import Item


class ItemRepository:
    """
    ItemRepository 用于处理与 Item 相关的数据库操作。
    包括获取用户的道具、创建道具以及通过用户 ID 和道具名称查找道具。
    """

    def __init__(self):
        """构造函数用于初始化可能的配置或服务，当前没有额外初始化。"""
        pass

    async def get_by_user_id(self, user_id: int) -> List[Item]:
        """
        根据用户 ID 获取所有的 Item。

        :param user_id: 用户 ID。
        :return: 返回与用户 ID 相关联的所有 Item 对象列表。
        """
        return await Item.filter(user_id=user_id).all()

    async def create(self, user_id: int, name: str, quantity: int) -> Item:
        """
        创建新的 Item。

        :param user_id: 用户 ID，表示该 Item 所属的用户。
        :param name: 道具名称。
        :param quantity: 道具数量。
        :return: 创建成功的 Item 对象。
        """
        return await Item.create(user_id=user_id, name=name, quantity=quantity)

    async def get_by_user_id_and_name(
        self, user_id: int, item_name: str
    ) -> Optional[Item]:
        """
        根据用户 ID 和道具名称获取特定的 Item。

        :param user_id: 用户 ID。
        :param item_name: 道具名称。
        :return: 如果找到，返回对应的 Item 对象，否则返回 None。
        """
        return await Item.filter(user_id=user_id, name=item_name).first()
