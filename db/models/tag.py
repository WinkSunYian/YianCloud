from tortoise import fields, models


class Tag(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=32)
    expiry_date = fields.DatetimeField()
    user = fields.ForeignKeyField(
        "models.User", related_name="tags", on_delete=fields.CASCADE
    )

    class Meta:
        table = "tag"
