import numpy as np
import random

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
        file.pop(0)
    return Resultat

# parcours en profondeur
def parcour_profondeur(M, d):
    mat = conversion(M)
    n = len(M)
    couleur = {}
    for i in range(n):
        couleur[i] = 'blanc'
    couleur[d] = 'vert'
    pile=[d]
    Resultat=[]
    while pile !=[]:
        i=pile[-1]
        Succ_blanc=[]
        for j in range(n):
            if (mat[i,j]==1 and couleur[j]=='blanc'):
                Succ_blanc.append(j)
        if Succ_blanc!=[]:
            v= Succ_blanc[0]
            couleur[v]='vert'
            pile.append(v)
            Resultat.append((i, v))  # Ajouter la fleche (i, j) a la liste des resultats
        else:
            pile.pop()
    return Resultat


def hasard(M):
    fleche = []
    for i in range(0,len(M)-1):
        for y in range(0,len(M)-1):
            if M[i][y] != np.inf :
                fleche.append((i, y))  # Ajouter la fleche (i, j) a la liste des resultats
    return random.sample(fleche, len(fleche))
