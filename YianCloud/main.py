from fastapi import FastAPI
import uvicorn
from tortoise import Tortoise
from tortoise.contrib.fastapi import register_tortoise

from apps.YianBot.routes import router as yianbot_router
from apps.Tests.routes import router as test_router

app = FastAPI()
app.include_router(test_router, prefix="/test", tags=["Router test"])
app.include_router(yianbot_router, prefix="/yianbot", tags=["Router YianBot"])


Tortoise._init_timezone(
    use_tz=False,
    timezone="Asia/Shanghai",
)

register_tortoise(
    app=app,
    config="tortoise_config.json",
    generate_schemas=False,  # 第一次运行时，需要生成数据库表结构
    add_exception_handlers=True,
)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        port=80,
        reload=True,
    )
