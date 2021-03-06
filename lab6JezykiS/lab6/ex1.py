import numpy as np

"""
Krótkie wyjaśnienie ode mnie:

rysujemy macierz biorąc drugi wyraz na górę, pierwszy na lewo np dla 'marka', 'ariada':

    a r i a d a
  m 0 0 0 0 0 0
  a 0 0 0 0 0 0
  r 0 0 0 0 0 0
  k 0 0 0 0 0 0
  a 0 0 0 0 0 0
  
Dopisujemy długości wyrazów:

    a r i a d a
  m 0 1 2 3 4 5
  a 1 0 0 0 0 0
  r 2 0 0 0 0 0
  k 3 0 0 0 0 0
  a 4 0 0 0 0 0
  
Cały algorytm polega na sprawdzeniu który koszt jest najmniejszy w dwóch przypadkach:
    1. litera jest taka sama, wtedy bierzemy wartość z lewego górnego rogu.
    2. litery są różne, wtedy szukamy minimum z następującego schematu:
    
        zamiana     | dodanie
        usunięcie   | jesteś tutaj!
          
        i dodajemy do tej liczby 1.

Wynikowa macierz wygląda tak:

    a r i a d a
  m 0 1 2 3 4 5
  a 1 1 2 2 3 4
  r 2 1 2 3 3 4
  k 3 2 2 3 4 4
  a 4 3 3 2 3 4
 
Szukana wartość znajduje się w prawym dolnym rogu i dla tego przypadku wynosi 4.

"""

def levenshtein_distance(s, t):
    m = len(s)
    n = len(t)
    d = np.empty((m, n))

    for i in range(0, m):
        d[i][0] = i
    for j in range(0, n):
        d[0][j] = j

    for i in range(1, m):
        for j in range(1, n):
            if s[i] == t[j]:
                cost = 0
            else:
                cost = 1
            d[i][j] = min(
                d[i - 1, j] + 1,
                d[i, j - 1] + 1,
                d[i - 1, j - 1] + cost
            )
    return d[m - 1][n - 1]


print(levenshtein_distance('pies', 'pies'))
print(levenshtein_distance('granit', 'granat'))
print(levenshtein_distance('orczyk', 'oracz'))
print(levenshtein_distance('marka', 'ariada'))
