from pydantic import BaseModel
import json


def load_config(config_file):
    with open(config_file, "r") as f:
        config = json.load(f)
    return config


class Database(BaseModel):
    host: str
    port: int
    user: str
    password: str
    database: str

    @property
    def db_url(self):
        return f"mysql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"


class AppKey(BaseModel):
    APPKEYS: list


DatabaseConfig = Database(**load_config("configs/database.json"))
AppKeyConfig = AppKey(**load_config("configs/AppKey.json"))

TORTOISE_ORM = {
    "connections": {
        "default": DatabaseConfig.db_url,
    },
    "apps": {
        "models": {
            "models": ["apps.YianBot.models"],
            "default": True,
        },
    },
}
