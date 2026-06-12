from fastapi.testclient import TestClient
from starter_code import app

client = TestClient(app)


def test_crud_endpoints():
    response = client.get("/items")
    assert response.status_code == 200
    assert response.json() == []

    response = client.post("/items", json={"name": "book", "price": 9.99})
    assert response.status_code == 201
    item = response.json()
    assert item["id"] == 1
    assert item["name"] == "book"
    assert item["price"] == 9.99

    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json()["name"] == "book"

    response = client.put("/items/1", json={"name": "notebook", "price": 7.50})
    assert response.status_code == 200
    updated = response.json()
    assert updated["name"] == "notebook"
    assert updated["price"] == 7.5

    response = client.delete("/items/1")
    assert response.status_code == 204

    response = client.get("/items/1")
    assert response.status_code == 404
