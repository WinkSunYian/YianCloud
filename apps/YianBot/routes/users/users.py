# from fastapi import APIRouter, Depends, HTTPException
# from fastapi.encoders import jsonable_encoder
# from db.models import User
# from apps.YianBot.controllers.security import validate_app_key
# from common.resp import respSuccessJson, respErrorJson
# from common.error_code import ERROR_USER_NOT_FOUND

# router = APIRouter()


# @router.get(
#     "",
#     summary="获取用户信息",
#     description="获取指定QQ号的用户信息",
# )
# async def get_user_info(user_id: str, app_key: str = Depends(validate_app_key)):
#     user = await User.get_or_none(qq=user_id)
#     if not user:
#         return respErrorJson(ERROR_USER_NOT_FOUND)
#     return respSuccessJson(data=jsonable_encoder(user), msg="获取成功")


# @router.post("", summary="注册用户", description="注册一个新的用户")
# async def post(user_id: str, app_key: str = Depends(validate_app_key)):
#     user = await User.create(account=f"qq{user_id}", qq=user_id)
#     return respSuccessJson(data=jsonable_encoder(user), msg="注册成功")
