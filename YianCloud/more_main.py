from fastapi import FastAPI

import uvicorn
from tortoise import Tortoise
from tortoise.contrib.fastapi import register_tortoise
from core.HostRouterMiddleware import HostRouterMiddleware

from apps.YianBot.routes import router as yianbot_router
from apps.Tests.routes import router as test_router


from configs.Config import DatabaseConfig

yianbot = FastAPI()
test = FastAPI()
app = FastAPI()

yianbot.include_router(test_router, prefix="/api", tags=["Router test"])
test.include_router(yianbot_router, prefix="/api", tags=["Router YianBot"])

host_app_map = {
    "bot.sunyian.cloud": yianbot,
    "test.sunyian.cloud": test,
}


app.add_middleware(HostRouterMiddleware, host_app_map=host_app_map)

Tortoise._init_timezone(use_tz=False, timezone="Asia/Shanghai")
register_tortoise(
    app=app,
    db_url=DatabaseConfig.db_url,
    modules={"models": ["apps.YianBot.models"]},
    generate_schemas=False,  # 自动生成数据库表结构，第一次运行时设置为True
    add_exception_handlers=True,
)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        port=8000,
        reload=True,
    )
