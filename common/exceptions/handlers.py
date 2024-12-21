from fastapi import Request
from fastapi.responses import JSONResponse
from .BaseHTTPException import BaseHTTPException


async def global_exception_handler(request: Request, exc: BaseHTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content=exc.to_dict(),
    )
