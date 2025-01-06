from typing import Optional, Union
from pydantic import BaseModel


class ResponseModel(BaseModel):
    status_code: int
    message: Optional[str]
    data: Union[dict, list]
