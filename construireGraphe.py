import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import genererMatrice as gm

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
            if matrice[i][j] > 0:
                G.add_edge(i, j, weight=matrice[i][j])
                
    # Dessin du graphe orienté pondéré
    nx.draw(G, nx.spring_layout(G), with_labels=True)

    # Récuperation les poids des arretes
    poids = nx.get_edge_attributes(G, "weight")  
    # Ajout des libelles sur le graphe
    nx.draw_networkx_edge_labels(G, nx.spring_layout(G), edge_labels=poids)

    # Affichage du graphe dessiné
    plt.show()   
    
     

M = gm.graphe(5, 0, 20)
construireGraphe(M)         