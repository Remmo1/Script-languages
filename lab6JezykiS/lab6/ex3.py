import pandas as pd
import argparse
from ex1 import levenshtein_distance

FILENAME = '/media/remmo/Acer/Uczelnia/Semestr4/Jezyki Skryptowe/laby/lab6JezykiS/covid.txt'


def readCountryNames(path):
    df = pd.read_csv(path, delimiter='\t')
    df = df.drop_duplicates(subset=['countriesAndTerritories'])
    df = df['countriesAndTerritories']
    return df


names = readCountryNames(FILENAME)

parser = argparse.ArgumentParser(description='Wyszukiwanie podobnych nazw krajow')
parser.add_argument('-c', '--country', type=str, metavar='', required=True)
parser.add_argument('-n', '--isnear', type=int, metavar='', required=True)

args = parser.parse_args()

resultList = []
for name in names:
    dis = levenshtein_distance(args.country, name)
    if dis <= args.isnear:
        resultList.append((name, dis))

resultList.sort(key=lambda x: x[1], reverse=True)
for pair in resultList:
    print(pair[0], '    ', pair[1])
