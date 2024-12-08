class Core:
    pass


class Setting(Core):
    HOST: str = "0.0.0.0"
    PORT: str = 8000
    WRITE_LOG: bool = True
