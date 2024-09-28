from fastapi import APIRouter
from apps.YianBot.models import User
from core.Config import Config

router = APIRouter()

@router.get(
    "/",
    summary="这是一个根路由的描述",
    description="这是一个根路由的详细描述",
    deprecated=True,
)
async def default():
    users = await User.create(account="235345", password="1243", qq="111")
    return 1


@router.get(
    "/{user_id}",
    summary="获取用户信息",
    description="获取指定用户的详细信息",
)
async def get(user_id: str):
    user = await User.get(user_id)
    return {"message": user_id}
