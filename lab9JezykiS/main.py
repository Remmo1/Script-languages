import re
from random import randint
from typing import Any

import fastapi
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel

from Classes.First_name import First_name
from Classes.Last_name import Last_name

app = FastAPI()

people = {}


# klasa Osoba
class Pearson(BaseModel):
    name: str
    last_name: str
    email: str
    phone_number: str


# Żeby wykorzystać kod z listy 8 musimy podmienić imię i nazwisko przed dodaniem osoby, ponieważ konstruktor nie
# pozwala domyślnie na typy napisane przez użytkownika
def conversion(pearson: Pearson):
    pearson.name = First_name(pearson.name).get_text()
    pearson.last_name = Last_name(pearson.last_name).get_text()
    if not check_phone_number(pearson.phone_number):
        raise fastapi.HTTPException(status_code=400, detail="Podany numer telefonu nie jest polski lub poprawny!")
    if not check_email(pearson.email):
        raise fastapi.HTTPException(status_code=400, detail="Podany email nie pochodzi z pwr!")


@app.get("/")
def home():
    return {"Witam": "w bazie danych osob!"}


@app.post("/people")
def add_pearson(pearson: Pearson):
    conversion(pearson)
    pearson_id = id_generator()
    while pearson_id in people:
        pearson_id = id_generator()

    people[pearson_id] = pearson
    return people[pearson_id]


@app.get("/people")
def get_everyone():
    if people:
        return people
    else:
        raise fastapi.HTTPException(status_code=404, detail="Nie ma zadnych osob w bazie!")


@app.get("/people/last_name/{last_name}")
def get_by_last_name(last_name: str = Query(None, title="name")):
    result = {}
    for pearson_id in people:
        if people[pearson_id].last_name == last_name:
            result[pearson_id] = people[pearson_id]
    if not result:
        raise fastapi.HTTPException(status_code=404, detail="Brak osoby o nazwisku " + last_name + " w bazie")
    else:
        return result


@app.get("/people/id/{pearson_id}")
def get_by_id(pearson_id: str = Path(None, description="Id szukanej osoby")):
    return people[pearson_id]


@app.delete("/people/{pearson_id}")
def delete_pearson_from_database(pearson_id: str = Query(..., description="Id osoby do usuniecia")):
    if pearson_id not in people:
        raise fastapi.HTTPException(status_code=404, detail="Brak osoby o podanym id w bazie")

    del people[pearson_id]
    return {"Success": "Item deleted!"}


# generator numerów id
def id_generator():
    sum_a = 0
    id_n = ''
    for _ in range(7):
        value = randint(0, 9)
        sum_a += value
        id_n += str(value)
    id_n += str(sum_a % 97)
    return id_n


# regexy sprawdzające telefon i email
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
