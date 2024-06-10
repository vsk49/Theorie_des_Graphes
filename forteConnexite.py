import numpy as np

import bellmanFordVariants as bf
import genererMatrice as gm

# from nomFichier import nomVariable

# verifier si une matrice est fortement connexe
def fc(M):
    n = len(M)
    # utiliser le parcours profondeur pour verifier la forte connexite
    for i in range(n):
        flechesVisites = bf.parcour_profondeur(M, i)
        # mettre les noeuds visites dans un ensemble
        sommetsVisites = set(node for edge in flechesVisites for node in edge)
        # Si le nombre de noeuds < n, le graphe n'est pas fortement connexe
        if len(sommetsVisites) < n:
            return False
    # sinon, le graphe est fortement connexe
    return True

# retourne le pourcentage de graphes fortement connexes (50% de fleches)
def test_stat_fc(n):
    nbGraphesFortConnexes = 0
    nbGraphs = 300
    for _ in range(nbGraphs):
        M = gm.graphe(n, 1, 10)
        M_Reduire = bf.conversion(M)
        if fc(M_Reduire):
            nbGraphesFortConnexes += 1
    return nbGraphesFortConnexes / nbGraphs

# retourne la taille minimale de graphe fortement connexe
def trouver_n():
    n = 1
    while test_stat_fc(n) < 0.99:
        n += 1
    return n
        
# retourne le pourcentage de graphes fortement connexes (p% de fleches)
def test_stat_fc2(n, p):
    nbGraphesFortConnexes = 0
    nbGraphs = 300
    for _ in range(nbGraphs):
        M = gm.graphe2(n, p, 1, 10)
        M_Reduire = bf.conversion(M)
        if fc(M_Reduire):
            nbGraphesFortConnexes += 1
    return nbGraphesFortConnexes / nbGraphs

# retourne le seuil de p pour avoir 99% de graphes fortement connexes
def seuil(n):
    p = 0.01
    while test_stat_fc2(n, p) < 0.99:
        p += 0.01
    return p

# TESTS FONCTIONS
# print(test_stat_fc(10))
# print(trouver_n())
# print(test_stat_fc2(10, 0.4))
# print(seuil(12))
# print(seuil(18))
"""
P3 = np.array([
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1],
    [0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0],
    [1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0],
    [1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0],
    [1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1],
    [0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
    [1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
    [0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0],
    [0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0]
])
# print(fc(P3))
M3 = np.array([
    [15, 1, np.inf, np.inf, np.inf, np.inf, 11, 2, np.inf, np.inf],
    [np.inf, np.inf, 11, 9, np.inf, np.inf, np.inf, np.inf, np.inf, 15],
    [np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, 16, np.inf, np.inf],
    [np.inf, 3, np.inf, np.inf, np.inf, 13, np.inf, np.inf, np.inf, np.inf],
    [np.inf, np.inf, np.inf, np.inf, 4, np.inf, 9, np.inf, np.inf, 11],
    [np.inf, np.inf, np.inf, np.inf, 15, np.inf, np.inf, np.inf, 14, -7],
    [-7, np.inf, np.inf, 11, np.inf, 6, np.inf, np.inf, np.inf, np.inf],
    [np.inf, np.inf, np.inf, 1, 5, np.inf, -7, 13, np.inf, np.inf],
    [np.inf, np.inf, 1, 6, np.inf, 5, 17, np.inf, 18, 9],
    [8, 11, np.inf, np.inf, 15, np.inf, np.inf, 13, np.inf, np.inf]
])
M4 = [
    [np.inf, -1, 2, np.inf, -3],
    [np.inf, 1, np.inf, 3, 4],
    [5, np.inf, -5, np.inf, np.inf],
    [np.inf, -2, np.inf, -4, 6],
    [7, 8, np.inf, -9, np.inf]
]
M3_no_cycle = np.array([
    [np.inf, 1, np.inf, np.inf, -1],
    [np.inf, np.inf, 2, np.inf, np.inf],
    [np.inf, np.inf, np.inf, 3, np.inf],
    [2, np.inf, np.inf, np.inf, -2],
    [np.inf, 4, np.inf, 5, np.inf]
])
# print(fc(M3))
# print(fc(M4))
# print(fc(M3_no_cycle))
"""

# Partiel
from matrices import P3

# print(trouver_n())
# print(seuil(18))
# print(fc(P3))
