import sys
from fastapi import APIRouter, Response
from fastapi import __version__ as fastapi_version

router = APIRouter()


@router.get("/")
def server_status(response: Response, token: str | None = None):
    if token == "token":
        data = {
            "运行状态": "正常",
            "FastApi版本": fastapi_version,
            "Python版本": sys.version_info,
        }
        return data
    else:
        response.status_code = 404
        return {"error": "Not Found"}
