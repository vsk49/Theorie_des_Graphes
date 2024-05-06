import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def estSymetrique(matrice):
    # verifier si une matrice est carree
    if len(matrice) != len(matrice[0]):
        return False
    # verifier la symmetrie d'une matrice
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            if matrice[i][j] != matrice[j][i]:
                return False
    return True

def construireGraphe(matrice):
    if estSymetrique(matrice):
        G = nx.Graph()
    else:
        G = nx.DiGraph()
        
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            if matrice[i][j] == 1:
                G.add_edge(i, j, weight=1)
                
    # Dessin du graphe orienté pondéré
    positions = nx.spring_layout(G) 
    nx.draw(G, positions, with_labels=True)

    # Récuperation les poids des arretes
    poids = nx.get_edge_attributes(G, "weight")  
    # Ajout des libelles sur le graphe
    nx.draw_networkx_edge_labels(G, positions, edge_labels=poids)

    # Affichage du graphe dessiné
    plt.show()      

M = np.array([[1, 0, 1, 1], 
              [1, 1, 0, 1], 
              [0, 1, 0, 1], 
              [0, 0, 1, 0]])

construireGraphe(M)
            