from fastapi import Depends
from utils.ServiceRouter import ServiceRouter
from apps.YianBot.services.SignInService import SignInService
from core.security import get_appkey
from core.Container import Container  # 引入容器


class SignInRouter(ServiceRouter):
    def __init__(self):
        self.set_path("/users/{user_id}/sign-in")
        self.set_desc("put", "签到", "获取签到信息")
        self.setup_routes()

    # 依赖注入 SignInService
    async def put(
        self,
        user_id: str,
        sign_in_service: SignInService = Depends(
            Container().get_sign_in_service
        ),  # 使用 Depends 注入
        app_key: str = Depends(get_appkey),
    ):
        message = await sign_in_service.sign_in(user_id)
        return self.res(message=message)
