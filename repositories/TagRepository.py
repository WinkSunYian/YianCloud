from db.models import Tag
from datetime import datetime
from typing import List


class TagRepository:
    @staticmethod
    async def get_by_user_id(user_id: int) -> List[Tag]:
        """通过用户 ID 获取标签"""
        return await Tag.filter(user_id=user_id).all()

    @staticmethod
    async def create(user_id: int, name: str, expiry_date: datetime) -> Tag:
        """为用户添加标签"""
        return await Tag.create(user_id=user_id, name=name, expiry_date=expiry_date)
