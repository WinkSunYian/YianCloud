from fastapi import Depends
from pydantic import BaseModel
from typing import Union
from utils.ServiceRouter import ServiceRouter
from services.UserService import UserService
from services.UserMetadataService import UserMetadataService
from core.security import get_appkey
from common.error_code import ERROR_USER_NOT_FOUND


class UserMetadataRequest(BaseModel):
    key: str
    value: Union[str, int, float]


class UserMetadataRouter(ServiceRouter):
    def __init__(self):
        self.set_path("/users/{user_id}/meta_data")
        self.setup_routes()

    async def get(self, user_id, app_key=Depends(get_appkey)):
        user = await UserService.get_user(user_id)
        return self.res(data=user)

    async def post(
        self,
        user_id,
        user_meta_data_request: UserMetadataRequest,
        app_key=Depends(get_appkey),
    ):
        user = await UserService.get_user(user_id)
        metadata = await UserMetadataService.create(
            user_id=user.id,
            key=user_meta_data_request.key,
            value=user_meta_data_request.value,
        )
        return self.res(status_code=201, data=metadata)
