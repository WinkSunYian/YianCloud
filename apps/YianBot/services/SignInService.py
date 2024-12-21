from datetime import datetime, timedelta
from random import choice
from repositories.UserRepository import UserRepository
from repositories.TagRepository import TagRepository
from services.ItemService import ItemService


class SignInService:
    award_list = {"软糖": [i for i in range(10, 20)], "小熊饼干": [0, 0, 0, 1]}

    @staticmethod
    async def sign_in(identifier: str):
        """签到"""
        user = await UserRepository.get_user(identifier)
        if not user:
            raise ValueError("用户不存在！")
        if await SignInService.check_sign_in(user.id):
            raise ValueError("今日已签到！")
        await SignInService.add_sign_in_tag(user.id)
        award_msg = await SignInService.sign_in_award(user.id)
        return "签到成功！" + award_msg

    @staticmethod
    async def sign_in_award(user_id: int):
        """签到奖励"""
        award_msg = ""
        for item_name, award_range in SignInService.award_list.items():
            quantity = choice(award_range)
            if quantity <= 0:
                continue
            await ItemService.add_quantity(
                user_id,
                item_name,
                amount=quantity,
            )
            award_msg += f"获得了{quantity}个{item_name}！"
        return award_msg

    @staticmethod
    async def check_sign_in(user_id: int):
        """检测是否签到"""
        await TagRepository.clear_expired(user_id=user_id)
        return await TagRepository.check_exist(user_id=user_id, name="签到")

    @staticmethod
    async def add_sign_in_tag(user_id: int):
        """添加签到标签"""
        # 设置过期时间为明天0点
        expiry_date = (datetime.now() + timedelta(days=1)).replace(
            hour=0, minute=0, second=0, microsecond=0
        )
        return await TagRepository.create(
            user_id=user_id, name="签到", expiry_date=expiry_date
        )
