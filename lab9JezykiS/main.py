import functools
import re
from random import seed, randint
from typing import Optional

from fastapi import FastAPI, Path

from Classes.First_name import First_name
from Classes.Ident_number import Ident_number
from Classes.Last_name import Last_name
from Classes.Pearson import Pearson

app = FastAPI()
PEOPLE = {}


# generator id
def id_generator():
    seed(1)
    sum_a = 0
    id_n = ''
    for _ in range(7):
        value = randint(0, 9)
        sum_a += value
        id_n += str(value)
    id_n += str(sum_a % 97)
    return id_n


# regexy sprawdzajace telefon i email
def check_phone_number(number):
    phone_pattern = re.compile(r'(\+\d\d )?[1-9]\d{2}[ -.]?\d{3}[ -.]?\d{3}')
    matches = phone_pattern.finditer(number)

    for match in matches:
        if match.group(1) is None:
            return True
        else:
            return match.group(1) == '+48 '
    return False


def check_email(address):
    email_pattern = \
        re.compile(r'((\d{6})?([a-zA-Z]+\.[a-zA-Z]+)?([a-zA-Z]+\.[a-zA-Z]+-[a-zA-Z]+)?)@([a-zA-Z]+\.)?(pwr.edu.pl)')
    matches = email_pattern.finditer(address)

    for m in matches:
        data = m.group(1)
        if data is not None:
            return True
        else:
            return False


@app.post("/people")
def add_person(name: str, last_name: str, email: str, phone_number: str):
    # utworzenie id
    new_id = id_generator()
    while new_id in PEOPLE:
        new_id = id_generator()

    # sprawdzenie emaila
    if not check_phone_number(phone_number) or not check_email(email):
        return {
            "Error 400": "Znaleziono blad w numerze telefonu lub emailu, prosze upewnic sie ze wprowadzane dane sa "
                         "prawidlowe"}

    # nie wiem czy to robic
    First_name.open_file(First_name.FILEPATH)

    # sklejenie danych w jeden tekst
    ok_name = First_name(name)
    ok_last_name = Last_name(last_name)
    data = new_id + ' ' + ok_name.get_text() + ' ' + ok_last_name.get_text()

    # dodanie nowej osoby
    new_person = Pearson(data)
    PEOPLE[new_id] = {
        (new_person, email, phone_number)
    }

    return {"Pomyslnie dodano osobe"}

@app.get("/people")
def get_everybody():
    if PEOPLE:
        return PEOPLE
    else:
        return {"Nie dodales jeszcze zadnej osoby"}

@app.get("/people/{last_name}")
def get_by_last_name(last_name: str):
    result = {}
    for id in PEOPLE:
        for data in PEOPLE[id]:
            if data == last_name:
                result[id] = PEOPLE[id]
    return result







"""

PEOPLE = {
    1: {"Nowak", "Kamil"},
    2: {"Malgorzata", "Wolska"}
}


result = {}
for id in PEOPLE:
    for data in PEOPLE[id]:
        if data == "Nowak":
            result[id] = PEOPLE[id]

for i in result:
    print(result)



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
