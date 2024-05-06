import networkx as nx
import numpy as np
# import matplotlib.pyplot as plt

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
        
    for sommets in range(1, len(matrice) + 1):
        G.add_node(str(sommets))
        
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            if matrice[i][j] == 1:
                G.add_edge(str(i), str(j))
                
    nx.draw_networkx(G)
    
M = np.array([[1, 0, 1, 1], 
              [0, 1, 0, 0], 
              [1, 1, 1, 1], 
              [0, 0, 0, 1]])

construireGraphe(M)
            