from db.models import User
from typing import Optional


class UserRepository:

    @staticmethod
    async def get_user(identifier: str):
        """
        根据 identifier (qq 或 account) 获取用户信息。
        - 如果 identifier 是数字，认为是 qq。
        - 如果 identifier 是字母，认为是 account。
        """
        if identifier.isdigit():
            user = await UserRepository.get_by_qq(identifier)
        else:
            user = await UserRepository.get_by_account(identifier)
        return user

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
        return await User.get_or_none(qq=qq)

    @staticmethod
    async def create(account: str, qq: str, password: Optional[str] = None) -> User:
        """创建用户"""
        return await User.create(account=account, password=password, qq=qq)
