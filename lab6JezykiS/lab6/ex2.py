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

FILENAME_UBUNTU = '/media/remmo/Acer/Uczelnia/Semestr4/Jezyki Skryptowe/laby/lab6JezykiS/covid.txt'
FILENAME_WINDOWS = 'C:\\Uczelnia\\Semestr4\\Jezyki Skryptowe\\laby\\lab6JezykiS\\covid.txt'

df = pd.read_csv(FILENAME_WINDOWS, delimiter='\t')

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
