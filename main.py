from fastapi import FastAPI
import uvicorn
from core.fastapi_init_content import init, shutdown
from core.router import auto_register_routes
from core.setting import Setting
from middleware.HostRouterMiddleware import HostRouterMiddleware


def create_app() -> FastAPI:
    app = FastAPI()

    # 通过配置来获取主机到应用的映射
    host_app_map = get_host_app_map()

    # 设置事件处理器
    setup_event_handlers(app)

    # 添加中间件来根据 Host 路由到不同的应用
    setup_middleware(app, host_app_map)

    # 注册主机相关的路由
    auto_register_routes_for_host_apps(host_app_map)

    return app


def get_host_app_map() -> dict:
    """返回主机到应用的映射，可以从配置文件中读取"""
    return {
        "bot.sunyian.cloud": FastAPI(
            docs_url="/api/docs",
            openapi_url="/api/openapi.json",
            redoc_url="/api/redoc",
        ),
        "test.sunyian.cloud": FastAPI(
            docs_url="/api/docs",
            openapi_url="/api/openapi.json",
            redoc_url="/api/redoc",
        ),
    }


def setup_middleware(app: FastAPI, host_app_map: dict):
    """设置Host路由中间件"""
    app.add_middleware(HostRouterMiddleware, host_app_map=host_app_map)


def setup_event_handlers(app: FastAPI):
    """设置事件处理器"""
    app.add_event_handler("startup", init)
    app.add_event_handler("shutdown", shutdown)


def auto_register_routes_for_host_apps(host_app_map: dict):
    """为每个主机映射的应用自动注册路由"""
    for host, app in host_app_map.items():
        if host == "bot.sunyian.cloud":
            auto_register_routes(app, router_path="/api", directory="apps/YianBot")
        elif host == "test.sunyian.cloud":
            auto_register_routes(app, router_path="/api", directory="apps/Tests")


# 创建应用
app = create_app()

# 启动应用
if __name__ == "__main__":
    uvicorn.run("main:app", port=Setting.PORT, reload=True)
