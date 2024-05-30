import numpy as np
import genererMatrice as gm
import bellmanFordVariants as bf

def fc(M):
    n = len(M)
    # utiliser le parcours profondeur pour verifier la forte connexite
    for i in range(n):
        visited_edges = bf.parcour_profondeur(M, i)
        # mettre les noeuds visites dans un ensemble
        visited_nodes = set(node for edge in visited_edges for node in edge)
        # Si le nombre de noeuds < n, le graphe n'est pas fortement connexe
        if len(visited_nodes) < n:
            return False
    # sinon, le graphe est fortement connexe
    return True

def test_stat_fc(n):
    nbGraphesFortConnexes = 0
    nbGraphs = 300
    for i in range(nbGraphs):
        M = gm.graphe(n, 1, 10)
        if fc(M):
            nbGraphesFortConnexes += 1
    return nbGraphesFortConnexes / nbGraphs

def trouver_n():
    n = 1
    while True:
        if test_stat_fc(n) >= 0.99:
            return n
        n += 1
        
def test_stat_fc2(n, p):
    nbGraphesFortConnexes = 0
    nbGraphs = 300
    for i in range(nbGraphs):
        M = gm.graphe2(n, p, 1, 10)
        if fc(M):
            nbGraphesFortConnexes += 1
    return nbGraphesFortConnexes / nbGraphs

def seuil(n):
    p = 1
    while test_stat_fc2(n, p) >= 0.99:
        p -= 0.1
    return p
        
print(trouver_n())
print(test_stat_fc2(10, 0.4))
print(seuil(12))