from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi


def generate_custom_openapi(app: FastAPI):
    """生成自定义的 OpenAPI 方法"""

    def custom_openapi():
        if app.openapi_schema:
            return app.openapi_schema
        openapi_schema = get_openapi(
            title="YianCloud API",
            version="1.0.0",
            description="这是一个自定义的 API 文档",
            routes=app.routes,
        )
        # 遍历所有路径和方法，移除 422 响应
        for path, methods in openapi_schema["paths"].items():
            for method, details in methods.items():
                if "422" in details.get("responses", {}):
                    del details["responses"]["422"]
        app.openapi_schema = openapi_schema
        return app.openapi_schema

    return custom_openapi
