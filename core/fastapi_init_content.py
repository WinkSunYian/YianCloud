from db.session import datebase_connect, datebase_disconnect


async def init():
    print("启动FastAPI")
    print("建立数据库连接")
    await datebase_connect(generate_schemas=False)


async def shutdown():
    print("关闭FastAPI")
    print("断开数据库连接")
    await datebase_disconnect()
