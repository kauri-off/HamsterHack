from pydantic import BaseModel


class ClickerUser(BaseModel):
    id: str
    totalCoins: int | float
    balanceCoins: int | float
    level: int
    availableTaps: int
    lastSyncUpdate: int
    exchangeId: str
    maxTaps: int
