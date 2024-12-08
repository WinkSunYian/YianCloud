from tortoise import Tortoise
from configs.DATABASE import DATABASE


async def datebase_connect(generate_schemas=True):

    # 使用Asia/Shanghai时区
    Tortoise._init_timezone(use_tz=False, timezone="Asia/Shanghai")
    await Tortoise.init(
        {
            "connections": {"default": DATABASE.DATABASE_URL},
            "apps": {
                "models": {
                    "models": ["db.models"],
                    "default_connection": "default",
                }
            },
        }
    )
    # 生成数据库表结构
    if generate_schemas:
        await Tortoise.generate_schemas()


async def datebase_disconnect():
    await Tortoise.close_connections()
