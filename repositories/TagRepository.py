from db.models import Tag
from datetime import datetime
from typing import List
from db.models import User


class TagRepository:
    @staticmethod
    async def get_by_user(user: User) -> List[Tag]:
        """通过用户对象获取标签"""
        return await Tag.filter(user=user).all()

    @staticmethod
    async def create(user: User, name: str, expiry_date: datetime) -> Tag:
        """为用户对象添加标签"""
        return await Tag.create(user=user, name=name, expiry_date=expiry_date)
