import numpy as np

# trouver le chemin le plus court d'un graphe donne a partir
# de sa matrice d'adjacence et d'un sommet de depart
def Dijkstra(M, d):
    # Etape 1 : initialisation
    distances = {v : np.inf for v in range(len(M))}
    distances[d] = 0
    predecesseurs = {v : -1 for v in range(len(M))}
    sommetsVisites = [d]
    sommetsnonVisites = [v for v in range(len(M))]
    sommetsnonVisites.remove(d)
    
    # Etape 2 : boucle principale
    while len(sommetsVisites) < len(M):
        # utilisation de l'algorithme valeurPlusPetite pour
        # trouver le sommet u non visite de distance minimale
        u = -1
        sMin = np.inf
        for i in sommetsnonVisites:
            if distances[i] < sMin:
                u = i
                sMin = distances[i]
        # ajout de u dans sommetsVisites et suppression de u
        sommetsnonVisites.remove(u)
        sommetsVisites.append(u)
        # mise a jour des distances et des predecesseurs
        for v in sommetsnonVisites:
            if M[u][v] != 0 and distances[u] + M[u][v] < distances[v]:
                distances[v] = distances[u] + M[u][v]
                predecesseurs[v] = u
                
    # Etape 3 : construction du chemin trouve sous une forme de liste
    cheminTrouve = [] # une liste de sommets du chemin trouve
    sommet = len(M) - 1
    while sommet != -1:
        cheminTrouve.insert(0, sommet)
        sommet = predecesseurs[sommet]
        
    return cheminTrouve