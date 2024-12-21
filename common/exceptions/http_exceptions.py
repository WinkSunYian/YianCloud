from .BaseHTTPException import BaseHTTPException


class NotFoundException(BaseHTTPException):
    def __init__(
        self,
        status_code: int = 404,
        msg: str = "",
        data: dict = None,
        detail: str = "资源不存在",
    ):
        super().__init__(status_code=status_code, msg=msg, data=data, detail=detail)


class UserNotFoundException(BaseHTTPException):
    def __init__(
        self,
        status_code: int = 404,
        msg: str = "",
        data: dict = None,
        detail: str = "用户不存在",
    ):
        super().__init__(status_code=status_code, msg=msg, data=data, detail=detail)


class TargetNotFoundException(BaseHTTPException):
    def __init__(
        self,
        status_code: int = 404,
        msg: str = "",
        data: dict = None,
        detail: str = "目标不存在",
    ):
        super().__init__(status_code=status_code, msg=msg, data=data, detail=detail)


class UnauthorizedException(BaseHTTPException):
    def __init__(self, status_code: int = 404, msg: str = "", data: dict = None):
        super().__init__(status_code=status_code, msg=msg, data=data)


class BadRequestException(BaseHTTPException):
    def __init__(self, status_code: int = 404, msg: str = "", data: dict = None):
        super().__init__(status_code=status_code, msg=msg, data=data)
