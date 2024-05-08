import numpy.random as rd
import numpy as np

# FONCTION 

# n correspond à la taille de la matrice
# a et b avec a < b, sont des entiers correspondants à l'intervalle de la matrice
def graphe(n, a, b):
    # Génère une matrice avec 50% de 0 et 50% de 1
    M = rd.randint(0, 2, (n, n))
    # Transforme les 0 en infini et convertit la matrice en float
    M = M.astype('float64')
    
    # Remplace les coefficients 1 par des valeurs choisies aléatoirement entre a et b
    for i in range(n):
        for j in range(n):
            if M[i][j] == 1:
                M[i][j] = rd.randint(a, b)
            else:
                M[i][j] = float('inf')

    return M

# n correspond a la taille de la matrice
# a et b avec a < b, sont des entiers correspondants à l'intervalle de la matrice
# p est la proportion variable de fleche
def graphe2(n, p, a, b):
    # Initialiser une matrice de taille n
    M = np.zeros((n, n))
    # Conversion de la matrice en float
    M = M.astype('float64')

    for i in range(n):
        for j in range(n):
            # utiliser np.random.binomial pour générer un nombre aléatoire entre 0 et 1
            if rd.binomial(1, p):
                # si 1, generer un poids aleatoire entre a and b
                M[i][j] = rd.randint(a, b)
            else:
                # et np.inf sinon
                M[i][j] = float('inf')

    return M

# EXEMPLE / TEST FONCTION
print("Graphe 1")
print(graphe(6, 1, 20))
print("Graphe 2")
print(graphe2(6, 0.4, 1, 20))  
# Utilisation d'une proportion de 40% de flèches
