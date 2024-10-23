from fastapi import APIRouter, Depends
from apps.YianBot.models import User, Tag
from pydantic import BaseModel
from datetime import datetime
from core.security import validate_app_key

router = APIRouter()


class TagCreate(BaseModel):
    name: str
    expiry_date: datetime


@router.get("/qq/{qq}")
async def get(qq: str, app_key: str = Depends(validate_app_key)):
    user = await User.get(qq=qq)
    tags = await user.get_tags()
    return tags


@router.post("/qq/{qq}")
async def post(
    qq: str, tag_create: TagCreate, app_key: str = Depends(validate_app_key)
):
    user = await User.get(qq=qq)
    tag = await user.add_tag(name=tag_create.name, expiry_date=tag_create.expiry_date)
    return tag
