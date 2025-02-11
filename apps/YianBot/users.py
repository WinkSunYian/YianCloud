from fastapi import Depends
from utils.ServiceRouter import ServiceRouter
from services.UserService import UserService
from core.security import get_appkey
from core.Container import Container
from common.exceptions.http_exceptions import UserNotFoundException


class UserRouter(ServiceRouter):
    def __init__(self):
        self.set_path("/users/{user_id}")
        self.setup_routes()

    async def get(self, user_id, app_key=Depends(get_appkey)):
        user = await UserService.get_user(user_id)
        if not user:
            raise UserNotFoundException()
        return self.res(data=user)

    async def post(self, user_id, app_key=Depends(get_appkey)):
        user = await UserService.create(account=f"qq_{user_id}", qq=user_id)
        return self.res(status_code=201, data=user)
