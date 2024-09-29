from fastapi import APIRouter
from apps.YianBot.models import User

router = APIRouter()


@router.get(
    "/account/{account}",
    summary="获取用户信息",
    description="获取指定账号的用户信息",
)
async def get(account: str):
    user = await User.get(account=account)
    return user


@router.get(
    "/qq/{qq}",
    summary="获取用户信息",
    description="获取指定QQ号的用户信息",
)
async def get(qq: str):
    user = await User.get(qq=qq)
    if not user:
        return {"message": "用户不存在"}
    return user


@router.get(
    "/all",
    summary="获取所有用户信息",
    description="获取所有用户信息",
)
async def get():
    users = await User.all()
    return users
