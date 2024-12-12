from fastapi import Depends
from utils.ServiceRouter import ServiceRouter
from services.UserService import UserService
from core.security import get_appkey
from common.error_code import ERROR_USER_NOT_FOUND

class TagRouter(ServiceRouter):
    def __init__(self):
        self.set_path("/users/{user_id}/tags")
        self.set_desc("get", "获取用户所有标签", "获取用户所有标签")
        self.setup_routes()

    async def get(self, user_id: str, app_key: str = Depends(get_appkey)):
        user_service = await UserService.get_user(user_id)
        if not user_service:
            return self.res(error=ERROR_USER_NOT_FOUND)
        tags = await UserService.get_tags(user_service)
        return self.res(data=tags)
