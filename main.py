from fastapi import FastAPI
import uvicorn
from core.fastapi_init_content import startup, shutdown
from core.router import auto_register_routes
from core.setting import Setting
from middleware.HostRouterMiddleware import HostRouterMiddleware
from utils.openapi import generate_custom_openapi
from common.exceptions.handlers import global_exception_handler, BaseHTTPException


def create_app() -> FastAPI:
    app = FastAPI()
    app_bot = FastAPI(
        docs_url="/api/docs",
        openapi_url="/api/openapi.json",
        redoc_url="/api/redoc",
    )
    app_test = FastAPI(
        docs_url="/api/docs",
        openapi_url="/api/openapi.json",
        redoc_url="/api/redoc",
    )
    host_app_map = {
        "bot.sunyian.cloud": app_bot,
        "test.sunyian.cloud": app_test,
    }

    setup_event_handlers(app)
    setyp_host_router_middleware(app, host_app_map)
    auto_register_routes_for_host_apps(app, host_app_map)

    setup_exception_handlers(app_bot)
    setup_exception_handlers(app_test)

    app_bot.openapi = generate_custom_openapi(app=app_bot)
    app_test.openapi = generate_custom_openapi(app=app_test)

    return app


def setyp_host_router_middleware(app: FastAPI, host_app_map: dict):
    """设置Host路由中间件"""
    app.add_middleware(HostRouterMiddleware, host_app_map=host_app_map)


def setup_event_handlers(app: FastAPI):
    """设置事件处理器"""
    app.add_event_handler("startup", startup)
    app.add_event_handler("shutdown", shutdown)


def auto_register_routes_for_host_apps(app: FastAPI, host_app_map: dict):
    """为每个主机映射的应用自动注册路由"""
    for host, sub_app in host_app_map.items():
        if host == "bot.sunyian.cloud":
            auto_register_routes(sub_app, router_path="/api", directory="apps/YianBot")
        elif host == "test.sunyian.cloud":
            auto_register_routes(sub_app, router_path="/api", directory="apps/Tests")


def setup_exception_handlers(app: FastAPI):
    app.add_exception_handler(BaseHTTPException, global_exception_handler)


# 创建应用
app = create_app()

# 启动应用
if __name__ == "__main__":
    uvicorn.run("main:app", port=Setting.PORT, reload=True)
