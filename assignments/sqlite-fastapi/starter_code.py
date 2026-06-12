import sqlite3
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

db = sqlite3.connect("items.db", check_same_thread=False)

def init_db() -> None:
    db.execute(
        """
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL
        )
        """
    )
    db.commit()


class ItemCreate(BaseModel):
    name: str
    price: float


class Item(ItemCreate):
    id: int


def row_to_item(row: sqlite3.Row) -> Item:
    return Item(id=row[0], name=row[1], price=row[2])


@app.on_event("startup")
def startup_event() -> None:
    db.row_factory = sqlite3.Row
    init_db()


@app.get("/items", response_model=List[Item])
def list_items() -> List[Item]:
    cursor = db.execute("SELECT id, name, price FROM items")
    return [row_to_item(row) for row in cursor.fetchall()]


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int) -> Item:
    cursor = db.execute("SELECT id, name, price FROM items WHERE id = ?", (item_id,))
    row = cursor.fetchone()
    if row is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return row_to_item(row)


@app.post("/items", response_model=Item, status_code=201)
def create_item(item: ItemCreate) -> Item:
    cursor = db.execute(
        "INSERT INTO items (name, price) VALUES (?, ?)",
        (item.name, item.price),
    )
    db.commit()
    item_id = cursor.lastrowid
    return Item(id=item_id, name=item.name, price=item.price)


@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: ItemCreate) -> Item:
    cursor = db.execute(
        "UPDATE items SET name = ?, price = ? WHERE id = ?",
        (item.name, item.price, item_id),
    )
    db.commit()
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Item not found")
    return Item(id=item_id, name=item.name, price=item.price)


@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int) -> None:
    cursor = db.execute("DELETE FROM items WHERE id = ?", (item_id,))
    db.commit()
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Item not found")
