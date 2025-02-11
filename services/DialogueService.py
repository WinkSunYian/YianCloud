from repositories.DialogueRepository import DialogueRepository


class DialogueService:
    """
    DialogueService 负责处理对话相关的业务逻辑。
    它提供了与对话记录交互的功能，例如获取用户对话记录和创建对话。
    """

    def __init__(self, dialogue_repository: DialogueRepository):
        """
        构造函数用于注入依赖的 DialogueRepository。

        :param dialogue_repository: DialogueRepository 实例。
        """
        self.dialogue_repository = dialogue_repository

    async def get_by_user_id(self, user_id: int, limit: int):
        """
        获取指定用户 ID 的对话记录。

        :param user_id: 用户 ID。
        :param limit: 获取记录的最大数量。
        :return: 对话记录列表。
        """
        return await self.dialogue_repository.get_by_user_id(user_id, limit)

    async def create(self, user_id: int, role: str, content: str):
        """
        创建一条新的对话记录。

        :param user_id: 用户 ID。
        :param role: 角色，可能是 'user' 或 'assistant'。
        :param content: 对话内容。
        :return: 创建的对话对象。
        """
        return await self.dialogue_repository.create(user_id, role, content)
