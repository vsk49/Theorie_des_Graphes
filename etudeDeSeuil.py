from forteConnexite import *
import matplotlib.pyplot as plt
import numpy as np
import time

def grapheSeuil():
    n = np.array([i for i in range(10, 41)])
    plt.plot(n, [seuil(i) for i in n], label='Seuil de forte connexité')
    plt.xlabel("taille du graphe")
    plt.ylabel('Seuil de forte connexité')
    plt.title('Seuil de forte connexité en fonction de la taille du graphe')
    plt.legend()
    plt.show()
    
def TempsSeuil(n):
    debut = time.perf_counter()
    seuil(n)
    fin = time.perf_counter()
    return fin - debut
    
def grapheSeuilLogLog():
    n = np.array([i for i in range(1, 21)])
    plt.loglog(n, [TempsSeuil(i) for i in n], label='Seuil de forte connexité')
    plt.xlabel("taille du graphe")
    plt.ylabel('Seuil de forte connexité')
    plt.title('Seuil de forte connexité en fonction de la taille du graphe')
    plt.legend()
    plt.show()

grapheSeuilLogLog()