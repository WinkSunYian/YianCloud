from fastapi import APIRouter, WebSocket
from starlette.websockets import WebSocketDisconnect
from apps.YianBot.models import User

router = APIRouter()


@router.websocket()
async def websocket_endpoint(websocket: WebSocket):
    print("WebSocket连接")
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            response = f"{data}"
            await websocket.send_text(response)
    except WebSocketDisconnect:
        print("WebSocket连接已断开")
