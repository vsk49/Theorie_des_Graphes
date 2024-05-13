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

def construireChemin(matrice, chemin):
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
        nx.draw_networkx_edges(G, positions, edgelist=edges, edge_color='r', width=2)

        plt.show()
        
M = gm.graphe(5, 0, 20)
construireChemin(M, Dijkstra(M, 0))