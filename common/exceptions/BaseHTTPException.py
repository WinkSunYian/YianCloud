from fastapi import HTTPException


class BaseHTTPException(HTTPException):
    def __init__(
        self, status_code: int, message: str, data: dict = None, detail: str = None
    ):
        super().__init__(status_code=status_code, detail=detail)

        self.status_code = status_code
        self.message = message
        self.data = data or {}

    def to_dict(self):
        """将异常信息转换为字典格式"""
        return {
            "status_code": self.status_code,
            "message": self.message if self.message else self.detail,
            "detail": self.detail,
            "data": self.data,
        }
