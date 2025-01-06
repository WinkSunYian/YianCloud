from repositories.UserRepository import UserRepository
from common.exceptions.http_exceptions import UserNotFoundException


class UserService:
    @staticmethod
    async def get_user(user_id):
        user = await UserRepository.get_user(user_id)
        if not user:
            raise UserNotFoundException()
        return user

    @staticmethod
    async def create(account: str, qq: str, password=None):
        return await UserRepository.create(account=account, qq=qq, password=password)
