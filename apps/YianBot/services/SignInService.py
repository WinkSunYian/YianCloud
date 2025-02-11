from datetime import datetime, timedelta
from random import choice
from common.exceptions.http_exceptions import (
    TodaySignedException,
    UserNotFoundException,
)


class SignInService:
    award_list = {"软糖": [i for i in range(10, 20)], "小熊饼干": [0, 0, 0, 1]}

    def __init__(
        self,
        user_repository,
        tag_repository,
        item_service,
    ):
        """
        初始化时注入所需的依赖
        :param user_repository: 用户仓库
        :param tag_repository: 标签仓库
        :param item_service: 道具服务
        """
        self.user_repository = user_repository
        self.tag_repository = tag_repository
        self.item_service = item_service

    async def sign_in(self, identifier: str):
        """签到"""
        user = await self.user_repository.get_user(identifier)
        if not user:
            raise UserNotFoundException()
        if await self.check_sign_in(user.id):
            raise TodaySignedException()
        await self.add_sign_in_tag(user.id)
        award_msg = await self.sign_in_award(user.id)
        return "签到成功！" + award_msg

    async def sign_in_award(self, user_id: int):
        """签到奖励"""
        award_msg = ""
        for item_name, award_range in self.award_list.items():
            quantity = choice(award_range)
            if quantity <= 0:
                continue
            await self.item_service.add_quantity(
                user_id,
                item_name,
                amount=quantity,
            )
            award_msg += f"获得了{quantity}个{item_name}！"
        return award_msg

    async def check_sign_in(self, user_id: int):
        """检测是否签到"""
        await self.tag_repository.clear_expired(user_id=user_id)
        return await self.tag_repository.check_exist(user_id=user_id, name="签到")

    async def add_sign_in_tag(self, user_id: int):
        """添加签到标签"""
        # 设置过期时间为明天0点
        expiry_date = (datetime.now() + timedelta(days=1)).replace(
            hour=0, minute=0, second=0, microsecond=0
        )
        return await self.tag_repository.create(
            user_id=user_id, name="签到", expiry_date=expiry_date
        )
