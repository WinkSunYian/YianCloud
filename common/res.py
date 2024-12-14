from models.ResponseModel import ResponseModel
from typing import Optional, Union, Dict, List
from fastapi.responses import Response, JSONResponse
from common.error_code import ErrorBase


def response_data(
    error: ErrorBase = None,
    status_code=200,
    msg: str = "[MSG]",
    data: Union[Dict, List] = {},
    response: Optional[Response] = None,
) -> ResponseModel:
    if response:
        return response

    return JSONResponse(
        status_code=status_code,
        content=ResponseModel(
            code=error.code if error else 0,
            msg=error.msg + msg if error else msg,
            data=data,
        ).model_dump(),
    )
