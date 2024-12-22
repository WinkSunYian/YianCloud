from repositories.UserRepository import UserRepository


class UserService:
    @staticmethod
    async def get_user(user_id):
        return await UserRepository.get_user(user_id)

    @staticmethod
    async def create(account: str, qq: str, password=None):
        return await UserRepository.create(account=account, qq=qq, password=password)
