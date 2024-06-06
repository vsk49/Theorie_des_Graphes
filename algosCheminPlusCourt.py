import numpy as np

import bellmanFordVariants as bf


def Dijkstra(M, d):
    dist = {v: np.inf for v in range(len(M))}
    dist[d] = 0
    pred = {v: -1 for v in range(len(M))}
    sommetsVisites = []

    while len(sommetsVisites) < len(M):
        u = -1
        sMin = np.inf
        for i in range(len(M)):
            if i not in sommetsVisites and dist[i] < sMin:
                sMin = dist[i]
                u = i
        # sauter la boucle si u est -1 (aucun sommet trouvé)
        if u == -1:
            break

        sommetsVisites.append(u)

        for v in range(len(M)):
            if v not in sommetsVisites and M[u][v] > 0:
                if dist[u] + M[u][v] < dist[v]:
                    dist[v] = dist[u] + M[u][v]
                    pred[v] = u

    cheminTrouve = {}
    for s in range(len(M)):
        if s != d:
            if dist[s] < np.inf:
                # Chemin trouvé, construire l'itinéraire
                itineraire = [s]
                u = pred[s]
                while u != -1:
                    itineraire.insert(0, u)
                    u = pred[u]

                cheminTrouve[s] = (dist[s], itineraire)
            else:
                cheminTrouve[s] = (
                    "sommet non joignable à d par un chemin dans le graphe G"
                )

    return cheminTrouve


def poids(u, v, M):
    return M[u][v]


def BellmanFord(M, d, ordre="largeur"):
    dist = {v: np.inf for v in range(len(M))}
    dist[d] = 0
    pred = {v: -1 for v in range(len(M))}

    if ordre == "hasard":
        edges = bf.hasard(M)
    elif ordre == "largeur":
        edges = bf.parcour_largeur(M, d)
    elif ordre == "profondeur":
        edges = bf.parcour_profondeur(M, d)

    # Iterations pour la mise-a-jour des distances
    iterations = 0
    for _ in range(len(M)):
        modification = False
        for u, v in edges:
            if dist[u] != np.inf and dist[u] + M[u][v] < dist[v]:
                dist[v] = dist[u] + M[u][v]
                pred[v] = u
                modification = True
        iterations += 1
        if not modification:
            break

    print(f"Number of iterations: {iterations}")

    # Verification des cycles poids negatifs
    if cycle_poids_négatif(M, dist):
        print("Cycle poids negatif detecte")

    # construire les results
    résultats = {}
    for s in range(len(M)):
        if dist[s] == np.inf:
            résultats[s] = "Pas de chemin de d vers s"
        else:
            chemin = reconstruire_chemin(pred, d, s)
            résultats[s] = (dist[s], chemin)

    return résultats


def mettre_à_jour_distances(M, dist, pred):
    modification = False
    for u in range(len(M)):
        for v in range(len(M)):
            if dist[u] != np.inf and dist[u] + poids(u, v, M) < dist[v]:
                dist[v] = dist[u] + poids(u, v, M)
                pred[v] = u
                modification = True
    return modification


def cycle_poids_négatif(M, dist):
    for u in range(len(M)):
        for v in range(len(M)):
            if dist[u] != np.inf and dist[u] + poids(u, v, M) < dist[v]:
                return True
    return False


def reconstruire_chemin(pred, départ, final):
    chemin = []
    noeud_actuel = final
    while noeud_actuel != départ:
        chemin.insert(0, noeud_actuel)
        noeud_actuel = pred[noeud_actuel]
    chemin.insert(0, départ)
    return chemin


# EXEMPLE / TEST FONCTION

M3 = np.array([
    [15, 1, np.inf, np.inf, np.inf, np.inf, 11, 2, np.inf, np.inf, 17, np.inf, 4, np.inf, np.inf],
    [np.inf, np.inf, 11, 9, np.inf, np.inf, np.inf, np.inf, np.inf, 15, np.inf, np.inf, np.inf, 3, np.inf],
    [np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, 16, np.inf, np.inf, np.inf, 8, np.inf, np.inf, 14],
    [np.inf, 3, np.inf, np.inf, np.inf, 13, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf],
    [np.inf, np.inf, np.inf, np.inf, 4, np.inf, 9, np.inf, np.inf, 11, np.inf, 13, np.inf, 15, np.inf],
    [np.inf, np.inf, np.inf, np.inf, 15, np.inf, np.inf, np.inf, 14, 7, 19, np.inf, np.inf, np.inf, 1],
    [7, np.inf, np.inf, 11, np.inf, 6, np.inf, np.inf, np.inf, np.inf, np.inf, 4, 18, 3, 20],
    [np.inf, np.inf, np.inf, 1, 5, np.inf, 7, 13, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, 8],
    [np.inf, np.inf, 1, 6, np.inf, 5, 17, np.inf, 18, 9, 4, np.inf, 11, np.inf, np.inf],
    [8, 11, np.inf, np.inf, 15, np.inf, np.inf, 13, np.inf, np.inf, np.inf, np.inf, 12, np.inf, 9]
])
N3 = np.array([
    [11, 2, np.inf, np.inf, np.inf, 1, np.inf, 16, np.inf, 6, np.inf, np.inf, np.inf, np.inf, np.inf],
    [np.inf, np.inf, -7, 1, 3, 6, np.inf, np.inf, 10, np.inf, 17, np.inf, np.inf, 15, np.inf],
    [15, np.inf, np.inf, np.inf, 6, np.inf, np.inf, 10, np.inf, 8, np.inf, np.inf, 19, np.inf, 9],
    [np.inf, np.inf, np.inf, np.inf, 12, 17, np.inf, np.inf, np.inf, np.inf, 5, np.inf, 16, 13, np.inf],
    [np.inf, np.inf, 15, np.inf, 4, np.inf, 9, np.inf, np.inf, 11, np.inf, 13, np.inf, 15, np.inf],
    [np.inf, 9, 8, np.inf, np.inf, np.inf, np.inf, np.inf, 14, -7, 19, 16, 4, 8, 3],
    [17, np.inf, np.inf, 11, np.inf, 6, np.inf, np.inf, np.inf, 10, 14, 5, 18, 3, 20],
    [np.inf, np.inf, 3, 1, 5, np.inf, -7, 13, np.inf, np.inf, np.inf, np.inf, 6, np.inf, 8],
    [np.inf, np.inf, 1, 6, np.inf, 5, 17, np.inf, 18, 9, 4, np.inf, 11, np.inf, np.inf],
    [8, 11, np.inf, np.inf, 15, np.inf, np.inf, 13, np.inf, np.inf, np.inf, 12, np.inf, -7, 9]
])
P3 = np.array([
    [1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0],
    [1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0],
    [1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1],
    [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0]
])

# print(Dijkstra(M3, 5))
print(BellmanFord(N3, 3, "largeur"))
print(BellmanFord(N3, 3, "profondeur"))
print(BellmanFord(N3, 3, "hasard"))
