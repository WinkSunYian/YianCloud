from fastapi import HTTPException, Request
from typing import Optional
from configs.APP_KEY import APP_KEY


def get_appkey(request: Request) -> Optional[str]:
    appkey = request.headers.get("app-key")

    # 做一个简易的验证
    appkey = verify_appkey(appkey)
    return appkey


def verify_appkey(appkey: str) -> str:
    """
    验证 appkey 是否有效。
    """
    if appkey not in APP_KEY.APP_KEYS:
        raise HTTPException(status_code=403, detail="Invalid appkey")

    return APP_KEY.APP_KEYS[appkey]
