from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
import uvicorn
from middleware.HostRouterMiddleware import HostRouterMiddleware
from core.fastapi_init_content import init, shutdown
from core.router import auto_register_routes


def create_app() -> FastAPI:
    app = FastAPI()
    # setup_middleware(app)
    setup_event_handlers(app)
    auto_register_routes(app, router_path="/yianbot/api", directory="apps/YianBot")
    auto_register_routes(app, router_path="/tests/api", directory="apps/Tests")
    return app


def setup_middleware(app: FastAPI):
    app.add_middleware(HostRouterMiddleware)


def setup_event_handlers(app: FastAPI):
    app.add_event_handler("startup", init)
    app.add_event_handler("shutdown", shutdown)


app = create_app()


# def custom_openapi():
#     if app.openapi_schema:
#         return app.openapi_schema
#     openapi_schema = get_openapi(
#         # title="Custom API",
#         version="1.0.0",
#         description="这是一个自定义的 API 文档",
#         routes=app.routes,
#     )
#     # 遍历所有路径和方法，移除 422 响应
#     for path, methods in openapi_schema["paths"].items():
#         for method, details in methods.items():
#             if "422" in details.get("responses", {}):
#                 del details["responses"]["422"]
#     app.openapi_schema = openapi_schema
#     return app.openapi_schema


# app.openapi = custom_openapi

if __name__ == "__main__":
    uvicorn.run(
        "test_main:app",
        port=80,
        reload=True,
    )
