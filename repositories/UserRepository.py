from db.models import User
from typing import Optional


class UserRepository:
    @staticmethod
    async def get_by_id(user_id: int) -> Optional[User]:
        """通过用户 ID 获取用户"""
        return await User.filter(id=user_id).first()

    @staticmethod
    async def get_by_account(account: str) -> Optional[User]:
        """通过账户名获取用户"""
        return await User.filter(account=account).first()

    @staticmethod
    async def get_by_qq(qq: str) -> Optional[User]:
        """通过 QQ 获取用户"""
        return await User.filter(qq=qq).first()

    @staticmethod
    async def create(account: str, password: str, qq: str) -> User:
        """创建用户"""
        return await User.create(account=account, password=password, qq=qq)
