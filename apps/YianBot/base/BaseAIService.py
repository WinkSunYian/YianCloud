from abc import ABC, abstractmethod


class BaseAIService(ABC):
    @abstractmethod
    async def get_response(
        self, messages: list, temperature: float = 1.3, stream: bool = False
    ) -> str:
        """获取 AI 回复"""
        pass
