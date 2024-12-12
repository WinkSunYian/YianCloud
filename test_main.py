from fastapi import FastAPI
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

if __name__ == "__main__":
    uvicorn.run(
        "test_main:app",
        port=80,
        reload=True,
    )
