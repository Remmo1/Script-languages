from typing import Optional

from fastapi import FastAPI, Path

app = FastAPI()

inventory = {
    1: {
        "name": "Milk",
        "price": 3.99,
        "brand": "Regular"
    }
}


@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(None, description="The ID of the item", gt=0, lt=2)):
    return inventory[item_id]

@app.get("/get-by-name")
def get_item(name: str):
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
    return {"Data": "Not found"}


"""
====================== Przyklad z ich strony ====================

from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

# strona do testowania: http://127.0.0.1:8000/docs

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

"""