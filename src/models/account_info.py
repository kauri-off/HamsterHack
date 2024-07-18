from pydantic import BaseModel

class AccountInfo(BaseModel):
    id: str
    at: str
    name: str
    avatar: dict
    telegramUserIds: list
    cryptoWalletUserIds: list
    deviceIds: list
    appleUserIds: list
    googleUserIds: list
