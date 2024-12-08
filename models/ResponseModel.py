from typing import Optional, Union
from pydantic import BaseModel


class ResponseModel(BaseModel):
    code: int
    msg: Optional[str]
    data: Union[dict, list]
