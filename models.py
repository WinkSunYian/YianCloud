from tortoise import fields, models


class User(models.Model):
    id = fields.IntField(pk=True)
    account = fields.CharField(max_length=32, unique=True)
    password = fields.CharField(max_length=32, null=True)
    qq = fields.CharField(max_length=10, null=True)
    backpack = fields.OneToOneField(
        "models.Backpack", related_name="user", null=True, on_delete=fields.SET_NULL
    )
    dialogues = fields.ForeignKeyField(
        "models.Dialogue", related_name="uesr", null=True
    )

    class Meta:
        table = "user"


class Backpack(models.Model):
    id = fields.IntField(pk=True)
    items = fields.ForeignKeyField("models.Item", related_name="backpack")

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

    class Meta:
        table = "dialogue"
