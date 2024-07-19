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
    def __init__(self, session: Session) -> None:
        self.logger = logging.getLogger("HamsterHack")
        self.session = session

        if session.token:
            self.endpoint = endpoints.Endpoints(session.token)
        elif session.init_data:
            self.endpoint = endpoints.Endpoints(endpoints.Endpoints.auth_by_telegram(session.init_data))
        else:
            self.logger.critical("Cannot get token or init_data, check config")
            exit()

        self.account_info = self.endpoint.account_info()
        self.info = self.endpoint.sync()

    def tap(self):
        if not self.session.tap:
            return

        self.info = self.endpoint.sync()

        self.info = self.endpoint.tap(self.info, self.info.availableTaps)
        self.logger.info(f"Name: {self.account_info.name} | Balance: {round(self.info.balanceCoins):,} | Level: {self.info.level}")

    def update(self):
        if not self.session.upgrade:
            return

        self.update_boosts()
        self.get_daily()

        while self.update_mining():
            pass

    def update_mining(self) -> bool:
        upgrades = self.endpoint.upgrades_for_buy()
        upgrades = list(filter(lambda up: up.isAvailable and not up.isExpired, upgrades.upgradesForBuy))
        upgrades = list(filter(lambda up: up.price<self.info.balanceCoins, upgrades))
        # upgrades = list(filter(lambda up: up.section=="PR&Team", upgrades))
        # upgrades = list(filter(lambda up: up.price>2000, upgrades))

        upgrades.sort()

        if upgrades:
            upgrade = upgrades[0]
            if upgrade.profit() < 0.15:
                return False
            self.info = self.endpoint.buy_upgrade(upgrade)
            self.logger.info(f"Name: {self.account_info.name} buy ({upgrade.name}) level ({upgrade.level+1}) | Balance: {round(self.info.balanceCoins):,}")
            return True

        return False

    def update_boosts(self):
        boosts = self.endpoint.boosts_for_buy()

        for boost in boosts.boostsForBuy:
            self.apply_free_boost(boost)

    def apply_free_boost(self, boost: Boost):
        if boost.price == 0 and boost.cooldownSeconds == 0:
            self.endpoint.buy_boost(boost)

            if boost.id == "BoostFullAvailableTaps":
                self.logger.info(f"Name: {self.account_info.name} Now has full energy!")

    def get_daily(self):
        tasks = self.endpoint.list_task()

        for task in tasks.tasks:
            if task.id == "streak_days" and not task.isCompleted:
                self.endpoint.check_task(task)
                self.logger.info(f"Name: {self.account_info.name} new day, new streak!")



class Main:
    def __init__(self) -> None:
        self.logger = setup_logging()
        self.config = ConfigManager()

        self.accounts: list[Account] = []

        for session in self.config.get_config().sessions:
            self.accounts.append(Account(session))

    def run(self):
        while True:
            for account in self.accounts:
                try:
                    account.tap()
                    account.update()
                except Exception as e:
                    self.logger.error(f"Error, user: {account.account_info.name} | {e}")

            time.sleep(30)


if __name__ == "__main__":
    main = Main()
    main.run()
