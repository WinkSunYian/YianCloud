from fastapi import Depends
from utils.ServiceRouter import ServiceRouter
from services.UserService import UserService


class UserRouter(ServiceRouter):
    def __init__(self):
        self.set_path("/user/{user_id}")
        self.setup_routes()

    async def get(self, user_id, app_key=Depends()):
        user = await UserService.get_user(user_id)
        return self.res(data=user)
