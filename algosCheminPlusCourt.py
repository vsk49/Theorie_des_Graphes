import numpy as np
import bellmanFordVariants as bf

def Dijkstra(M, d):
    # creation d'un dictionnaire pour stocker les sommets et leurs distances
	dist = {v : np.inf for v in range(len(M))}
	dist[d] = 0
	# creation d'un dictionnaire pour stocker les sommets et leurs predecesseurs
	pred = {v : -1 for v in range(len(M))}
	# creation d'une liste pour stocker les sommets visités
	sommetsVisites = []

	# la boucle principale
	while len(sommetsVisites) < len(M):
		# trouver le sommet u non visité avec la distance minimale
		u = -1
		sMin = np.inf
		for i in range(len(M)):
			if i not in sommetsVisites and dist[i] < sMin:
				sMin = dist[i]
				u = i
		# sauter la boucle si u est -1 (aucun sommet trouvé)
		if u == -1:  
			break

		# marquer u comme visité
		sommetsVisites.append(u)

		# mettre à jour les distances des sommets non visités
		for v in range(len(M)):
			if v not in sommetsVisites and M[u][v] > 0:
				if dist[u] + M[u][v] < dist[v]:
					dist[v] = dist[u] + M[u][v]
					pred[v] = u

	# construire les résultats
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
				cheminTrouve[s] = "sommet non joignable à d par un chemin dans le graphe."

	return cheminTrouve

def poids(u, v, M):
	return M[u][v]

def BellmanFord(M, d, ordre='largeur'):
	dist = {v : np.inf for v in range(len(M))}
	dist[d] = 0
	pred = {v : -1 for v in range(len(M))}

	if ordre == 'hasard':
		edges = bf.hasard(M)
	elif ordre == 'largeur':
		edges = bf.parcour_largeur(M, d)
	elif ordre == 'profondeur':
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

	# print(f"Number of iterations: {iterations}")

	# Verification des cycles poids negatifs
	# if cycle_poids_négatif(M, dist):
	#   print("Cycle poids negatif detecte")

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

M = [[1, 2, np.inf, 7], 
	 [np.inf, np.inf, 1, np.inf], 
	 [5, 4, 3, 2], 
	 [6, np.inf, np.inf, 6]]
print(Dijkstra(M, 0))
# print(BellmanFord(M, 0, 'largeur'))
# print(BellmanFord(M, 0, 'profondeur'))
# print(BellmanFord(M, 0, 'hasard'))

