from fastapi import FastAPI
import uvicorn
from middleware.HostRouterMiddleware import HostRouterMiddleware
from core.fastapi_init_content import init, shutdown
from core.router import auto_register_routes
from utils.openapi import generate_custom_openapi
from common.exceptions.handlers import global_exception_handler, BaseHTTPException


def create_app() -> FastAPI:
    app = FastAPI()
    # setup_middleware(app)
    setup_event_handlers(app)
    setup_exception_handlers(app)
    auto_register_routes(app, router_path="/yianbot/api", directory="apps/YianBot")
    auto_register_routes(app, router_path="/tests/api", directory="apps/Tests")
    app.openapi = generate_custom_openapi(app=app)

    return app


def setup_middleware(app: FastAPI):
    app.add_middleware(HostRouterMiddleware)


def setup_event_handlers(app: FastAPI):
    app.add_event_handler("startup", init)
    app.add_event_handler("shutdown", shutdown)


def setup_exception_handlers(app: FastAPI):
    app.add_exception_handler(BaseHTTPException, global_exception_handler)


app = create_app()


if __name__ == "__main__":
    uvicorn.run(
        "test_main:app",
        port=80,
        reload=True,
    )
