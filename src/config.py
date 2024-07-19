import json
import logging
import os

from pydantic import BaseModel


class Session(BaseModel):
    token: str | None = None
    init_data: str | None = None
    tap: bool
    upgrade: bool

class Config(BaseModel):
    sessions: list[Session]

class ConfigManager:
    def __init__(self, file_path: str="/app/env/config.json") -> None:
        if not os.path.exists(file_path):
            ConfigManager.error(file_path)

        with open(file_path, 'r') as f:
            self.__config = Config(**json.load(f))

    def get_config(self) -> Config:
        return self.__config

    @staticmethod
    def error(file_path: str):
        with open(file_path, "w") as f:
            f.write(Config(sessions=[Session(token="Bearer <token>", tap=True, upgrade=True)]).json())

        logging.getLogger("HamsterHack").critical("Config not found, check env/config.json")
        exit()
