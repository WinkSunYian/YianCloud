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
        计算打劫的数量，数量在 -10 到 20 之间随机生成，
        并根据目标道具数量和用户道具数量进行限制。
        :param user_id: 打劫者用户 ID
        :param target_id: 目标用户 ID
        :param item_name: 道具名称
        :return: 打劫的结果
        """
        # 获取打劫者和目标用户的道具
        user, user_item = await self._get_user_and_item(user_identifier, item_name)

        target = await self.user_service.get_user(target_identifier)
        if not target:
            raise TargetNotFoundException()  # 目标用户不存在

        target_item = await self.item_service.get_by_user_id_and_name(
            target.id, item_name
        )
        if not target_item:
            return {
                "message": f"{target_identifier}的背包里没有{item_name}",
            }

        # 根据目标道具的数量和用户道具数量来确定打劫数量的范围
        min_robbery_quantity = -10  # 反抢最小数量
        max_robbery_quantity = 20  # 正常抢劫最大数量

        # 计算用户道具的数量限制
        user_item_quantity = user_item.quantity if user_item else 0
        target_item_quantity = target_item.quantity

        # 正常打劫：确保抢劫数量在 0 和 20 之间，并且不能超过目标的道具数量
        normal_robbery_max = min(max_robbery_quantity, target_item_quantity)

        # 反抢：用户道具不足时，反抢的最大数量为 -10 至 0 之间，且不超过 10
        if user_item_quantity <= 0:
            min_robbery_quantity = -min(10, target_item_quantity)
            max_robbery_quantity = 0
        else:
            # 正常打劫范围
            min_robbery_quantity = max(-10, -user_item_quantity)
            max_robbery_quantity = normal_robbery_max

        robbery_quantity = random.randint(min_robbery_quantity, max_robbery_quantity)

        # 判断打劫结果
        if robbery_quantity > 0:
            # 正常打劫：减少目标道具数量，增加打劫者道具数量
            await self.item_service.add_quantity(user.id, item_name, robbery_quantity)
            await self.item_service.reduce_quantity(
                target.id, item_name, robbery_quantity
            )

            return {
                "message": f"打劫成功,抢走了{item_name} x {robbery_quantity}",
                "robbery_quantity": robbery_quantity,
            }
        elif robbery_quantity < 0:
            # 反抢：减少打劫者道具数量，增加目标道具数量
            robbery_quantity = abs(robbery_quantity)  # 确保反抢为正数
            await self.item_service.add_quantity(user.id, item_name, robbery_quantity)
            await self.item_service.reduce_quantity(
                target.id, item_name, robbery_quantity
            )
            return {
                "message": f"打劫失败,反被抢走了{item_name} x {robbery_quantity}",
                "robbery_quantity": robbery_quantity,
            }
        else:
            return {
                "message": f"打劫失败,被帽子叔叔发现了",
                "robbery_quantity": robbery_quantity,
            }
