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
		# sauter la boucle si u est -1 (aucun sommet trouvé)
		if u == -1:  
			break

		sommetsnonVisites.remove(u)
		sommetsVisites.append(u)

		for v in sommetsnonVisites:
			# Chercher les np.inf au lieu des 0
			if M[u][v] != np.inf and distances[u] + M[u][v] < distances[v]:  
				distances[v] = distances[u] + M[u][v]
				predecesseurs[v] = u

	cheminTrouve = []
	sommet = len(M) - 1
	while sommet != -1:
		cheminTrouve.insert(0, sommet)
		sommet = predecesseurs[sommet]

	return cheminTrouve

def poids(u, v, M):
    return M[u][v]

def BellmanFord(M, d):
    distances = {v : np.inf for v in range(len(M))}
    distances[d] = 0
    predecesseurs = {v : -1 for v in range(len(M))}

    # Iterations to update distances
    for i in range(len(M)):
        if not mettre_à_jour_distances(M, distances, predecesseurs):
            break # No modification in the last round

    # Checking for negative weight cycles
    if cycle_poids_négatif(M, distances):
        print("Negative weight cycle detected")

    # Constructing results
    résultats = {}
    for s in range(len(M)):
        if distances[s] == np.inf:
            résultats[s] = "No path from d to s"
        else:
            chemin = reconstruire_chemin(predecesseurs, d, s)
            résultats[s] = (distances[s], chemin)

    return résultats

def mettre_à_jour_distances(M, distances, predecesseurs):
    modification = False
    for u in range(len(M)):
        for v in range(len(M)):
            if distances[u] != np.inf and distances[u] + poids(u, v, M) < distances[v]:
                distances[v] = distances[u] + poids(u, v, M)
                predecesseurs[v] = u
                modification = True
    return modification

def cycle_poids_négatif(M, distances):
    for u in range(len(M)):
        for v in range(len(M)):
            if distances[u] != np.inf and distances[u] + poids(u, v, M) < distances[v]:
                return True
    return False

def reconstruire_chemin(predecesseurs, départ, final):
    chemin = []
    noeud_actuel = final
    while noeud_actuel != départ:
        chemin.insert(0, noeud_actuel)
        noeud_actuel = predecesseurs[noeud_actuel]
    chemin.insert(0, départ)
    return chemin