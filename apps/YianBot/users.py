from fastapi import Depends
from utils.ServiceRouter import ServiceRouter
from core.security import get_appkey
from core.Container import Container
from common.exceptions.http_exceptions import UserNotFoundException


class UserRouter(ServiceRouter):
    def __init__(self):
        self.container = Container()
        self.user_service = self.container.get_user_service()
        self.set_path("/users/{user_id}")
        self.setup_routes()

    async def get(self, user_id, app_key=Depends(get_appkey)):
        user = await self.user_service.get_user(user_id)
        if not user:
            raise UserNotFoundException()
        return self.res(data=user)

    async def post(self, user_id, app_key=Depends(get_appkey)):
        user = await self.user_service.create(account=f"qq_{user_id}", qq=user_id)
        return self.res(status_code=201, data=user)
