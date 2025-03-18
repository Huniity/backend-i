#Create a test file named test_main.py:

from fastapi.testclient import TestClient
from src.session_11.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the FastAPI API!"}

#=====================================#

def test_create_item_success():
    response = client.post("/items/", json={"name": "Test Item"})
    assert response.status_code == 200
    assert response.json() == { "item": {"name": "Test Item"}}

def test_create_item_failure():
    response = client.post("/items/", json={"name": ""})
    assert response.status_code == 422
    assert response.json()["detail"] == "Item must have a name"

#=====================================#

def test_put_item_success():
    response = client.put("/items/0", json={"name": "Updated Test Item"})
    assert response.status_code == 200
    assert response.json() == {"item": {"name": "Updated Test Item"}}

def test_put_item_failure():
    response = client.put("/items/999", json={"name": "Updated Test Item"})
    assert response.status_code == 400
    assert response.json()["detail"] == "Item does not exist"

#=====================================#

# def test_delete_item_success():
#     response = client.post("/items/", json={"name": "Test Item"})
#     assert response.status_code == 200
#     assert response.json() == {"item": {"name": "Test Item"}}

# def test_delete_item_failure():
#     response = client.post("/items/", json={"description": "No name provided"})
#     assert response.status_code == 400
#     assert response.json()["detail"] == "Item must have a name"