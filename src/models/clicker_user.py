from pydantic import BaseModel

class Upgrade(BaseModel):
    id: str
    level: int
    lastUpgradeAt: int
    snapshotReferralsCount: int

class ClickerUser(BaseModel):
    id: str
    totalCoins: int
    balanceCoins: int
    level: int
    availableTaps: int
    lastSyncUpdate: int
    exchangeId: str
    boosts: dict
    upgrades: dict[str, Upgrade]
    tasks: dict
    airdropTasks: dict
    referralsCount: int
    maxTaps: int
    earnPerTap: int
    earnPassivePerSec: int
    earnPassivePerHour: int
    lastPassiveEarn: int
    tapsRecoverPerSec: int
    createdAt: str
