import os


class Config:

    @staticmethod
    def init():
        # 初始化配置
        print("初始化配置")

    @staticmethod
    def get(key, default=None):
        # 获取配置
        return key

Config.init()

a = Config.get("routes.apps", {})
print(a)
