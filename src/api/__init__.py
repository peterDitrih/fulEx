import asyncio
import sqlalchemy as sa
import aiohttp
from fastapi import FastAPI
import src.api.protocols
from src.api import users, protocols, stats
from src.database import DatabaseSettings, create_database_url
from src.user.service import UserService
from src.stats.service import StatsService
from src.stats.models import StatsAddRequestV1

db_settings = DatabaseSettings()
engine = sa.create_engine(
    create_database_url(db_settings),
    future=True
)
user_service = UserService(engine)
stats_service = StatsService(engine)


def get_application() -> FastAPI:
    application = FastAPI(
        title='GitHub Repo Stats',
        description='Сервис сбора статистических данных о популярности репозиториев на GitHub.',
        version='1.0.0'
    )

    application.include_router(users.router)
    application.include_router(stats.router)

    application.dependency_overrides[protocols.UserServiceProtocol] = lambda: user_service
    application.dependency_overrides[protocols.StatsServiceProtocol] = lambda: stats_service
    return application


async def scan_users():
    while True:
        users = user_service.get_all_users()
        async with aiohttp.ClientSession() as session:
            for user in users:
                async with session.get(f'https://api.github.com/users/{user.login}/repos', ssl=False) as response:
                    users_repos = await response.json()
                stats_service.delete_stats_by_user_id(user.id)
                for repo in users_repos:
                    repo_obj = StatsAddRequestV1(
                        user_id=user.id,
                        repo_id=repo['id'],
                        date=repo['created_at'],
                        stargazers=repo['stargazers_count'],
                        forks=repo['forks'],
                        watchers=repo['watchers'],
                    )
                    stats_service.add_stat(repo_obj)

        await asyncio.sleep(86400)

try:
    loop = asyncio.get_running_loop()
    asyncio.create_task(scan_users())
except RuntimeError:
    pass

app = get_application()
