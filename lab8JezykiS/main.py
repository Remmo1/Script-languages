# Zadanie 5
from Classes.Pearson import Pearson

people = []
with open('/media/remmo/Acer/Uczelnia/Semestr4/Jezyki Skryptowe/laby/lab8JezykiS/plikTestowy', 'r') as f:
    lines = f.readlines()

    for line in lines:
        people.append(Pearson(line))

    for pearson in people:
        print(pearson.__str__())
