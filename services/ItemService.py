from repositories.ItemRepository import ItemRepository
from repositories.UserRepository import UserRepository


class ItemService:

    @staticmethod
    async def get_by_user(identifier) -> list:
        """获取用户道具列表"""
        user = await UserRepository.get_user(identifier)
        items = await ItemRepository.get_by_user_id(user_id=user.id)
        return [{"name": item.name, "quantity": item.quantity} for item in items]

    @staticmethod
    async def add_quantity(user_id: int, item_name: str, amount: int):
        """
        增加用户的某个道具的数量。
        :param user_id: 用户 ID。
        :param item_name: 道具名称。
        :param amount: 增加的数量。
        :return: 更新后的 Item。
        """
        if amount <= 0:
            raise ValueError("增加的数量必须大于 0")

        item = await ItemRepository.get_by_user_id_and_name(user_id, item_name)
        if not item:
            return await ItemRepository.create(
                user_id=user_id, name=item_name, quantity=amount
            )

        item.quantity += amount
        await item.save()
        return item

    @staticmethod
    async def reduce_quantity(user_id: int, item_name: str, amount: int):
        """
        :param user_id: 用户 ID。
        :param item_name: 道具名称。
        :param amount: 减少的数量。
        :return: 更新后的 Item。
        """
        if amount <= 0:
            raise ValueError("减少的数量必须大于 0")

        item = await ItemRepository.get_by_user_id_and_name(user_id, item_name)
        if not item:
            raise ValueError(f"用户 {user_id} 的道具 '{item_name}' 不存在")

        if item.quantity < amount:
            raise ValueError(
                f"用户 {user_id} 的道具 '{item_name}' 数量不足，无法减少 {amount} 个"
            )

        item.quantity -= amount
        await item.save()
        return item
