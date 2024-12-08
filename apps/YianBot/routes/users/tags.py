# from fastapi import APIRouter, HTTPException, Depends
# from fastapi.encoders import jsonable_encoder
# from pydantic import BaseModel
# from datetime import datetime

# # from apps.YianBot.controllers.security import validate_app_key
# from db.models import User
# from apps.YianBot.schemas.ResponseModel import ResponseModel

# router = APIRouter()


# class TagCreate(BaseModel):
#     name: str
#     expiry_date: datetime


# @router.get("/tags", summary="获取用户所有的标签", description="获取用户所有的标签")
# async def get(user_id: str, app_key: str = Depends(validate_app_key)):
#     user = await User.get_or_none(qq=user_id)
#     if not user:
#         return ResponseModel(code=2, msg="用户不存在")
#     tags = await user.get_tags()
#     return ResponseModel(
#         code=0, msg="成功获取标签", data={"tags": jsonable_encoder(tags)}
#     )


# # @router.get("/tags/{tag_name}", summary="获取用户标签", description="获取用户标签")
# # async def get(user_id: str, tag_name: str, app_key: str = Depends(validate_app_key)):
# #     user = await User.get_or_none(qq=user_id)
# #     if not user:
# #         raise HTTPException(status_code=404, detail="用户不存在")
# #     tag = await user.get_tag(tag_name)
# #     if not tag:
# #         raise HTTPException(status_code=404, detail="标签不存在")
# #     return {"user_id": user.id, "tag": tag}


# @router.post(
#     "/tags", summary="创建用户标签", description="创建用户标签", status_code=201
# )
# async def post(
#     user_id: str, tag_create: TagCreate, app_key: str = Depends(validate_app_key)
# ):
#     user = await User.get_or_none(qq=user_id)
#     if not user:
#         raise HTTPException(status_code=404, detail="用户不存在")
#     tag = await user.add_tag(name=tag_create.name, expiry_date=tag_create.expiry_date)
#     return {"message": "成功创建标签", "tag": tag}
