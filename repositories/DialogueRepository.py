from db.models import Dialogue
from typing import List, Optional


from db.models import Dialogue, User


class DialogueRepository:
    @staticmethod
    async def get_recent_dialogues(user: User, limit: int):
        """
        获取用户最近的对话记录。
        :param user: 用户实例
        :param limit: 获取的最大条数
        :return: 对话记录列表
        """
        return (
            await Dialogue.filter(user_id=user.id)
            .order_by("-timestamp")
            .limit(limit)
            .all()
        )

    @staticmethod
    async def create_dialogue(user: "User", role: str, content: str):
        """
        创建一条对话记录。
        :param user: 用户实例
        :param role: 角色 ("user" 或 "assistant")
        :param content: 对话内容
        :return: 创建的对话对象
        """
        return await Dialogue.create(user_id=user.id, role=role, content=content)
