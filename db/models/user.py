from tortoise import fields, models
from db.models import Dialogue, Backpack, Tag
from datetime import datetime


class User(models.Model):
    id = fields.IntField(pk=True)
    account = fields.CharField(max_length=32, unique=True)
    password = fields.CharField(max_length=32, null=True)
    qq = fields.CharField(max_length=10, unique=True)

    class Meta:
        table = "user"
