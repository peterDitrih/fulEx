from typing import List

from fastapi import APIRouter, Depends, Path, status

from src.api.protocols import StatsServiceProtocol
from src.stats.models import StatsResponseV1, StatsAddRequestV1

router = APIRouter(
    tags=['Stats']
)


@router.get(
    path='/v1/stats',
    response_model=List[StatsResponseV1],
    summary='Список всех записей статистики',
    description='Возвращает список всех записей статистики.'
)
def get_all_stats(
        stats_service: StatsServiceProtocol = Depends()
):
    return stats_service.get_all_stats()


@router.delete(
    path='/v1/stats/{user_id}',
    summary='Удалить все записи статистики определенного пользователя',
    description='Удаляет все записи статистики определенного пользователя.'
)
def delete_stat_by_user_id(
        user_id: int = Path(..., ge=1),
        stats_service: StatsServiceProtocol = Depends()
):
    stats_service.delete_stats_by_user_id(user_id)


@router.put(
    path='/v1/stats',
    status_code=status.HTTP_201_CREATED,
    summary='Добавить запись статистики',
    description='Добавляет запись статистики.'
)
def add_stat(
        stat_data: StatsAddRequestV1,
        stats_service: StatsServiceProtocol = Depends()
):
    stats_service.add_stat(stat_data)


@router.delete(
    path='/v1/stats',
    summary='Удалить всех пользователей',
    description='Удаляет всех пользователей.'
)
def delete_all_user(
        stats_service: StatsServiceProtocol = Depends()
):
    stats_service.delete_all_stats()
