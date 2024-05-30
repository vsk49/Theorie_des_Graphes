import numpy as np

def Red(M):
    k = np.shape(M)[0]
    N = M
    for i in range(k):
        for j in range(k):
            N[i][j] = min(N[i][j], 1)
    return N

"""
def Trans1(M):
    k = np.shape(M)[0]
    N = M               # pour calculer M + M^2 + ... + M^k
    P = M               # pour calculer M^2, M^3, ..., M^k
    for i in range(k - 1):
        P = np.dot(P, M)
        N = N + P
    for i in range(k):
        for j in range(k):
            # on remplace les valeurs de N par 1 si elles sont non nulles
            N[i][j] = min(N[i][j], 1)
    return N
"""

def Trans1(M):
    k = np.shape(M)[0]
    N = M
    P = M
    for _ in range(k - 1):
        P = np.dot(P, M)
        N = Red(N + P)
    return N


def RoyWarshall(M):
    k = np.shape(M)[0]
    N = np.copy(M)
    for i in range(k):
        for j in range(k):
            if N[i][j] == 1:
                for l in range(k):
                    if N[j][l] == 1:
                        N[i][l] = 1
    return N

M = [[0, 0, 1, 1, 0, 0, 0], 
     [1, 0, 0, 0, 1, 0, 0], 
     [0, 1, 0, 1, 0, 0, 0], 
     [0, 0, 0, 0, 1, 0, 1], 
     [0, 0, 0, 0, 0, 1, 0], 
     [0, 0, 0, 0, 1, 0, 0], 
     [0, 1, 0, 0, 0, 0, 0]]
print("Graphe 1")
print(Trans1(M))
print("Graphe 2")
print(RoyWarshall(M))