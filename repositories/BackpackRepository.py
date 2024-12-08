from db.models import Backpack
from typing import Optional


class BackpackRepository:
    @staticmethod
    async def get_by_user_id(user_id: int) -> Optional[Backpack]:
        """通过用户 ID 获取背包"""
        return await Backpack.filter(user_id=user_id).first()
    