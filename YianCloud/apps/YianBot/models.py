from tortoise import fields, models
from datetime import datetime


class User(models.Model):
    id = fields.IntField(pk=True)
    account = fields.CharField(max_length=32, unique=True)
    password = fields.CharField(max_length=32, null=True)
    qq = fields.CharField(max_length=10, unique=True)

    class Meta:
        table = "user"

    async def get_backpack(self):
        """获取与该用户相关的背包"""
        return await Backpack.get(user=self)

    async def get_dialogues(self, num=None):
        """获取与该用户相关的对话记录"""
        if num is not None:
            return await Dialogue.filter(user=self).limit(num).all()
        return await Dialogue.filter(user=self).all()

    async def get_tags(self):
        """获取与该用户相关的标签"""
        return await Tag.filter(user=self).all()

    async def add_tag(self, name: str, expiry_date: datetime):
        """添加标签"""
        tag = await Tag.create(user=self, name=name, expiry_date=expiry_date)
        return tag

    async def add_dialogue(self, role: str, content: str):
        """添加对话记录"""
        dialogue = await Dialogue.create(user=self, role=role, content=content)
        return dialogue


class Tag(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=32)
    expiry_date = fields.DatetimeField()
    user = fields.ForeignKeyField(
        "models.User", related_name="tags", on_delete=fields.CASCADE
    )

    class Meta:
        table = "tag"


class Backpack(models.Model):
    id = fields.IntField(pk=True)
    items = fields.ForeignKeyField("models.Item", related_name="backpack")
    user = fields.OneToOneField(
        "models.User", related_name="backpack", on_delete=fields.CASCADE
    )

    class Meta:
        table = "backpack"


class Item(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100)
    quantity = fields.IntField()

    class Meta:
        table = "item"


class Dialogue(models.Model):
    id = fields.IntField(pk=True)
    role = fields.CharField(max_length=20)
    content = fields.TextField()
    timestamp = fields.DatetimeField(auto_now_add=True)
    user = fields.ForeignKeyField(
        "models.User", related_name="dialogues", on_delete=fields.CASCADE
    )

    class Meta:
        table = "dialogue"
