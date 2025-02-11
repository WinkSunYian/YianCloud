from fastapi import Depends
from pydantic import BaseModel
from utils.ServiceRouter import ServiceRouter
from core.Container import Container
from core.security import get_appkey


class TagRequest(BaseModel):
    target_id: str


class RobberyRouter(ServiceRouter):
    def __init__(self):
        self.container = Container()
        self.robbery_service = (
            self.container.get_robbery_service()
        )  # 从容器中获取 RobberyService
        self.set_path("/users/{user_id}/robbery")
        self.set_desc("post", "打劫用户", "打劫用户")
        self.setup_routes()

    async def post(
        self, user_id: str, tag_request: TagRequest, app_key: str = Depends(get_appkey)
    ):
        # 使用容器注入的 robbery_service 执行打劫逻辑
        robbery = await self.robbery_service.calculate_robbery(
            user_id, tag_request.target_id, "软糖"
        )
        return self.res(message=robbery["message"])
