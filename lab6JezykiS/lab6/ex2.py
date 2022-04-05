# zadanie 2
import argparse
import pandas as pd

parser = argparse.ArgumentParser(description='Policz ilosc przypadkow dla kraju i miesiaca')
parser.add_argument('-c', '--country', type=str, metavar='', required=True, help='Nazwa szukanego kraju')
parser.add_argument('-m', '--month', type=int, metavar='', required=True, help='Numer szukanego miesiaca')

group = parser.add_mutually_exclusive_group()
group.add_argument('-q', '--quiet', action='store_true', help='wyswietl tylko wynik')
group.add_argument('-v', '--verbose', action='store_true', help='wyswietl wszystkie dane')

args = parser.parse_args()

FILENAME = '/media/remmo/Acer/Uczelnia/Semestr4/Jezyki Skryptowe/laby/lab6JezykiS/lab6/covid.txt'

df = pd.read_csv(FILENAME, delimiter='\t')

sumOfCovid = 0
for index, row in df.iterrows():
    if row['countriesAndTerritories'] == args.country and row['month'] == args.month:
        sumOfCovid = sumOfCovid + int(row['cases'])

if args.quiet:
    print(sumOfCovid)
elif args.verbose:
    print('Suma przypadkow z miesiaca %s dla kraju %s wynosi %s' % (args.month, args.country, sumOfCovid))
else:
    print('Suma przypadkow = %s' % sumOfCovid)

"""

country = input('Podaj nazwe kraju: ')

while True:
    try:
        month = int(input('Podaj miesiac (numer od 1 do 12): '))
        if month < 1 or month > 12:
            raise ValueError
        break
    except ValueError:
        print('Podaj liczbe od 1 do 12!!!')

file = open(FILENAME, 'r')
next(file)
lines = file.readlines()
searched = []

for line in lines:
    if line.split('	')[6] == country and int(line.split('	')[2]) == month:
        searched.append(line)

sumOfCases = 0
for line in searched:
    sumOfCases = sumOfCases + int(line.split('	')[4])

print("Suma z miesiaca %d dla kraju %s jest rowna: %d" % (month, country, sumOfCases))

"""
