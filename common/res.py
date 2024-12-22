from models.ResponseModel import ResponseModel
from typing import Optional, Union, Dict, List
from fastapi.responses import Response, JSONResponse
from common.error_code import ErrorBase


def response_data(
    status_code=200,
    msg: str = "成功",
    data: Union[Dict, List] = {},
    response: Optional[Response] = None,
) -> ResponseModel:
    if response:
        return response

    return JSONResponse(
        status_code=status_code,
        content=ResponseModel(
            status_code=status_code,
            msg=msg,
            data=data,
        ).model_dump(),
    )
