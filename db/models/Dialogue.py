from tortoise import fields, models


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
