import requests
from fastapi import status
from fastapi.testclient import TestClient

from src.api import app

client: requests.Session = TestClient(app)

anvdev_user = {
    'id': 28631927,
    'login': 'anvdev',
    'name': 'Ivan Titov'
}

anvdev_stat = {
    'user_id': 28631927,
    'date': '2022-04-14',
    'forks': 0,
    'repo_id': 481611622,
    'stargazers': 1,
    'watchers': 1,
}


def test_user_stats():
    response = client.delete('/v1/stats')
    assert response.status_code == status.HTTP_200_OK

    response = client.delete('/v1/users')
    assert response.status_code == status.HTTP_200_OK

    response = client.put('/v1/users', json=anvdev_user)
    assert response.status_code == status.HTTP_201_CREATED

    response = client.put('/v1/stats', json=anvdev_stat)
    assert response.status_code == status.HTTP_201_CREATED

    response = client.get('/v1/users')
    assert response.json() == [anvdev_user]

    response = client.get('/v1/stats')
    assert response.json() == [anvdev_stat]

    response = client.get(f'/v1/users/{anvdev_user["id"]}/stats')
    json_data = response.json()
    assert json_data['user'] == anvdev_user
    assert json_data['stats'] == [anvdev_stat]

    response = client.delete(f'/v1/stats/{anvdev_user["id"]}')
    assert response.status_code == status.HTTP_200_OK

    response = client.get('/v1/stats')
    assert response.json() == []

    response = client.delete(f'/v1/users/{anvdev_user["id"]}')
    assert response.status_code == status.HTTP_200_OK

    response = client.get('/v1/users')
    assert response.json() == []
