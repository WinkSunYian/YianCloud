from fastapi import APIRouter, HTTPException, Depends
from apps.YianBot.models import User
from pydantic import BaseModel
from datetime import datetime
from core.security import validate_app_key

router = APIRouter()


class TagCreate(BaseModel):
    name: str
    expiry_date: datetime


@router.get("/by-qq/{qq}")
async def get(qq: str, app_key: str = Depends(validate_app_key)):
    user = await User.get_or_none(qq=qq)
    if not user:
        raise HTTPException(status_code=404, detail="用户不存在")
    tags = await user.get_tags()
    return {"user_id": user.id, "tags": tags}


@router.post("/by-qq/{qq}", status_code=201)
async def post(
    qq: str, tag_create: TagCreate, app_key: str = Depends(validate_app_key)
):
    user = await User.get_or_none(qq=qq)
    if not user:
        raise HTTPException(status_code=404, detail="用户不存在")
    tag = await user.add_tag(name=tag_create.name, expiry_date=tag_create.expiry_date)
    return {"message": "成功创建标签", "tag": tag}
