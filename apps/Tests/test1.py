from fastapi import Depends
from utils.ServiceRouter import ServiceRouter
from common.error_code import ERROR_USER_NOT_FOUND
from apps.YianBot.services.ChatService import ChatService
from repositories.DialogueRepository import DialogueRepository
from db.models import Dialogue, Tag


class test1(ServiceRouter):
    def __init__(self):
        self.set_path("/test1")
        self.set_desc("get", "这是get方法的描述", "这是get方法的详细描述")
        self.setup_routes()

    async def get(self, qq):
        data = await Tag.filter(user_qq=qq)
        print(data)
        return self.res(data={"data": data})

    async def post(self):
        return self.res(error=ERROR_USER_NOT_FOUND, msg="这是一条附加信息")

    async def put(self):
        return self.path
