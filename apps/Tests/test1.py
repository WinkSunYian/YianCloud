from fastapi import Depends
from utils.ServiceRouter import ServiceRouter
from common.error_code import ERROR_USER_NOT_FOUND
from services.UserService import UserService
from apps.YianBot.services.ChatService import ChatService


class test1(ServiceRouter):
    def __init__(self):
        self.set_path("/test1")
        self.set_desc("get", "这是get方法的描述", "这是get方法的详细描述")
        self.set_desc("post", "这是post方法的描述", "这是post方法的详细描述")
        self.set_desc("put", "这是put方法的描述", "这是put方法的详细描述")
        self.set_desc("delete", "这是delete方法的描述", "这是delete方法的详细描述")
        self.setup_routes()

    async def get(self, qq, message):
        chat = await ChatService.get_gpt_response(qq, message)
        return self.res(data={"chat": chat})

    async def post(self):
        return self.res(error=ERROR_USER_NOT_FOUND, msg="这是一条附加信息")

    async def put(self):
        return self.path
