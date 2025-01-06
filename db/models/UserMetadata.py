from tortoise import fields, models
from db.models import Dialogue, Tag
from datetime import datetime


class UserMetadata(models.Model):
    id = fields.IntField(pk=True)
    key = fields.CharField(max_length=64)
    value = fields.JSONField()
    user = fields.ForeignKeyField(
        "models.User", related_name="metadata", on_delete=fields.CASCADE
    )

    class Meta:
        table = "user_metadata"
