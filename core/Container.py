from repositories.UserRepository import UserRepository
from repositories.UserMetadataRepository import UserMetadataRepository
from repositories.ItemRepository import ItemRepository
from repositories.TagRepository import TagRepository
from services.UserService import UserService
from services.UserMetadataService import UserMetadataService
from services.ItemService import ItemService
from services.TagService import TagService
from apps.YianBot.services.ChatAIService import ChatAIService
from apps.YianBot.services.ChatGPTService import ChatGPTService
from apps.YianBot.services.DeepSeekService import DeepSeekService
from apps.YianBot.services.RobberyService import RobberyService
from apps.YianBot.services.SignInService import SignInService


class Container:
    _instance = None

    def __new__(cls, *args, **kwargs):
        """确保容器是单例的"""
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
            # 初始化服务
            cls._instance._initialize_services()
        return cls._instance

    def _initialize_services(self):
        """初始化所有依赖关系，避免重复创建"""
        # 初始化仓库
        self.user_repository = UserRepository()
        self.user_metadata_repository = UserMetadataRepository()
        self.item_repository = ItemRepository()
        self.tag_repository = TagRepository()

        # 初始化服务
        self.user_service = UserService(self.user_repository)
        self.user_metadata_service = UserMetadataService(self.user_metadata_repository)
        self.item_service = ItemService(self.item_repository, self.user_repository)
        self.tag_service = TagService(self.tag_repository)
        self.chat_gpt_service = ChatGPTService()
        self.deep_seek_service = DeepSeekService()

        # 初始化业务服务
        self.robbery_service = RobberyService(self.user_service, self.item_service)
        self.sign_in_service = SignInService(
            self.user_service, self.tag_service, self.item_service
        )

        # 初始化 ChatAIService 并注入其依赖
        self.chat_ai_service = ChatAIService(
            self.user_metadata_service, self.chat_gpt_service
        )

    # 获取各个服务的实例
    def get_chat_ai_service(self):
        return self.chat_ai_service

    def get_user_service(self):
        return self.user_service

    def get_user_metadata_service(self):
        return self.user_metadata_service

    def get_item_service(self):
        return self.item_service

    def get_tag_service(self):
        return self.tag_service

    def get_chat_gpt_service(self):
        return self.chat_gpt_service

    def get_deep_seek_service(self):
        return self.deep_seek_service

    def get_robbery_service(self):
        return self.robbery_service

    def get_sign_in_service(self):
        return self.sign_in_service
