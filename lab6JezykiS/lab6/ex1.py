import numpy as np

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
