from models.ResponseModel import ResponseModel
from typing import Optional, Union, Dict, List
from fastapi.responses import Response, JSONResponse


def response_data(
    status_code=200,
    message: str = "成功",
    data: Union[Dict, List] = {},
    response: Optional[Response] = None,
) -> ResponseModel:
    if response:
        return response

    return JSONResponse(
        status_code=status_code,
        content=ResponseModel(
            status_code=status_code,
            message=message,
            data=data,
        ).model_dump(),
    )
