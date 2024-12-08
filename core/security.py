from fastapi import HTTPException, Request
from typing import Optional
from configs.APP_KEY import APP_KEY
from common.res import response_data


def get_appkey(request: Request) -> Optional[str]:
    appkey = request.headers.get("app-key")
    return appkey


def verify_appkey(appkey: str, appid: str) -> str:
    """
    验证 appkey 是否有效。
    """
    if appkey not in APP_KEY.APP_KEYS:
        raise HTTPException(status_code=403, detail="Invalid appkey")

    return APP_KEY.APP_KEYS[appkey]
