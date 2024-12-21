from services.ItemService import ItemService
from services.UserService import UserService
from common.exceptions.http_exceptions import (
    UserNotFoundException,
    TargetNotFoundException,
)
import random


class RobberyService:

    @staticmethod
    async def calculate_robbery(
        user_identifier: int, target_identifier: int, item_name: str
    ):
        """
        计算打劫的数量，数量在 -10 到 20 之间随机生成，
        并根据目标道具数量进行限制。
        :param user_id: 打劫者用户 ID
        :param target_id: 目标用户 ID
        :param item_name: 道具名称
        :return: 打劫的结果
        """
        # 获取打劫者和目标用户的道具
        user = await UserService.get_user(user_identifier)
        if not user:
            raise UserNotFoundException()

        target = await UserService.get_user(target_identifier)
        if not target:
            return {
                "message": f"{target_identifier}的背包里没有{item_name}",
            }

        user_item = await ItemService.get_by_user_id_and_name(user.id, item_name)

        target_item = await ItemService.get_by_user_id_and_name(target.id, item_name)
        if not target_item:
            return {
                "message": f"{target_identifier}的背包里没有{item_name}",
            }

        # 根据目标道具的数量来确定打劫数量的范围
        min_robbery_quantity = -min(10, user_item.quantity) if user_item else 0
        max_robbery_quantity = min(20, target_item.quantity)
        robbery_quantity = random.randint(min_robbery_quantity, max_robbery_quantity)

        # 判断打劫结果
        if robbery_quantity > 0:
            # 减少目标道具数量，增加打劫者道具数量
            await ItemService.reduce_quantity(target.id, item_name, robbery_quantity)
            await ItemService.add_quantity(user.id, item_name, robbery_quantity)

            return {
                "message": f"打劫成功,抢走了{item_name} x {robbery_quantity}",
                "robbery_quantity": robbery_quantity,
            }
        elif robbery_quantity < 0:
            await ItemService.reduce_quantity(user.id, item_name, -robbery_quantity)
            return {
                "message": f"打劫失败,反被抢走了{item_name} x {abs(robbery_quantity)}",
                "robbery_quantity": robbery_quantity,
            }
        else:
            return {
                "message": f"打劫失败,被帽子叔叔发现了",
                "robbery_quantity": robbery_quantity,
            }
