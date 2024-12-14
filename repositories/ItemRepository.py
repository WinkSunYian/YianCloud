from tortoise.exceptions import DoesNotExist
from typing import List, Optional
from db.models import Item


class ItemRepository:

    @staticmethod
    async def get_by_user_id(user_id: int) -> List[Item]:
        """根据用户 ID 获取 Item。"""
        return await Item.filter(user_id=user_id).all()

    @staticmethod
    async def create(
        user_id: int,
        name: str,
        quantity: int,
    ) -> Item:
        """
        创建 Item。
        :param user_id: 用户 ID。
        :param name: 道具名称。
        :param quantity: 道具数量。
        :return: 创建的 Item 对象。
        """
        return await Item.create(user_id=user_id, name=name, quantity=quantity)

    @staticmethod
    async def get_by_user_id_and_name(user_id: int, item_name: str) -> Optional[Item]:
        """
        根据用户 ID 和道具名称获取 Item。
        :param user_id: 用户 ID。
        :param item_name: 道具名称。
        :return: 对应的 Item 对象，或 None。
        """
        return await Item.filter(user_id=user_id, name=item_name).first()
