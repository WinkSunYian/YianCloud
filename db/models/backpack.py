from tortoise import fields, models


class Backpack(models.Model):
    id = fields.IntField(pk=True)
    items = fields.ForeignKeyField("models.Item", related_name="backpack")
    user = fields.OneToOneField(
        "models.User", related_name="backpack", on_delete=fields.CASCADE
    )

    class Meta:
        table = "backpack"
