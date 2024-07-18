from pydantic import BaseModel


class Boost(BaseModel):
    id: str
    price: int
    earnPerTap: int
    maxTaps: int
    cooldownSeconds: int
    level: int
    maxTapsDelta: int
    earnPerTapDelta: int

class BoostsForBuy(BaseModel):
    boostsForBuy: list[Boost]
