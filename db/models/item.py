from tortoise import fields, models


class Item(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100)
    quantity = fields.IntField()
    user = fields.ForeignKeyField(
        "models.User", related_name="items", on_delete=fields.CASCADE
    )

    class Meta:
        table = "item"
