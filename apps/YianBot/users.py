from fastapi import Depends
from utils.ServiceRouter import ServiceRouter
from repositories.UserRepository import UserRepository
from core.security import get_appkey


class UserRouter(ServiceRouter):
    def __init__(self):
        self.set_path("/users/{user_id}")
        self.setup_routes()

    async def get(self, user_id, app_key=Depends(get_appkey)):
        user = await UserRepository.get_user(user_id)
        return self.res(data=user)

    async def post(self, user_id, app_key=Depends(get_appkey)):
        user = await UserRepository.create(account=f"qq_{user_id}", qq=user_id)
        return self.res(data=user)
