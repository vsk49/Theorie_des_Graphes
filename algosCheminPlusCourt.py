import numpy as np
import bellmanford as bf

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

def BellmanFord(M, d, order='random'):
    dist = {v : np.inf for v in range(len(M))}
    dist[d] = 0
    pred = {v : -1 for v in range(len(M))}

    if order == 'random':
        edges = bm.hasard(M)
    elif order == 'breadth':
        edges = bm.parcour_largeur(M, d)
    elif order == 'depth':
        edges = bm.parcour_profondeur(M, d)

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