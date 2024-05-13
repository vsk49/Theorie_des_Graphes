import genererMatrice as gm
import algosCheminPlusCourt as acpc
import time

# retourne le temps de calcul de l'algorithme de Dijkstra
def TempsDij(n):
    M = gm.graphe(n, 1, 50)
    debut = time.time()
    for i in range(n):
        acpc.Dijkstra(M, i)
    fin = time.time()
    tempsExecution = fin - debut
    return tempsExecution

# retourne le temps de calcul de l'algorithme de Bellman-Ford
def TempsBF(n, ordre='aleatoire'):
    M = gm.graphe(n, 1, 50)
    debut = time.time()
    for i in range(n):
        acpc.BellmanFord(M, i, ordre)
    fin = time.time()
    tempsExecution = fin - debut
    return tempsExecution
    

# Test de la fonction TempsDij
print(TempsDij(100))
print(TempsBF(100, 'largeur'))
print(TempsBF(100, 'profondeur'))
print(TempsBF(100, 'aleatoire'))