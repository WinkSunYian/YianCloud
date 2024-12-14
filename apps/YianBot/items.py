from fastapi import Depends
from utils.ServiceRouter import ServiceRouter
from services.ItemService import ItemService
from core.security import get_appkey


class ItemRouter(ServiceRouter):
    def __init__(self):
        self.set_path("/users/{user_id}/items")
        self.set_desc("get", "获取用户的物品列表", "获取用户的物品列表")
        self.setup_routes()

    async def get(self, user_id: str, appkey: str = Depends(get_appkey)):
        item_list = await ItemService.get_by_user(user_id)
        return self.res(data=item_list)
