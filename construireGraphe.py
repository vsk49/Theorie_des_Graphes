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
    positions = nx.spring_layout(G)
    print(positions)           
    nx.draw(G, positions, with_labels=True)

    # Récuperation les poids des arretes
    poids = nx.get_edge_attributes(G, "weight")  
    # Ajout des libelles sur le graphe
    nx.draw_networkx_edge_labels(G, positions, edge_labels=poids)

    # Affichage du graphe dessiné
    plt.show()   
    
# Test de la fonction construireGraphe
M1 = [[0, 1, 2, 3, 4], 
      [1, 0, 5, 6, 7], 
      [2, 5, 0, 8, 9], 
      [3, 6, 8, 0, 10], 
      [4, 7, 9, 10, 0]]
construireGraphe(M1)   