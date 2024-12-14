from db.models import Tag
from datetime import datetime
from typing import List
from db.models import User


class TagRepository:
    @staticmethod
    async def get_by_user_id(user_id: int) -> List[Tag]:
        """通过用户ID获取标签"""
        return await Tag.filter(user_id=user_id).all()

    @staticmethod
    async def create(user_id: int, name: str, expiry_date: datetime) -> Tag:
        """创建标签"""
        return await Tag.create(user_id=user_id, name=name, expiry_date=expiry_date)

    @staticmethod
    async def check_exist(user_id: int, name: str) -> bool:
        """检查标签是否存在"""
        return await Tag.filter(user_id=user_id, name=name).exists()

    @staticmethod
    async def clear_expired(user_id: int):
        """清除过期标签"""
        await Tag.filter(user_id=user_id, expiry_date__lt=datetime.now()).delete()
