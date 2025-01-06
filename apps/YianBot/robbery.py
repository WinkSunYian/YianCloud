from fastapi import Depends
from utils.ServiceRouter import ServiceRouter
from core.security import get_appkey
from services.UserService import UserService
from pydantic import BaseModel
from apps.YianBot.services.RobberyService import RobberyService

# from common.exceptions.http_exceptions import


class TagRequest(BaseModel):
    target_id: str


class RobberyRouter(ServiceRouter):
    def __init__(self):
        self.set_path("/users/{user_id}/robbery")
        self.set_desc("post", "打劫用户", "打劫用户")
        self.setup_routes()

    async def post(
        self, user_id: str, tag_request: TagRequest, app_key: str = Depends(get_appkey)
    ):
        robbery = await RobberyService.calculate_robbery(
            user_id, tag_request.target_id, "软糖"
        )
        return self.res(message=robbery["message"])
