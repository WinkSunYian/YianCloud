from fastapi import Header, HTTPException
from configs.Config import AppKeyConfig


async def validate_app_key(app_key: str = Header(...)):
    if app_key is None:
        raise HTTPException(status_code=403, detail="App Key is required")
    if app_key not in AppKeyConfig.APPKEYS:
        raise HTTPException(status_code=403, detail="Invalid App Key")
    return app_key
