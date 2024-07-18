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

class Main:
    def __init__(self) -> None:
        self.logger = setup_logging()
        self.config = ConfigManager()
        self.endpoints = endpoints.Endpoints(self.config.get_token())

        self.account_info = self.endpoints.account_info()

        for _ in range(3):
            if not self.sync():
                break
        else:
            self.logger.critical("Failed to sync, all attempts failed")
            exit()

    def run(self):
        self.logger.info(f"Name: {self.account_info.name}")
        self.logger.info(f"ID: {self.account_info.id}")

        while True:
            self.sync()
            self.logger.info(f"Energy {self.info.availableTaps}/{self.info.maxTaps} | Balance: {round(self.info.totalCoins):,} | Level: {self.info.level}")

            try:
                self.endpoints.tap(self.info, self.info.availableTaps)
            except:
                self.logger.error("Failed to tap")

            time.sleep(10)

    def sync(self) -> bool:
        '''Return True if error'''

        try:
            self.info = self.endpoints.sync()
            return False
        except:
            self.logger.error("Failed to sync")
            time.sleep(3)
            return True

if __name__ == "__main__":
    main = Main()
    main.run()
