import genererMatrice as gm
import algosCheminPlusCourt as acpc
import matplotlib.pyplot as plt
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
def TempsBF(n, ordre='hasard'):
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
print(TempsBF(100, 'hasard'))

# Tracer les courbes de temps de calcul
def tracerCourbes():
    n = [i for i in range(2, 201, 10)]
    tempsDij = [TempsDij(i) for i in n]
    tempsBF_largeur = [TempsBF(i, 'largeur') for i in n]
    # tempsBF_profondeur = [TempsBF(i, 'profondeur') for i in n]
    # tempsBF_hasard = [TempsBF(i, 'hasard') for i in n]

    plt.plot(n, tempsDij, label='Dijkstra')
    plt.plot(n, tempsBF_largeur, label='Bellman-Ford largeur')
    # plt.plot(n, tempsBF_profondeur, label='Bellman-Ford profondeur')
    # plt.plot(n, tempsBF_hasard, label='Bellman-Ford hasard')
    plt.xlabel('Nombre de sommets')
    plt.ylabel('Temps de calcul(s)')
    plt.title('Temps de calcul des algorithmes de plus court chemin')
    plt.legend()
    plt.show()
    
tracerCourbes()