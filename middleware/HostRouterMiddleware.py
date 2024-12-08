from starlette.types import ASGIApp, Receive, Scope, Send


class HostRouterMiddleware:
    def __init__(self, app: ASGIApp, host_app_map: dict):
        self.app = app
        self.host_app_map = host_app_map

    async def __call__(self, scope: Scope, receive: Receive, send: Send):
        if scope["type"] in ("http", "websocket"):
            headers = dict(scope["headers"])
            host = headers.get(b"host", b"").decode().split(":")[0]
            target_app = self.host_app_map.get(host)
            if target_app:
                await target_app(scope, receive, send)
                return
        # 如果未匹配，默认使用原始 app 处理
        await self.app(scope, receive, send)
