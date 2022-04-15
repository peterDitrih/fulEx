from typing import List

from src.user.models import UserResponseV1, UserAddRequestV1
from src.stats.models import StatsResponseV1, StatsAddRequestV1


class UserServiceProtocol:
    def get_all_users(self) -> List[UserResponseV1]:
        raise NotImplementedError

    def get_user_by_id(self, id: int) -> UserResponseV1:
        raise NotImplementedError

    def add_user(self, user: UserAddRequestV1) -> None:
        raise NotImplementedError

    def delete_user_by_id(self, id: int) -> None:
        raise NotImplementedError


class StatsServiceProtocol:
    def delete_all_stats(self) -> None:
        raise NotImplementedError

    def get_all_stats(self) -> List[StatsResponseV1]:
        raise NotImplementedError

    def get_stats_by_user_id(self, user_id: int) -> List[StatsResponseV1]:
        raise NotImplementedError

    def add_stat(self, stat: StatsAddRequestV1) -> None:
        raise NotImplementedError

    def delete_stats_by_user_id(self, user_id: int) -> None:
        raise NotImplementedError
