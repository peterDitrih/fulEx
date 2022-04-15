from typing import List

from sqlalchemy import select, insert, delete
from sqlalchemy.future import Engine

from src.database import tables
from src.stats.models import StatsResponseV1, StatsAddRequestV1


class StatsService:
    def __init__(self, engine: Engine) -> None:
        self._engine = engine

    def get_all_stats(self) -> List[StatsResponseV1]:
        query = select(tables.stats)
        with self._engine.connect() as connection:
            stats_data = connection.execute(query)
        stats = []
        for stat_data in stats_data:
            stat = StatsResponseV1(
                user_id=stat_data['user_id'],
                repo_id=stat_data['repo_id'],
                date=stat_data['date'],
                stargazers=stat_data['stargazers'],
                forks=stat_data['forks'],
                watchers=stat_data['watchers'],
            )
            stats.append(stat)
        return stats

    def get_stats_by_user_id(self, user_id: int) -> List[StatsResponseV1]:
        query = select(tables.stats).where(tables.stats.c.user_id == user_id)
        with self._engine.connect() as connection:
            stats_data = connection.execute(query)
        stats = []
        for stat_data in stats_data:
            stat = StatsResponseV1(
                user_id=stat_data['user_id'],
                repo_id=stat_data['repo_id'],
                date=stat_data['date'],
                stargazers=stat_data['stargazers'],
                forks=stat_data['forks'],
                watchers=stat_data['watchers'],
            )
            stats.append(stat)
        return stats

    def add_stat(self, stat: StatsAddRequestV1) -> None:
        query = insert(tables.stats).values(
            user_id=stat.user_id,
            repo_id=stat.repo_id,
            date=stat.date,
            stargazers=stat.stargazers,
            forks=stat.forks,
            watchers=stat.watchers,
        )
        with self._engine.connect() as connection:
            connection.execute(query)
            connection.commit()

    def delete_stats_by_user_id(self, user_id: int) -> None:
        query = delete(tables.stats).where(tables.stats.c.user_id == user_id)
        with self._engine.connect() as connection:
            connection.execute(query)
            connection.commit()

    def delete_all_stats(self) -> None:
        query = delete(tables.stats)
        with self._engine.connect() as connection:
            connection.execute(query)
            connection.commit()
