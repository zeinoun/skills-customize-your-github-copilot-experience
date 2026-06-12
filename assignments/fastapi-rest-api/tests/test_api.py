from fastapi.testclient import TestClient
from starter_code import app

client = TestClient(app)


def test_crud_flow():
    # initial list is empty
    r = client.get("/items")
    assert r.status_code == 200
    assert r.json() == []

    # create an item
    r = client.post("/items", json={"name": "apple", "price": 1.25})
    assert r.status_code == 201
    item = r.json()
    assert item["id"] == 1
    assert item["name"] == "apple"

    # list now contains the item
    r = client.get("/items")
    assert r.status_code == 200
    assert len(r.json()) == 1

    # retrieve the item
    r = client.get("/items/1")
    assert r.status_code == 200
    assert r.json()["id"] == 1

    # delete the item
    r = client.delete("/items/1")
    assert r.status_code == 204

    # now not found
    r = client.get("/items/1")
    assert r.status_code == 404
