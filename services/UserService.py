from repositories.UserRepository import UserRepository
from repositories.BackpackRepository import BackpackRepository
from repositories.DialogueRepository import DialogueRepository
from repositories.TagRepository import TagRepository
from typing import Optional, List
from datetime import datetime
from db.models import User


class UserService:
    @staticmethod
    async def get_user(identifier: str) -> Optional[User]:
        """
        根据 identifier (qq 或 account) 获取用户信息。
        - 如果 identifier 是数字，认为是 qq。
        - 如果 identifier 是字母，认为是 account。
        """
        if identifier.isdigit():
            user = await UserRepository.get_by_qq(identifier)
        else:
            user = await UserRepository.get_by_account(identifier)
        return user

    @staticmethod
    async def create_user(account: str, password: str, qq: str) -> dict:
        """创建用户"""
        user = await UserRepository.create(account, password, qq)
        return {"id": user.id, "account": user.account, "qq": user.qq}

    @staticmethod
    async def get_user_backpack(user: User) -> Optional[dict]:
        """获取用户背包信息"""
        backpack = await BackpackRepository.get_by_user(user)
        if backpack:
            return {"id": backpack.id, "items": backpack.items}
        return None

    @staticmethod
    async def get_user_dialogues(user: User, limit: Optional[int] = None) -> List[dict]:
        """获取用户的对话记录"""
        dialogues = await DialogueRepository.get_recent_dialogues(user, limit)
        return [
            {"id": d.id, "role": d.role, "content": d.content, "timestamp": d.timestamp}
            for d in dialogues
        ]

    @staticmethod
    async def add_user_dialogue(user: User, role: str, content: str) -> dict:
        """添加用户对话记录"""
        dialogue = await DialogueRepository.create_dialogue(user, role, content)
        return {
            "id": dialogue.id,
            "role": dialogue.role,
            "content": dialogue.content,
            "timestamp": dialogue.timestamp,
        }

    @staticmethod
    async def get_user_tags(user: User) -> List[dict]:
        """获取用户标签"""
        tags = await TagRepository.get_by_user(user)
        return [
            {"id": t.id, "name": t.name, "expiry_date": t.expiry_date} for t in tags
        ]

    @staticmethod
    async def add_user_tag(user: User, name: str, expiry_date: datetime) -> dict:
        """为用户添加标签"""
        tag = await TagRepository.create(user, name, expiry_date)
        return {"id": tag.id, "name": tag.name, "expiry_date": tag.expiry_date}
