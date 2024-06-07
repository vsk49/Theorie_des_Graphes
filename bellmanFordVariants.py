import random

import numpy as np

# FONCTION 

# convertir matrice pondérée en binaire
def conversion(mat):
    convertis = np.copy(mat)
    for x in range(len(convertis)):
        for y in range(len(convertis)):
            if mat[x][y] == np.inf or int(mat[x][y]) == 0 :
                convertis[x][y] = 0
            else:
                convertis[x][y] = 1
    return convertis
    
# parcours en largeur
def parcour_largeur(M, d):
    mat = conversion(M)
    n = len(M)
    couleur = {}
    flechesVisites = set()
    for i in range(n):
        couleur[i] = 'blanc'
    couleur[d] = 'vert'
    file = [d]
    Resultat = []
    while file != []:
        i = file[0]
        for j in range(n):
            if (mat[file[0]][j] == 1 and couleur[j] == 'blanc'):
                file.append(j)
                couleur[j] = 'vert'
                Resultat.append((i, j))  # Ajouter la fleche (i, j) a la liste des resultats
                flechesVisites.add((i, j))
        file.pop(0)
    # Chercher les aretes non visitees
    for i in range(n):
        for j in range(n):
            if mat[i][j] == 1 and (i, j) not in flechesVisites:
                Resultat.append((i, j))  # Ajouter la fleche (i, j) a la liste des resultats
    return Resultat

# parcours en profondeur
def parcour_profondeur(M, d):
    mat = conversion(M)
    n = len(M)
    couleur = {}
    flechesVisites = set()
    for i in range(n):
        couleur[i] = 'blanc'
    couleur[d] = 'vert'
    pile = [d]
    Resultat = []
    while pile != []:
        i = pile[-1]
        Succ_blanc = []
        for j in range(n):
            if (mat[i, j] == 1 and couleur[j] == 'blanc'):
                Succ_blanc.append(j)
        if Succ_blanc != []:
            v = Succ_blanc[0]
            couleur[v] = 'vert'
            pile.append(v)
            Resultat.append((i, v))  # Ajouter la fleche (i, v) a la liste des resultats
            flechesVisites.add((i, v))
        else:
            pile.pop()
    # Chercher les aretes non visitees
    for i in range(n):
        for j in range(n):
            if mat[i][j] == 1 and (i, j) not in flechesVisites:
                Resultat.append((i, j))  # Ajouter la fleche (i, j) a la liste des resultats
    return Resultat

def hasard(M):
    fleche = []
    for i in range(0, len(M)):
        for y in range(0, len(M)):
            if M[i][y] != np.inf:
                fleche.append((i, y))  # Add the edge (i, y) to the result list
    random.shuffle(fleche)  # Randomly shuffle the result list
    return fleche

# TESTS FONCTIONS
"""
M3 = np.array([
    [15, 1, np.inf, np.inf, np.inf, np.inf, 11, 2, np.inf, np.inf],
    [np.inf, np.inf, 11, 9, np.inf, np.inf, np.inf, np.inf, np.inf, 15],
    [np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, 16, np.inf, np.inf],
    [np.inf, 3, np.inf, np.inf, np.inf, 13, np.inf, np.inf, np.inf, np.inf],
    [np.inf, np.inf, np.inf, np.inf, 4, np.inf, 9, np.inf, np.inf, 11],
    [np.inf, np.inf, np.inf, np.inf, 15, np.inf, np.inf, np.inf, 14, -7],
    [-7, np.inf, np.inf, 11, np.inf, 6, np.inf, np.inf, np.inf, np.inf],
    [np.inf, np.inf, np.inf, 1, 5, np.inf, -7, 13, np.inf, np.inf],
    [np.inf, np.inf, 1, 6, np.inf, 5, 17, np.inf, 18, 9],
    [8, 11, np.inf, np.inf, 15, np.inf, np.inf, 13, np.inf, np.inf]
])
print(parcour_largeur(M3, 6))
print(parcour_profondeur(M3, 6))
print(hasard(M3))
M4 = [
    [np.inf, -1, 2, np.inf, -3],
    [np.inf, 1, np.inf, 3, 4],
    [5, np.inf, -5, np.inf, np.inf],
    [np.inf, -2, np.inf, -4, 6],
    [7, 8, np.inf, -9, np.inf]
]
print(parcour_largeur(M4, 4))
print(parcour_profondeur(M4, 4))
print(hasard(M4))
"""