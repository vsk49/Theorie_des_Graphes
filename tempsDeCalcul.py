import genererMatrice as gm
import algosCheminPlusCourt as acpc
import matplotlib.pyplot as plt
import numpy as np
import time

# retourne le temps de calcul de l'algorithme de Dijkstra
def TempsDij(n):
    M = gm.graphe(n, 1, 200)
    debut = time.time()
    for i in range(n):
        acpc.Dijkstra(M, i)
    fin = time.time()
    return fin - debut

# retourne le temps de calcul de l'algorithme de Bellman-Ford
def TempsBF(n, ordre='largeur'):
    M = gm.graphe(n, 1, 200)
    debut = time.time()
    for i in range(n):
        acpc.BellmanFord(M, i, ordre)
    fin = time.time()
    return fin - debut
    
# Test de la fonction TempsDij
print(TempsDij(50))

# Test de la fonction TempsBF
print(TempsBF(50, 'largeur'))

# Tracer les courbes de temps de calcul
def tracerCourbes():
    n = np.array([i for i in range(2, 201, 10)])
    tempsDij = np.array([TempsDij(i) for i in n])
    tempsBF_largeur = np.array([TempsBF(i, 'largeur') for i in n])

    plt.plot(n, tempsDij, label='Dijkstra')
    plt.plot(n, tempsBF_largeur, label='Bellman-Ford largeur')
    plt.xlabel('Nombre de sommets')
    plt.ylabel('Temps de calcul(s)')
    plt.title('Temps de calcul des algorithmes de plus court chemin')
    plt.legend()
    plt.show()

def tracerCourbesLogLog():
    n = np.array([i for i in range(2, 201, 10)])
    tempsDij = np.array([TempsDij(i) for i in n])
    tempsBF_largeur = np.array([TempsBF(i, 'largeur') for i in n])

    plt.plot(np.log(n), np.log(tempsDij), label='Dijkstra')
    plt.plot(np.log(n), np.log(tempsBF_largeur), label='Bellman-Ford largeur')
    plt.xlabel('log(Nombre de sommets)')
    plt.ylabel('log(Temps de calcul(s))')
    plt.title('Temps de calcul des algorithmes de plus court chemin')
    plt.legend()
    plt.show()
    
tracerCourbesLogLog()