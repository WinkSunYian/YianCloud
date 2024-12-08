from tortoise import fields, models


class Item(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100)
    quantity = fields.IntField()

    class Meta:
        table = "item"
