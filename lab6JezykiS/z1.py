import numpy as np

def levenshteinDistance(s, t):
    d = np.empty((0,0))
    m = len(s)
    n = len(t)
    
    for i in range(0, m):
        d[i][0] = i
    for j in range(0, n):
        d[j][0] = j
        
    cost = 0
    for i in range(0, m):
        for j in range (0, n):
            if s[i] == t[j]:
                cost = 0
            else:
                cost = 1
            d[i][j] = min(
                            d[i - 1, j] + 1,
                            d[i, j - 1] + 1,
                            d[i - 1, j - 1] + cost            
                        )
    return d[m][n]