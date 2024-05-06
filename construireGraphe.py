import networkx as nx
import numpy as np

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
        
    for sommets in range(len(matrice)):
        G.add_node(sommets)
        
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            if matrice[i][j] == 1:
                G.add_edge(i, j)
                
    nx.draw_networkx(G, node_color='blue', node_size=500, edge_color='red', 
                     with_labels=True, font_size=10, font_color='white')
    
    
    
    
def cheminExiste(matrice, chemin):
    # verifier si ce chemin existe dans la matrice
    for i in range(len(chemin) - 1):
        if matrice[chemin[i]][chemin[i + 1]] != 1:
            return False
    return True
    
def construireChemin(matrice, chemin):
    if estSymetrique(matrice):
        G = nx.Graph()
    else:
        G = nx.DiGraph()
        
    for sommets in range(len(matrice)):
        G.add_node(sommets)
        
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            if matrice[i][j] == 1:
                G.add_edge(i, j)
                
    nx.draw_networkx(G, node_color='blue', node_size=500, edge_color='red', 
                     with_labels=True, font_size=10, font_color='white')
    
    

M = np.array([[1, 0, 1, 1], 
              [1, 1, 0, 1], 
              [0, 1, 0, 1], 
              [0, 0, 1, 0]])

# construireGraphe(M)
construireChemin(M, np.array([0, 2, 1, 3]))
            