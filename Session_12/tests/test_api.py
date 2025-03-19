import pytest
from fastapi.testclient import TestClient
from session_12.main import api
from fastapi import status



@pytest.fixture(scope="session")
def client():
    return TestClient(api)

def test_api_create_task(client):
    response = client.post("/task")
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() is not None

def test_api_create_task_failure(client):
    response = client.post("/taskk")
    assert response.status_code == status.HTTP_404_NOT_FOUND

