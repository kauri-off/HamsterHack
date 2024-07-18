from dotenv import dotenv_values


class ConfigManager:
    def __init__(self, file_path: str="/app/env/.env") -> None:
        self.__config = dotenv_values(file_path)

    def get_token(self) -> str:
        return self.__config.get("TOKEN")
