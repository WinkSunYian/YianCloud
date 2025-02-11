from common.exceptions.http_exceptions import (
    UserNotFoundException,
    TargetNotFoundException,
)
import random


class RobberyService:
    def __init__(self, user_service, item_service):
        """
        初始化时注入所需的服务
        :param user_service: 用户服务
        :param item_service: 道具服务
        """
        self.user_service = user_service
        self.item_service = item_service

    async def _get_user_and_item(self, user_id: int, item_name: str):
        """获取用户和道具"""
        user = await self.user_service.get_user(user_id)
        if not user:
            raise UserNotFoundException()

        user_item = await self.item_service.get_by_user_id_and_name(user.id, item_name)
        if not user_item:
            return None

        return user, user_item

    async def calculate_robbery(
        self, user_identifier: int, target_identifier: int, item_name: str
    ):
        """
        计算打劫的数量，数量在 -10 到 20 之间随机生成， 并根据目标道具数量进行限制。
        :param user_id: 打劫者用户 ID
        :param target_id: 目标用户 ID
        :param item_name: 道具名称
        :return: 打劫的结果
        """
        # 获取打劫者和目标用户的道具
        user, user_item = await self._get_user_and_item(user_identifier, item_name)

        target = await self.user_service.get_user(target_identifier)
        if not target:
            return {
                "message": f"{target_identifier}的背包里没有{item_name}",
            }

        target_item = await self.item_service.get_by_user_id_and_name(
            target.id, item_name
        )
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
            await self.item_service.add_quantity(user.id, item_name, robbery_quantity)
            await self.item_service.reduce_quantity(
                target.id, item_name, robbery_quantity
            )

            return {
                "message": f"打劫成功,抢走了{item_name} x {robbery_quantity}",
                "robbery_quantity": robbery_quantity,
            }
        elif robbery_quantity < 0:
            # 减少打劫者道具数量，增加目标道具数量
            await self.item_service.add_quantity(user.id, item_name, robbery_quantity)
            await self.item_service.reduce_quantity(
                target.id, item_name, robbery_quantity
            )
            return {
                "message": f"打劫失败,反被抢走了{item_name} x {abs(robbery_quantity)}",
                "robbery_quantity": robbery_quantity,
            }
        else:
            return {
                "message": f"打劫失败,被帽子叔叔发现了",
                "robbery_quantity": robbery_quantity,
            }
