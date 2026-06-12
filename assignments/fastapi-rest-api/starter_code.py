from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Item(BaseModel):
    id: int | None = None
    name: str
    price: float

_db: List[Item] = []
_id_counter = 1

@app.get("/items", response_model=List[Item])
def list_items():
    return _db

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    for item in _db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.post("/items", response_model=Item, status_code=201)
def create_item(item: Item):
    global _id_counter
    item.id = _id_counter
    _id_counter += 1
    _db.append(item)
    return item

@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    for i, item in enumerate(_db):
        if item.id == item_id:
            _db.pop(i)
            return
    raise HTTPException(status_code=404, detail="Item not found")
