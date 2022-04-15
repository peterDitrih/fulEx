from typing import List

from fastapi import APIRouter, status, Depends, Path

from src.api.protocols import UserServiceProtocol
from src.api.protocols import StatsServiceProtocol
from src.user.models import UserResponseV1, UserAddRequestV1, UserStatsResponseV1

router = APIRouter(
    tags=['Users']
)


@router.get(
    path='/v1/users',
    response_model=List[UserResponseV1],
    summary='Список пользователей',
    description='Возвращает список всех пользователей.'
)
def get_all_users(
        user_service: UserServiceProtocol = Depends()
):
    return user_service.get_all_users()


@router.get(
    path='/v1/users/{id}',
    response_model=UserResponseV1,
    summary='Информация о пользователе',
    description='Возвращает информацию о пользователе.'
)
def get_user(
        id: int = Path(..., ge=1),
        user_service: UserServiceProtocol = Depends()
):
    return user_service.get_user_by_id(id)


@router.get(
    path='/v1/users/{id}/stats',
    response_model=UserStatsResponseV1,
    summary='Информация о пользователе',
    description='Возвращает информацию о пользователе.'
)
def get_user_stats(
        id: int = Path(..., ge=1),
        user_service: UserServiceProtocol = Depends(),
        stats_service: StatsServiceProtocol = Depends()
):
    result = {}
    result['user'] = user_service.get_user_by_id(id)
    result['stats'] = stats_service.get_stats_by_user_id(id)
    return result


@router.put(
    path='/v1/users',
    status_code=status.HTTP_201_CREATED,
    summary='Добавить пользователя',
    description='Добавляет пользователя для отслеживания популярности репозиториев.',
)
def add_user(
        user_data: UserAddRequestV1,
        user_service: UserServiceProtocol = Depends()
):
    user_service.add_user(user_data)


@router.delete(
    path='/v1/users/{id}',
    summary='Удалить пользователя',
    description='Удаляет пользователя.'
)
def delete_user(
        id: int = Path(..., ge=1),
        user_service: UserServiceProtocol = Depends()
):
    user_service.delete_user_by_id(id)


@router.delete(
    path='/v1/users',
    summary='Удалить всех пользователей',
    description='Удаляет всех пользователей.'
)
def delete_all_user(
        user_service: UserServiceProtocol = Depends()
):
    user_service.delete_all_users()
