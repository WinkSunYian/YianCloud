from fastapi import Depends
from utils.ServiceRouter import ServiceRouter
from common.error_code import ERROR_USER_NOT_FOUND
from apps.YianBot.services.ChatService import ChatService
from apps.YianBot.services.SignInService import SignInService
from core.security import get_appkey


class SignInRouter(ServiceRouter):
    def __init__(self):
        self.set_path("/users/{user_id}/sign-in")
        self.set_desc("put", "签到", "获取签到信息")
        self.setup_routes()

    async def put(self, user_id: str, app_key: str = Depends(get_appkey)):
        msg = await SignInService.sign_in(user_id)
        return self.res(msg=msg)
