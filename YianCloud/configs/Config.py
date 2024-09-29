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


DatabaseConfig = Database(**load_config("configs/database.json"))
