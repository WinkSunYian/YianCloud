from db.models import User
from typing import Optional


class UserRepository:
    """
    UserRepository 用于处理与用户（User）相关的数据库操作。
    包括根据 identifier 获取用户、根据用户 ID 获取用户、通过账户或 QQ 获取用户，以及创建用户。
    """

    def __init__(self):
        """构造函数用于初始化可能的配置或服务，当前没有额外初始化。"""
        pass

    async def get_user(self, identifier: str) -> Optional[User]:
        """
        根据 identifier (qq 或 account) 获取用户信息。

        :param identifier: 可以是用户的 QQ（数字）或账户名（字母）。
        :return: 如果找到用户则返回 User 对象，否则返回 None。
        """
        if identifier.isdigit():
            user = await self.get_by_qq(identifier)
        else:
            user = await self.get_by_account(identifier)
        return user

    async def get_by_id(self, user_id: int) -> Optional[User]:
        """
        根据用户 ID 获取用户。

        :param user_id: 用户 ID。
        :return: 返回对应的用户对象，如果没有找到则返回 None。
        """
        return await User.filter(id=user_id).first()

    async def get_by_account(self, account: str) -> Optional[User]:
        """
        根据账户名获取用户。

        :param account: 用户账户名。
        :return: 返回对应的用户对象，如果没有找到则返回 None。
        """
        return await User.get_or_none(account=account)

    async def get_by_qq(self, qq: str) -> Optional[User]:
        """
        根据 QQ 获取用户。

        :param qq: 用户的 QQ 号码。
        :return: 返回对应的用户对象，如果没有找到则返回 None。
        """
        return await User.get_or_none(qq=qq)

    async def create(
        self, account: str, qq: str, password: Optional[str] = None
    ) -> User:
        """
        创建新的用户。

        :param account: 用户账户名。
        :param qq: 用户 QQ。
        :param password: 用户密码，默认为 None。
        :return: 创建成功的用户对象。
        """
        return await User.create(account=account, password=password, qq=qq)
