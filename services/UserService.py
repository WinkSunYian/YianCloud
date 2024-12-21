from repositories.UserRepository import UserRepository


class UserService:
    @staticmethod
    async def get_user(user_id):
        return await UserRepository.get_user(user_id)

    @staticmethod
    async def create(user):
        return await UserRepository.create(user)
