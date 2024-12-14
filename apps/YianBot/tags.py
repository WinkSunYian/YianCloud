from fastapi import Depends
from utils.ServiceRouter import ServiceRouter
from repositories.TagRepository import TagRepository
from core.security import get_appkey
from common.error_code import ERROR_USER_NOT_FOUND
from pydantic import BaseModel
from datetime import datetime


class TagRequest(BaseModel):
    name: str
    expiry_date: datetime


class TagRouter(ServiceRouter):
    def __init__(self):
        self.set_path("/users/{user_id}/tags")
        self.set_desc("get", "获取用户所有标签", "获取用户所有标签")
        self.set_desc("post", "创建标签", "创建标签")
        self.setup_routes()

    async def get(self, user_id: str, app_key: str = Depends(get_appkey)):
        tags = await TagRepository.get_by_user_id(user_id)
        return self.res(data=tags)

    async def post(
        self,
        tags_request: TagRequest,
        user_id: str,
        app_key: str = Depends(get_appkey),
    ):
        tag = await TagRepository.create(
            user_id=user_id,
            name=tags_request.name,
            expiry_date=tags_request.expiry_date,
        )
        return self.res(data=tag)
