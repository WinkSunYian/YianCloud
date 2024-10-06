from fastapi import FastAPI
import uvicorn
from tortoise import Tortoise
from tortoise.contrib.fastapi import register_tortoise

from apps.YianBot.routes import router as yianbot_router
from apps.Tests.routes import router as test_router


from configs.Config import DatabaseConfig

app = FastAPI()
app.include_router(test_router, prefix="/test", tags=["Router test"])
app.include_router(yianbot_router, prefix="/yianbot", tags=["Router YianBot"])


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
        "test_main:app",
        port=80,
        reload=True,
    )
