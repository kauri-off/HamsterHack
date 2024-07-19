from pydantic import BaseModel

class Task(BaseModel):
    id: str
    isCompleted: bool
    rewardCoins: int | float

class ListTask(BaseModel):
    tasks: list[Task]
