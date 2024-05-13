import networkx as nx
import matplotlib.pyplot as plt
import construireGraphe as cg
import genererMatrice as gm
from algosCheminPlusCourt import Dijkstra

def cheminExiste(matrice, chemin):
    # verifier si ce chemin existe dans la matrice
    for i in range(len(chemin) - 1):
        if matrice[chemin[i]][chemin[i + 1]] < 1:
            return False
    return True

import matplotlib.pyplot as plt
import networkx as nx

def construireChemin(matrice, chemin: list):
    # les codes sont identique a ceux de la fonction construireGraphe
    if cg.estSymetrique(matrice):
        G = nx.Graph()
    else:
        G = nx.DiGraph()
        
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            if matrice[i][j] > 0:
                G.add_edge(i, j, weight=matrice[i][j])
                
    positions = nx.spring_layout(G) 
    nx.draw(G, positions, with_labels=True)

    poids = nx.get_edge_attributes(G, "weight")  
    nx.draw_networkx_edge_labels(G, positions, edge_labels=poids)
    
    if cheminExiste(matrice, chemin) == False:
        print("le chemin n'existe pas dans le graphe!")
    else:
        # Coloration en rouge du chemin
        edges = [(chemin[i], chemin[i + 1]) for i in range(len(chemin) - 1)]
        nx.draw_networkx_edges(G, positions, edgelist=edges, edge_color='red', width=2, alpha=1)

        plt.show()
        
M = [[0, 0, 5, 2, 3], 
     [1, 0, 0, 0, 0], 
     [0, 0, 0, 0, 3], 
     [0, 0, 0, 0, 4], 
     [0, 3, 0, 0, 2]]
construireChemin(M, [0, 2, 4, 1, 0])