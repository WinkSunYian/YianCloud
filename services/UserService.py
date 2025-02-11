from repositories.UserRepository import UserRepository
from common.exceptions.http_exceptions import UserNotFoundException


class UserService:
    """
    UserService 负责处理与用户相关的业务逻辑。
    它提供了获取用户信息和创建用户的功能。
    """

    def __init__(self, user_repository: UserRepository):
        """
        构造函数用于注入依赖的 UserRepository。

        :param user_repository: UserRepository 实例。
        """
        self.user_repository = user_repository

    async def get_user(self, user_id: str):
        """
        根据用户 ID 获取用户信息。

        :param user_id: 用户 ID。
        :return: 用户对象，如果未找到用户则抛出 UserNotFoundException。
        """
        user = await self.user_repository.get_user(user_id)
        if not user:
            raise UserNotFoundException()
        return user

    async def create(self, account: str, qq: str, password=None):
        """
        创建一个新的用户。

        :param account: 账户名。
        :param qq: 用户 QQ。
        :param password: 用户密码。
        :return: 创建的用户对象。
        """
        return await self.user_repository.create(
            account=account, qq=qq, password=password
        )
