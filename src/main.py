from config import *
import endpoints
from models import *
import time
import logging

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

    def run(self):
        while True:
            try:
                self.sync()
            except:
                self.logger.error("Failed to sync")
                time.sleep(3)
                continue

            if self.endpoints.tap(self.info, self.info.availableTaps).status_code == 200:
                self.logger.info(f"Clicked {self.info.availableTaps}/{self.info.maxTaps} | Current: {self.info.totalCoins:,}")

            time.sleep(10)

    def sync(self):
        self.info = self.endpoints.sync()

if __name__ == "__main__":
    main = Main()
    main.run()
