from fastapi import FastAPI
from tortoise import Tortoise
from tortoise.contrib.fastapi import register_tortoise
import uvicorn

from middleware.HostRouterMiddleware import HostRouterMiddleware
from apps.YianBot.routes import router as yianbot_router
from apps.Tests.routes import router as test_router
from configs.Config import DatabaseConfig

# 创建主应用
app = FastAPI()
# 创建子应用
yianbot = FastAPI(
    docs_url="/api/docs",  # 设置 Swagger UI 文档路径
    redoc_url="/api/redoc",  # 设置 ReDoc 文档路径
    openapi_url="/api/openapi.json",  # 设置 OpenAPI schema 路径
)
test = FastAPI(
    docs_url="/api/docs",  # 设置 Swagger UI 文档路径
    redoc_url="/api/redoc",  # 设置 ReDoc 文档路径
    openapi_url="/api/openapi.json",  # 设置 OpenAPI schema 路径
)

# 为子应用添加路由
yianbot.include_router(yianbot_router, prefix="/api", tags=["Router YianBot"])
test.include_router(test_router, prefix="/api", tags=["Router test"])

# 定义主机和应用的映射
host_app_map = {
    "bot.sunyian.cloud": yianbot,
    "test.sunyian.cloud": test,
}

# 添加中间件
app.add_middleware(HostRouterMiddleware, host_app_map=host_app_map)

# 数据库和时区配置
Tortoise._init_timezone(use_tz=False, timezone="Asia/Shanghai")
register_tortoise(
    app=app,
    db_url=DatabaseConfig.db_url,
    modules={"models": ["db.models"]},
    generate_schemas=False,  # 第一次运行时可以设置为 True
    add_exception_handlers=True,
)

# 启动应用
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        port=8000,
        reload=True,
    )
