from fastapi import Depends
from utils.ServiceRouter import ServiceRouter
from core.Container import Container  # 引入容器
from core.security import get_appkey


class ItemRouter(ServiceRouter):
    def __init__(self):
        self.container = Container()  # 获取容器实例
        self.item_service = (
            self.container.get_item_service()
        )  # 从容器中获取 ItemService
        self.set_path("/users/{user_id}/items")
        self.set_desc("get", "获取用户的物品列表", "获取用户的物品列表")
        self.setup_routes()

    async def get(self, user_id: str, app_key: str = Depends(get_appkey)):
        # 使用容器注入的 item_service 获取用户物品列表
        item_list = await self.item_service.get_by_user(user_id)
        return self.res(data=item_list)
