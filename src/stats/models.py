from pydantic import BaseModel, Field
import datetime


class StatsResponseV1(BaseModel):
    user_id: int = Field(..., ge=1)
    repo_id: int = Field(..., ge=1)
    date: datetime.date
    stargazers: int = Field(..., ge=0)
    forks: int = Field(..., ge=0)
    watchers: int = Field(..., ge=0)


class StatsAddRequestV1(BaseModel):
    user_id: int = Field(..., ge=1)
    repo_id: int = Field(..., ge=1)
    date: str
    stargazers: int = Field(..., ge=0)
    forks: int = Field(..., ge=0)
    watchers: int = Field(..., ge=0)
