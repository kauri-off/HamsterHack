import json

from pydantic import BaseModel


class Config(BaseModel):
    token_list: list[str] | None
    init_data: list[str] | None

class ConfigManager:
    def __init__(self, file_path: str="/app/env/config.json") -> None:
        with open(file_path, 'r') as f:
            self.__config = Config(**json.load(f))

    def get_config(self) -> Config:
        return self.__config
