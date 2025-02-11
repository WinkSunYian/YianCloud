from repositories.ItemRepository import ItemRepository
from repositories.UserRepository import UserRepository


class ItemService:
    """
    ItemService 负责处理用户道具相关的业务逻辑。
    它提供了对道具列表的获取、道具数量的增减及调整等功能。
    """

    def __init__(
        self, item_repository: ItemRepository, user_repository: UserRepository
    ):
        """
        构造函数用于注入依赖的 ItemRepository 和 UserRepository。

        :param item_repository: ItemRepository 实例。
        :param user_repository: UserRepository 实例。
        """
        self.item_repository = item_repository
        self.user_repository = user_repository

    async def get_by_user(self, identifier: str) -> list:
        """
        获取指定用户的道具列表。

        :param identifier: 用户标识（可以是 QQ 或账户名）。
        :return: 道具名称和数量的列表。
        """
        user = await self.user_repository.get_user(identifier)
        items = await self.item_repository.get_by_user_id(user.id)
        return [{"name": item.name, "quantity": item.quantity} for item in items]

    async def get_by_user_id_and_name(self, user_id: int, item_name: str):
        """
        根据用户 ID 和道具名称获取道具。

        :param user_id: 用户 ID。
        :param item_name: 道具名称。
        :return: 对应的 Item 对象，或 None。
        """
        return await self.item_repository.get_by_user_id_and_name(user_id, item_name)

    async def add_quantity(self, user_id: int, item_name: str, amount: int):
        """
        增加指定用户道具的数量。

        :param user_id: 用户 ID。
        :param item_name: 道具名称。
        :param amount: 增加的数量。
        :return: 更新后的 Item 对象。
        """
        if amount <= 0:
            raise ValueError("增加的数量必须大于 0")

        item = await self.item_repository.get_by_user_id_and_name(user_id, item_name)
        if not item:
            return await self.item_repository.create(
                user_id=user_id, name=item_name, quantity=amount
            )

        item.quantity += amount
        await item.save()
        return item

    async def reduce_quantity(self, user_id: int, item_name: str, amount: int):
        """
        减少指定用户道具的数量。

        :param user_id: 用户 ID。
        :param item_name: 道具名称。
        :param amount: 减少的数量。
        :return: 更新后的 Item 对象。
        """
        if amount <= 0:
            raise ValueError("减少的数量必须大于 0")

        item = await self.item_repository.get_by_user_id_and_name(user_id, item_name)
        if not item:
            raise ValueError(f"用户 {user_id} 的道具 '{item_name}' 不存在")

        if item.quantity < amount:
            raise ValueError(
                f"用户 {user_id} 的道具 '{item_name}' 数量不足，无法减少 {amount} 个"
            )

        item.quantity -= amount
        await item.save()
        return item

    async def adjust_quantity(self, user_id: int, item_name: str, amount: int):
        """
        根据传入的数量调整用户道具的数量。

        :param user_id: 用户 ID。
        :param item_name: 道具名称。
        :param amount: 调整的数量。
        :return: 更新后的 Item 对象。
        """
        if amount == 0:
            raise ValueError("调整的数量不能为 0")

        item = await self.item_repository.get_by_user_id_and_name(user_id, item_name)

        if not item:
            if amount > 0:
                return await self.item_repository.create(
                    user_id=user_id, name=item_name, quantity=amount
                )
            else:
                raise ValueError(
                    f"用户 {user_id} 的道具 '{item_name}' 不存在，无法减少数量"
                )

        if amount > 0:
            item.quantity += amount
        else:
            if item.quantity < abs(amount):
                raise ValueError(
                    f"用户 {user_id} 的道具 '{item_name}' 数量不足，无法减少 {abs(amount)} 个"
                )
            item.quantity += amount

        await item.save()
        return item
