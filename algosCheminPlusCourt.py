import numpy as np

def Dijkstra(M, d):
    distances = {v : np.inf for v in range(len(M))}
    distances[d] = 0
    predecesseurs = {v : -1 for v in range(len(M))}
    sommetsVisites = [d]
    sommetsnonVisites = [v for v in range(len(M))]
    sommetsnonVisites.remove(d)

    while len(sommetsVisites) < len(M):
        u = -1
        sMin = np.inf
        for i in sommetsnonVisites:
            if distances[i] < sMin:
                u = i
                sMin = distances[i]

        if u == -1:  # Break the loop if no node was found
            break

        sommetsnonVisites.remove(u)
        sommetsVisites.append(u)

        for v in sommetsnonVisites:
            if M[u][v] != np.inf and distances[u] + M[u][v] < distances[v]:  # Check for np.inf instead of 0
                distances[v] = distances[u] + M[u][v]
                predecesseurs[v] = u

    cheminTrouve = []
    sommet = len(M) - 1
    while sommet != -1:
        cheminTrouve.insert(0, sommet)
        sommet = predecesseurs[sommet]

    return cheminTrouve