from fastapi import Depends
from utils.ServiceRouter import ServiceRouter
from core.Container import Container
from core.security import get_appkey
from common.exceptions.http_exceptions import UserNotFoundException
from datetime import datetime
from pydantic import BaseModel


class TagRequest(BaseModel):
    name: str
    expiry_date: datetime


class TagRouter(ServiceRouter):
    def __init__(self):
        self.container = Container()
        self.user_service = self.container.get_user_service()
        self.tag_service = self.container.get_tag_service()
        self.set_path("/users/{user_id}/tags")
        self.set_desc("get", "获取用户所有标签", "获取用户所有标签")
        self.set_desc("post", "创建标签", "创建标签")
        self.setup_routes()

    async def get(self, user_id: str, app_key: str = Depends(get_appkey)):
        user = await self.user_service.get_user(user_id)
        tags = await self.tag_service.get_by_user_id(user_id=user.id)
        return self.res(data=[tag.name for tag in tags])

    async def post(
        self,
        tags_request: TagRequest,
        user_id: str,
        app_key: str = Depends(get_appkey),
    ):
        user = await self.user_service.get_user(user_id)
        if not user:
            raise UserNotFoundException()
        tag = await self.tag_service.create(
            user_id=user_id,
            name=tags_request.name,
            expiry_date=tags_request.expiry_date,
        )
        return self.res(status_code=201, data=tag)
