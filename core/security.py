from fastapi import HTTPException, Request, Header
from typing import Optional
from configs.APP_KEY import APP_KEY


def get_appkey(app_key: str = Header(..., alias="app-key")) -> str:
    """
    从请求头中获取 app-key 并返回
    :param app_key: 请求头中的 app-key
    """
    app_key = verify_appkey(app_key)
    return app_key


def verify_appkey(appkey: str) -> str:
    """
    验证 appkey 是否有效。
    """
    if appkey not in APP_KEY.APP_KEYS:
        raise HTTPException(status_code=403, detail="Invalid appkey")

    return APP_KEY.APP_KEYS[appkey]
