from pydantic import BaseModel, Field
from src.stats.models import StatsResponseV1
from typing import List


class UserResponseV1(BaseModel):
    id: int = Field(..., ge=1)
    login: str
    name: str


class UserAddRequestV1(BaseModel):
    id: int = Field(..., ge=1)
    login: str
    name: str


class UserStatsResponseV1(BaseModel):
    user: UserResponseV1
    stats: List[StatsResponseV1]
