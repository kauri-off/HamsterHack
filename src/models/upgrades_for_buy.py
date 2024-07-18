from pydantic import BaseModel


class Upgrade(BaseModel):
    id: str
    name: str
    price: int | float
    profitPerHour: int | float
    section: str
    level: int
    currentProfitPerHour: int | float
    profitPerHourDelta: int | float
    isAvailable: bool
    isExpired: bool

    def __lt__(self, other):
        if self.price == 0:
            return False
        elif other.price == 0:
            return True
        return self.profit() > other.profit()

    def profit(self):
        if self.price == 0:
            return 99999999999
        return self.profitPerHour/self.price


class UpgradesForBuy(BaseModel):
    upgradesForBuy: list[Upgrade]
