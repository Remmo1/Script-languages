import re
from random import seed, randint
from typing import Optional

from fastapi import FastAPI, Path

from Classes.First_name import First_name
from Classes.Ident_number import Ident_number
from Classes.Last_name import Last_name
from Classes.Pearson import Pearson


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


def add_person(name: str, last_name: str, email: str, phone_number: str):
    # utworzenie id
    new_id = id_generator()
    while new_id in PEOPLE:
        new_id = id_generator()
    ok_id = Ident_number(new_id)

    # sprawdzenie emaila
    if not check_phone_number(phone_number) or not check_email(email):
        return {
            "Error 400": "Znaleziono blad w numerze telefonu lub emailu, prosze upewnic sie ze wprowadzane dane sa "
                         "prawidlowe"}

    First_name.open_file(First_name.FILEPATH)
    # sklejenie danych w jeden tekst
    ok_name = First_name(name)
    ok_last_name = Last_name(last_name)
    data = ok_id.getId() + ' ' + ok_name.get_text() + ' ' + ok_last_name.get_text()

    # dodanie nowej osoby
    new_person = Pearson(data)
    PEOPLE[ok_id] = {
        (new_person, email, phone_number)
    }

add_person('aLEkSAnDRa', 'WolSKA', '211023@student.pwr.edu.pl', '123456789')