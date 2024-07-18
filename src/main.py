import logging
import time

import endpoints
from config import *
from models import *


def setup_logging():
    logger = logging.getLogger("HamsterHack")
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        '[%(name)s] %(levelname)s -> %(message)s'
    )

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)

    return logger

class Account:
    def __init__(self, token) -> None:
        self.logger = logging.getLogger("HamsterHack")
        self.endpoint = endpoints.Endpoints(token)
        self.account_info = self.endpoint.account_info()

    def tap(self):
        self.info = self.endpoint.sync()

        self.info = self.endpoint.tap(self.info, self.info.availableTaps)
        self.logger.info(f"Name: {self.account_info.name} | Balance: {round(self.info.totalCoins):,} | Level: {self.info.level}")


class Main:
    def __init__(self) -> None:
        self.logger = setup_logging()
        self.config = ConfigManager()

        self.accounts: list[Account] = []
        for token in self.config.get_token_list():
            self.accounts.append(Account(token))

    def run(self):
        while True:
            for account in self.accounts:
                try:
                    account.tap()
                except:
                    self.logger.error(f"Error, user: {account.account_info.name}")

            time.sleep(10)


if __name__ == "__main__":
    main = Main()
    main.run()
