from fastapi import Header, HTTPException
from configs.Config import AppKeyConfig
from typing import Optional


async def validate_app_key(app_key: Optional[str] = Header(None)):
    if app_key is None:
        raise HTTPException(status_code=403, detail="缺少AppKey")
    if app_key not in AppKeyConfig.APPKEYS:
        raise HTTPException(status_code=403, detail="无效的AppKey")
    return app_key
