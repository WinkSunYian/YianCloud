from fastapi import APIRouter, Depends, HTTPException
from apps.YianBot.models import User
from core.security import validate_app_key

router = APIRouter()


@router.get(
    "/account/{account}",
    summary="获取用户信息",
    description="获取指定账号的用户信息",
)
async def get(account: str, app_key: str = Depends(validate_app_key)):
    user = await User.get_or_none(account=account)
    if not user:
        raise HTTPException(status_code=404, detail="用户不存在")
    return user


@router.get(
    "/qq/{qq}",
    summary="获取用户信息",
    description="获取指定QQ号的用户信息",
)
async def get_user_info(qq: str, app_key: str = Depends(validate_app_key)):
    user = await User.get_or_none(qq=qq)
    if not user:
        raise HTTPException(status_code=404, detail="用户不存在")
    return user


@router.get(
    "/all",
    summary="获取所有用户信息",
    description="获取所有用户信息",
)
async def get():
    users = await User.all()
    return users


@router.post("/qq/{qq}", summary="注册用户")
async def post(qq: str, app_key: str = Depends(validate_app_key)):
    user = await User.create(account=f"qq{qq}", qq=qq)
    return user
