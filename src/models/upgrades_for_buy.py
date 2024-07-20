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
    cooldownSeconds: int | None = 0

    def ratio(self):
        return self.price / self.profitPerHour

class Section(BaseModel):
    section: str
    isAvailable: bool

class UpgradesForBuy(BaseModel):
    upgradesForBuy: list[Upgrade]
    sections: list[Section]
