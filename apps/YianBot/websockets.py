from fastapi import APIRouter, WebSocket
from starlette.websockets import WebSocketDisconnect

router = APIRouter()


@router.websocket("/bot")
async def websocket_endpoint(websocket: WebSocket):
    print("WebSocket连接")
    await websocket.accept()
    async for data in websocket.iter_text():
        response = f"{data}"
        await websocket.send_text(response)


@router.get("/test")
async def test():
    return {"message": "这是websocket测试"}
